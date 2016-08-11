/** 

Several attributes have been depreciated from this script. It's 4am in the morning :(


CALLUMS COOL ERROR HANDLING SCRIPT

I made this myself. Thanks Kia for teaching me JavaScript :D. 

In the browser this piece of code redirects the 'iframe' (object tag) to the news.html iff Java is enabled.
In other words: this means 'iframe' returns to its default data path when JS isn't working for the user. 
That data path is an accessibility page designed for non-JS users!

Conclusion, JavaScript swaps HTML elements to JS compatible elements iff Javascript is enabled. So it error handles itself! 

Clever huh? Originally I was going to have an 'accessibility page' with a <noscript> tag element for non-JS users but I thought why not just set the default as the non-Java page and have Java change the page to the correct one! Saves lots of coding time: hit two birds with one stone!

Own java code mostly!!**/

/** Ready the page*/


/** Open UAC */

$(document).ready(function() {
        var new_url = 'UAC_success.html';
 		$('#uac').attr('data', new_url);
        $('#uac').load(new_url);
    });



/** Finished ready */

/** Open popup */

function popupWindow(url)
{
  window.open(url);
}




/**This JScript allows people to enter by using a form that asks for a
UserID and Password. Imported from from http://javascriptkit.com/script/cut76.shtml and slightly modified to suit needs**/

function pasuser(form) {
if (form.id.value=="admin") {
if (form.pass.value=="test") {
location="UAC_session.html"
} else {
alert("Invalid Username or Password")
}
} else {  alert("Invalid Username or Password")
}
}


/**This JScript saves a session via cookies. Imported from from http://www.daniweb.com/web-development/javascript-dhtml-ajax/threads/19283/how-to-save-session-values-in-javascript and amended to fit my needs**/

