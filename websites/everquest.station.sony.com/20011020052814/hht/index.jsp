






<head>

<!-- #BeginEditable "doctitle" -->

<title>EverQuest: You're In Our World Now</title>

<!-- #EndEditable --> 

<link rel="stylesheet" href="/includes/eqstyle.css">

</head>



<body onLoad="release=1;start=1;timead();showCrossNav();" marginwidth="0" marginheight="0" leftmargin="0" topmargin="0" background="images/bg.gif">
































<script language="JavaScript" src="/common/dropdown_array.js"> </script>





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

var NS = (navigator.appName == "Netscape") && (navigator.appVersion.indexOf("BeIA") == -1);

var IE4 = (document.all) && (navigator.appVersion.indexOf("BeIA") == -1);

var NS4 = document.layers;

var NS6 = (navigator.userAgent.indexOf("Netscape6")>=0);

var eVilla = (navigator.appName == "Netscape") && (navigator.appVersion.indexOf("BeIA") >= 0);

var Opera5 = (navigator.appVersion.indexOf("5.")>=0) && (navigator.appName.indexOf("Opera")>=0)



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

var adurl = "/common/global_nav/nav_ad.jsp";



/*

 *  signinPop() and signinProfile() WERE HERE

 */



//fixes Netscape resize bug



self.name="nav";release=0;

function nullit() {

	return true

	}

window.onerror=nullit;



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

  features1 ="'statusbar=yes,status=yes,toolbar,scrollbars=yes,resizable=yes,width=800,height=" + hh1 + ",top=40,left=" + yy1 + "'";

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

	qx = setTimeout('timead()',60000)

	}

	

function loadad() { // loads ads for Netscape

	

	

	id = "adlayer1"

	if(document.layers) {

	  if(start){

            adlayer1 = new Layer(468);

	    start=0;

          }

  	  

	  adlayer1.top = 0

	  adlayer1.left = 340

	  adlayer1.clip.height = 80

	  adlayer1.clip.width = 468

	  adlayer1.load(adurl,468);

	  adlayer1.visibility ="visible"

	  q = setTimeout('timead()',60000) // changes ad

	}

}



function showCrossNav()

{

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

	dotOff[j].src = "/common/images/global_nav//crossnav/dot" + j + "0.gif"

	dotOn[j].src = "/common/images/global_nav//crossnav/dot" + j + "1.gif"

}

for(j=0;j<6;j++)

{	sections[j] = new Image

	sections[j].src = "/common/images/global_nav//crossnav/middle" + j + ".gif"

}

