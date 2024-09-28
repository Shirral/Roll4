//initialize sidenav
$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
});

$( "#categoryp" ).on( "click", function() {
    $( "#categoryselect" ).toggle("slow");
});

$( ".notesbtn" ).on( "click", function() {
    let divs = document.getElementsByClassName("notesbtn");
    let len = divs.length;
    let num;
    for (var i = 1; i <= len; i++){
        if (this.id == "notesbtn"+i){
            num = i;
            break;
        } 
    }

    $(".notesview").each(function(i, notediv) {
        if ($(notediv).find("p").html().trim() == "") {
            $(notediv).removeAttr("id");
          }
    });

    $( "#notes"+num ).toggle("slow");
  });

function shownotesicon(){$(".noteswrapper").each(function(i, notediv) {
    if ($(notediv).find("p").html().trim() !== "") {
        $(notediv).find(".notestxt i").html("notes")
      }
})};

shownotesicon();

// let divs = document.getElementsByClassName("notesbtn");
//     let len = divs.length;
//     let num;
//     for (var i = 1; i <= len; i++){
//         if (this.id == "notesbtn"+i){
//             num = i;
//             break;
//         } 
//     }

// listitemnum = $('spanhere'+spannum).toint(lookup js nem)
// listitemnum = 8;
// listitemnum = $("#number"+spannum)

$(".rolldiebtn").on( "click", function() {
    let die = document.getElementsByClassName("notesbtn").length;
        
    console.log('link working!')
    console.log(Math.floor(Math.random() * die) + 1)
});