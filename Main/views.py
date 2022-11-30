from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, RegistryForm, CreateCardAnimal, CreateNewsShelter, DateVisits, AddRegisterForm, HotEmail, \
    BudgetMonth, NewShelterReport, FormLostAnimals, FormChatLogin, FormTakeAnimal, ShelterHotReport, ChangeCardAnimal, \
    CreateAnimalReport, LoginFormUser, RegistryFormUser
from .models import Collection, Partners, ShelterAccount, ShelterNews, ShelterReport, LostAnimals, ChatLogin, \
    TakeAnimal, AnimalReport, UserAccount
from .send_email import send_for_email


def inject_form(request):  # Работает на всех страницах
    data = {}
    data["info_check"] = 0

    data["form_login"] = LoginForm()
    data["form_registry"] = RegistryForm()

    data["form_login_user"] = LoginFormUser()
    data["form_rigistry_user"] = RegistryFormUser()

    form_registry_add = ShelterAccount()
    form_registry_user_add = UserAccount()

    if request.method == 'POST':
        # Авторизация

        # form_login_user = LoginFormUser(request.POST)
        try:
            temp_registry_user_email_id = UserAccount.objects.get(email_user=request.POST.get('email_user')).id
            if UserAccount.objects.get(id=temp_registry_user_email_id).password_user == request.POST.get(
                    'password_user'):
                if UserAccount.objects.get(id=temp_registry_user_email_id).register_user == "Принять":
                    redirectc = redirect("login_user",
                                         rights=f'{request.POST.get("email_user")}&{request.POST.get("password_user")}')
                    data['redirect'] = redirectc
                else:
                    data["info_check"] = 2
            else:
                data["info_check"] = 3
        except:
            pass

        form_login = LoginForm(request.POST)
        if form_login.is_valid():
            try:
                temp_registry_email_id = ShelterAccount.objects.filter(email=request.POST.get("login_email"))[0].id
                if ShelterAccount.objects.filter(id=temp_registry_email_id)[0].password == \
                        ShelterAccount.objects.filter(password=request.POST.get("login_password"))[0].password:
                    if ShelterAccount.objects.filter(id=temp_registry_email_id)[0].register == "Принять":
                        redirectc = redirect("login",
                                             rights=f'{request.POST.get("login_email")}&{request.POST.get("login_password")}')
                        # data = {}
                        data['redirect'] = redirectc
                    else:
                        data["info_check"] = 2
                else:
                    data["info_check"] = 3
            except:
                pass

        # Регистрация
        form_registry = RegistryForm(request.POST)
        if form_registry.is_valid():
            form_registry_add.username = form_registry.cleaned_data['username']
            form_registry_add.email = form_registry.cleaned_data['email']
            form_registry_add.password = form_registry.cleaned_data['password']
            form_registry_add.city = form_registry.cleaned_data['city']
            form_registry_add.address = form_registry.cleaned_data['address']
            form_registry_add.save()
            send_for_email('', str(request.POST.get("name")),
                           f"http://xn-----6kcsebroh5bqkw3c.xn--p1ai/admin/Main/accountshelter/{form_registry_add.id}/change/",
                           "Новая регистрация приюта")
            data["info_check"] = 1
            return data
        # else:
        #     data["info_check"] = 4

        form_registry_user = RegistryFormUser(request.POST)
        if form_registry_user.is_valid():
            form_registry_user_add.name_user = form_registry_user.cleaned_data['username']
            form_registry_user_add.email_user = form_registry_user.cleaned_data['email']
            form_registry_user_add.password_user = form_registry_user.cleaned_data['password']

            try:
                form_registry_user_add.save()
            except IntegrityError:
                data["info_check"] = 4
                return data

            send_for_email('', str(request.POST.get("username")),
                           f"http://xn-----6kcsebroh5bqkw3c.xn--p1ai/admin/Main/accountuser/{form_registry_add.id}/change/",
                           "Новая регистрация пользователя")
            data["info_check"] = 1
            User.objects.create_user(form_registry_user_add.username, form_registry_user_add.email,
                                                form_registry_user_add.username)
        # else:
        #     data["info_check"] = 4
    return data


