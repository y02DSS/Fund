from calendar import c
from django import forms

from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import ShelterAccount, Collection, ShelterNews, LostAnimals, ShelterReport, LostAnimals, TakeAnimal, ShelterHotReport, AnimalReport, UserAccount

# Форма авторизации приюта
class LoginForm(forms.Form): 
    login_email = forms.EmailField(label='Email', max_length=100)
    login_password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


# Форма регистрации приюта 
class RegistryForm(ModelForm):
      class Meta:
         model = ShelterAccount
         fields = ['username', 'email', 'password', 'city', 'address']
         labels = {
            'name': 'Название приюта',
            'email': 'Введите email',
            'password': 'Придумайте пароль',
            'city': 'Введите город',
            'address': 'Введите адрес',
         }
         widgets = {
            'password': forms.PasswordInput,
         }


class LoginFormUser(ModelForm):
   class Meta:
      model = UserAccount
      fields = ['email', 'password']
      labels = {
         'email': 'Email',
         'password': 'Пароль'
      }
      widgets = {
         'password': forms.PasswordInput,
      }
      

class RegistryFormUser(ModelForm):
   class Meta:
      model = UserAccount
      fields = ['username', 'email', 'password']
      labels = {
         'username': 'Введите имя',
         'email': 'Введите email',
         'password': 'Придумайте пароль'
      }
      widgets = {
         'password': forms.PasswordInput,
      }


# Создать карточку питомника
class AddRegisterForm(ModelForm):
   CHOICES_CARD=[('credit-card','Добавить счет для физ. лица'),
         ('bank-card','Добавить счет для юр. лица')]
   choices_type_card = forms.ChoiceField(choices=CHOICES_CARD, widget=forms.RadioSelect, label='Выберите тип счета', required=False)   
   class Meta:
      model = ShelterAccount
      fields = ['about', 'director_name', 'contact', 'choices_type_card', 'requisites', 'social_network', 'number_of_animals', 'logo']
      labels = {
         'about': 'Опишите приют',
         'director_name': 'Имя директора приюта',
         'contact': 'Ввидите номер телефона',
         'social_network': 'Добавьте ссылки на социальные сети',
         'number_of_animals': 'Сколько сейчас у вас животных?',
         'logo': 'Загрузите лого',
      }


# Даты посещения 
class DateVisits(ModelForm):
   class Meta:
      model = ShelterAccount
      fields = ['date_visits']
      labels = {'date_visits': 'Даты посещений'}


# Форма создания карточки животного
class CreateCardAnimal(ModelForm):
     class Meta:
         model = Collection
         fields = ['name', 'comment', 'summ', 'photo', 'video', 'status', 'breed', 'gender', 'age']
         labels = {
            'name': 'Имя питомца',
            'comment': 'Коментарий',
            'summ': 'Необходимая сумма',
            'photo': 'Загрузите фотографию',
            'video': 'Загрузите видео',
            'status': 'Где сейчас находится питомец',
            'breed': 'Порода',
            'gender': 'Пол',
            'age': 'Возраст'
         }


# Форма отправки отчета животного
class CreateAnimalReport(ModelForm):
   class Meta:
      model = AnimalReport
      fields = ['report_animal', 'text_animal', 'file_animal']
      labels = {
         'report_animal': 'Имя отчета',
         'text_animal': 'Добаьте текст отчета',
         'file_animal': 'Добавьте фото'
      }
      

# Изменить карточку животного
class ChangeCardAnimal(ModelForm):
      class Meta:
         model = Collection
         fields = ['name', 'comment', 'summ', 'photo', 'video', 'status', 'breed', 'gender', 'age']
         labels = {
            'name': 'Имя питомца',
            'comment': 'Коментарий',
            'summ': 'Необходимая сумма',
            'photo': 'Загрузите фотографию',
            'video': 'Загрузите видео',
            'status': 'Где сейчас находится питомец',
            'breed': 'Порода',
            'gender': 'Пол',
            'age': 'Возраст',
         }


# Форма создания новости приюта
class CreateNewsShelter(ModelForm):
   class Meta:
      model = ShelterNews
      fields = ['name_news', 'text_news']
      labels = {
         'name_news': 'Название новости',
         'text_news': 'Напишите новость'
      }


# Форма пропавшего животного
class AddLostAnimals(ModelForm):
   class Meta:
      model = LostAnimals
      fields = ['photo', 'city', 'breed', 'description']


# Форма отправки email
class HotEmail(ModelForm):
   class Meta:
      model = ShelterHotReport
      fields = ['name_hot', 'text_hot']
      labels = {
         'name_hot': "Название",
         'text_hot': "Описание"
      }


# Форма бюджета в месяц
class BudgetMonth(forms.Form):
   budget_money = forms.CharField(widget=forms.Textarea, label="Необходимая сумма", )
   budget_file = forms.FileField(required=False, label="Добавьте файл")


# Форма новостей приюта
class NewShelterReport(ModelForm):
   class Meta:
      model = ShelterReport
      fields = ['name_report', 'text_report', 'file_report']
      labels = {
         'name_report': 'Имя отчета',
         'text_report': 'Описание',
         'file_report': 'Добавьте файл'
      }


# Форма потерянного животного
class FormLostAnimals(ModelForm):
   class Meta:
      model = LostAnimals
      fields = ['photo', 'city', 'breed', 'contact', 'description']
      labels = {
         'photo': 'Добавляем фото',
         'city': 'Введите города',
         'breed': 'Введите породу',
         'contact': 'Оставьте свои контакты',
         'description': 'Добавьте описание'
      }


# Форма чата
class FormChatLogin(forms.Form):
   text = forms.CharField(
      label='', 
      widget=forms.Textarea(
            attrs={"placeholder": "Введите ваше сообщение",}
      ),
    )


# Форма забрать животного
class FormTakeAnimal(ModelForm):
   class Meta:
      model = TakeAnimal
      fields = ['name', 'contact', 'city']
      labels = {
         'name': 'Введите имя',
         'contact': 'Введите контакты',
         'city': 'Введите свой город'
      }