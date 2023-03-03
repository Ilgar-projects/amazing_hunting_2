from django.db import models

'''не забыть после создания нового приложения добавить его в settings.py/INSTALLED_APPS
    И конечно же после создания модели сделать миграции 
    python manage.py makemigrations и потом сразу python manage.py migrate   
    и до этого нужно установить специальный пакет для работы с картинками pip install Pillow '''


class Company(models.Model):
    name = models.CharField(max_length=20)  # название компании, 20 символов

    logo = models.ImageField(upload_to='logos/')
    # ImageField колонка с картинками будет. upload_to куда класть картинки(путь до директории)
    # место где лежат все медиафайлы контролируется специальными настройками в django