from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Count, Avg
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from amazing_hunting import settings
from vacancies.models import Vacancy, Skill
from vacancies.seriallizers import VacancyDetailSerializer, VacancyListSerializer, VacancyCreateSerializer, \
    VacancyUpdateSerializer, VacancyDestroySerializer, SkillSerializer


# 1- создаём вьюшку
def hello(request):  # request это данные которые послал пользователь
    return HttpResponse("hello world")  # принимает от пользователя рекуэст и возвращает текст Hello world


# 2- и теперь эту вьюшку нужно объявить в urls.py
# 3- потом в setting в INSTALLED_APPS в котором имена всех приложений в нашем джанго проекте
# 'vacancies' это записали в setting в INSTALLED_APPS.

class SkillsViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class VacancyListView(ListAPIView):
    queryset = Vacancy.objects.all()  # список всех записей модели
    serializer_class = VacancyListSerializer

    #     paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
    #     page_number = request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)
    #     # пагинатор


class VacancyDetailView(RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializer


class VacancyCreateView(CreateAPIView):  # создание вакансии
    queryset = Vacancy.objects.all()
    serializer_class = VacancyCreateSerializer


class VacancyUpdateView(UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyUpdateSerializer


class VacancyDeleteView(DestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDestroySerializer


class UserVacancyDetaiView(View):  # первый вариант группировки
    '''отдельный класс для вывода всех вакансий конкретного пользователя'''

    def get(self, request):
        user_qs = User.objects.annotate(vacancies=Count('vacancy'))
        '''метод эннотэйд делает дополнительную колонку по которой можно что то посчитать
           например сумму или количество, минимум и т.д. в общем всё то, что может
           применяться к сгруппированным данным'''

        paginator = Paginator(user_qs, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        # пагинатор

        users = []
        for user in page_obj:
            users.append({
                "id": user.id,
                "name": user.username,  # имя пользователя
                "vacancies": user.vacancies  # количество вакансий который он опубликовал
            })

        response = {
            "items": users,  # наши юзеры
            "total": paginator.count,
            "num_pages": paginator.num_pages,  # количество страниц
            "avg": user_qs.aggregate(avg=Avg('vacancies'))["avg"]
            # Втораой способ группировки данных. Она считает данные сразу по всем записям из этой таблицы
            # среднее количество по колонке вакансий
            # если применяем аггригэйт, то тогда уже нельзя будет применять Count, annotate, ордер_бай
            # выдаёт словарь. avg это название колонки и в ней результат Avg('vacancies')
        }

        return JsonResponse(response)
