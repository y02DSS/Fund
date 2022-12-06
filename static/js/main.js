

$('#money_summ').keyup(function() {
    var val = $('#money_summ').val();//Получаем данные из input
    $('#money_summ_view').html('Поддержать на '+ val+' руб');//Вставляем значение в тег с классом txt
});

// Форма со входом и регистрацией
var login_form = document.getElementById("login");

var registry_form = document.getElementById("registry");

var login_user_form = document.getElementById("login_user");
var registry_user_form = document.getElementById("rigistry_user");

var form_name = document.getElementById("form_name");

registry_form.style.display = "none";
login_user_form.style.display = "none"
registry_user_form.style.display = "none"

$("#login_button").on("click", function() { 
    form_name.innerHTML = "Вход для приютов"
    registry_form.style.display = "none"
    login_form.style.display = "block"
});

$("#registry_button").on("click", function() { 
    form_name.innerHTML = "Регистрация для приютов"
    registry_form.style.display = "block"
    login_form.style.display = "none"
});


$(".switch_user_form").on("click", function() { 
    form_name.innerHTML = "Вход для пользователей"
    login_user_form.style.display = "block"
    registry_form.style.display = "none"
    login_form.style.display = "none"
});

$(".switch_shelter_form").on("click", function() { 
    form_name.innerHTML = "Вход для приютов"
    login_form.style.display = "block"
    login_user_form.style.display = "none"
    registry_user_form.style.display = "none"
});


$("#login_user_button").on("click", function() { 
    form_name.innerHTML = "Вход для пользователей"
    registry_user_form.style.display = "none"
    login_user_form.style.display = "block"
});

$("#registry_user_button").on("click", function() { 
    form_name.innerHTML = "Регистрация для пользователей"
    registry_user_form.style.display = "block"
    login_user_form.style.display = "none"
});




// Динамическое отображение нужной формы в login
var all_forms = document.getElementsByName("all_forms")[0];

var onesForm = document.getElementsByClassName("onesForm")[0]

var form_create_card_shelter = document.getElementById("form_create_card_shelter");
var form_create_card_animal = document.getElementById("form_create_card_animal");
var form_change_card_shelter = document.getElementById("form_change_card_shelter");
var form_create_news_shelter = document.getElementById("form_create_news_shelter");
var form_date_visits = document.getElementById("form_date_visits");
var form_hot_email = document.getElementById("form_hot_email");
var form_create_animal_report = document.getElementById("form_create_animal_report");
var form_budget_month = document.getElementById("form_budget_month");
var form_new_shelter_report = document.getElementById("form_new_shelter_report");


// Круговые диаграммы


function drawArc(id, persent){
    var c=document.getElementById(id);
    var ctx=c.getContext("2d");
    ctx.strokeStyle = 'rgb(17, 81, 117)';
    ctx.beginPath();
    var persent_arc = 2*Math.PI * (persent / 100)
    ctx.arc(70,70,57,-1.5,persent_arc-1.5);
    ctx.lineWidth = 13
    ctx.stroke();    
}


$(function(){
    $('canvas[onload]').trigger('onload');
});


$(form_create_card_shelter).on("mouseover", function() { 
    all_forms.id = form_create_card_shelter.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_create_card_shelter').innerHTML;
    // document.getElementById('FORM_form_create_card_shelter').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_create_card_shelter.getElementsByClassName("text")[0].innerHTML

    // Смена реквизитов
    var id_requisites = $('#id_requisites')
    var main_block = document.createElement('div');
    var result = document.getElementById("id_requisites")

    $("#id_choices_type_card_0").on("click", function() { 
        result.value = ""
        $("label[for=id_requisites").text('Введите номер карты:')
        main_block.style.display = 'none'
        main_block.innerHTML = ''
        result.style.display = "block"
    });

    $("#id_choices_type_card_1").on("click", function() { 
        result.value = ""
        main_block.innerHTML = ''

        $("label[for=id_requisites").text('Введите реквизиты:')
        result.style.display = "none"
        main_block.style.display = 'flex'
        main_block.classList = 'row'
        main_block.id = 'result'

        var dict = ["Название организации", "Юридический адрес", "ИНН", "КПП", "ОГРН", "Расчетный счет", "Банк", "ИНН банка", "БИК банка", "Корреспондентский счет", "Юридический адрес банка"]

        for (var i = 0; i < dict.length; i += 1) {
            var label = document.createElement('label')
            label.innerText = dict[i]

            var second_block = document.createElement('div')
            second_block.classList = 'col-6'
            main_block.appendChild(second_block)
            second_block.appendChild(label).appendChild(document.createElement('input'))
        }

        id_requisites.after(main_block)

        var result_field = document.getElementById("result").getElementsByTagName("div")        
 
        $("#submit_result").on("click", function(){
            result.value = ''
            for (var i = 0; i < result_field.length; i += 1) {
                result.value += dict[i] + ": " + String((result_field[i].getElementsByTagName("label")[0].getElementsByTagName("input")[0]).value) + "; ";
            }
        });
    });
});


