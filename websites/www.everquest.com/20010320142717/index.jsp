






<head>
<title>EverQuest: You're In Our World Now</title>
<link rel="stylesheet" href="includes/eqstyle.css">

<script language="JavaScript"><!--
var axel = Math.random() + "";
var ord = axel * 1000000000000000000;
// -->
</script>
</head>

<body onLoad="release=1;start=1;timead();showCrossNav();" marginwidth="0" marginheight="0" leftmargin="0" topmargin="0" background="images/main_bg.jpg">













<!--calculate current total number of players on all games and sites-->
<!--must have this variable declared above the "totalPlayersOnline.jsp" include so it can be seen further down-->





 



<!--set session variables to null if this is a new session-->




<!--look for and process sony_station_id cookie-->












<script language="JavaScript" src="http://www.station.sony.com/common/dropdown_array.js"> </script>
<script language="javascript">
/*
 * sas 10/23/00, new login pop up window code for EverQuest site
 * as well as code to reload the main page so it grabs the newly set cookies and session vars.
 */
  self.name = "home";

  function loginWin(pid){
    var from_URL = document.location;
var url="https://login.station.sony.com/login/login.jsp?returnURL="+from_URL+"&pid="+pid;
   window.open(url, "signin", "width=280,height=350,status=yes,resizable=no");
  }

  function reloadIt(){
    location.reload(true);
  }

</script>

<!-- BEGIN NAV -->
<!-- BEGIN CODE PASTED FROM GLOBAL_NAV_DROPLET.JHTML 10/22/2000 MCG -->
<script>
function nullit(){
  return true
}; 
window.onerror=nullit;
release=0;
dhtml=0;
var NS = (navigator.appName == "Netscape");
IE4 = document.all; 
NS4 = document.layers;

if ((IE4) || (NS4) || (NS6)){
  dhtml=1;
}

/*
 * sas 11.29.00 IT IS BELIEVED WE DO NOT NEED TO SUPPORT USERS WITHOUT JAVASCRIPT ENABLED
 * SO THE FUNCTION BELOW HAS BEEN COMMENTED OUT. PEOPLE TO ASK:  ERIC ?, PAUL CANNELLA

function redirect(){
  if(dhtml==0){
    self.location="global_nav_njs.jhtml"
  }
}
onLoad=redirect()
*/
</script>

<script language="JavaScript" src="/services/login.js"></script>

<script language="javascript">
// note: can't html comment in the script tag when using java type=print !!!	
var adurl = "/includes/jsp/everquest.jsp?ads=";

/*
 *  signinPop() and signinProfile() WERE HERE
 */

//fixes Netscape resize bug

self.name="nav";release=0;
function nullit() {
	return true
	}
window.onerror=nullit;

var NS = (navigator.appName == "Netscape");
IE4 = document.all;
NS4 = document.layers;

if ((IE4) || (NS4)){
  dhtml=1;
}

if(NS4){
  origWidth = innerWidth
  origHeight = innerHeight
}

function open_servwin(n) {
  if(dhtml) {
    yy1 = ((screen.width)/2)  - 315;
    hh1 = Math.round((screen.height) * .7)
  }
  else{
    yy1=0;hh1=445
  }
  features1 ="'statusbar=yes,status=yes,toolbar,scrollbars=yes,resizable=yes,width=640,height=" + hh1 + ",top=40,left=" + yy1 + "'";
  servicesFrame = window.open(n,"servicesFrame",features1);
}
	
/*
 * LEAPTO() WAS HERE
 */

function re() { // Netscape Resize Code
	pageURL = self.location;
	if (NS4) {
	  if (innerWidth != origWidth || innerHeight != origHeight){ 
	    location.replace(pageURL)
          };
	}
}

window.onResize = re;

function timead() { // sets off loading of NS ad ; reveals IE iframe
  if(release){
    if(NS4){
      loadad();
    }
    if(IE4){
      qq =  setTimeout("expose()",1)
    }
  }
}

function expose() { //  reveals IE iframe
	adgo='document.adlayeri.location ="' + adurl + '"'
	eval(adgo)
	var def = 'document.all.adlayer.style.visibility="visible"'
	eval(def)
	qx = setTimeout('timead()',45000)
	}
	
function loadad() { // loads ads for Netscape
	id = "adlayer1"
	if(document.layers) {
	  if(start){
            adlayer1 = new Layer(468);
	    start=0;
          }
	  adlayer1.top = 0
	  adlayer1.left = 190
	  adlayer1.clip.height = 80
	  adlayer1.clip.width = 468
	  adlayer1.load(adurl,468);
	  adlayer1.visibility ="visible"
	  q = setTimeout('timead()',45000) // changes ad
	}
}

function showCrossNav()
{
	if(false)
	{	(NS4) ? (document.layers["crossnavigation"].left = 755) : (document.all["crossnavigation"].style.left = 755);
		(NS4) ? (document.layers["crossnavigation"].top = 7) : (document.all["crossnavigation"].style.top = 7);
	}
	(NS4) ? (document.layers["crossnavigation"].visibility = "show") : (document.all["crossnavigation"].style.visibility = "visible");
}
</script>