function menuRoll(which,status,sect){

	if (status){

		document["dot" + which].src = dotOn[which].src

		document["middle"].src = sections[sect].src

	}

	else{

		document["dot" + which].src = dotOff[which].src

		document["middle"].src = sections[0].src

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

<table width="100%" border="0" cellspacing="0" cellpadding="0" background="/common/images/global_nav//eq_global_nav_slice.gif" style="background-image: url(/common/images/global_nav//eq_global_nav_slice.gif);">

  <tr> 

	<td>

		

	  <table width="100%" border="0" cellspacing="0" cellpadding="0" background="">

		<tr> 

			<td rowspan="2" width="1"><img src="/common/images/global_nav//eq_global_nav_new.gif" width="154" height="105" border="0" usemap="#Logo"></td>

		  <td width="100%" height="81">

			<table width="100%" border="0" cellspacing="0" cellpadding="0">

			  <tr>

				<td align="center" width="100%"><div id="adlayer" class="adl">

<script language="JavaScript" type="text/javascript">

<!--

if(IE4){

	if(navigator.appVersion.indexOf("Mac")>=0){

		document.write('<nobr><iframe name="adlayeri" src=' + adurl + ' z-index="3" width="468" height="80" scrolling="no" marginheight=0 marginwidth=0 frameborder="no"></iframe></nobr>')

	}

	else {

		document.write('<nobr><iframe name="adlayeri" z-index="3" width="468" height="80" scrolling="no" marginheight=0 marginwidth=0 frameborder="no"></iframe></nobr>')

	}

}

else if (Opera5 || NS6) {

	document.write('<nobr><iframe name="adlayeri" src=' + adurl + ' z-index="3" width="468" height="80" scrolling="no" marginheight=0 marginwidth=0 frameborder="0"></iframe></nobr>')

}

else if (eVilla) {

	document.write('<nobr><iframe name="adlayeri" src=' + adurl + ' z-index="3" width="468" height="80" scrolling="no" marginheight=0 marginwidth=0 frameborder="no"></iframe></nobr>')

}

else {document.write('<img src="/common/images/global_nav//seethru.gif" width=1 height=60>');}

//-->

</script>

</div>

				</td>

				<td align="center" width="150" nowrap> <!-- Begin Sony Cross Nav --> 

				  <div id="crossnavigation" class="crossnav"> 

<script language="JavaScript">

document.write('<TABLE WIDTH="98" BORDER="0" CELLPADDING="0" CELLSPACING="0">');

document.write('<TR><TD WIDTH="98" COLSPAN="3"><img src="/common/images/global_nav//crossnav/top.gif" WIDTH=98 HEIGHT=17 ALT="" BORDER="0"></TD></TR>');

document.write('<TR>');

document.write('<TD WIDTH="13"><img src="/common/images/global_nav//crossnav/left.gif" WIDTH=13 HEIGHT=18 ALT="" BORDER="0"></TD>');

document.write('<TD WIDTH="80"><A HREF="http://www.sony.com/goto-sonysoe" target=_top><img src="/common/images/global_nav//crossnav/middle0.gif" NAME="middle" WIDTH=80 HEIGHT=18 ALT="" BORDER="0"></A></TD>');

document.write('<TD WIDTH="5"><img src="/common/images/global_nav//crossnav/right.gif" WIDTH=5 HEIGHT=18 ALT="" BORDER="0"></TD>');

document.write('</TR>');

document.write('<TR>');

document.write('<TD WIDTH="13"><img src="/common/images/global_nav//crossnav/lc.gif" WIDTH=13 HEIGHT=25 ALT="" BORDER="0"></TD>');

document.write('<TD WIDTH="80">');

document.write('<TABLE WIDTH="80" BORDER="0" CELLPADDING="0" CELLSPACING="0">');

document.write('<TR>');

document.write('<TD><A HREF="http://www.sony.com/goto-sonysoe" onmouseover="menuRoll(4,true,5)" onmouseout="menuRoll(4,false,0)" target=_top><img src="/common/images/global_nav//crossnav/dot40.gif" NAME="dot4" WIDTH=15 HEIGHT=12 ALT="" BORDER="0"></A></TD>');

document.write('<TD><A HREF="http://www.sony.com/goto-smesoe" onmouseover="menuRoll(0,true,1)" onmouseout="menuRoll(0,false,0)" target=_top><img src="/common/images/global_nav//crossnav/dot00.gif" NAME="dot0" WIDTH=17 HEIGHT=12 ALT="" BORDER="0"></A></TD>');

document.write('<TD><A HREF="http://www.sony.com/goto-spesoe" onmouseover="menuRoll(1,true,2)" onmouseout="menuRoll(1,false,0)" target=_top><img src="/common/images/global_nav//crossnav/dot10.gif" NAME="dot1" WIDTH=17 HEIGHT=12 ALT="" BORDER="0"></A></TD>');

document.write('<TD><A HREF="http://www.sony.com/goto-selsoe" onmouseover="menuRoll(2,true,3)" onmouseout="menuRoll(2,false,0)" target=_top><img src="/common/images/global_nav//crossnav/dot20.gif" NAME="dot2" WIDTH=17 HEIGHT=12 ALT="" BORDER="0"></A></TD>');

document.write('<TD><A HREF="http://www.sony.com/goto-sceasoe" onmouseover="menuRoll(3,true,4)" onmouseout="menuRoll(3,false,0)" target=_top><img src="/common/images/global_nav//crossnav/dot30.gif" NAME="dot3" WIDTH=14 HEIGHT=12 ALT="" BORDER="0"></A></TD>');

document.write('</TR>');

document.write('<TR>');

document.write('<TD COLSPAN="5"><img src="/common/images/global_nav//crossnav/bottom.gif" WIDTH=80 HEIGHT=13 ALT="" BORDER="0"></TD>');

document.write('</TR>');

document.write('</TABLE>');

document.write('</TD>');

document.write('<TD WIDTH="5"><img src="/common/images/global_nav//crossnav/rc.gif" WIDTH=5 HEIGHT=25 ALT="" BORDER="0"></TD>');	

document.write('</TR>');

document.write('</TABLE>');

document.close();

</script>

</div>

<!-- End Sony Cross Nav -->

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
 <img src="/common/images/global_nav//nav_comstation.gif" width="47" height="15" border="0" alt="" vspace=2></a>&nbsp;
<a href="http://www.station.sony.com/services/stationid.jhtml" target="_blank" onClick="open_servwin('http://www.station.sony.com/services/stationid.jhtml');return false"><img src="/common/images/global_nav//nav_dish.gif" width=15 height="15" border=0 alt="" vspace=2>
</a></td>

                   

<!--**********************************************-->		

</tr>

</table>

<!-- END AVACON, STATION NAME, COMM STATION -->

				</td>

				<td>

<table border="0" background="" cellspacing="0" cellpadding="0">

<tr>

<script language="JavaScript" type="text/javascript">

<!--

if(eVilla){

	document.write("<td nowrap width=\"65\" class=\"statmenu2\" background=\"\" nowrap>")

}

else{

	document.write("<td nowrap width=\"65\" class=\"statmenu\" background=\"\" nowrap>")

}

//-->

</script>

<noscript><td nowrap width="65" class="statmenu" background="" nowrap></noscript>

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

<script language="JavaScript" type="text/javascript">

<!--

if((NS4) || (IE4)){

//alert("NS4 or IE4");

	document.write("<ilayer>");

	document.write("<layer visibility=show>");

	document.write("<span class=iewrap1>");

	document.write("<span class=iewrap2 onMouseover=\"dropit(event,dropmenu0,true);event.cancelBubble=true;return false\" ");

	document.write("onMouseout=\"hidemenu()\">");

	document.write("<a href=\"http:\/\/www.station.sony.com\/games.jhtml\" onMouseover=\"if(document.layers) return dropit(event,dropmenu0,true)\" onMouseout=\"if(document.layers) return hidemenu()\">Games<\/a>&nbsp;|");

	document.write("<\/span>");

	document.write("<\/span>");

	document.write("<\/layer>");

	document.write("<\/ilayer><br>");	

}

else{

//alert("Neither");

	document.write("<a href=\"http:\/\/www.station.sony.com\/games.jhtml\">Games<\/a>&nbsp;|");

}

//-->

</script>

<noscript><a href="http://www.station.sony.com/games.jhtml">Games</a>&nbsp;|</noscript>

<!----------Menu 1 ends here---------->

</td>

<script language="JavaScript" type="text/javascript">

<!--

if(eVilla){

	document.write("<td background=\"\" nowrap class=\"statmenu2\">")

}

else{

	document.write("<td background=\"\" nowrap class=\"statmenu\">")

}

//-->

</script>

	<noscript><td background="" nowrap class="statmenu"></noscript>

	<a href="http://www.station.sony.com" target="_top">News</a> |

	<a href="http://www.station.sony.com/services/talk.jhtml" target="_top">Talk</a> |

	<a href="http://store.station.sony.com" target="_top">Store</a> |

	<a href="http://www.station.sony.com/services/accountinfo.jhtml" onClick="open_servwin('http://www.station.sony.com/services/accountinfo.jhtml'); return false" target="_blank">My Account</a> |

	<a href="http://www.station.sony.com/services/help.jhtml" onClick="open_servwin('http://www.station.sony.com/services/help.jhtml'); return false" target="_blank">Help</a>&nbsp;

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

<div id=dropmenu0 style="position:absolute;left:0;top:0;layer-background-color:#600000; background-color:#600000; width:120;visibility:hidden;border:2px solid #efab00;padding:0px;z-index:-100">

<script language="JavaScript1.2" type="text/javascript">

<!--

if (document.all)

dropmenu0.style.padding="4px"

for (i=0;i<menu1.length;i++)

document.write(menu1[i])



if (IE4)

document.all.dropmenu0.style.zIndex=100

//-->

</script>

</div>

<script language="JavaScript1.2">

if (document.layers){

document.dropmenu0.captureEvents(Event.CLICK)

document.dropmenu0.onclick=hidemenu

}

</script>

<!-- END NAV -->




<table cellpadding="0" cellspacing="0" width="100%" border="0" height="1">
  <tr> 
    <td width="497" height="75"><img src="images/header_left.gif" width="497" height="75"></td>
    <td background="images/header_mid.gif" width="50%" height="43">&nbsp;</td>
    <td width="286" height="43"><img src="images/header_right.gif" width="286" height="75"></td>
  </tr>
</table>

<table width="100%" border="0" cellspacing="0" cellpadding="0" height="100%">
  <tr> 
    <td width="1" background="images/menu.gif" valign="top"> 
      <table width="1" border="0" cellspacing="0" cellpadding="0">
        <tr> 
          <td><img src="../images/spacer.gif" width="151" height="15"></td>
        </tr>
        <tr align="right"> 
          <td> 
            <table width="100%" border="0" cellspacing="0" cellpadding="0" background="">
              <tr> 
                <td valign="top" align="right"><!-- #BeginEditable "menu" --><table width="135" border="0" cellspacing="0" cellpadding="0" background="">
  <tr> 
    <td width="135" valign="top" align="right" class="menu"> 
	  <!-- Begin Main --> 
      <b class="menuHeader"><a href="/hht/index.jsp">Home</a></b><br>
      <b class="menuHeader"><a href="/index.jsp">EverQuest.com</a></b><br>
      <b class="menuHeader"><a href="http://boards.station.sony.com/ubb/harpys-head/cgi-bin/Ultimate.cgi" target="_blank">Forums</a></b><br>
      <!-- End Main --><br>
      <!-- Begin Tavern Menu --><br>
      <b class="menuHeader"><a href="/hht/index.jsp">Harpy's Head Tavern</a></b><br>
      <a href="/hht/feature.jsp">Features <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/hht/veliouslore/index.jsp">Velious Lore <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/hht/weekly.jsp">Dear Mennix <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/hht/history.jsp">History <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/hht/quests/index.jsp">Quests <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/hht/events/index.jsp">Events <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <a href="/hht/profiles/index.jsp">Character Profiles <img src="/images/1d.gif" width="16" height="14" border="0" align="absmiddle"></a><br>
      <!-- Begin Tavern Menu --><br>
	  </td>
  </tr>
</table>
<!-- #EndEditable --></td>
                <td width="1"><img src="../images/spacer.gif" width="15" height="25"></td>
              </tr>
            </table>
          </td>
        </tr>
        <tr> 
          <td>&nbsp;</td>
        </tr>
      </table>
    </td>
    <td valign="top"> 
      <table width="100%" border="0" cellspacing="0" cellpadding="10">
        <tr valign="top"> 
          <td><br>
            <i></i><!-- #BeginEditable "body" --> 
                <center>
                  <div align="center"><img height=111 src="images/harpyheadsign.gif" width=429> 
                  </div>

<p>Got some EverQuest news to submit?<br>

E-mail the EverQuest Webmaster at <a href="mailto:eqwebmaster@verant.com">eqwebmaster@verant.com.</a></p>

<p> 

<table width="70%" border="0" cellpadding="0" cellspacing="0" height="27">
  <tr>
    <td width="1"><img src="images/wood_l.gif" width="117" height="28"></td>
    <td width=100% background="images/wood_mid.gif">
      <div align="center"><nobr><b><font color=#ffffff>
        October 18, 2001 - Thursday
      </font></b></nobr></div>
    </td>
    <td width="1"><img src="images/wood_r.gif" width="128" height="27"></td>
  </tr>
</table><br><table width="90%" align=center border=0>
	<tbody>
	<tr>
		<td valign=top>
			<p><b>Knock Knock</b></p>
			<p><a href="http://everquest.station.sony.com/hht/weekly.jsp" target="_new"><img src="/images/mennix.gif" border="0" align="left"></a>Not everyone has the same sense of humor. What causes one person to laugh may cause another to scratch his head in total befuddlement. In this week�s edition of <a href="http://everquest.station.sony.com/hht/weekly.jsp" target="_new">Dear Mennix</a>, the Handsome Halfling gives the young dwarf Jeminea some pointers on telling jokes to ogres. <br><br>Dear Mennix is publicly provided as a service to the citizens in Norrath to aid them in their daily struggles. It is privately provided in order to keep Mennix safely tucked away and occupied so that he does not become a nuisance to others.</p>
		</td>
	</tr>
	</tbody>
</table>
<br>


<table width="70%" border="0" cellpadding="0" cellspacing="0" height="27">
  <tr>
    <td width="1"><img src="images/wood_l.gif" width="117" height="28"></td>
    <td width=100% background="images/wood_mid.gif">
      <div align="center"><nobr><b><font color=#ffffff>
        October 15, 2001 - Monday
      </font></b></nobr></div>
    </td>
    <td width="1"><img src="images/wood_r.gif" width="128" height="27"></td>
  </tr>
</table><br><table width="90%" align=center border=0>
	<tbody>
	<tr>
		<td valign=top>
			<p><b>Wednesday Night in Norrath Issue #69</b></p>
			<p>The new edition of Wednesday Night in Norrath is now available.<br><br><a href="http://www.evilavatar.com/EA/Editorials/WednesdayNightinNorrath/M33870/" target="_new">Episode 69</a>: I've fallen and I can't get up or So much to do, so little time?<br><br>The WNiN gang return to Dalnair's with too few members, and too little time.</p>
		</td>
	</tr>
	</tbody>
</table>
<br>


<table width="90%" align=center border=0>
	<tbody>
	<tr>
		<td valign=top>
			<p><b>Naked Troll Race Results - Druzzil Ro</b></p>
			<p>Thank you to all the people who entered the race this Saturday (10-13 01)and to everyone in the Arcane Sisterhood who helped out and manned the Check-points along the way. The event was truly fun for all....<br><br>The winners of the race are:<br><br><b>1st place:</b><br><br>Imaco (Imacolata of the Arcane Sisterhood, Druzzil Ro Server)<br><br><b>2nd place:</b><br><br>Drinalracer (Keniff, Drinal Server)<br><br><b>3rd place:</b><br><br>Gagukaka (Desirey of Vampiric Acolyte, Druzzil Ro Server)<br><br><b>Honorable Mention</b><br><br>These runners deserve to have there names listed. They just refused to give up and kept at it until they finished:<br><br>TenSpeed (Tenman of Vampiric Acolyte, Druzzil Ro Server)<br>KSGO (Tabor of Kindred Spirit Guardians, Druzzil Ro Server)<br><br>Following the race a few of the Trolls decided to have a "BUTT Drag" race around the arena. That was a whole sight in and of itself.<br><br>Pics of the race will be up on the site (www.arcanesisterhood.com) some time during the week in the screenshots section. Please check them out.<br><br>Please keep an eye on our message boards for our next event. The Arcane Sisterhood will be hosting a tournament on Saturday 11/24/01 in the Arena. It will be Team vs. Team. All the details will be up on the site in the near future.<br><br>Good luck to all and thanks for making the event one to remember<br><br>Kajira Lakajira<br>Shadow Knight<br>Arcane Sisterhood - Guild Leader<br>Druzzil-Ro<br></p>
		</td>
	</tr>
	</tbody>
</table>
<br>


<table width="70%" border="0" cellpadding="0" cellspacing="0" height="27">
  <tr>
    <td width="1"><img src="images/wood_l.gif" width="117" height="28"></td>
    <td width=100% background="images/wood_mid.gif">
      <div align="center"><nobr><b><font color=#ffffff>
        October 10, 2001 - Wednesday
      </font></b></nobr></div>
    </td>
    <td width="1"><img src="images/wood_r.gif" width="128" height="27"></td>
  </tr>
</table><br><table width="90%" align=center border=0>
	<tbody>
	<tr>
		<td valign=top>
			<p><b>RPGwear Launches New Website</b></p>
			<p>Earlier this week, <a href="http://www.rpgwear.com/" target="_new">RPGwear.com</a> launched its redesigned website. It has improved navigation so users can find things easier, an order tracking utility so customers can check the status of their order any time, a product keyword search, and a streamlined shopping cart.<br><br>In addition to launching the new site, RPGwear also publicly introduced its affiliate program - a great way for game-related sites to make a little extra money.<br><br>RPGwear�s new products this month include mouse pads and key chains that feature designs from its EverQuest class shirts, including the Druid, Ranger, Necromancer, Monk, and Shadow Knight. The Bard, Magician, and Shaman class shirts are now in production and should be available within the next two weeks. All the class shirts should be finished in early November, including the new Beastlord class from Luclin.<br><br>RPGwear will be attending the <a href="http://everquest.station.sony.com/fanfaire/" target="_new">EverQuest Fan Fair</a> in Orlando on Oct 19th � 20th and the EQ Fest 2001 gathering in Houston on Nov 3rd - 4th<br></p>
		</td>
	</tr>
	</tbody>
</table>
<br>


<table width="70%" border="0" cellpadding="0" cellspacing="0" height="27">
  <tr>
    <td width="1"><img src="images/wood_l.gif" width="117" height="28"></td>
    <td width=100% background="images/wood_mid.gif">
      <div align="center"><nobr><b><font color=#ffffff>
        October 8, 2001 - Monday
      </font></b></nobr></div>
    </td>
    <td width="1"><img src="images/wood_r.gif" width="128" height="27"></td>
  </tr>
</table><br><table width="90%" align=center border=0>
	<tbody>
	<tr>
		<td valign=top>
			<p><b>A Tale from Norrath </b></p>
			<p>Adventurers, glory seekers, and plunder-hungry knaves,<br><br>A few new tavern tales have been circulating from across the Deep.  It appears that strife and civil unrest have once again plagued the lands of Kunark.  Stories of treachery and terror within the ranks of the Sarnak have spilled forth from the mountain fortress of Chardok.<br><br>Only a few of the most cunning spies have made their way into the Sarnak hive during this brief time of turmoil, and their reports may have serious implications.  The Brood of Di`zok seems to be more organized than before.  Their leadership is becoming more structured... and much more brutal.  Production in the mines appears to be increasing and soldiers have been amassing in great numbers.<br><br>Other tales have come from this mountain fortress as well.  Terror squads and interrogators have decimated the ranks of reported Sarnak traitors.  These squads have been working under the leadership of one of the Sarnak Collective's newest council members, Korucust.  It can only be presumed that this cleansing is another step towards strengthening the foul brood.<br><br>These tales are hard to confirm, since many of your adventurous kind are prone to drink and to the occasional mistruth.  If these tales are true, it would only stand to reason that new dangers may reveal new wealth and glory.  Perhaps it is time for you to gather your best gear, finish your mug of ale, and head out to investigate.<br><br>Good luck adventurers.<br><br>-The EverQuest Team</p>
		</td>
	</tr>
	</tbody>
</table>
<br>


<table width="90%" align=center border=0>
	<tbody>
	<tr>
		<td valign=top>
			<p><b>Read all about it!</b></p>
			<p>Boisterous shouts can be heard across the lands as carriers herald the arrival of the latest volume of their city's newspapers.  Citizens rush to get a copy of these publications to read the featured articles, latest gossip, and community news for their hometowns.<br><br>-The EverQuest Team</p>
		</td>
	</tr>
	</tbody>
</table>
<br>




<p>&nbsp;</p>


                  <p class=copynotice align="center">Harpy's Head Tavern� is a trademark of Sony Online Entertainment Inc.<br>

                    Copyright �, 2000, Sony Online Entertainment Inc. All rights reserved</p>

                  <p>&nbsp;</p>
                  </center>
            <!-- #EndEditable --></td>
        </tr>
      </table>
    </td>
  </tr>
</table>
</body>
</html>