$(form_create_card_animal).on("mouseover", function() { 
    all_forms.id = form_create_card_animal.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_create_card_animal').innerHTML;
    // document.getElementById('FORM_form_create_card_animal').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_create_card_animal.getElementsByClassName("text")[0].innerHTML
});


$(form_change_card_shelter).on("mouseover", function() { 
    all_forms.id = form_change_card_shelter.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_change_card_shelter').innerHTML;
    // document.getElementById('FORM_form_change_card_shelter').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_change_card_shelter.getElementsByClassName("text")[0].innerHTML
});

$(form_create_news_shelter).on("mouseover", function() { 
    all_forms.id = form_create_news_shelter.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_create_news_shelter').innerHTML;
    // document.getElementById('FORM_form_create_news_shelter').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_create_news_shelter.getElementsByClassName("text")[0].innerHTML
});

$(form_date_visits).on("mouseover", function() { 
    all_forms.id = form_date_visits.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_date_visits').innerHTML;
    // document.getElementById('FORM_form_date_visits').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_date_visits.getElementsByClassName("text")[0].innerHTML
});

$(form_hot_email).on("mouseover", function() { 
    all_forms.id = form_hot_email.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_hot_email').innerHTML;
    // document.getElementById('FORM_form_hot_email').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_hot_email.getElementsByClassName("text")[0].innerHTML
});

$(form_budget_month).on("mouseover", function() { 
    all_forms.id = form_budget_month.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_budget_month').innerHTML;
    // document.getElementById('FORM_form_budget_month').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_budget_month.getElementsByClassName("text")[0].innerHTML;
    var collection_budget = document.getElementById('collection_budget').innerHTML.split('          ');
    for (let i=1; i<collection_budget.length-1; i += 1) {
        document.getElementById('id_budget_money').innerHTML += collection_budget[i].slice(1)
    }
    document.getElementById('id_budget_money').innerHTML += 'Необходимая сумма: ' + document.getElementById('need_summ').innerHTML.slice(1,-9) + ' + (Впишете свое значение)'
});

$(form_new_shelter_report).on("mouseover", function() { 
    all_forms.id = form_new_shelter_report.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_new_shelter_report').innerHTML;
    // document.getElementById('FORM_form_new_shelter_report').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_new_shelter_report.getElementsByClassName("text")[0].innerHTML
});

var close_all_forms = document.getElementsByClassName("close-all-forms")

$(close_all_forms[0]).on("click", function() { 
    document.getElementById('FORM_form_create_card_shelter').style.display = 'none';
    document.getElementById('FORM_form_create_card_animal').style.display = 'none';
    document.getElementById('FORM_form_change_card_animal').style.display = 'none';
    document.getElementById('FORM_form_change_card_shelter').style.display = 'none';
    document.getElementById('FORM_form_create_news_shelter').style.display = 'none';
    document.getElementById('FORM_form_date_visits').style.display = 'none';
    document.getElementById('FORM_form_hot_email').style.display = 'none';
    document.getElementById('FORM_form_create_animal_report').style.display = 'none';
    document.getElementById('FORM_form_budget_month').style.display = 'none';
    document.getElementById('FORM_form_new_shelter_report').style.display = 'none';
});

$(close_all_forms[1]).on("click", function() { 
    document.getElementById('FORM_form_create_card_shelter').style.display = 'none';
    document.getElementById('FORM_form_create_card_animal').style.display = 'none';
    document.getElementById('FORM_form_change_card_animal').style.display = 'none';
    document.getElementById('FORM_form_change_card_shelter').style.display = 'none';
    document.getElementById('FORM_form_create_news_shelter').style.display = 'none';
    document.getElementById('FORM_form_date_visits').style.display = 'none';
    document.getElementById('FORM_form_hot_email').style.display = 'none';
    document.getElementById('FORM_form_create_animal_report').style.display = 'none';
    document.getElementById('FORM_form_budget_month').style.display = 'none';
    document.getElementById('FORM_form_new_shelter_report').style.display = 'none';
    
});


$(window).scroll(function(){
    if($(window).scrollTop()>300){
    $('#elem').show()
    }
})