<SCRIPT LANGUAGE="JavaScript">
var nscp = (navigator.appName == "Netscape")
var dotOff = new Array(5)
var dotOn = new Array(5)
var sections = new Array(6)
for(j=0;j<5;j++)
{	dotOff[j] = new Image
	dotOn[j] = new Image
	dotOff[j].src = "/images/nav/crossnav/dot" + j + "0.gif"
	dotOn[j].src = "/images/nav/crossnav/dot" + j + "1.gif"
}
for(j=0;j<6;j++)
{	sections[j] = new Image
	sections[j].src = "/images/nav/crossnav/middle" + j + ".gif"
}
function menuRoll(which,status,sect)
{	if (status)
	{	
		if (NS4)
		{	document.crossnavigation.document["middle"].src = sections[sect].src;
			document.crossnavigation.document["dot" + which].src = dotOn[which].src;
		} else
		{	document.all["middle"].src = sections[sect].src;
			document.all["dot" + which].src = dotOn[which].src;
		}
	} else
	{	
		if (NS4)
		{	document.crossnavigation.document["dot" + which].src = dotOff[which].src;
			document.crossnavigation.document["middle"].src = sections[0].src;
		} else
		{	document.all["dot" + which].src = dotOff[which].src;
			document.all["middle"].src = sections[0].src;
		}
	}
}
</SCRIPT>

<SCRIPT LANGUAGE="JavaScript">
var axel = Math.random() + "";
var ord = axel * 1000000000000000000;

// added by tmf 08.23.2000

var login_url = ""
var signin_message=""
var param_target=""
var param_url=""
var features = "scrollbars=no,height=350,width=280,top=100,left=150";
function nullit() {return true}; window.onerror=nullit;
NS4 = document.layers;
level4browser = ((navigator.appVersion.indexOf("4.")>=0) || (navigator.appVersion.indexOf("5.")>=0)) ? 1 : 0
    if(level4browser) {
        xw  = screen.width / 2; xh = screen.height / 2; xw = xw - 150;  xh = xh - 205;
        var features = "scrollbars=no,height=350,width=280," + "left=" + xw + ",top=" + xh;
        }
        else {var features = "scrollbars=no,height=350,width=280,top=100,left=150";}
if ((navigator.appVersion.indexOf("3.")>=0) && (navigator.appName.indexOf("Microsoft")>=0)){
        features= "scrollbars=no,height=350,width=279";}

cookieson=1;    
var NS = navigator.appName.indexOf("Netscape");
document.cookie = "#"; 
(document.cookie) ? cookieson=1 : cookieson=0;
var hp_refresh=0; var open_popup  = 1;


self.name = "mainWindow";
njs=0;open_pop = 1;

/*
 * OPEN_LOGIN_WIN() WAS HERE
 */

// tmf mod 06.18.2000 - login_url needs to point to https, which means we need to know what server we're on
if (document.domain == "platform.station.sony.com") {
        login_url = "http://" + document.domain + ":40002/services/login.jhtml";
} else {
        login_url = "https://" + document.domain + "/services/login.jhtml";
}

</SCRIPT>

<SCRIPT language=JavaScript>
<!-- hide javascript

var winOpts = 'resizeable=no,scrollbars=no,menubar=no,toolbar=yes,width=525,height=450';

function popUp(pPage) {
popUpWin = window.open(pPage,'popWin',winOpts);
if(popUp.opener==null) popUp.opener=window;
}

//-->
</SCRIPT>
<script language="JavaScript" src="/common/comm_opener.js">
</script>

<SCRIPT language=JavaScript>
<!--
function isSelected(form) {	
var sCheck
for(var i = 0; i < form.ITN.length; i++)
	if(form.ITN[i].checked != false) sCheck = 1;


if(sCheck == 1) return true;
else{
	alert("Please select an item");
	return false;
    }	
}
//-->
</SCRIPT>
<!-- END CODE PASTED FROM GLOBAL_NAV_DROPLET.JHTML 10/22/2000 MCG -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" background="/images/nav/eq_global_nav_slice.gif">
  <tr> 
	<td>
		
	  <table width="100%" border="0" cellspacing="0" cellpadding="0" background="">
		<tr> 
			<td rowspan="2" width="1"><img src="/images/nav/eq_global_nav_new.gif" width="154" height="105" border="0" usemap="#Logo"></td>
		  <td width="100%" height="81">
			<table width="100%" border="0" cellspacing="0" cellpadding="0">
			  <tr>
				<td align="center" width="100%"><div id="adlayer" class="adl">
<script>
if(IE4){
  if(navigator.appVersion.indexOf("Mac")>=0){
    document.write('<nobr><iframe name="adlayeri" src=' + adurl + ' z-index="3" width="468" height="80" scrolling="no" marginheight=0 marginwidth=0 frameborder="no"></iframe></nobr>')}
  else {
    document.write('<nobr><iframe name="adlayeri" z-index="3" width="468" height="80" scrolling="no" marginheight=0 marginwidth=0 frameborder="no"></iframe></nobr>')}}
else {document.write('<img src="/images/seethru.gif" width=1 height=60>');}
</script>
</div>
				</td>
				<td align="center" width="150" nowrap> <!-- Begin Sony Cross Nav --> 
				  <div id="crossnavigation" class="crossnav"> 
