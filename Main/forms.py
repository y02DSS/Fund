from calendar import c
from django import forms

from django.forms import ModelForm

from .models import AccountShelter, Collection, ShelterNews, LostAnimals, ShelterReport, LostAnimals, TakeAnimal, ShelterHotReport

# Форма авторизации
class LoginForm(forms.Form): 
    login_email = forms.EmailField(label='Email', max_length=100)
    login_password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


# Форма регистрации
class RegistryForm(ModelForm):
      class Meta:
         model = AccountShelter
         fields = ['name', 'email', 'password', 'city', 'address']
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

# Создать карточку питомника
class AddRegisterForm(ModelForm):
   CHOICES_CARD=[('credit-card','Добавить счет для физ. лица'),
         ('bank-card','Добавить счет для юр. лица')]
   choices_type_card = forms.ChoiceField(choices=CHOICES_CARD, widget=forms.RadioSelect, label='Выберите тип счета')   

   class Meta:
      model = AccountShelter
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
# class XYZ_DateInput(forms.DateInput):
#     input_type = "date"
#     def __init__(self, **kwargs):
#         kwargs["format"] = "%Y-%m-%d"
#         super().__init__(**kwargs)

# class DateVisits(ModelForm):
#    class Meta:
#       model = AccountShelter
#       fields = ['date_visits']
#       labels = {'date_visits': 'Дата посещения'}
#       widgets = {
#          'date_visits': XYZ_DateInput(format=["%Y-%m-%d"], ),
#       }

class DateVisits(ModelForm):
   class Meta:
      model = AccountShelter
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

# Форма удаления карточки животного
class DeleteCardAnimal(forms.Form):
   pass


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


#
class BudgetMonth(forms.Form):
   budget_money = forms.CharField(widget=forms.Textarea, label="Необходимая сумма", )
   budget_file = forms.FileField(required=False, label="Добавьте файл")


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


class FormChatLogin(forms.Form):
   text = forms.CharField(
      label='', 
      widget=forms.Textarea(
            attrs={"placeholder": "Введите ваше сообщение",}
      ),
    )

class FormTakeAnimal(ModelForm):
   class Meta:
      model = TakeAnimal
      fields = ['name', 'contact', 'city']
      labels = {
         'name': 'Введите имя',
         'contact': 'Введите контакты',
         'city': 'Введите свой город'
      }