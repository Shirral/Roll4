//initialize sidenav
$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
});

$( ".notesbtn" ).on( "click", function() {
    
    let divs = document.getElementsByClassName("notesbtn");
    let len = divs.length;
    let num;
    console.log(num);
    for (var i = 1; i <= len; i++){
        if (this.id == "notesbtn"+i){
            num = i;
            break;
        } 
    }
    console.log(num);

    $( "#notes"+num ).toggle("slow");
  });