<script language="JavaScript">
document.write('<TABLE WIDTH="98" BORDER="0" CELLPADDING="0" CELLSPACING="0">');
document.write('<TR><TD WIDTH="98" COLSPAN="3"><img src="/images/nav/crossnav/top.gif" WIDTH=98 HEIGHT=17 ALT="" BORDER="0"></TD></TR>');
document.write('<TR>');
document.write('<TD WIDTH="13"><img src="/images/nav/crossnav/left.gif" WIDTH=13 HEIGHT=18 ALT="" BORDER="0"></TD>');
document.write('<TD WIDTH="80"><A HREF="http://www.sony.com/goto-sonysoe" target=_top><img src="/images/nav/crossnav/middle0.gif" NAME="middle" WIDTH=80 HEIGHT=18 ALT="" BORDER="0"></A></TD>');
document.write('<TD WIDTH="5"><img src="/images/nav/crossnav/right.gif" WIDTH=5 HEIGHT=18 ALT="" BORDER="0"></TD>');
document.write('</TR>');
document.write('<TR>');
document.write('<TD WIDTH="13"><img src="/images/nav/crossnav/lc.gif" WIDTH=13 HEIGHT=25 ALT="" BORDER="0"></TD>');
document.write('<TD WIDTH="80">');
document.write('<TABLE WIDTH="80" BORDER="0" CELLPADDING="0" CELLSPACING="0">');
document.write('<TR>');
document.write('<TD><A HREF="http://www.sony.com/goto-sonysoe" onmouseover="menuRoll(4,true,5)" onmouseout="menuRoll(4,false,0)" target=_top><img src="/images/nav/crossnav/dot40.gif" NAME="dot4" WIDTH=15 HEIGHT=12 ALT="" BORDER="0"></A></TD>');
document.write('<TD><A HREF="http://www.sony.com/goto-smesoe" onmouseover="menuRoll(0,true,1)" onmouseout="menuRoll(0,false,0)" target=_top><img src="/images/nav/crossnav/dot00.gif" NAME="dot0" WIDTH=17 HEIGHT=12 ALT="" BORDER="0"></A></TD>');
document.write('<TD><A HREF="http://www.sony.com/goto-spesoe" onmouseover="menuRoll(1,true,2)" onmouseout="menuRoll(1,false,0)" target=_top><img src="/images/nav/crossnav/dot10.gif" NAME="dot1" WIDTH=17 HEIGHT=12 ALT="" BORDER="0"></A></TD>');
document.write('<TD><A HREF="http://www.sony.com/goto-selsoe" onmouseover="menuRoll(2,true,3)" onmouseout="menuRoll(2,false,0)" target=_top><img src="/images/nav/crossnav/dot20.gif" NAME="dot2" WIDTH=17 HEIGHT=12 ALT="" BORDER="0"></A></TD>');
document.write('<TD><A HREF="http://www.sony.com/goto-sceasoe" onmouseover="menuRoll(3,true,4)" onmouseout="menuRoll(3,false,0)" target=_top><img src="/images/nav/crossnav/dot30.gif" NAME="dot3" WIDTH=14 HEIGHT=12 ALT="" BORDER="0"></A></TD>');
document.write('</TR>');
document.write('<TR>');
document.write('<TD COLSPAN="5"><img src="/images/nav/crossnav/bottom.gif" WIDTH=80 HEIGHT=13 ALT="" BORDER="0"></TD>');
document.write('</TR>');
document.write('</TABLE>');
document.write('</TD>');
document.write('<TD WIDTH="5"><img src="/images/nav/crossnav/rc.gif" WIDTH=5 HEIGHT=25 ALT="" BORDER="0"></TD>');	
document.write('</TR>');
document.write('</TABLE>');
document.close();
</script>
</div>
<!-- End Sony Cross Nav -->
<div style="font-size: 8pt; color: #ffffff">25338 Players Online</div>
				  </td>
			  </tr>
			</table>
		  </td>
		  </tr>
		  <tr> 
			
		  <td height="23">
			<table width="100%" border="0" cellspacing="0" cellpadding="0">
			  <tr>
				<td width="100%" align="left">
<!-- BEGIN AVACON, STATION NAME, COMM STATION -->
<table border="0" bgcolor="" background="" cellpadding="0" cellspacing="0">
<tr>
<!--**********************************************-->
                     
                            <td>&nbsp;</td>
                     
                           <td>&nbsp;</td>
                         <td><a href="http://www.station.sony.com/services/stationid.jhtml" target="_blank" onClick="open_servwin('http://www.station.sony.com/services/stationid.jhtml');return false">
                            <img src="/images/nav/nav_comstation.gif" width="47" height="15" border="0" alt="" vspace=2>
                            <img src="/images/nav/nav_dish.gif" width=15 height="15" border=0 alt="" vspace=2>
                          </a></td>
                   
<!--**********************************************-->		
</tr>
</table>
<!-- END AVACON, STATION NAME, COMM STATION -->
				</td>
				<td>
<table border="0" background="" cellspacing="0" cellpadding="0">
<tr>
<td nowrap width="65" class="statmenu" background="" nowrap>
<script language="JavaScript1.2">
//reusable
var visibleVar="null";
var currentLayer="null";
var timerOn = "null";
var zindex=100; // dd

if (navigator.appName == "Netscape") 
	{
		layerStyleRef="layer.";
		layerRef="document.layers";
		styleSwitch="";
		visibleVar="show";
		hideVar="hide";
		leftString="layerName.left=event.pageX-event.layerX"
		rightString="layerName.top=event.pageY-event.layerY+19"
	}
	else
	{
		layerStyleRef="layer.style.";
		layerRef="document.all";
		styleSwitch=".style";
		visibleVar="visible";
		hideVar="hidden";
		leftString="layerName.style.left=document.body.scrollLeft+window.event.clientX-window.event.offsetX"
		rightString="layerName.style.top=document.body.scrollTop+window.event.clientY-window.event.offsetY+17"
		if(navigator.appVersion.indexOf("Mac")>=0 && navigator.appVersion.indexOf("MSIE 4.")>=0)
		{
		// fix for Mac IE 4.X bug with event.offsetX
		leftString="layerName.style.left=document.body.scrollLeft+window.event.clientX"
		rightString="layerName.style.top=document.body.scrollTop+window.event.clientY+20"
		}
	}

