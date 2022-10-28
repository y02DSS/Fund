from django.db import models


class ShelterNews(models.Model): # Все новости приютов
    name_news = models.CharField(max_length=200)
    date_news = models.DateField(auto_now_add=True)
    text_news = models.TextField()

    def __str__(self):
        return self.name_news


class ShelterReport(models.Model):
    company_report = models.CharField(max_length=200)
    name_report = models.CharField(max_length=200)
    text_report = models.TextField(blank=True, null=True)
    file_report = models.FileField(upload_to='static/uploads/files/reports')

    def __str__(self):
        return self.name_report


class AccountShelter(models.Model): # Личные кабинеты приютов
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)  
    about = models.TextField(max_length=1000, blank=True, null=True)
    logo = models.FileField(upload_to='static/img/accounts', blank=True, null=True)
    director_name = models.CharField(max_length=200, blank=True, null=True)
    contact = models.CharField(max_length=200, blank=True, null=True)
    requisites = models.CharField(max_length=200, blank=True, null=True)
    social_network = models.CharField(max_length=200, blank=True, null=True)
    number_of_animals = models.IntegerField(blank=True, null=True, default=0)
    news = models.ManyToManyField(ShelterNews, blank=True, null=True)
    # reports = models.ForeignKey(ShelterReport, on_delete = models.CASCADE, blank=True, null=True)
    # date_visits = models.DateField(blank=True, null=True)
    date_visits = models.TextField(max_length=1000, blank=True, null=True)
    register = models.CharField(max_length=10, choices=(('Отклонить', 'Отклонить'), ('Принять', 'Принять')), default="Отклонить")

    def __str__(self):
        return self.name


class TakeAnimal(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.contact


class Collection(models.Model): # Карточка с животным
    name = models.CharField(max_length=200)
    comment = models.TextField(blank=True, null=True)
    summ = models.FloatField(max_length=200)
    summ_now = models.FloatField(max_length=200, blank=True, null=True)
    summ_persent = models.CharField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='static/img/cardsAnimal', blank=True, null=True)
    video = models.FileField(upload_to='static/video/cardsAnimal', blank=True, null=True)
    status = models.CharField(max_length=200, choices=(("В приюте", "В приюте"), ("Забрали", "Забрали"), ("Не опреденно", "Не опреденно"), ("Архив", "Архив")))
    breed = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('Девочка', 'Девочка'), ('Мальчик', 'Мальчик')), blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200)
    is_take = models.CharField(max_length=200, blank=True, null=True)
    choice_shelter = models.ForeignKey(AccountShelter, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name


class Partners(models.Model): # Раздел с партнерами
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    about = models.CharField(max_length=1000)
    contact = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    logo = models.FileField(upload_to='static/img/companies')

    def __str__(self):
        return self.name


class LostAnimals(models.Model): # Раздел с потерянными животными
    photo = models.FileField(upload_to='static/img/lostAnimals')
    city = models.CharField(max_length=200)
    breed = models.CharField(max_length=200, blank=True, null=True, default="Без породы")
    contact = models.CharField(max_length=200)
    description = models.CharField(max_length=3000, blank=True, null=True)
    

class ChatLogin(models.Model): # Чат для приютов
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=10000)

    def __str__(self):
        return self.name + ' ' + self.text[:20] + '...'