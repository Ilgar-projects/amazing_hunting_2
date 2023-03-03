from rest_framework import serializers

from authentication.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data) # сохранит пользователя как есть, то есть с открытым паролем

        user.set_password(user.password) # засекречиваем. хешируем пароль и возвращаем с хешированным паролем юзера
        user.save()

        return user