function hidemenu()
{
	timerOn = setTimeout("hidenow(currentLayer)", 500)
}

function hidenow(layerName)
{
//alert('layerName'+styleSwitch+'.visibility="'+hideVar+'"');
	eval('layerName'+styleSwitch+'.visibility="'+hideVar+'"');
// ie	layerName.style.visibility="hidden";
// ns	layerName.visibility="hide";
}



function dropit(event,layerName,position)
{
	if(timerOn != "null") 
	{
		clearTimeout(timerOn);
		if(layerName != currentLayer)
		{
			hidenow(currentLayer);
		}
	}
	if(layerName != "noMenu")
	{
			
//alert('layerName'+styleSwitch+'.visibility="'+visibleVar+'"');
		eval( 'layerName'+styleSwitch+'.visibility="'+visibleVar+'"');
// ie		layerName.style.visibility="visible";
// ns		layerName.visibility="show";

	if( position == true )
	{
		eval(leftString);
		eval(rightString);
	}

		currentLayer = layerName;
	}
}
</script>

<!----------Menu 1 starts here---------->
<ilayer>
<layer visibility=show>
<span class=iewrap1>
<span class=iewrap2 onMouseover="dropit(event,dropmenu0,true);event.cancelBubble=true;return false" 
onMouseout="hidemenu()">
<a href="http://www.station.sony.com/games.jhtml" onMouseover="if(document.layers) return dropit(event,dropmenu0,true)" 
onMouseout="if(document.layers) return hidemenu()">Games</a>&nbsp;|
</span>
</span>
</layer>
</ilayer><br>
<!----------Menu 1 ends here---------->
</td>
<td background="" nowrap class="statmenu">
											<a href="http://www.station.sony.com" target="_top">News</a> |
											<a href="http://www.station.sony.com/services/talk.jhtml" target="_top">Talk</a> |
											<a href="http://www.station.sony.com/store" target="_top">Store</a> |
											<a href="Javascript:onClick=open_servwin('http://www.station.sony.com/services/accountinfo.jhtml')">My Account</a> |
											<a href="Javascript:onClick=open_servwin('http://www.station.sony.com/services/help.jhtml')">Help</a>&nbsp;
</td>
</tr>
</table>
				</td>
			  </tr>
			</table>
		  </td>
		  </tr>
		</table>
	</td>
  </tr>
</table>
<map name="Logo">
<area alt="Join-Free!" coords="79,56,146,70" href="http://www.station.sony.com/services/register.jhtml" shape="RECT">
<area alt="Sign In!" coords="9,56,76,70" href="Javascript:onClick=loginWin('Welcome to the Station. Please sign in')">
<area alt="The Station" coords="0,0,153,55" href="http://www.station.sony.com" target="_top">
<area alt="The Station" coords="0,70,154,104" href="http://www.station.sony.com" target="_top">
</map>
<div id=dropmenu0 style="position:absolute;left:0;top:0;layer-background-color:#600000; background-color:#600000; width:120;visibility:hidden;border:1px solid #efab00;padding:0px">
<script language="JavaScript1.2">
if (document.all)
dropmenu0.style.padding="4px"
for (i=0;i<menu1.length;i++)
document.write(menu1[i])
</script>
</div>
<script language="JavaScript1.2">
if (document.layers){
document.dropmenu0.captureEvents(Event.CLICK)
document.dropmenu0.onclick=hidemenu
}
</script>
<!-- END NAV -->



<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr>
		<td width="1" background="images/header_r_tile.gif"><img src="images/header_l.gif" width="201" height="72"></td>
		<td width="100%">
		<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/header_r_tile.gif">
			<tr>
				<td><img src="images/spacer.gif" width="10" height="72"></td>
			</tr>
		</table>
		</td>
	</tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr valign="top">
		<td height="100%" rowspan="2" background="images/nav_bottom_wide_bg.gif">
		<table width="1" border="0" cellspacing="0" cellpadding="0" background="" height="1">
			<tr>
				<td width="1" rowspan="2" valign="bottom" background="images/nav_l.gif"><img src="images/nav_left_side_sliver.gif" width="10" height="146" align="bottom"></td>
				<td rowspan="2" valign="top" height="1">
				<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/nav_bg.gif">
					<tr valign="top" align="right">
						<td><p><!-- #BeginEditable "menu" -->