def index(request):
    collection = Collection.objects.filter(status="В приюте")
    shelterAll = ShelterAccount.objects.all()
    all_partners = Partners.objects.all()
    citys = []
    for city in shelterAll:
        if city.city not in citys:
            citys.append(city.city)
    return render(request, "index.html",
                  {"collection": collection[:3], "shelterAll": shelterAll, "all_partners": all_partners,
                   "citys": len(citys)})


def allAnimals(request):
    collection = Collection.objects.filter(status="В приюте")
    all_shelters = ShelterAccount.objects.all()
    cities = []
    for city in all_shelters:
        if city.city not in cities:
            cities.append(city.city)
    animal_shelters = []
    for shelter in all_shelters:
        animal_shelters.append(shelter)
    return render(request, "allAnimals.html", {"collection": collection,
                                               "citys": cities,
                                               "shelters": animal_shelters})


def helpPage(request, help_id):
    animal = Collection.objects.get(id=help_id)

    new_take_animal = TakeAnimal()

    shelter = ShelterAccount.objects.get(id=animal.choice_shelter.id)

    animalReports = animal.animalReport

    if request.method == 'POST':
        form_take_animal = FormTakeAnimal(request.POST)
        if form_take_animal.is_valid():
            name = form_take_animal.cleaned_data['name']
            new_take_animal.name = name
            contact = form_take_animal.cleaned_data['contact']
            new_take_animal.contact = contact
            city = form_take_animal.cleaned_data['city']
            new_take_animal.city = city
            new_take_animal.save()
            animal.is_take = new_take_animal.id
            animal.save()
            shelter = animal.choice_shelter
            send_for_email(shelter.email, f"http://xn-----6kcsebroh5bqkw3c.xn--p1ai/help/{animal.id}",
                           f'Хочет забрать {name} из города {city}, контакты: {contact}',
                           f"Хотят забрать {new_take_animal.name}")
            return redirect(helpPage, help_id)
    else:
        form_take_animal = FormTakeAnimal()

    return render(request, "helpPage.html", {"animal": animal, "form_take_animal": form_take_animal, "shelter": shelter,
                                             "animalReports": animalReports})


def lostAnimal(request):
    lostAnimals = LostAnimals.objects.all()[::-1]
    breedAnimals = []
    cityAnimals = []
    for animal in lostAnimals:
        if animal.breed not in breedAnimals:
            breedAnimals.append(animal.breed)
        if animal.city not in cityAnimals:
            cityAnimals.append(animal.city)

    return render(request, "lostAnimal.html",
                  {"lostAnimals": lostAnimals, "breedAnimals": breedAnimals, "cityAnimals": cityAnimals})


def newLostAnimal(request):
    info_check_animal = 0
    form_lostAnimals = LostAnimals()
    newLostAnimal = FormLostAnimals(request.POST, request.FILES)
    if newLostAnimal.is_valid():  # Регистрация
        key = request.POST.get('key')
        try:
            check_key = UserAccount.objects.get(key=key).key_used
            if check_key > 0:
                UserAccount.objects.update(key_used=check_key - 1)
                form_lostAnimals.photo = request.FILES["photo"]
                form_lostAnimals.city = request.POST.get("city")
                if request.POST.get("breed") != "":
                    form_lostAnimals.breed = request.POST.get("breed")
                else:
                    form_lostAnimals.breed = "Не определена"
                form_lostAnimals.contact = request.POST.get("contact")
                form_lostAnimals.description = request.POST.get("description")
                form_lostAnimals.save()
            else:
                info_check_animal = 1
        except:
            info_check_animal = 2

    return render(request, "newLostAnimal.html",
                  {"newLostAnimal": newLostAnimal, "info_check_animal": info_check_animal})


def fullLostAnimal(request, lostID):
    lostAnimal = LostAnimals.objects.get(id=lostID)
    return render(request, "fullLostAnimal.html", {"lostAnimal": lostAnimal})


