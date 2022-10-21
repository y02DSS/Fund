from gc import collect
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Collection, Partners, AccountShelter, ShelterNews, ShelterReport
from .forms import LoginForm, RegistryForm, CreateCardAnimal, CreateNewsShelter, DateVisits, AddRegisterForm, HotEmail, BudgetMonth, NewShelterReport
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages

from .send_email import send_for_email

def inject_form(request):  # Работает на всех страницах
    data = {}
    data["form_login"] = LoginForm()
    data["form_registry"] = RegistryForm()
    form_registry_add = AccountShelter()
    if request.method == 'POST':

        form_registry = RegistryForm(request.POST)
        if form_registry.is_valid(): # Регистрация
            form_registry_add.name = request.POST.get("name")
            form_registry_add.email = request.POST.get("email")
            form_registry_add.password = request.POST.get("password")
            form_registry_add.save()

        form_login = LoginForm(request.POST)
        if form_login.is_valid(): # Авторизация
            temp_registry_email_id = AccountShelter.objects.filter(email=request.POST.get("login_email"))[0].id
            if AccountShelter.objects.filter(id=temp_registry_email_id)[0].password == AccountShelter.objects.filter(password=request.POST.get("login_password"))[0].password:
                if AccountShelter.objects.filter(id=temp_registry_email_id)[0].register == "Принять":
                    # return {'data': data, 'redirect': redirect("login", rights = f'{request.POST.get("login_email")}&{request.POST.get("login_password")}')} # Где-то ошибка
                    redirectc = redirect("login", rights = f'{request.POST.get("login_email")}&{request.POST.get("login_password")}')
                    data['redirect'] = redirectc
                else:
                    print('Вас ещё не подтвердили')
            else:
                print('Вы ввели не верный логин или пароль')

    else:
        form_login = LoginForm()
        form_registry = RegistryForm()
    return data
    

def index(request):
    collection = Collection.objects.all()
    return render(request, "index.html", {"collection": collection})


def helpPage(request, helpID):
    animal = Collection.objects.get(id=helpID)
    return render(request, "helpPage.html", {"animal": animal})


def support(request):
    shelterAll = AccountShelter.objects.all()
    return render(request, "support.html", {"shelterAll": shelterAll})


def registry(request):
    shelterAll = AccountShelter.objects.all()
    return render(request, "registry.html", {"shelterAll": shelterAll})


def partners(request):
    all_partners = Partners.objects.all()
    return render(request, "partners.html", {"all_partners": all_partners})


def shelters(request):
    shelterAll = AccountShelter.objects.all()
    return render(request, "shelters.html", {"shelterAll": shelterAll})


def shelters_news(request, name_shelter, id_shelter):
    shelter_news = AccountShelter.objects.filter(id=id_shelter)[0]
    print(shelter_news.id, id_shelter)
    return render(request, "shelter_news.html", {"shelter_news": shelter_news})


