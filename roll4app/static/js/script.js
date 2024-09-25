//initialize sidenav
$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
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