<table width="130" border="0" cellspacing="0" cellpadding="0" background="">
  <tr> 
    <td width="130" valign="top" align="right" class="menu"> 
      <!-- Home -->
      <br>
      <b class="menuHeader"><a href="/index.jsp">Home</a></b><br>
      <b class="menuHeader"><a href="/kunark/everquest_h.jsp">The Ruins of Kunark</a></b><br>
      <b class="menuHeader"><a href="http://station.sony.com/velious/">The Scars of Velious</a></b><br>
      <b class="menuHeader"><a href="/hht/index.jsp">Harpy's Head Tavern</a></b><br>
	  <b class="menuHeader"><a href="/2ndanniversary/index.jsp">2nd Anniversary</a></b><br>
      <b class="menuHeader"><a href="http://www.station.sony.com/fanfaire">Fan Faire</a></b><br>
      <b class="menuHeader"><a href="http://boards.station.sony.com/cgi-bin/Ultimate.cgi?action=intro" target="eq_new">Forums</a></b><br>
      <!-- End Home -->
      <br>
      <!-- EverQuest.com -->
      <br>
      <b class="menuHeader"><a href="/index.jsp">EverQuest.com</a></b><br>
      <a href="/main/info.jsp">Game Info <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/main/faq.jsp">EverQuest FAQ <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="http://www.station.sony.com/store/" target="_top">Buy EverQuest <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/main/indev.jsp">In Development <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/main/letter.jsp">Producer Letter <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/main/screenshots.jsp">Screenshots <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/main/multimedia.jsp">Multimedia <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/main/press.jsp">In The Press <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/main/awards.jsp">Awards <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <!--<a href="/main/credits.jsp">Site Credits <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>-->
      <!-- End EverQuest.com -->
      <br>
      <!-- Support -->
      <br>
      <b class="menuHeader"><a href="/support/index.jsp">Support</a></b><br>
      <a href="/support/faq/install.jsp">Installation FAQ <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/support/faq/video.jsp">Video FAQ <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/support/faq/sound.jsp">Sound FAQ <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/support/faq/drivers.jsp">Drivers FAQ <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <!--<a href="/support/faq/network.jsp">Network FAQ <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>-->
      <a href="/support/faq/billing.jsp">Billing FAQ <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/support/faq/naming.jsp">Naming FAQ <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/support/keyboard.jsp">Keyboard Layout <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/support/account.jsp">Creating an Account <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/support/conduct.jsp">Rules of Conduct <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/support/naming.jsp">Naming Policy <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/netstat/downtime.jsp">Scheduled Downtime <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/netstat/index.jsp">Network Status <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <!-- End Support -->
      <br>
      <!-- Guidebook -->
      <br>
      <b class="menuHeader"><a href="/guidebook/index.jsp">Guidebook</a></b><br>
      <a href="/guidebook/manual.jsp">Manual <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/guidebook/races.jsp">Races <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/guidebook/classes.jsp">Classes <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <!--<a href="/guidebook/deities.jsp">Deities <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>-->
      <a href="/guidebook/skills.jsp">Skills <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/guidebook/equipment.jsp">Equipment <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <!--<a href="/guidebook/bestiary.jsp">Bestiary <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>-->
      <a href="/guidebook/atlas/index.jsp">Atlas <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <!-- End Guidebook -->
      <br>
      <!-- Begin Contact Us -->
      <br>
      <b class="menuHeader"><a href="/main/contact.jsp">Contact Us</a></b><br>
      <!-- End Contact Us -->
      <br>
    </td>
  </tr>
</table>
<!-- #EndEditable --></p></td>
					</tr>
					<tr>
						<td background=""><p><img src="images/nav_col_mid_top.gif" width="130" height="26"></p></td>
					</tr>
					<tr>
						<td>
						<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/nav_bottom_wood_bg2.gif" height="1">
							<tr>
								<td height="1">
								<script language="JavaScript"><!--
								document.write('<CENTER><TABLE CELLPADDING="0" CELLSPACING="0"BORDER="0"><TR><TD>');
								document.write('<NOLAYER>');
								document.write('<IFRAME SRC="http://ad.doubleclick.net/adi/games.everquest.spde.dart/home_btn;eq=eq_5;sz=120x90;tile=5;ord=' + ord + '" width="120" height="90" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no">');
								document.write('<A HREF="http://ad.doubleclick.net/jump/games.everquest.spde.dart/home_btn;eq=eq_5;sz=120x90;tile=5;ord=' + ord + '" target="_blank"><IMG SRC="games.everquest.spde.dart/everquest;eq=eq_5;sz=120x90;tile=5;ord=' + ord + '" width="120" height="90" border="0"></A>');
								document.write('</IFRAME>');
								document.write('</NOLAYER>');
								document.write('<ilayer id="ph3" visibility="hide" width="120" height="90"></ilayer>');
								document.write('</TD></TR></TABLE></CENTER>');
								//-->
								</script>
								</td>
							</tr>
						</table>
						</td>
					</tr>
					<tr valign="top">
						<td>
						<table width="100%" border="0" cellspacing="0" cellpadding="0" background="images/nav_bottom_wood_bg2.gif">
							<tr valign="top">
								<td><p><img src="images/spacer.gif" width="20" height="19"></p></td>
							</tr>
						</table>
						</td>
					</tr>
				</table>
				</td>
				<td width="1" rowspan="2" valign="bottom" background="images/nav_r.gif"><img src="images/nav_right_side_sliver.gif" width="10" height="135" align="bottom"></td>
			</tr>
		</table>
		</td>
		<td width="100%" rowspan="3">
		<table width="100%" border="0" cellspacing="0" cellpadding="10">
			<tr valign="top">
				<td><!-- #BeginEditable "body" -->
				            <table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td>
                  <table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td width="1"><img src="images/news_dividers.gif" width="45" height="20"></td>
                      <td width="10">&nbsp; </td>
                      	<td class="subHeader" width="100%">
							EverQuest Turns Two!
						</td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr>
                <td>
					March 16, 2001 marks the second anniversary of EverQuest. It�s been a great two years and the game has come a long way since the early days! Not only have we seen the popularity of the game continue to soar, but we�ve also seen two expansions that added completely new continents� continents that are filled with new creatures, new quests, and new challenges.<br><br>To commemorate this special event, we're pleased to unveil a new Quicktime movie of EverQuest, featuring an original musical composition from Sam Powell (who also did the recent musical score for The Scars of Velious), shot by Travis Ball, and edited by Paul Tighe.  You can check it out in on our special <A HREF="http://everquest.station.sony.com/2ndanniversary/index.jsp">2nd Anniversary site</A>!<br><br>As a special surprise, we're also releasing one of the earliest forms of the EverQuest client. Less than 2 megs zipped up, it's well worth the download if you're interested in seeing how EverQuest started.  You can find this proof of concept client <A HREF="http://everquest.station.sony.com/2ndanniversary/eqclient.jsp">right here</A>.<br><br>Once again, thanks to all the many people who have shared in the grand adventure that is EverQuest.
				</td>
              </tr>
            </table>
            <br>


            <table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td>
                  <table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td width="1"><img src="images/news_dividers.gif" width="45" height="20"></td>
                      <td width="10">&nbsp; </td>
                      	<td class="subHeader" width="100%">
							EverQuest Fan Faire Update!
						</td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr>
                <td>
					The rooms at the $109 rate for the Sheraton Hotel and Marina are sold out. But... I just negotiated another 30 rooms for Friday and Saturday night at $149. If you want to attend and stay at the Sheraton, reserve your room and make your reservations for the Fan Faire quickly! The Fan Faire itself is almost sold out as well! -- Cindy
				</td>
              </tr>
            </table>
            <br>


            <table width="100%" border="0" cellspacing="0" cellpadding="0">
              <tr>
                <td>
                  <table width="100%" border="0" cellspacing="0" cellpadding="0">
                    <tr>
                      <td width="1"><img src="images/news_dividers.gif" width="45" height="20"></td>
                      <td width="10">&nbsp; </td>
                      	<td class="subHeader" width="100%">
							A New and Improved Contact List
						</td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr>
                <td>
					The <a href="http://everquest.station.sony.com/main/contact.jsp" target="_new">Contact</a> page of EverQuest.com has been updated. All of the most current EverQuest contact addresses have been listed in order to better help the EverQuest community properly direct their inquiries.
				</td>
              </tr>
            </table>
            <br>


