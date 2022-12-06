"""TRANTOR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Main import views

urlpatterns = [
    path('', views.index),
    path('help/<int:help_id>', views.helpPage, name='helpPage'),
    path('allAnimals', views.allAnimals, name='allAnimals'),
    path('lostAnimal', views.lostAnimal, name='lostAnimal'),
    path('newLostAnimal', views.newLostAnimal, name='newLostAnimal'),
    path('fullLostAnimal/<int:lost_id>', views.fullLostAnimal, name='fullLostAnimal'),
    path('support', views.support, name='support'),
    path('partners', views.partners, name='partners'),
    path('archive', views.archive, name='archive'),
    path('archive_animal/<str:help_id>', views.archive_animal, name='archive_animal'),
    path('about', views.about, name='about'),
    path('volunteers', views.volunteers, name='volunteers'),
    path('shelters', views.shelters, name='shelters'),
    path('shelter_reports/<str:name_shelter>&<str:id_shelter>', views.shelter_reports, name='shelter_reports'),
    path('shelter_animals/<str:name_shelter>&<str:id_shelter>', views.shelter_animals, name='shelter_animals'),
    path('shelters/<str:name_shelter>&<str:id_shelter>', views.shelters_news, name='shelters_news'),
    path('get_animal_change_form/<str:animal_card_id>', views.get_animal_change_form, name="get_animal_change_form"),
    path('login', views.login_shelter, name='login'),
    # path('login?animal_report=<str:animal_report>', name="animal_report"),
    path('login_user', views.login_user, name='login_user'),
    path('admin/', admin.site.urls),
]
