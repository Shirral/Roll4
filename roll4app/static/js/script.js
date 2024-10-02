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

function shownotes(){
    let divs = document.getElementsByClassName("listitem");
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
}

$( ".listitem" ).on( "click", (shownotes))
    
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
    let die = document.getElementsByClassName("listitem").length;
        
    let result = (Math.floor(Math.random() * die) + 1);
    let resultspan = $("#rollresult");
    let darkmodecheck = $(".darkmodecheck").html().trim();
    $(resultspan).html(result);
    if (resultspan != ""){
        $("#rollresultdiv").css("display", "flex");
        if (darkmodecheck == "True"){
            $(".listitem").css("background-color", "#757575");
            $("#notesbtn"+result).css("background-color", "#d84315");
        } else {
            $(".listitem").css("background-color", "");
            $("#notesbtn"+result).css("background-color", "#ff7043 ");
        }
        
    }

    let data = {
        "rollResult": result,
        "listID": $("#listidhere").html().trim()
    };

    fetch("/saveroll", {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(data),
    }).then(response => response.json()).then(data => {
        console.log("Roll saved:", data);
    })
});


function checkdarkmode() {
    let darkmodecheck = $(".darkmodecheck").html().trim();
    if (darkmodecheck == "True"){
        $("body").removeClass("brown lighten-5").addClass("grey darken-3 white-text");
        $("#profiledelete").removeClass("text-darken-3").addClass("text-lighten-1");
        $(".cardimport").not(".colour, .newbutton").css("background-color", "#757575");
        $("#categoryp").css("color", "#ff7043");
        $("#mainbody input").addClass("white-text");
        $("#mainbody textarea").addClass("white-text");

    }
};

checkdarkmode();

$(document).ready(function() {
    darkmodecheck = $(".darkmodecheck").html().trim();
    if (darkmodecheck == "True"){
        $(".select-wrapper .select-dropdown").css("color", "white");
        $(".select-wrapper .caret").css("fill", "white");
        $(".select-wrapper ul").css("background-color", "#757575");
        $(".dropdown-content li>a, .dropdown-content li>span").css("color", "white");
        $("span.checkmark").toggleClass("darkmode");
    }
});