<br>
				<table width="100%" border="0" cellspacing="0" cellpadding="0" height="46">
					<tr>
						<td width="1"><img src="images/sheild.gif" width="59" height="38">
						</td>
						<td width="1"><img src="images/products.gif" width="87" height="46">
						</td>
						<td width="1"><img src="images/bar_l.gif" width="35" height="42">
						</td>
						<td width="100%" background="images/bar_mid.gif"><h5><img src="images/spacer.gif" width="100%" height="1"></h5>
						</td>
						<td width="1"><img src="images/bar_r.gif" width="31" height="42">
						</td>
					</tr>
				</table>
				<br>
				<table width="100%" border="0" cellspacing="0" cellpadding="0">
					<tr>
						<td class="subHeader">EverQuest: The Ruins of Kunark</td>
						<td rowspan="2" width="10">&nbsp;</td>
						<td rowspan="2" align="center" valign="top" width="103"><img src="images/kunark_box.gif" width="103" height="106" class="menu"><br>
						</td>
					</tr>
					<tr>
						<td valign="top"><div align="justify">Prepare to enter an enormous virtual environment; an entire world with its own diverse species, economic systems, alliances, and politics.  Choose from a variety of races and classes, and begin your quest in any number of cities or villages throughout several continents.  From there, equip yourself for adventure, seek allies and knowledge, and head out into a rich world of dungeons, towers, crypts, evil abbeys -- anything conceivable -- even planes and realities beyond your imagination. Learn skills, earn experience, acquire treasure and equipment, meet friends and encounter enemies.  A multitude of quests and adventures await, but you choose your role, you define your destiny.</div></td>
					</tr>
				</table>
				<br>
				<table width="100%" border="0" cellspacing="0" cellpadding="0">
					<tr>
						<td rowspan="2" align="center" valign="top" width="88"><img src="images/velious_box.gif" width="88" height="108"></td>
						<td width="10">&nbsp;</td>
						<td class="subHeader">EverQuest: The Scars of Velious</td>
					</tr>
					<tr>
						<td width="10">&nbsp;</td>
						<td valign="top"><div align="justify">Veeshan the great Crystalline Dragon marked Norrath by striking the continent of Velious with her foreclaw, and deposited her brood there to dwell. The legends of that time also tell that Veeshan blasted Velious with her breath, encasing it in eternal ice and creating a barrier of deadly ice floes and stormy weather. This marked the beginning of the Age of Scale.</div></td>
					</tr>
				</table>
				<p align="center">&nbsp;</p>
				<p align="center">&nbsp;</p>
				<p align="center">&nbsp;</p>
				<!-- #EndEditable -->
				</td>
			</tr>
		</table>
		</td>
		
    <td width="1" align="center"><a href="/2ndanniversary/index.jsp"><img src="/images/2ndann.gif" width="160" height="100" border="0"></a></p>
		
      <table width="100%" border="0" cellspacing="0" cellpadding="0" background="/images/burlap.gif" rowspan="3">
			
        <tr>
				
          <td align="center">
				
            <table width="171" border="0" cellspacing="0" cellpadding="0" height="31">
					
              <tr>
						
                <td width="10"><img src="/images/news.gif" width="76" height="31"></td>
                <td background="images/news_m.gif" width="150">&nbsp;</td>
                <td width="11"><img src="images/news_end.gif" width="11" height="31"></td>
              </tr>
				
            </table>
          </td>
        </tr>
			
        <tr>
				
          <td>
				
            <table width="100%" border="0" cellspacing="0" cellpadding="10">
					
              <tr valign="top">
						
                <td>
                  <div align="center">
                    <p>Looking for EverQuest community news? Drop by the <A HREF="/hht/index.jsp">Harpy's Head Tavern</A>.</p>
                  </div>
                </td>
              </tr>
					
              <tr valign="top">
						
                <td>
						
                  <SCRIPT LANGUAGE="JavaScript"><!--
						document.write('<CENTER><TABLE CELLPADDING="0" CELLSPACING="0"BORDER="0"><TR><TD>');
						document.write('<NOLAYER>');
						document.write('<IFRAME SRC="http://ad.doubleclick.net/adi/games.everquest.spde.dart/home_btn;eq=eq_3;sz=120x90;tile=3;ord=' + ord + '?" width="120" height="90" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no">');
						document.write('<A HREF="http://ad.doubleclick.net/jump/games.everquest.spde.dart/home_btn;eq=eq_3;sz=120x90;tile=3;ord=' + ord + '?" target="_blank"><IMG SRC="http://ad.doubleclick.net/ad/games.everquest.spde.dart/everquest;eq=eq_3;sz=120x90;tile=3;ord=' + ord + '?" width="120" height="90" border="0"></A>');
						document.write('</IFRAME>');
						document.write('</NOLAYER>');
						document.write('<ilayer id="ph3" visibility="hide" width="120" height="90"></ilayer>');
						document.write('</TD></TR></TABLE></CENTER>');
						//-->
						</SCRIPT></p>
						
                  <script language="JavaScript"><!--
						document.write('<CENTER><TABLE CELLPADDING="0" CELLSPACING="0"BORDER="0"><TR><TD>');
						document.write('<NOLAYER>');
						document.write('<IFRAME SRC="http://ad.doubleclick.net/adi/games.everquest.spde.dart/home_btn;eq=eq_4;sz=120x90;tile=4;ord=' + ord + '?" width="120" height="90" marginwidth="0" marginheight="0" hspace="0" vspace="0" frameborder="0" scrolling="no">');
						document.write('<A HREF="http://ad.doubleclick.net/jump/games.everquest.spde.dart/home_btn;abr=!ie;eq=eq_4;sz=120x90;tile=4;ord=' + ord + '?" target="_blank"><IMG SRC="http://ad.doubleclick.net/ad/games.everquest.spde.dart/everquest;abr=!ie;eq=eq_4;sz=120x90;tile=4;ord=' + ord + '?" width="120" height="90" border="0"></A>');
						document.write('</IFRAME>');
						document.write('</NOLAYER>');
						document.write('<ilayer id="ph4" visibility="hide" width="120" height="90"></ilayer>');
						document.write('</TD></TR></TABLE></CENTER>');
						//-->
						</script>
						</td>
              </tr>
					
