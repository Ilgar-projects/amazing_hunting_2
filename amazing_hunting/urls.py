"""amazing_hunting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from vacancies import views

urlpatterns = [
    path('admin/', admin.site.urls),  # в скобках путь и название функции
    path('api-auth/', include('rest_framework.urls')),
    path('hello/', views.hello),
    path('vacancy/', include('vacancies.urls')),
    path('company/', include('companies.urls')),
    path('user/', include('authentication.urls')),
    # функция include всем урлам из vacancies.urls приставляется префикс 'vacancy'
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
   чтобы открывать картинки через админку в браузере, а чтобы открывались предусмотрен специальный url
   называется static . В который мы передаём путь, то есть url по которму будем чтото отдавать.
   И затем мы привязываем его к тому откуда значения для этого урла брать,
   то есть привязывается папочка с статическими данными document_root=settings.MEDIA_ROOT 
   Усли работаем в режиме разработчика, то есть DEBUG=True то пишем так
   if settings.DEBUG:
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   Если отключен дебаг, то работать не будет
'''
