$('#money_summ').keyup(function() {
    var val = $('#money_summ').val();//Получаем данные из input
    $('#money_summ_view').html('Поддержать на '+ val+' руб');//Вставляем значение в тег с классом txt
});


// Форма со входом и регистрацией
var login_form = document.getElementById("login");
var registry_form = document.getElementById("registry");
var form_name = document.getElementById("form_name");

registry_form.style.display = "none";

document.getElementById("login_button").onclick = function() {
    form_name.innerHTML = "Вход"
    registry_form.style.display = "none"
    login_form.style.display = "block"
};

document.getElementById("registry_button").onclick = function() {
    form_name.innerHTML = "Регистрация"
    registry_form.style.display = "block"
    login_form.style.display = "none"
};

// Динамическое отображение нужной формы в login
var all_forms = document.getElementsByName("all_forms")[0];

var onesForm = document.getElementsByClassName("onesForm")[0]

// const forms = ["form_create_card_shelter", "form_create_card_animal"];

// for (let i = 0; i < forms.length; i += 1) {
//     const index = document.getElementById(forms[i]);
//     $(index).on("click", function() { 
//         all_forms.id = index.getAttribute("data-bs-target").slice(1);
//         onesForm.innerHTML = document.getElementById('FORM_${forms[i]}').innerHTML;
//         document.getElementById('FORM_${forms[i]}').style.display = 'block';
//         document.getElementById('NameLabel').innerHTML = index.innerHTML
//     });
// }



var form_create_card_shelter = document.getElementById("form_create_card_shelter");
var form_create_card_animal = document.getElementById("form_create_card_animal");
var form_create_news_shelter = document.getElementById("form_create_news_shelter");
var form_date_visits = document.getElementById("form_date_visits");

$(form_create_card_shelter).on("click", function() { 
    all_forms.id = form_create_card_shelter.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_create_card_shelter').innerHTML;
    document.getElementById('FORM_form_create_card_shelter').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_create_card_shelter.innerHTML
});


$(form_create_card_animal).on("click", function() { 
    all_forms.id = form_create_card_animal.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_create_card_animal').innerHTML;
    document.getElementById('FORM_form_create_card_animal').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_create_card_animal.innerHTML
});


$(form_create_news_shelter).on("click", function() { 
    all_forms.id = form_create_news_shelter.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_create_news_shelter').innerHTML;
    document.getElementById('FORM_form_create_news_shelter').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_create_news_shelter.innerHTML
});


$(form_date_visits).on("click", function() { 
    all_forms.id = form_date_visits.getAttribute("data-bs-target").slice(1);
    onesForm.innerHTML = document.getElementById('FORM_form_date_visits').innerHTML;
    document.getElementById('FORM_form_date_visits').style.display = 'block';
    document.getElementById('NameLabel').innerHTML = form_date_visits.innerHTML
});


close_all_forms = document.getElementsByClassName("close-all-forms")

$(close_all_forms[0]).on("click", function() { 
    document.getElementById('FORM_form_create_card_shelter').style.display = 'none';
    document.getElementById('FORM_form_create_card_animal').style.display = 'none';
    document.getElementById('FORM_form_create_news_shelter').style.display = 'none';
    document.getElementById('FORM_form_date_visits').style.display = 'none';
});