<!-- #BeginEditable "sidebar" -->

					
              <tr valign="top">
					
						
                <td>
						
                  <table width="100%" border="0" cellspacing="0" cellpadding="10">
							
                    <tr valign="top">
								
                      <td>
                        <p align="center">&nbsp;</p>
                        <script language = "JavaScript">
<!--
function openWindow() {
eqpoll = window.open("http://poll.station.sony.com/cgi-bin/viewpollr.cgi?p=396","eqpoll","height=620,width=385,resizable=yes");
}
//-->
</script>

<p align="center"><b>The World May Never Know</b></p>
<p>How many Troll licks does it take to get to the center of a gnome?</p>

<form action="http://poll.station.sony.com/cgi-bin/pollsubmit.cgi" onSubmit="openWindow()" method="post" target="eqpoll">

<input type=hidden name=poll_id value=396>
	<div align="left">
	<table width="100%" border="0" cellspacing="0" cellpadding="2">
	
	<tr>
		<td valign=top><input type="radio" name="answer_id" value="972"></td>
		<td>1</td>
	</tr>
	
	<tr>
		<td valign=top><input type="radio" name="answer_id" value="973"></td>
		<td>2</td>
	</tr>
	
	<tr>
		<td valign=top><input type="radio" name="answer_id" value="974"></td>
		<td>3</td>
	</tr>
	
	<tr>
		<td valign=top><input type="radio" name="answer_id" value="975"></td>
		<td>*CRUNCH*</td>
	</tr>
	
	</table>
    <p align=center><center>
	<input type=submit value=" Vote! "> <br><br>
	<a href="http://poll.station.sony.com/cgi-bin/viewpollr.cgi?p=396" onclick="openWindow(); return false" target="_blank">See results</a>
	</center>
	</p>
	</div>
</form>

                      </td>
                    </tr>
						
                  </table>
                  <table width="100%" border="0" cellspacing="0" cellpadding="10">
							
                    <tr valign="top">
								
                      <td>
                        <div align="center">
								
                          <p><A HREF="/netstat/index.jsp">Network Status</A></p>
                          <p><A HREF="/netstat/downtime.jsp">Scheduled Downtime</A></p>
                        </div>
                      </td>
                    </tr>
							
                    <tr valign="top">
								
                      <td>
                        <table width="100%" border="0" cellpadding="0" cellpadding="0">
