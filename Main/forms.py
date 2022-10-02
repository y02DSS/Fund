from django import forms

from django.forms import ModelForm

from .models import AccountShelter, Collection, ShelterNews, LostAnimals

# Форма авторизации
class LoginForm(forms.Form): 
    login_email = forms.EmailField(label='Email', max_length=100)
    login_password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


# Форма регистрации
class RegistryForm(ModelForm):
      class Meta:
         model = AccountShelter
         fields = ['name', 'email', 'password', 'city', 'address', 'logo']
         labels = {
            'name': 'Название приюта',
            'email': 'Введите email',
            'password': 'Придумайте пароль',
            'city': 'Введите город',
            'address': 'Введите адрес',
            'logo': 'Загрузите лого',
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
      fields = ['about', 'director_name', 'contact', 'choices_type_card', 'requisites', 'social_network', 'number_of_animals']
      labels = {
         'about': 'Опишите приют',
         'director_name': 'Имя директора приюта',
         'contact': 'Ввидите номер телефона',
         'requisites': 'Введите свои реквизиты',
         'social_network': 'Добавьте ссылки на социавльные сети',
         'number_of_animals': 'Сколько сейчас у вас животных?'
      }


# Даты посещения 
class XYZ_DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)

class DateVisits(ModelForm):
   class Meta:
      model = AccountShelter
      fields = ['date_visits']
      labels = {'date_visits': 'Дата посещения'}
      widgets = {
         'date_visits': XYZ_DateInput(format=["%Y-%m-%d"], ),
      }


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

# Форма создания новости приюта
class CreateNewsShelter(ModelForm):
   class Meta:
      model = ShelterNews
      fields = ['name_news', 'text_news']
      labels = {
         'name_news': 'Название новости',
         'text_news': 'Напишите новость'
      }

class AddLostAnimals(ModelForm):
   class Meta:
      model = LostAnimals
      fields = ['photo', 'city', 'breed', 'description']