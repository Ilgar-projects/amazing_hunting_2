from django.contrib import admin

from vacancies.models import Vacancy, Skill

# вызовим атрибут site и из неё функцию register
# в которую передадим нашу модель Vacancy
admin.site.register(Vacancy)
# этого минимально достаточно чтобы отобразить нашу модель в админ панель

admin.site.register(Skill)