<tr><td align="left"><b>Total Online:</td><td align="right">23973</b></td></tr><br>
<tr><td align="left"><span class="sidebar">Chat Server</span></td><td align="right"><span class="sidebar"><font color="green"><b>31</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Ayonae Ro</span></td><td align="right"><span class="sidebar"><font color="green"><b>563</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Bertoxxulous</span></td><td align="right"><span class="sidebar"><font color="green"><b>674</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Brell Serilis</span></td><td align="right"><span class="sidebar"><font color="green"><b>574</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Bristlebane</span></td><td align="right"><span class="sidebar"><font color="green"><b>711</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Cazic-Thule</span></td><td align="right"><span class="sidebar"><font color="green"><b>536</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Drinal</span></td><td align="right"><span class="sidebar"><font color="green"><b>687</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Druzzil Ro</span></td><td align="right"><span class="sidebar"><font color="green"><b>585</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">E'ci</span></td><td align="right"><span class="sidebar"><font color="green"><b>1204</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Erollisi Marr</span></td><td align="right"><span class="sidebar"><font color="green"><b>720</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Fennin Ro</span></td><td align="right"><span class="sidebar"><font color="red">DOWN</font></span></td></tr>
<tr><td align="left"><span class="sidebar">Innoruuk</span></td><td align="right"><span class="sidebar"><font color="green"><b>721</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Karana</span></td><td align="right"><span class="sidebar"><font color="green"><b>1002</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Lanys T'Vyl</span></td><td align="right"><span class="sidebar"><font color="green"><b>649</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Luclin</span></td><td align="right"><span class="sidebar"><font color="green"><b>567</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Mithaniel Marr</span></td><td align="right"><span class="sidebar"><font color="green"><b>660</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Morell-Thule</span></td><td align="right"><span class="sidebar"><font color="green"><b>750</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Povar</span></td><td align="right"><span class="sidebar"><font color="green"><b>561</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Prexus</span></td><td align="right"><span class="sidebar"><font color="green"><b>642</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Quellious</span></td><td align="right"><span class="sidebar"><font color="green"><b>644</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Rallos Zek </span></td><td align="right"><span class="sidebar"><font color="green"><b>522</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Rodcet Nife</span></td><td align="right"><span class="sidebar"><font color="green"><b>708</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Saryrn</span></td><td align="right"><span class="sidebar"><font color="green"><b>726</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Solusek Ro</span></td><td align="right"><span class="sidebar"><font color="green"><b>647</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Tallon Zek </span></td><td align="right"><span class="sidebar"><font color="green"><b>491</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Tarew Marr</span></td><td align="right"><span class="sidebar"><font color="green"><b>574</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Terris-Thule</span></td><td align="right"><span class="sidebar"><font color="green"><b>493</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Test Server</span></td><td align="right"><span class="sidebar"><font color="green"><b>88</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">The Nameless</span></td><td align="right"><span class="sidebar"><font color="green"><b>954</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">The Rathe</span></td><td align="right"><span class="sidebar"><font color="green"><b>641</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">The Seventh Hammer</span></td><td align="right"><span class="sidebar"><font color="green"><b>598</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">The Tribunal</span></td><td align="right"><span class="sidebar"><font color="green"><b>582</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Tholuxe Paells</span></td><td align="right"><span class="sidebar"><font color="green"><b>653</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Torvonnilous</span></td><td align="right"><span class="sidebar"><font color="green"><b>576</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Tunare</span></td><td align="right"><span class="sidebar"><font color="green"><b>918</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Vallon Zek </span></td><td align="right"><span class="sidebar"><font color="green"><b>511</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Vazaelle</span></td><td align="right"><span class="sidebar"><font color="green"><b>608</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Veeshan</span></td><td align="right"><span class="sidebar"><font color="red">DOWN</font></span></td></tr>
<tr><td align="left"><span class="sidebar">Xegony</span></td><td align="right"><span class="sidebar"><font color="green"><b>701</b></font></span></td></tr>
<tr><td align="left"><span class="sidebar">Xev</span></td><td align="right"><span class="sidebar"><font color="green"><b>532</b></font></span></td></tr>
</table>

                      </td>
                    </tr>
						
                  </table>
              </tr>
					
<!-- #EndEditable -->
									
				
            </table>
          </td>
        </tr>
		
      </table>
    </td>
		<td width="1" rowspan="3"><img src="images/spacer.gif" width="10" height="10"></td>
	</tr>
	<tr valign="top">
	</tr>
</table>

<SCRIPT LANGUAGE="JavaScript"><!--
document.write('<layer src="http://ad.doubleclick.net/adl/games.everquest.spde.dart/home_btn;eq=eq_3;sz=120x90;tile=3;ord=' + ord + '?" width="120" height="90" onload="moveToAbsolute(ph3.pageX,ph3.pageY); visibility=\'show\';" clip="120,90"></layer>');
//-->
</SCRIPT>
<SCRIPT LANGUAGE="JavaScript"><!--
document.write('<layer src="http://ad.doubleclick.net/adl/games.everquest.spde.dart/home_btn;eq=eq_4;sz=120x90;tile=4;ord=' + ord + '?" width="120" height="90" onload="moveToAbsolute(ph4.pageX,ph4.pageY); visibility=\'show\';" clip="120,90"></layer>');
//-->
</SCRIPT>

</body>

</html>