def support(request):
    shelterAll = ShelterAccount.objects.all()
    return render(request, "support.html", {"shelterAll": shelterAll})


def partners(request):
    all_partners = Partners.objects.all()
    return render(request, "partners.html", {"all_partners": all_partners})


def archive(request):
    collection_taken = Collection.objects.filter(status='Забрали')
    collection_archive = Collection.objects.filter(status='Другая причина')
    collection_died = Collection.objects.filter(status='Умер')
    return render(request, "archive.html",
                  {"collection_taken": collection_taken, "collection_archive": collection_archive,
                   "collection_died": collection_died})


def archive_animal(request, helpID):
    animal = Collection.objects.get(id=helpID)
    return render(request, "archiveAnimal.html", {"animal": animal})


def about(request):
    all_partners = Partners.objects.all()
    return render(request, "about.html", {"all_partners": all_partners})


def volunteers(request):
    all_partners = Partners.objects.all()
    return render(request, "volunteers.html", {"all_partners": all_partners})


def shelters(request):
    shelterAll = ShelterAccount.objects.all()
    return render(request, "shelters.html", {"shelterAll": shelterAll})


def shelters_news(request, name_shelter, id_shelter):
    shelter_news = ShelterAccount.objects.filter(id=id_shelter)[0]
    return render(request, "shelter_news.html", {"shelter_news": shelter_news})


def shelter_reports(request, name_shelter, id_shelter):
    shelter_reports = ShelterReport.objects.filter(company_report=name_shelter)
    return render(request, "shelterReports.html", {"shelter_reports": shelter_reports, "name_shelter": name_shelter})


def shelter_animals(request, name_shelter, id_shelter):
    shelter_collection = Collection.objects.filter(choice_shelter=id_shelter)
    return render(request, "shelterAnimals.html",
                  {"shelter_collection": shelter_collection, "name_shelter": name_shelter})


# @login_required
def login_user(request, rights):
    temp_user_rights = rights.split('&')
    account_user = UserAccount.objects.filter(email_user=temp_user_rights[0])[0]

    return render(request, "loginUser.html", {"rights": rights, "account_user": account_user})