def login(request, rights):
    temp_rights = rights.split('&')
    temp_registry_email_id = AccountShelter.objects.filter(email=temp_rights[0])[0].id

    new_shelter = AccountShelter.objects.filter(email=temp_rights[0])[0]
    new_collection = Collection()
    new_news = ShelterNews()
    new_report = ShelterReport()

    if AccountShelter.objects.filter(id=temp_registry_email_id)[0].password == AccountShelter.objects.filter(password=temp_rights[1])[0].password:
        name_account = AccountShelter.objects.filter(id=temp_registry_email_id)[0].name
        if request.method == 'POST': 

            # if request.POST.get('delete'): # Удаление питомца
            #     print(1111111111111111)

            form_create_card_shelter = AddRegisterForm(request.POST)
            if form_create_card_shelter.is_valid():
                new_shelter.about = form_create_card_shelter.cleaned_data["about"]
                new_shelter.director_name = form_create_card_shelter.cleaned_data["director_name"]
                new_shelter.contact = form_create_card_shelter.cleaned_data["contact"]
                new_shelter.requisites = form_create_card_shelter.cleaned_data["requisites"]
                new_shelter.social_network = form_create_card_shelter.cleaned_data["social_network"]
                new_shelter.number_of_animals = form_create_card_shelter.cleaned_data["number_of_animals"]
                new_shelter.save()
                return redirect(login, rights)
    
            form_create_card_animal = CreateCardAnimal(request.POST, request.FILES)
            if form_create_card_animal.is_valid():
                new_collection = form_create_card_animal.save(commit=False)
                new_collection.name = form_create_card_animal.cleaned_data["name"]
                new_collection.comment = form_create_card_animal.cleaned_data["comment"]
                new_collection.summ = form_create_card_animal.cleaned_data["summ"]
                new_collection.summ_now = 0
                new_collection.photo = form_create_card_animal.cleaned_data["photo"]
                new_collection.video = form_create_card_animal.cleaned_data["video"]
                new_collection.status = form_create_card_animal.cleaned_data["status"]
                new_collection.breed = form_create_card_animal.cleaned_data["breed"]
                new_collection.gender = form_create_card_animal.cleaned_data["gender"]
                new_collection.age = form_create_card_animal.cleaned_data["age"]
                new_collection.city = AccountShelter.objects.filter(id=temp_registry_email_id)[0].city
                new_collection.choice_shelter = AccountShelter.objects.get(id=temp_registry_email_id)
                new_collection.save()
                new_shelter.number_of_animals += 1
                new_shelter.save()
                return redirect(login, rights)
            
            form_create_news_shelter = CreateNewsShelter(request.POST)
            if form_create_news_shelter.is_valid():
                new_news.name_news = form_create_news_shelter.cleaned_data["name_news"]
                new_news.text_news = form_create_news_shelter.cleaned_data["text_news"]
                new_news.save()
                accoun_for_new_news = AccountShelter.objects.filter(email=temp_rights[0])[0]
                # new_news.add(accoun_for_new_news) # Добавить множество именно к этому объекту
                return redirect(login, rights)
            
            form_hot_email = HotEmail(request.POST)
            if form_hot_email.is_valid():
                email = request.POST.get("email_hot")
                text = request.POST.get("text_hot")
                send_for_email(email, text, "Срочный запрос")
                return redirect(login, rights)

            form_budget_month = BudgetMonth(request.POST, request.FILES)
            if form_budget_month.is_valid():
                budget_money = form_budget_month.cleaned_data["budget_money"]
                if request.FILES:
                    budget_file = request.FILES["budget_file"]
                    with open('static/uploads/files/budget/'+budget_file.name, 'wb+') as destination:  
                        for chunk in budget_file.chunks():  
                            destination.write(chunk)   
                    send_for_email(str(AccountShelter.objects.filter(email=temp_rights[0])[0].name) + ' Необходимая сумма: ' + budget_money,
                                    budget_money, "Отчет от "+str(AccountShelter.objects.filter(email=temp_rights[0])[0].name), 
                                    'static/uploads/files/budget/'+budget_file.name)
                else:
                    send_for_email(str(AccountShelter.objects.filter(email=temp_rights[0])[0].name) + ' Необходимая сумма: ' + budget_money,
                                    budget_money, "Бюджет от "+str(AccountShelter.objects.filter(email=temp_rights[0])[0].name))
                return redirect(login, rights)

            form_new_shelter_report = NewShelterReport(request.POST, request.FILES) 
            if form_new_shelter_report.is_valid():
                company_report = str(AccountShelter.objects.filter(email=temp_rights[0])[0].name)
                new_report.company_report = company_report
                name_report = form_new_shelter_report.cleaned_data["name_report"]
                new_report.name_report = name_report
                text_report = form_new_shelter_report.cleaned_data["text_report"]
                new_report.text_report = text_report
                file_report = form_new_shelter_report.cleaned_data["file_report"]
                new_report.file_report = file_report
                new_report.save()
                send_for_email(name_report,
                                text_report, 
                                "Отчет от "+company_report, 
                                'static/uploads/files/reports/'+file_report.name)

            form_date_visits = DateVisits(request.POST)
            if form_date_visits.is_valid():
                new_date = form_date_visits.cleaned_data['date_visits']
                # new_date.save()
                return redirect(login, rights)

        else:
            form_create_card_shelter = AddRegisterForm()
            form_create_card_animal = CreateCardAnimal()
            form_create_news_shelter= CreateNewsShelter()
            form_date_visits = DateVisits()
            form_hot_email = HotEmail()
            form_budget_month = BudgetMonth()
            form_new_shelter_report = NewShelterReport()
        
        collection = Collection.objects.filter(choice_shelter=AccountShelter.objects.filter(email=temp_rights[0])[0].id)

        return render(request, "login.html", {"rights": rights,
                                            "name_account": name_account,
                                            "form_create_card_shelter": form_create_card_shelter,
                                            "form_create_card_animal": form_create_card_animal,
                                            "form_create_news_shelter": form_create_news_shelter,
                                            "form_date_visits": form_date_visits,
                                            "form_budget_month": form_budget_month,
                                            "form_new_shelter_report": form_new_shelter_report,
                                            "form_hot_email": form_hot_email,
                                            "shelter": new_shelter,
                                            "collection": collection
                                            })
