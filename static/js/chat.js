function ajax_chat(rights) {
    setTimeout(() => {
        $.ajax({url: rights, success: function(result){
            var finish_result = document.getElementById("chat")
                finish_result.innerHTML = ''
                var result_temp = result.split("$")
                result_temp.pop()
                for (i=0; i<result_temp.length; i++) {
                    if (i % 2 !== 0) {
                        continue;
                    }
                    var teg_p = document.createElement("p");
                    var teg_span = document.createElement("span");
                    teg_span.innerHTML = result_temp[i] + ': ';
                    teg_p.appendChild(teg_span);
                    teg_p.innerHTML += result_temp[i+1]
                    finish_result.appendChild(teg_p);
                };
        }});
        ajax_chat(rights)
    }, "5000")
}

$(document).ready(function () {
    var rights = document.getElementById("rights").innerHTML.replace('amp;', '');
    ajax_chat(rights)
});

// Многострочная вставка в placeholder
document.getElementById("id_date_visits").placeholder = 'Понедельник - 8:30-17:00' + '\n' + 
                                                        'Вторник - 8:30-17:00' + '\n' +
                                                        'Среда - 8:30-17:00' + '\n' +
                                                        'Четверг - 8:30-17:00' + '\n' +
                                                        'Пятница - 8:30-17:00' + '\n' +
                                                        'Суббота - не работаем' + '\n' +
                                                        'Воскресенье - не работаем' + '\n' 





