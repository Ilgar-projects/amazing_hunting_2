from django.db import models

from authentication.models import User


class Skill(models.Model):
    '''после создания нового класса добавить admin.site.register(Skill)
       в файл admin.py'''

    name = models.CharField(max_length=20)  # 20 символов
    is_active = models.BooleanField(default=True)


    class Meta:  # в основном используют класс Meta в виде перечисления каких нибудь атрибутов
        verbose_name = "Навык"  # как будем называть нашу модель
        verbose_name_plural = "Навыки"  # имя во множественном числе

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    STATUS = [
        ("draft", "Черновик"),
        ("open", "Открыта"),
        ("closed", "Закрыта")
    ]

    slug = models.SlugField(max_length=50)  # slug нужен для красивого отображения url
    text = models.CharField(max_length=2000)
    status = models.CharField(max_length=6, choices=STATUS, default="draft")
    created = models.DateField(auto_now_add=True)
    # auto_now_add=True поставить текущее значение (дата) в момент создания

    # чтобы связать таблицы. User это название модели с которой будем связываться.
    # on_delete атрибут означающий что делать если родительская в данный момент модель User запись будет удалена
    # если удалить пользователя, то конечно же хотим удалить и его вакансии
    # CASCADE каскадное удаление всех связанны записей
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # это как я понял связь один к многим one2many
    # айди джанго создаст сам

    skills = models.ManyToManyField(Skill)

    # (Skills) модель на которую будет ссылаться
    # так и пишется многиекомногим, вид связи в базах данных
    # дальше джанго сам создаст промежуточную таблицу, привяжет все внешние ключи и так далее

    # null=True означает что поле может быть пустым
    # при любых изменениях в моделях нужно делать миграцию
    # в терминале прописать python manage.py makemigrations потом python manage.py migrate
    # likes = models.IntegerField(default=0)
    class Meta:  # в основном используют класс Meta в виде перечисления каких нибудь атрибутов
        verbose_name = "Вакансия"  # как будем называть нашу модель, то есть за место названия vacancies или Vacancy
        verbose_name_plural = "Вакансии"  # имя во множественном числе

        # второй метод сортировки используется редко, и его не советуют. через модели в мета
        # выполняется по умолчанию к любому запросу орднринг
        # ordering = ["text"] # в данном случае по text
        # если с минусом, то в обратном порядке ordering = ["-text"]

    def __str__(self):
        return self.slug

    @property  # и теперь будет вести себя этот метод как атрибут
    def username(self):
        return self.user.username if self.user else None
