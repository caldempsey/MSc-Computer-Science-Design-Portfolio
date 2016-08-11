/** 
CALLUMS COOL ERROR HANDLING SCRIPT

I made this myself. Thanks Kia for teaching me JavaScript :D. 

In the browser this piece of code redirects the 'iframe' (object tag) to the news.html iff Java is enabled.
In other words: this means 'iframe' returns to its default data path when JS isn't working for the user. 
That data path is an accessibility page designed for non-JS users!

Conclusion, JavaScript swaps HTML elements to JS compatible elements iff Javascript is enabled. So it error handles itself! 

Clever huh? Originally I was going to have an 'accessibility page' with a <noscript> tag element for non-JS users but I thought why not just set the default as the non-Java page and have Java change the page to the correct one! Saves lots of coding time: hit two birds with one stone!

Own javascript code mostly!!**/

/** Ready the page*/

/** IF Javascript is enabled: accessibility mode OFF and instantiate JS links  */

window.onload = function() {
$('DIV.nojs, .nojs a').remove();
$('a').attr('href', '#')
};


/** Open UAC */

$(document).ready(function() {
        var new_url = 'UAC_success.html';
 		$('#uac').attr('data', new_url);
        $('#uac').load(new_url);
    });


/** Open homepage */

$(document).ready (function() {
	$('#iframe').attr('src', 'home.html');
	window.frames["iframe"].location.reload();
    });

/** Remove noscript tags from iframe replace with isscript */
$(document).ready(function(){
        $("#nonscript").attr("class", "isscript"); });




/** Set hrefs, Javascript is enabled */

/** Finished ready */

/** Open popup */

function popupWindow(url)
{
  window.open(url);
}


/** Change iframe */

function homeFunction() {
	$('#iframe').attr('src', 'home.html');
	window.frames["iframe"].location.reload();
}

function liveFunction() {
	$('#iframe').attr('src', 'live.html');
	window.frames["iframe"].location.reload();
}


function tutorialFunction_1_1() {
	$('#iframe').attr('src', 'Tutorials/Amateur/jab-cross.html');
	window.frames["iframe"].location.reload();
}

function tutorialFunction_2_1() {
	$('#iframe').attr('src', 'Tutorials/Intermediate/2-on-1.html');
	window.frames["iframe"].location.reload();
}

function tutorialFunction_3_1() {
	$('#iframe').attr('src', 'Tutorials/Expert/Shoryuken.html');
	window.frames["iframe"].location.reload();
}

function contactFunction() {
    	$('#iframe').attr('src', 'contact.html');
	window.frames["iframe"].location.reload();
}

/** REDIRECTTS: since no iframe */
function communityFunction() {
	window.location.replace("http://www.reddit.com/r/evolutionmma")
}

function UACFunction()
{
    window.location.replace("UAC_success.html")
}

function tutorialFunction_1_1img()
{
    window.location.replace("Tutorials/Amateur/jab-cross.html")
}

function tutorialFunction_2_1img()
{
    window.location.replace("Tutorials/Intermediate/2-on-1.html")
}

function tutorialFunction_3_1img()
{
    window.location.replace("Tutorials/Expert/Shoryuken.html")
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

