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
