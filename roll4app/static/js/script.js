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


$(".rolldiebtn").on( "click", function() {
    let die = document.getElementsByClassName("notesbtn").length;
        
    let result = (Math.floor(Math.random() * die) + 1);
    let resultspan = $("#rollresult");
    $(resultspan).html(result);
    if (resultspan != ""){
        $("#rollresultdiv").css("display", "flex");
        $(".notesbtn").css("background-color", "");
        $("#notesbtn"+result).css("background-color", "yellow");
    }
});


function checkdarkmode() {
    darkmodecheck = $(".darkmodecheck").html().trim();
    if (darkmodecheck == "True"){
        $("body").removeClass("brown lighten-5").addClass("grey darken-3 white-text");
        $("#profiledelete").removeClass("text-darken-3").addClass("text-lighten-1");
      }
};

checkdarkmode();

