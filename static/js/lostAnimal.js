// Фильтрация животных
$("#all_filters").on("mouseover", function() { 
    var lost_cards_shelters = ($("#lost_cards_shelters").val())
    var lost_cards_city = ($("#lost_cards_city").val())

    var shelter = document.getElementsByClassName('card_animal');
    
    for (i=0; i<shelter.length; i++){
        if (lost_cards_city == "Все города"){
            if (lost_cards_shelters == "Все приюты"){
                shelter[i].style.display = "block"

            } else if (lost_cards_shelters == shelter[i].getAttribute("name").split("+")[0]){
                shelter[i].style.display = "block"

            } else {
                shelter[i].style.display = "none"
            }            
        }
        else{
            if (lost_cards_shelters == "Все приюты" & lost_cards_city == shelter[i].getAttribute("name").split("+")[1]){
                shelter[i].style.display = "block"

            } else if (lost_cards_shelters == shelter[i].getAttribute("name").split("+")[0] & lost_cards_city == shelter[i].getAttribute("name").split("+")[1]){
                shelter[i].style.display = "block"

            } else {
                shelter[i].style.display = "none"
            } 
        }
    }
});

// $("#lost_cards_city").on("click", function() { 
//     var lost_cards_shelters = ($("#lost_cards_shelters").val())
//     var lost_cards_city = ($("#lost_cards_city").val())
//     console.log(lost_cards_city)

//     var shelter = document.getElementsByClassName('card_animal');
    
//     for (i=0; i<shelter.length; i++){
//         if (lost_cards_shelters == "Все приюты"){
//             if (lost_cards_city == "Все города"){
//                 shelter[i].style.display = "block"
//             } else if (lost_cards_city == shelter[i].getAttribute("name").split("+")[1]){
//                 shelter[i].style.display = "block"
//             } else {
//                 shelter[i].style.display = "none"
//             }            
//         }
//     }
// });