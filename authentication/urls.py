from django.urls import path
from rest_framework.authtoken import views

from authentication.views import UserCreateView, Logout

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('login/', views.obtain_auth_token), # 3 шаг - подключаем путь для логина.
    path('logout/', Logout.as_view()), # 6 шаг - регистрируем
]
