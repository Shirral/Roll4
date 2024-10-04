//initialize Materialize functionalities
$(document).ready(function () {
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.modal').modal();
});

// show/hide the category dropdown menu on click
$( "#categoryp" ).on( "click", function() {
    $( "#categoryselect" ).toggle("slow");
});

// show notes added to a list item in listview.html
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

//show the notes upon clicking on the list item card
$( ".listitem" ).on( "click", (shownotes));
    
//show the add/edit notes section upon clicking on the add/edit notes button
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


//display a notes icon on the item cards for the list items that have notes on listview.html
function shownotesicon(){
    $(".noteswrapper").each(function(i, notediv) {
        if ($(notediv).find("p").html().trim() !== "") {
            $(notediv).find(".notestxt i").html("notes");
        }
    });
}

shownotesicon();

//die rolling function - runs upon clicking on the 'roll die' button
$(".rolldiebtn").on( "click", function() {
    
    let die = document.getElementsByClassName("listitem").length;
    let taskmode = $("#taskmodehere").html().trim();
    let listreset;

    //generate a random number between 1 and the number of the chosen die's sides (inclusive of both numbers)
    function dieroll(){
        return Math.floor(Math.random() * die) + 1;
    }        
    let result = dieroll();

    //task mode - roll every number of the list just once, block them from being rolled again
    if (taskmode == "True"){
        let rolled = $(".rolled"); //objects
        let rollednums = []; //list of just nums

        //save rolled numbers into an array
        rolled.each(function() {
            let num = $(this).find("span").html().trim();
            rollednums.push(num);
        });

        console.log(rollednums);

        //keep rerolling the die if the number rolled has been rolled before for this list;
        //reset the list if all the numbers have been rolled
        if (rolled.length != die){
            while (rollednums.includes(result.toString())) {
                result = dieroll();
            }
        } else {
            listreset = "reset";
            $(".listitem").removeClass("rolled");
        }
    }

    let resultspan = $("#rollresult");
    let darkmodecheck = $(".darkmodecheck").html().trim();

    //grey out the text on cards corresponding to the numbers that have been already rolled
    $(resultspan).html(result);
    if (resultspan != ""){
        $("#rollresultdiv").css("display", "flex");
        if (darkmodecheck == "True"){
            $(".listitem").css("background-color", "#757575");
            $(".listitem").removeClass("white-text");
            if (taskmode == "True"){
                $("#notesbtn"+result).addClass("rolled");
            }
            $("#notesbtn"+result).css("background-color", "#d84315").addClass("white-text");
        } else {
            $(".listitem").css("background-color", "");
            $(".listitem").removeClass("black-text");
            if (taskmode == "True"){
                $("#notesbtn"+result).addClass("rolled");
            }
            $("#notesbtn"+result).css("background-color", "#ff7043").addClass("black-text");
        }
    }

    //save the info about the taskmode being activated/deactivated and the status of the list's completion
    // to the database in a json file so that the whole thing happens without the page being refreshed
    if (taskmode == "True"){
        let data = {
            "rollResult": result,
            "listID": $("#listidhere").html().trim(),
            "listreset": listreset
        };

        fetch("/saveroll", {
            "method": "POST",
            "headers": {"Content-Type": "application/json"},
            "body": JSON.stringify(data),
        }).then(response => response.json()).then(data => {
            console.log("Roll saved:", data);
        });
    }
});

//checks if darkmode is on and styles the DOM elements accordingly
function checkdarkmode() {
    let darkmodecheck = $(".darkmodecheck").html().trim();
    if (darkmodecheck == "True"){
        $("body").removeClass("brown lighten-5").addClass("grey darken-3 white-text");
        $("#profiledelete").removeClass("text-darken-3").addClass("text-lighten-1");
        $(".cardimport").not(".colour, .newbutton").css("background-color", "#757575");
        $("#categoryp").css("color", "#ff7043");
        $("#mainbody input").addClass("white-text");
        $("#mainbody textarea").addClass("white-text");
        $(".dicewrapper a").css("color", "#ff7043");
    }
}

checkdarkmode();

//checks if darkmode is on and styles the DOM elements accordingly
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

//clicks on the link in the dicewrapper - makes the entire div clickable
$(".dicewrapper").on( "click", function() {
    $(this).find("a")[0].click();
});