@login_required
def login(request, rights):
    temp_rights = rights.split('&')

    card_id = None
    form_change_card_animal = None
    new_animal_report_id = None

    try:
        card_id = temp_rights[2]
        temp_card_id = card_id.split("_")
        if temp_card_id[0] == "animalCard":
            change_card_animal_id = int(temp_card_id[1])
            change_card_animal = Collection.objects.filter(id=change_card_animal_id)[0]
        elif temp_card_id[0] == "animalReport":
            new_animal_report_id = int(temp_card_id[1])
    except IndexError:
        pass

    temp_registry_email_id = ShelterAccount.objects.filter(email=temp_rights[0])[0].id

    new_shelter = ShelterAccount.objects.filter(email=temp_rights[0])[0]
    new_collection = Collection()
    new_news = ShelterNews()
    new_report = ShelterReport()
    new_messages_chat = ChatLogin()
    new_hot_report = ShelterHotReport()
    new_animal_report = AnimalReport()

    collection_budget = Collection.objects.filter(choice_shelter=new_shelter)
    need_summ = 0
    for animal_budget in collection_budget:
        need_summ += animal_budget.summ

    if ShelterAccount.objects.filter(id=temp_registry_email_id)[0].password == \
            ShelterAccount.objects.filter(password=temp_rights[1])[0].password:
        name_account = ShelterAccount.objects.filter(id=temp_registry_email_id)[0].username
        if request.method == 'POST':
            if request.POST.get("id") is not None:
                form_change_card_animal = ChangeCardAnimal(request.POST, request.FILES)
                if form_change_card_animal.is_valid():
                    temp_request_id = request.POST["id"]
                    Collection.objects.filter(id=temp_request_id).update(**form_change_card_animal.cleaned_data)
                    if 'photo' in form_change_card_animal.changed_data:
                        with open(f'static/img/cardsAnimal/{form_change_card_animal.cleaned_data["photo"]}',
                                  'wb+') as destination:
                            for chunk in form_change_card_animal.cleaned_data["photo"].chunks():
                                destination.write(chunk)
                        Collection.objects.filter(id=temp_request_id).update(
                            photo=f'static/img/cardsAnimal/{form_change_card_animal.cleaned_data["photo"]}')
                    if 'video' in form_change_card_animal.changed_data:
                        Collection.objects.filter(id=temp_request_id).update(
                            video=f'static/video/cardsAnimal/{form_change_card_animal.cleaned_data["video"]}')
            else:
                form_create_card_animal = CreateCardAnimal(request.POST, request.FILES)
                if form_create_card_animal.is_valid():
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
                    new_collection.city = ShelterAccount.objects.filter(id=temp_registry_email_id)[0].city
                    new_collection.choice_shelter = ShelterAccount.objects.get(id=temp_registry_email_id)
                    new_collection.save()
                    ShelterAccount.objects.filter(email=temp_rights[0]).update(
                        number_of_animals=new_shelter.number_of_animals + 1)
                    return redirect(login, rights)

            if request.POST.get("new_animal_report_id", "False"):
                form_create_animal_report = CreateAnimalReport(request.POST, request.FILES)
                if form_create_animal_report.is_valid():
                    this_collection = Collection.objects.get(
                        id=request.POST["new_animal_report_id"])  # передать тот же самый ID
                    new_animal_report.name_animal = this_collection.name
                    new_animal_report.report_animal = form_create_animal_report.cleaned_data["report_animal"]
                    new_animal_report.text_animal = form_create_animal_report.cleaned_data["text_animal"]
                    new_animal_report.file_animal = form_create_animal_report.cleaned_data["file_animal"]
                    new_animal_report.save()
                    this_collection.animalReport.add(new_animal_report)

            form_hot_email = HotEmail(request.POST)
            if form_hot_email.is_valid():
                name = form_hot_email.cleaned_data["name_hot"]
                new_hot_report.name_hot = name
                text = form_hot_email.cleaned_data["text_hot"]
                new_hot_report.text_hot = text
                new_hot_report.save()
                new_shelter.hotReport.add(new_hot_report)
                send_for_email('', str(name), text, "Срочный запрос " + str(new_shelter.name))
                return redirect(login, rights)

            form_create_card_shelter = AddRegisterForm(request.POST, request.FILES, instance=new_shelter)
            if form_create_card_shelter.is_valid():
                new_shelter = form_create_card_shelter.save(commit=False)
                new_shelter.about = form_create_card_shelter.cleaned_data["about"]
                new_shelter.director_name = form_create_card_shelter.cleaned_data["director_name"]
                new_shelter.contact = form_create_card_shelter.cleaned_data["contact"]
                new_shelter.requisites = form_create_card_shelter.cleaned_data["requisites"]
                new_shelter.social_network = form_create_card_shelter.cleaned_data["social_network"]
                new_shelter.number_of_animals = form_create_card_shelter.cleaned_data["number_of_animals"]
                new_shelter.logo = form_create_card_shelter.cleaned_data["logo"]
                new_shelter.save()
                return redirect(login, rights)

            form_create_news_shelter = CreateNewsShelter(request.POST)
            if form_create_news_shelter.is_valid():
                new_news.name_news = form_create_news_shelter.cleaned_data["name_news"]
                new_news.text_news = form_create_news_shelter.cleaned_data["text_news"]
                new_news.save()
                new_shelter.news.add(new_news)  # Добавить множество именно к этому объекту
                return redirect(login, rights)

            form_budget_month = BudgetMonth(request.POST, request.FILES)
            if form_budget_month.is_valid():
                budget_money = form_budget_month.cleaned_data["budget_money"]
                if request.FILES:
                    budget_file = request.FILES["budget_file"]
                    with open('static/uploads/files/budget/' + budget_file.name, 'wb+') as destination:
                        for chunk in budget_file.chunks():
                            destination.write(chunk)
                    send_for_email('', str(ShelterAccount.objects.filter(email=temp_rights[0])[
                                               0].name) + ' Необходимая сумма: ' + budget_money,
                                   budget_money,
                                   "Бюджет от " + str(ShelterAccount.objects.filter(email=temp_rights[0])[0].name),
                                   'static/uploads/files/budget/' + budget_file.name)
                else:
                    send_for_email('', str(ShelterAccount.objects.filter(email=temp_rights[0])[
                                               0].name) + ' Необходимая сумма: ' + budget_money,
                                   budget_money,
                                   "Бюджет от " + str(ShelterAccount.objects.filter(email=temp_rights[0])[0].name))
                return redirect(login, rights)

            form_new_shelter_report = NewShelterReport(request.POST, request.FILES)
            if form_new_shelter_report.is_valid():
                company_report = str(ShelterAccount.objects.filter(email=temp_rights[0])[0].name)
                new_report.company_report = company_report
                name_report = form_new_shelter_report.cleaned_data["name_report"]
                new_report.name_report = name_report
                text_report = form_new_shelter_report.cleaned_data["text_report"]
                new_report.text_report = text_report
                file_report = form_new_shelter_report.cleaned_data["file_report"]
                new_report.file_report = file_report
                new_report.save()
                send_for_email('',
                               name_report,
                               text_report,
                               "Отчет от " + company_report,
                               'static/uploads/files/reports/' + file_report.name)
                return redirect(login, rights)

            form_chat = FormChatLogin(request.POST)
            if form_chat.is_valid():
                new_messages_chat.name = new_shelter.city
                new_messages_chat.text = form_chat.cleaned_data['text']
                new_messages_chat.save()
                return redirect(login, rights)

            form_date_visits = DateVisits(request.POST)
            if form_date_visits.is_valid():
                temp_dates = form_date_visits.cleaned_data['date_visits']
                if temp_dates != "":
                    ShelterAccount.objects.filter(id=temp_registry_email_id).update(
                        date_visits=form_date_visits.cleaned_data['date_visits'])
                return redirect(login, rights)


        else:
            form_create_card_shelter = AddRegisterForm(instance=new_shelter)
            form_create_card_animal = CreateCardAnimal()

            if card_id:
                if card_id.split("_")[0] == "animalCard":
                    form_change_card_animal = ChangeCardAnimal(instance=change_card_animal)
            # form_change_card_animal = ChangeCardAnimal()

            form_create_animal_report = CreateAnimalReport()
            form_create_news_shelter = CreateNewsShelter()
            form_date_visits = DateVisits(instance=new_shelter)
            form_hot_email = HotEmail()
            form_chat = FormChatLogin()
            form_budget_month = BudgetMonth()
            form_new_shelter_report = NewShelterReport()

        messages_chat = ChatLogin.objects.all()
        collection = Collection.objects.filter(choice_shelter=ShelterAccount.objects.filter(email=temp_rights[0])[0].id)

        if request.is_ajax():
            temp_chat = ''
            messages_chat = ChatLogin.objects.all()
            for message in messages_chat:
                temp_chat += message.name + '$' + message.text + '$'
            return HttpResponse(temp_chat)

        return render(request, "login.html", {"rights": rights,
                                              "name_account": name_account,
                                              "form_create_card_shelter": form_create_card_shelter,
                                              "form_create_card_animal": form_create_card_animal,
                                              "form_change_card_animal": form_change_card_animal,
                                              "form_create_news_shelter": form_create_news_shelter,
                                              "form_date_visits": form_date_visits,
                                              "form_budget_month": form_budget_month,
                                              "form_new_shelter_report": form_new_shelter_report,
                                              "form_hot_email": form_hot_email,
                                              "form_create_animal_report": form_create_animal_report,
                                              "form_chat": form_chat,
                                              "shelter": new_shelter,
                                              "collection": collection,
                                              "collection_budget": collection_budget,
                                              "need_summ": need_summ,
                                              "messages_chat": messages_chat
                                              })
