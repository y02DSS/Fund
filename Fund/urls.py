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
    path('help/<int:helpID>', views.helpPage),
    path('allAnimals', views.allAnimals, name='allAnimals'),
    path('lostAnimal', views.lostAnimal, name='lostAnimal'),
    path('newLostAnimal', views.newLostAnimal, name='newLostAnimal'),
    path('support', views.support, name='support'),
    path('partners', views.partners, name='partners'),
    path('shelters', views.shelters, name='shelters'),
    path('shelters/<str:name_shelter>&<str:id_shelter>', views.shelters_news, name='shelters_news'),
    path('login/<str:rights>', views.login, name='login'),
    path('admin/', admin.site.urls),
]
