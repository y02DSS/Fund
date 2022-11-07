$('#money_summ').keyup(function() {
    var val = $('#money_summ').val();//Получаем данные из input
    $('#money_summ_view').html('Поддержать на '+ val+' руб');//Вставляем значение в тег с классом txt
});


// Форма со входом и регистрацией
var login_form = document.getElementById("login");
var registry_form = document.getElementById("registry");
var form_name = document.getElementById("form_name");

registry_form.style.display = "none";

var login_button = document.getElementById("login_button")
$(login_button).on("click", function() { 
    form_name.innerHTML = "Вход"
    registry_form.style.display = "none"
    login_form.style.display = "block"
});

var form_create_card_shelter_registry = document.getElementById("registry_button")
$(form_create_card_shelter_registry).on("click", function() { 
    form_name.innerHTML = "Регистрация"
    registry_form.style.display = "block"
    login_form.style.display = "none"
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

$(form_create_card_shelter).on("mouseover", function() { 
    all_forms.id = form_create_card_shelter.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_create_card_shelter').innerHTML;
    // document.getElementById('FORM_form_create_card_shelter').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_create_card_shelter.innerHTML

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
    document.getElementById('NameLabel').innerHTML = form_create_card_animal.innerHTML
});


$(form_change_card_shelter).on("mouseover", function() { 
    all_forms.id = form_change_card_shelter.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_change_card_shelter').innerHTML;
    // document.getElementById('FORM_form_change_card_shelter').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_change_card_shelter.innerHTML
});

$(form_create_news_shelter).on("mouseover", function() { 
    all_forms.id = form_create_news_shelter.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_create_news_shelter').innerHTML;
    // document.getElementById('FORM_form_create_news_shelter').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_create_news_shelter.innerHTML
});

$(form_date_visits).on("mouseover", function() { 
    all_forms.id = form_date_visits.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_date_visits').innerHTML;
    // document.getElementById('FORM_form_date_visits').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_date_visits.innerHTML
});

$(form_hot_email).on("mouseover", function() { 
    all_forms.id = form_hot_email.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_hot_email').innerHTML;
    // document.getElementById('FORM_form_hot_email').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_hot_email.innerHTML
});

$(form_budget_month).on("mouseover", function() { 
    all_forms.id = form_budget_month.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_budget_month').innerHTML;
    // document.getElementById('FORM_form_budget_month').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_budget_month.innerHTML;
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
    document.getElementById('NameLabel').innerHTML = form_new_shelter_report.innerHTML
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


//Отображение срочных запросов на странице helpPage
var hotReport_text = document.getElementsByClassName("hotReport-text")
var hotReport_line = document.getElementById("hotReport_line")
var hotReport_text_render = document.getElementsByClassName("hotReport-text-render")
hotReport_text[0].className = "hotReport-text hotReport-text-active";

hotReport_line.appendChild(hotReport_text_render[0].firstElementChild.cloneNode(true))

var arr_hotReport_text = [];
for(i=0; i<hotReport_text.length; ++i) {
	arr_hotReport_text.push(hotReport_text[i].innerHTML);
}

document.getElementById("hotReport_text").addEventListener('click', (event) => {
    let target = event.target; 
    var val = arr_hotReport_text.indexOf(target.innerHTML)

    for(i=0; i<hotReport_text.length; ++i) {
        hotReport_text[i].className = "hotReport-text";
    }

    target.className = "hotReport-text hotReport-text-active";
    hotReport_line.innerHTML = ''
    return hotReport_line.appendChild(hotReport_text_render[val].firstElementChild.cloneNode(true));

});


var Report_animals_text = document.getElementsByClassName("Report_animals-text")
var Report_animals_line = document.getElementById("Report_animals_line")
var Report_animals_text_render = document.getElementsByClassName("Report_animals-text-render")
Report_animals_text[0].className = "Report_animals-text Report_animals-text-active";

Report_animals_line.appendChild(Report_animals_text_render[0].firstElementChild.cloneNode(true))

var arr_Report_animals_text = [];
for(i=0; i<Report_animals_text.length; ++i) {
	arr_Report_animals_text.push(Report_animals_text[i].innerHTML);
}

document.getElementById("Report_animals").addEventListener('click', (event) => {
    let target = event.target; 
    var val = arr_Report_animals_text.indexOf(target.innerHTML)

    for(i=0; i<Report_animals_text.length; ++i) {
        Report_animals_text[i].className = "Report_animals-text";
    }

    target.className = "Report_animals-text Report_animals-text-active";
    Report_animals_line.innerHTML = ''
    return Report_animals_line.appendChild(Report_animals_text_render[val].firstElementChild.cloneNode(true));
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
threshold: [0.5] };
let observer = new IntersectionObserver(onEntry, options);
let elements = document.querySelectorAll('.element-animation');

for (let elm of elements) {
observer.observe(elm);
}


// отображение форм редактировать и отчет
var domParser = new DOMParser()

function load_change(id, url){

    axios.get(`${url}&animalCard_${String(id)}`)
    .then(function (response) {
        var updated_document = document.createElement("html");

        updated_document.innerHTML = response.data;

        form_change_card_animal = document.getElementById(`animal_card_${String(id)}`);
        form_element = updated_document.querySelector("#FORM_form_change_card_animal");
        onesForm.innerHTML = form_element.innerHTML;
        document.getElementById('NameLabel').innerHTML = "Редактировать";

        onesForm.innerHTML += `<input type="text" value="${String(id)}" name="id" maxlength="200" style="display: none" id="id_id">`;

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

        onesForm.innerHTML += `<input type="text" value="${String(id)}" name="new_animal_report_id" maxlength="200" style="display: none" id="id_id">`;

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





