// Used to toggle the menu on small screens when clicking on the menu button, want to make this an accordian someday
function toggleShow(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else { 
        x.className = x.className.replace(" w3-show", "");
    }
}

//used to expand the accordian and hilight the box
function myAccordian(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
        x.previousElementSibling.className += " w3-deepred";
    } else { 
        x.className = x.className.replace(" w3-show", "");
        x.previousElementSibling.className = 
        x.previousElementSibling.className.replace(" w3-deepred", "");
    }
}
