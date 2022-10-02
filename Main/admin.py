from django.contrib import admin
from .models import Collection, Partners, AccountShelter, ShelterNews, LostAnimals, ShelterReport

admin.site.register(Collection)
admin.site.register(Partners)
admin.site.register(AccountShelter)
admin.site.register(ShelterNews)
admin.site.register(LostAnimals)
admin.site.register(ShelterReport)
