from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

from companies.models import Company

'''
   создавать картинки через API . Добавление картинок обычно происходит отдельным методом
   Их не суют вместе с основными данными, поэтому будет UpdateView
'''

@method_decorator(csrf_exempt, name='dispatch')
class CompanyImageView(UpdateView):
    model = Company
    fields = ["name", "logo"]

    def patch(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.logo = request.FILES["logo"]
        # в FILES лежат все файлы, которые послал пользователь в качестве файлов
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "logo": self.object.logo.url if self.object.logo else None
            # чтобы не возникали разные проблемы,
            # делаем чтобы откывалась не сама картинка, а её ссылка
            # было "logo": self.object.logo

        })