// Регистрация
$('#registry').on('closed.bs.alert', function () {
    setTimeout("alert('Привет')", 1000);
})


// Чат в личном кабинете
var close_chat = document.getElementById("hidden_chat")
$(close_chat).on('click', function(){
    document.getElementsByClassName("chat-form")[0].style.display="none"
    document.getElementsByClassName("close-chat-form")[0].style.display="block"
})

var open_chat = document.getElementById("open_chat")
$(open_chat).on('click', function(){
    document.getElementsByClassName("chat-form")[0].style.display="block"
    document.getElementsByClassName("close-chat-form")[0].style.display="none"
})


// Фильтрация животных
var cards_animal = document.getElementById('cards_animal')

var select_shelter = document.getElementById('select_shelter')

$(select_shelter).on("click", function() { 
    document.getElementById("first_city").selected = true

    var $this = $(this);
    
    if ($this.hasClass('open')) {
        var shelter = document.getElementsByClassName('card_animal');
        for (i=0; i<shelter.length; i++) {
            if ($this.val() == "Все приюты"){
                shelter[i].style.display = 'block';

            } else if (shelter[i].getAttribute("name").split("+")[0] != $this.val()){
                shelter[i].style.display = 'none'; 
                         
            } else {
                shelter[i].style.display = 'block';
            }
        };
        $this.removeClass('open');

    }else {
        $this.addClass('open');
    }
});


var select_city = document.getElementById('select_city')

$(select_city).on("click", function() { 
    document.getElementById("first_shelter").selected = true

    var $this = $(this);
    
    if ($this.hasClass('open')) {
        var shelter = document.getElementsByClassName('card_animal');
        for (i=0; i<shelter.length; i++) {
            if ($this.val() == "Все города"){
                shelter[i].style.display = 'block';

            } else if (shelter[i].getAttribute("name").split("+")[1] != $this.val()){
                shelter[i].style.display = 'none'; 
                         
            } else {
                shelter[i].style.display = 'block';
            }
        };
        $this.removeClass('open');

    }else {
        $this.addClass('open');
    }
});


// Плавное появление элементов
function onEntry(entry) {
    entry.forEach(change => {
      if (change.isIntersecting) {
       change.target.classList.add('element-show');
      }
    });
}
  
let options = {
    threshold: [0.5] 
};
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.element-animation');

for (let elm of elements) {
    observer.observe(elm);
}


// отображение форм редактировать и отчет

function load_change(id, url){
    axios.get(`${url}/${String(id)}`)
    .then(function (response) {
        var updated_document = document.createElement("html");

        updated_document.innerHTML = response.data;

        form_change_card_animal = document.getElementById(`animal_card_${String(id)}`);
        form_element = updated_document.querySelector("#FORM_form_change_card_animal");
        onesForm.innerHTML = form_element.innerHTML;
        document.getElementById('NameLabel').innerHTML = "Редактировать";

        onesForm.innerHTML += `<input type="text" value="${String(id)}" name="id" maxlength="200" style="display: none" id="id_change">`;

        all_forms.id = "ChangeCardAnimal";
        $("#ChangeCardAnimal").modal("show");
    })
    .catch(function (error) {
        console.log(error);
    });

};

function load_report(id, url){
    axios.get(`${url}&animalReport_${String(id)}`)
    .then(function (response) {
        var updated_document = document.createElement("html");

        updated_document.innerHTML = response.data;

        form_change_card_animal = document.getElementById(`report_animal_card_${String(id)}`);
        form_element = updated_document.querySelector("#FORM_form_create_animal_report");
        onesForm.innerHTML = form_element.innerHTML;
        document.getElementById('NameLabel').innerHTML = "Отчет";

        onesForm.innerHTML += `<input type="text" value="${String(id)}" name="new_animal_report_id" maxlength="200" style="display: none" id="id_report">`;

        all_forms.id = "CreateAnimalReport";
        $("#CreateAnimalReport").modal("show");
    })
    .catch(function (error) {
        console.log(error);
    });

};

// Многострочная вставка в placeholder
document.getElementById("id_date_visits").placeholder = 'Понедельник - 8:30-17:00' + '\n' + 
                                                        'Вторник - 8:30-17:00' + '\n' +
                                                        'Среда - 8:30-17:00' + '\n' +
                                                        'Четверг - 8:30-17:00' + '\n' +
                                                        'Пятница - 8:30-17:00' + '\n' +
                                                        'Суббота - не работаем' + '\n' +
                                                        'Воскресенье - не работаем' + '\n' 





