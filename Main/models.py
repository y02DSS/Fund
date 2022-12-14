from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

import uuid


class ShelterNews(models.Model): # Все новости приютов
    name_news = models.CharField(max_length=200)
    date_news = models.DateField(auto_now_add=True)
    text_news = models.TextField()

    def __str__(self):
        return self.name_news

    class Meta:
        verbose_name = 'Новости приюта'
        verbose_name_plural = 'Новости приютов'


class ShelterReport(models.Model):
    company_report = models.CharField(max_length=200)
    name_report = models.CharField(max_length=200)
    text_report = models.TextField(blank=True, null=True)
    file_report = models.FileField(upload_to='static/uploads/files/reports')

    def __str__(self):
        return self.name_report

    class Meta:
        verbose_name = 'Отчеты приюта'
        verbose_name_plural = 'Отчеты приютов'


class ShelterHotReport(models.Model):
    name_hot = models.CharField(max_length=200)
    text_hot = models.TextField(max_length=1000)

    def __str__(self):
        return self.name_hot

    class Meta:
        verbose_name = 'Срочное сообщение'
        verbose_name_plural = 'Срочные сообщения'


class AnimalReport(models.Model):
    name_animal = models.CharField(max_length=200)
    report_animal = models.CharField(max_length=200)
    text_animal = models.TextField(max_length=3000)
    date_animal = models.DateField(auto_now_add=True)
    file_animal = models.FileField(upload_to='static/uploads/files/reports')

    def __str__(self):
        return self.name_animal

    class Meta:
        verbose_name = 'Отчет питомца'
        verbose_name_plural = 'Отчеты питомцев'


class ShelterAccount(AbstractUser): # Личные кабинеты приютов
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, blank=True)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True)
    about = models.TextField(max_length=5000, blank=True)
    logo = models.FileField(upload_to='static/img/accounts', blank=True)
    director_name = models.CharField(max_length=200, blank=True)
    contact = models.CharField(max_length=200, blank=True)
    requisites = models.CharField(max_length=500, blank=True)
    social_network = models.CharField(max_length=200, blank=True)
    number_of_animals = models.IntegerField(default=0)
    news = models.ManyToManyField(ShelterNews, blank=True)
    hotReport = models.ManyToManyField(ShelterHotReport, blank=True)
    date_visits = models.TextField(max_length=1000, blank=True)
    register = models.CharField(max_length=10, choices=(('Отклонить', 'Отклонить'), ('Принять', 'Принять')), default="Отклонить")

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="%(class)s_requests_created",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="%(class)s_requests_created",
        related_query_name="user",
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Личный кабинет приюта'
        verbose_name_plural = 'Личные кабинеты приютов'


class TakeAnimal(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.contact

    class Meta:
        verbose_name = 'Забрать питомца'
        verbose_name_plural = 'Забрать питомцев'


class AnimalCard(models.Model): # Карточка с животным
    name = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)
    summ = models.FloatField(max_length=200)
    summ_now = models.FloatField(max_length=200, blank=True, null=True)
    summ_persent = models.CharField(max_length=200, blank=True, null=True)
    photo = models.FileField(upload_to='static/img/cardsAnimal', blank=True, null=True)
    video = models.FileField(upload_to='static/video/cardsAnimal', blank=True, null=True)
    status = models.CharField(max_length=200, choices=(("В приюте", "В приюте"), ("Забрали", "Забрали"), ("Умер", "Умер"), ("Другая причина", "Другая причина (описать)")))
    breed = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('Девочка', 'Девочка'), ('Мальчик', 'Мальчик')), blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200)
    is_take = models.CharField(max_length=200, blank=True, null=True)
    animalReport = models.ManyToManyField(AnimalReport, blank=True, null=True)
    choice_shelter = models.ForeignKey(ShelterAccount, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'


class Partners(models.Model): # Раздел с партнерами
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    about = models.CharField(max_length=1000)
    contact = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    logo = models.FileField(upload_to='static/img/companies')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class LostAnimals(models.Model): # Раздел с потерянными животными
    photo = models.FileField(upload_to='static/img/lostAnimals')
    city = models.CharField(max_length=200)
    breed = models.CharField(max_length=200, blank=True, null=True, default="Без породы")
    contact = models.CharField(max_length=200)
    description = models.CharField(max_length=3000, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Потерянное животное'
        verbose_name_plural = 'Потерянные животные'
    

class ChatLogin(models.Model): # Чат для приютов
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=10000)

    def __str__(self):
        return self.name + ' ' + self.text[:20] + '...'

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чат'


class UserAccount(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, blank=True)
    key = models.CharField(max_length=50, default=uuid.uuid4)
    helped_animals = models.ManyToManyField(AnimalCard, blank=True, null=True)
    key_used = models.IntegerField(max_length=2, default=2)
    register_user = models.CharField(max_length=10, choices=(('Отклонить', 'Отклонить'), ('Принять', 'Принять')), default="Отклонить")

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="%(class)s_requests_created",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="%(class)s_requests_created",
        related_query_name="user",
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Личный кабинет пользователей'
        verbose_name_plural = 'Личный кабинет пользователя'
