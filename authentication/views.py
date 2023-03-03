from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import User
from authentication.serializers import UserCreateSerializer


# создавать пользователей можно только в ручную, встроенной функции в джанго нету
class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer

# 5 шаг - Реализация «выхода» Для того чтобы закрыть доступ пользователю, нужно удалить его токен.
class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

