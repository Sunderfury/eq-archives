<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html dir="ltr">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<meta http-equiv="Content-Style-Type" content="text/css">

<link rel="top" href="./index.php?sid=bc7be4263abd743f1955a2b32de70d1c" title="The Runes Forum Index" />
<link rel="search" href="./search.php?sid=bc7be4263abd743f1955a2b32de70d1c" title="Search" />
<link rel="help" href="./faq.php?sid=bc7be4263abd743f1955a2b32de70d1c" title="FAQ" />
<link rel="author" href="./memberlist.php?sid=bc7be4263abd743f1955a2b32de70d1c" title="Memberlist" />

<title>The Runes :: Index</title>
<!-- link rel="stylesheet" href="templates/subSilver/subSilver.css" type="text/css" -->
<style type="text/css">
<!--
/*
  The original subSilver Theme for phpBB version 2+
  Created by subBlue design
  http://www.subBlue.com

  NOTE: These CSS definitions are stored within the main page body so that you can use the phpBB2
  theme administration centre. When you have finalised your style you could cut the final CSS code
  and place it in an external file, deleting this section to save bandwidth.
*/

/* General page style. The scroll bar colours only visible in IE5.5+ */
body {
	background-color: #FBFBF9;
	scrollbar-face-color: #EEF3F6;
	scrollbar-highlight-color: #FFFFFF;
	scrollbar-shadow-color: #EEF3F6;
	scrollbar-3dlight-color: #D7DBE1;
	scrollbar-arrow-color:  #202664;
	scrollbar-track-color: #FDFFFF;
	scrollbar-darkshadow-color: #7C533F;
}

<!--body { margin: 0} -->

/* General font families for common tags */
font,th,td,p { font-family: Verdana, Arial, Helvetica, sans-serif }
a:link,a:active,a:visited { color : #202664; }
a:hover		{ text-decoration: underline; color : #DD6900; }
hr	{ height: 0px; border: solid #D7DBE1 0px; border-top-width: 1px;}

/* This is the border line & background colour round the entire page */
.bodyline	{ background-color: #FFFFFF; border: 1px #7C533F solid; }

/* This is the outline round the main forum tables */
.forumline	{ background-color: #FFFFFF; border: 2px #707470 solid; }

/* Main table cell colours and backgrounds */
td.row1	{ background-color: #FDFFFF; }
td.row2	{ background-color: #EEF3F6; }
td.row3	{ background-color: #D7DBE1; }

/*
  This is for the table cell above the Topics, Post & Last posts on the index.php page
  By default this is the fading out gradiated silver background.
  However, you could replace this with a bitmap specific for each forum
*/
td.rowpic {
		background-color: #FFFFFF;
		background-image: url(templates/subSilver/images/);
		background-repeat: repeat-y;
}

/* Header cells - the blue and silver gradient backgrounds */
th	{
	color: #404000; font-size: 11px; font-weight : bold;
	background-color: #202664; height: 25px;
	background-image: url(templates/subSilver/images/image7.gif);
}

td.cat,td.catHead,td.catSides,td.catLeft,td.catRight,td.catBottom {
			background-image: url(templates/subSilver/images/);
			background-color:#D7DBE1; border: #F7F7F7; border-style: solid; height: 28px;
}

/*
  Setting additional nice inner borders for the main table cells.
  The names indicate which sides the border will be on.
  Don't worry if you don't understand this, just ignore it :-)
*/
td.cat,td.catHead,td.catBottom {
	height: 29px;
	border-width: 0px 0px 0px 0px;
}
th.thHead,th.thSides,th.thTop,th.thLeft,th.thRight,th.thBottom,th.thCornerL,th.thCornerR {
	font-weight: bold; border: #FFFFFF; border-style: solid; height: 28px;
}
td.row3Right,td.spaceRow {
	background-color: #D7DBE1; border: #F7F7F7; border-style: solid;
}

th.thHead,td.catHead { font-size: 12px; border-width: 1px 1px 0px 1px; }
th.thSides,td.catSides,td.spaceRow	 { border-width: 0px 1px 0px 1px; }
th.thRight,td.catRight,td.row3Right	 { border-width: 0px 1px 0px 0px; }
th.thLeft,td.catLeft	  { border-width: 0px 0px 0px 1px; }
th.thBottom,td.catBottom  { border-width: 0px 1px 1px 1px; }
th.thTop	 { border-width: 1px 0px 0px 0px; }
th.thCornerL { border-width: 1px 0px 0px 1px; }
th.thCornerR { border-width: 1px 1px 0px 0px; }

/* The largest text used in the index page title and toptic title etc. */
.maintitle	{
	font-weight: bold; font-size: 22px; font-family: "Trebuchet MS",Verdana, Arial, Helvetica, sans-serif;
	text-decoration: none; line-height : 120%; color : #3A394F;
}

/* General text */
.gen { font-size : 12px; }
.genmed { font-size : 11px; }
.gensmall { font-size : 10px; }
.gen,.genmed,.gensmall { color : #3A394F; }
a.gen,a.genmed,a.gensmall { color: #202664; text-decoration: none; }
a.gen:hover,a.genmed:hover,a.gensmall:hover	{ color: #DD6900; text-decoration: underline; }

/* The register, login, search etc links at the top of the page */
.mainmenu		{ font-size : 11px; color : #3A394F }
a.mainmenu		{ text-decoration: none; color : #202664;  }
a.mainmenu:hover{ text-decoration: underline; color : #DD6900; }

/* Forum category titles */
.cattitle		{ font-weight: bold; font-size: 12px ; letter-spacing: 1px; color : #202664}
a.cattitle		{ text-decoration: none; color : #202664; }
a.cattitle:hover{ text-decoration: underline; }

/* Forum title: Text and link to the forums used in: index.php */
.forumlink		{ font-weight: bold; font-size: 12px; color : #202664; }
a.forumlink 	{ text-decoration: none; color : #202664; }
a.forumlink:hover{ text-decoration: underline; color : #DD6900; }

/* Used for the navigation text, (Page 1,2,3 etc) and the navigation bar when in a forum */
.nav			{ font-weight: bold; font-size: 11px; color : #3A394F;}
a.nav			{ text-decoration: none; color : #202664; }
a.nav:hover		{ text-decoration: underline; }

/* titles for the topics: could specify viewed link colour too */
.topictitle,h1,h2	{ font-weight: bold; font-size: 11px; color : #3A394F; }
a.topictitle:link   { text-decoration: none; color : #202664; }
a.topictitle:visited { text-decoration: none; color : #414783; }
a.topictitle:hover	{ text-decoration: underline; color : #DD6900; }

/* Name of poster in viewmsg.php and viewtopic.php and other places */
.name			{ font-size : 11px; color : #3A394F;}

/* Location, number of posts, post date etc */
.postdetails		{ font-size : 10px; color : #3A394F; }

/* The content of the posts (body of text) */
.postbody { font-size : 12px; line-height: 18px}
a.postlink:link	{ text-decoration: none; color : #202664 }
a.postlink:visited { text-decoration: none; color : #414783; }
a.postlink:hover { text-decoration: underline; color : #DD6900}

/* Quote & Code blocks */
.code {
	font-family: Courier, 'Courier New', sans-serif; font-size: 11px; color: #54765E;
	background-color: #F2F2F8; border: #D7DBE1; border-style: solid;
	border-left-width: 1px; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px
}

.quote {
	font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 11px; color: #444444; line-height: 125%;
	background-color: #F2F2F8; border: #D7DBE1; border-style: solid;
	border-left-width: 1px; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px
}

/* Copyright and bottom info */
.copyright		{ font-size: 10px; font-family: Verdana, Arial, Helvetica, sans-serif; color: #444444; letter-spacing: -1px;}
a.copyright		{ color: #444444; text-decoration: none;}
a.copyright:hover { color: #3A394F; text-decoration: underline;}

/* Form elements */
input,textarea, select {
	color : #3A394F;
	font: normal 11px Verdana, Arial, Helvetica, sans-serif;
	border-color : #3A394F;
}

/* The text input fields background colour */
input.post, textarea.post, select {
	background-color : #FFFFFF;
}

input { text-indent : 2px; }

/* The buttons used for bbCode styling in message post */
input.button {
	background-color : #FDFFFF;
	color : #3A394F;
	font-size: 11px; font-family: Verdana, Arial, Helvetica, sans-serif;
}

/* The main submit button option */
input.mainoption {
	background-color : #F2F2F8;
	font-weight : bold;
}

/* None-bold submit button */
input.liteoption {
	background-color : #F2F2F8;
	font-weight : normal;
}

/* This is the line in the posting page which shows the rollover
  help line. This is actually a text box, but if set to be the same
  colour as the background no one will know ;)
*/
.helpline { background-color: #EEF3F6; border-style: none; }

/* Import the fancy styles for IE only (NS4.x doesn't use the @import function) */
@import url("templates/subSilver/formIE.css");
-->
</style>
</head>
<body bgcolor="#FBFBF9" text="#3A394F" link="#202664" vlink="#414783">

<a name="top"></a>

<table width="100%" border="0" cellspacing="0" cellpadding="0" background ="templates/subSilver/images/headerback.jpg">
<tr width="100%" align="center" valign="top">
<td>
<img src="templates/subSilver/images/header.jpg" border="0" align="bottom" width="685" height="159" usemap="#Map" alt="TheRunes Homepage" vspace="0" /></a>
</td>
</tr>
</table>

<map name="Map">
  <area shape="rect" coords="175,9,535,106" href="http://www.therunes.net">
</map>

<table width="100%" cellspacing="10" cellpadding="10" border="0" align="center">
	<tr>
		<td class="bodyline"align="center"><table width="100%" cellspacing="0" cellpadding="0" border="0">
			<tr>
				<table cellspacing="0" cellpadding="2" border="0">
					<tr>
						<td align="center" valign="top" nowrap="nowrap"><span class="mainmenu"><a href="faq.php?sid=bc7be4263abd743f1955a2b32de70d1c" class="mainmenu"><img src="templates/subSilver/images/icon_mini_faq.gif" width="12" height="13" border="0" alt="FAQ" hspace="3" />FAQ</a>&nbsp; &nbsp;<a href="search.php?sid=bc7be4263abd743f1955a2b32de70d1c" class="mainmenu"><img src="templates/subSilver/images/icon_mini_search.gif" width="12" height="13" border="0" alt="Search" hspace="3" />Search</a>&nbsp; &nbsp;<a href="memberlist.php?sid=bc7be4263abd743f1955a2b32de70d1c" class="mainmenu"><img src="templates/subSilver/images/icon_mini_members.gif" width="12" height="13" border="0" alt="Memberlist" hspace="3" />Memberlist</a>&nbsp; &nbsp;<a href="groupcp.php?sid=bc7be4263abd743f1955a2b32de70d1c" class="mainmenu"><img src="templates/subSilver/images/icon_mini_groups.gif" width="12" height="13" border="0" alt="Usergroups" hspace="3" />Usergroups</a>&nbsp;
						&nbsp;<a href="profile.php?mode=register&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="mainmenu"><img src="templates/subSilver/images/icon_mini_register.gif" width="12" height="13" border="0" alt="Register" hspace="3" />Register</a></span>&nbsp;
						&nbsp;<a href="profile.php?mode=editprofile&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="mainmenu"><img src="templates/subSilver/images/icon_mini_profile.gif" width="12" height="13" border="0" alt="Profile" hspace="3" />Profile</a>&nbsp; &nbsp;<a href="privmsg.php?folder=inbox&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="mainmenu"><img src="templates/subSilver/images/icon_mini_message.gif" width="12" height="13" border="0" alt="Log in to check your private messages" hspace="3" />Log in to check your private messages</a>&nbsp; &nbsp;<a href="login.php?sid=bc7be4263abd743f1955a2b32de70d1c" class="mainmenu"><img src="templates/subSilver/images/icon_mini_login.gif" width="12" height="13" border="0" alt="Log in" hspace="3" />Log in</a></span></td>
					</tr>
<td align="center" width="100%" valign="middle"><span class="gen"></span></td>
</table>
</br />


<table width="100%" cellspacing="0" cellpadding="2" border="0" align="center">
  <tr>
	<td align="left" valign="bottom"><span class="gensmall">
	The time now is Wed Aug 24, 2005 5:27 am<br /></span><span class="nav"><a href="index.php?sid=bc7be4263abd743f1955a2b32de70d1c" class="nav">The Runes Forum Index</a></span></td>
	<td align="right" valign="bottom" class="gensmall">
		<a href="search.php?search_id=unanswered&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="gensmall">View unanswered posts</a></td>
  </tr>
</table>

<table width="100%" cellpadding="2" cellspacing="1" border="0" class="forumline">
  <tr>
	<th colspan="2" class="thCornerL" height="25" nowrap="nowrap">&nbsp;Forum&nbsp;</th>
	<th width="50" class="thTop" nowrap="nowrap">&nbsp;Topics&nbsp;</th>
	<th width="50" class="thTop" nowrap="nowrap">&nbsp;Posts&nbsp;</th>
	<th class="thCornerR" nowrap="nowrap">&nbsp;Last Post&nbsp;</th>
  </tr>
  <tr>
	<td class="catLeft" colspan="2" height="28"><span class="cattitle"><a href="index.php?c=7&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="cattitle">The Lobby</a></span></td>
	<td class="rowpic" colspan="3" align="right">&nbsp;</td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=40&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">General OOC</a><br />
	  </span> <span class="genmed">Just a place to hang out with the community. All welcome!<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">403</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">5649</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Tue Aug 23, 2005 2:08 am<br /><a href="profile.php?mode=viewprofile&amp;u=3246&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Bajen</a> <a href="viewtopic.php?p=107935&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107935"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=36&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Movies. Music and Books</a><br />
	  </span> <span class="genmed">Yes, there is RL out there somewhere!<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">129</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">1694</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Tue Aug 23, 2005 7:14 pm<br /><a href="profile.php?mode=viewprofile&amp;u=769&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Mel</a> <a href="viewtopic.php?p=107976&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107976"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=37&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Tech Talk</a><br />
	  </span> <span class="genmed">Here ya go Hikaru! As promised :)<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">66</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">487</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Tue Aug 16, 2005 10:37 am<br /><a href="profile.php?mode=viewprofile&amp;u=1453&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Bellanfear</a> <a href="viewtopic.php?p=107570&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107570"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=38&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Rants</a><br />
	  </span> <span class="genmed">A place to vent. Enter at own risk!<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">480</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">10263</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Mon Aug 22, 2005 1:09 pm<br /><a href="profile.php?mode=viewprofile&amp;u=776&amp;sid=bc7be4263abd743f1955a2b32de70d1c">brakeformezz</a> <a href="viewtopic.php?p=107899&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107899"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="catLeft" colspan="2" height="28"><span class="cattitle"><a href="index.php?c=2&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="cattitle">EverQuest Live</a></span></td>
	<td class="rowpic" colspan="3" align="right">&nbsp;</td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=39&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">EQLive General</a><br />
	  </span> <span class="genmed">General topics related to EQLive<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">2395</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">40261</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Wed Aug 24, 2005 3:04 am<br /><a href="profile.php?mode=viewprofile&amp;u=2332&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Khyla The Apathetic</a> <a href="viewtopic.php?p=107986&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107986"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=5&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Quests, Spells, Epic and Tradeskills</a><br />
	  </span> <span class="genmed">Questions, Info, Strats, Walk-Throughs.<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">761</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">11818</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Wed Aug 24, 2005 4:29 am<br /><a href="profile.php?mode=viewprofile&amp;u=51&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Nadia</a> <a href="viewtopic.php?p=107992&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107992"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=3&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Zones, NPC's - Strategies and Questions</a><br />
	  </span> <span class="genmed">Strategies, Questions, Information on Mobs, Zones, Expansions etc ... EPIC info being moved soon from this area! Please post Epic Info and Strats in area below.<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">984</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">10894</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Wed Aug 24, 2005 3:54 am<br /><a href="profile.php?mode=viewprofile&amp;u=51&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Nadia</a> <a href="viewtopic.php?p=107989&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107989"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=2&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Everything you wanted to know about AA, LP, and Tribute Points!</a><br />
	  </span> <span class="genmed">Questions and Information on AA's<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">315</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">6072</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Tue Aug 23, 2005 4:31 pm<br /><a href="profile.php?mode=viewprofile&amp;u=2332&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Khyla The Apathetic</a> <a href="viewtopic.php?p=107970&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107970"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=4&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Gear</a><br />
	  </span> <span class="genmed">Gear Suggestions, Information Including Augmentation etc<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">560</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">5284</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Wed Aug 24, 2005 4:44 am<br /><a href="profile.php?mode=viewprofile&amp;u=3246&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Bajen</a> <a href="viewtopic.php?p=107993&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107993"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=15&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Just The Facts Mam'..</a><br />
	  </span> <span class="genmed">A place to posts the FACTS --> data parsing<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">50</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">848</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Mon Jul 18, 2005 5:29 am<br /><a href="profile.php?mode=viewprofile&amp;u=2656&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Aaira</a> <a href="viewtopic.php?p=106465&amp;sid=bc7be4263abd743f1955a2b32de70d1c#106465"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=7&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Warstories, Character Journals and other Tales</a><br />
	  </span> <span class="genmed">This is the place to post those stories of old times... Why I remember back when...<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">57</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">282</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Fri Jul 08, 2005 9:07 am<br /><a href="profile.php?mode=viewprofile&amp;u=1617&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Cerpicio</a> <a href="viewtopic.php?p=106101&amp;sid=bc7be4263abd743f1955a2b32de70d1c#106101"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=16&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Brenlo/Developer Area</a><br />
	  </span> <span class="genmed">This is the place to ask Brenlo or Developers questions. You MUST read the rules before posting as they are slightly different in this area<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">232</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">1079</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Mon Aug 15, 2005 12:25 pm<br /><a href="profile.php?mode=viewprofile&amp;u=1125&amp;sid=bc7be4263abd743f1955a2b32de70d1c">caeadarie</a> <a href="viewtopic.php?p=107521&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107521"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="catLeft" colspan="2" height="28"><span class="cattitle"><a href="index.php?c=3&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="cattitle">EverQuest II, WOW And Other Games</a></span></td>
	<td class="rowpic" colspan="3" align="right">&nbsp;</td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=20&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">WoW etc</a><br />
	  </span> <span class="genmed">For those playing WoW or other nonEQ games!<br />
	  </span><span class="gensmall">Moderators <a href="profile.php?mode=viewprofile&amp;u=93&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Mezrin Kortex</a>, <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a>, <a href="groupcp.php?g=4155&amp;sid=bc7be4263abd743f1955a2b32de70d1c">World of Warcraft</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">4</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">52</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Fri Aug 19, 2005 12:30 pm<br /><a href="profile.php?mode=viewprofile&amp;u=1453&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Bellanfear</a> <a href="viewtopic.php?p=107779&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107779"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=45&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Vanguard</a><br />
	  </span> <span class="genmed">Vanguard: Saga of Heros<br />
	  </span><span class="gensmall">Moderators <a href="profile.php?mode=viewprofile&amp;u=93&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Mezrin Kortex</a>, <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">12</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">74</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Tue Aug 23, 2005 12:27 pm<br /><a href="profile.php?mode=viewprofile&amp;u=1450&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Nokei</a> <a href="viewtopic.php?p=107955&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107955"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="catLeft" colspan="2" height="28"><span class="cattitle"><a href="index.php?c=8&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="cattitle">EQ2</a></span></td>
	<td class="rowpic" colspan="3" align="right">&nbsp;</td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=29&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">General Gameplay</a><br />
	  </span> <span class="genmed">General Gameplay Discussion<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">268</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">2070</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Fri Aug 12, 2005 6:05 am<br /><a href="profile.php?mode=viewprofile&amp;u=3&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Juwel</a> <a href="viewtopic.php?p=107393&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107393"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=32&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Coercer/Illusionist</a><br />
	  </span> <span class="genmed">Discuss all aspects of play as it relates to the Coercer/Illusionist subclass<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">39</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">359</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Mon Jul 25, 2005 3:29 pm<br /><a href="profile.php?mode=viewprofile&amp;u=128&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Tradora</a> <a href="viewtopic.php?p=106689&amp;sid=bc7be4263abd743f1955a2b32de70d1c#106689"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=30&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Artisans</a><br />
	  </span> <span class="genmed">Discussions on Tradeskills<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">28</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">165</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Fri Mar 04, 2005 4:00 pm<br /><a href="profile.php?mode=viewprofile&amp;u=93&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Mezrin Kortex</a> <a href="viewtopic.php?p=98455&amp;sid=bc7be4263abd743f1955a2b32de70d1c#98455"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Quests</a><br />
	  </span> <span class="genmed">Discuss Quests<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">28</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">183</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Wed Aug 03, 2005 3:45 pm<br /><a href="profile.php?mode=viewprofile&amp;u=72&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Illusion</a> <a href="viewtopic.php?p=107050&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107050"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="catLeft" colspan="2" height="28"><span class="cattitle"><a href="index.php?c=6&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="cattitle">Miscellaneous</a></span></td>
	<td class="rowpic" colspan="3" align="right">&nbsp;</td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=11&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">UI's and other Misc. Things</a><br />
	  </span> <span class="genmed">UI's, timers, etc<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">56</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">458</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Mon Aug 22, 2005 10:07 am<br /><a href="profile.php?mode=viewprofile&amp;u=1453&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Bellanfear</a> <a href="viewtopic.php?p=107884&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107884"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=10&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Trade/Sell Spells Gear</a><br />
	  </span> <span class="genmed">Trade or sell Spells and Gear here. Be sure to include your SERVER name in the subject line<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">48</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">112</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Thu Jul 07, 2005 7:12 pm<br /><a href="profile.php?mode=viewprofile&amp;u=4202&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Neriak Drug Cartel (tm)</a> <a href="viewtopic.php?p=106064&amp;sid=bc7be4263abd743f1955a2b32de70d1c#106064"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=23&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Show Off Your Sigs!</a><br />
	  </span> <span class="genmed">For those who want to show off their signature/avatar art, but don't want them to load with every post you make show them off here. <br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">41</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">123</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Tue Aug 23, 2005 11:28 am<br /><a href="profile.php?mode=viewprofile&amp;u=1453&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Bellanfear</a> <a href="viewtopic.php?p=107950&amp;sid=bc7be4263abd743f1955a2b32de70d1c#107950"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" height="50"><img src="templates/subSilver/images/folder_big.gif" width="46" height="25" alt="No new posts" title="No new posts" /></td>
	<td class="row1" width="100%" height="50"><span class="forumlink"> <a href="viewforum.php?f=12&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="forumlink">Test Forum</a><br />
	  </span> <span class="genmed">As the Name Implies :-)<br />
	  </span><span class="gensmall">Moderator <a href="groupcp.php?g=31&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Site Moderators</a></span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">70</span></td>
	<td class="row2" align="center" valign="middle" height="50"><span class="gensmall">245</span></td>
	<td class="row2" align="center" valign="middle" height="50" nowrap="nowrap"> <span class="gensmall">Sat Apr 16, 2005 1:00 pm<br /><a href="profile.php?mode=viewprofile&amp;u=1137&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Nilmarth N'ilanthir</a> <a href="viewtopic.php?p=101238&amp;sid=bc7be4263abd743f1955a2b32de70d1c#101238"><img src="templates/subSilver/images/icon_latest_reply.gif" border="0" alt="View latest post" title="View latest post" /></a></span></td>
  </tr>
</table>

<table width="100%" cellspacing="0" border="0" align="center" cellpadding="2">
  <tr>
	<td align="left"><span class="gensmall"><a href="index.php?mark=forums&amp;sid=bc7be4263abd743f1955a2b32de70d1c" class="gensmall">Mark all forums read</a></span></td>
	<td align="right"><span class="gensmall">All times are GMT - 6 Hours</span></td>
  </tr>
</table>

<table width="100%" cellpadding="3" cellspacing="1" border="0" class="forumline">
  <tr>
	<td class="catHead" colspan="2" height="28"><span class="cattitle"><a href="viewonline.php?sid=bc7be4263abd743f1955a2b32de70d1c" class="cattitle">Who is Online</a></span></td>
  </tr>
  <tr>
	<td class="row1" align="center" valign="middle" rowspan="2"><img src="templates/subSilver/images/whosonline.gif" alt="Who is Online" /></td>
	<td class="row1" align="left" width="100%"><span class="gensmall">Our users have posted a total of <b>104011</b> articles<br />We have <b>4578</b> registered users<br />The newest registered user is <b><a href="profile.php?mode=viewprofile&amp;u=4583&amp;sid=bc7be4263abd743f1955a2b32de70d1c">vizion</a></b></span>
	</td>
  </tr>
  <tr>
	<td class="row1" align="left"><span class="gensmall">In total there are <b>18</b> users online :: 1 Registered, 0 Hidden and 17 Guests &nbsp; [ <span style="color:#404000">Administrator</span> ] &nbsp; [ <span style="color:#54765E">Moderator</span> ]<br />Most users ever online was <b>250</b> on Fri Sep 24, 2004 11:31 am<br />Registered Users: <a href="profile.php?mode=viewprofile&amp;u=3246&amp;sid=bc7be4263abd743f1955a2b32de70d1c">Bajen</a></span></td>
  </tr>
</table>

<table width="100%" cellpadding="1" cellspacing="1" border="0">
<tr>
	<td align="left" valign="top"><span class="gensmall">This data is based on users active over the past five minutes</span></td>
</tr>
</table>

<form method="post" action="login.php?sid=bc7be4263abd743f1955a2b32de70d1c">
  <table width="100%" cellpadding="3" cellspacing="1" border="0" class="forumline">
	<tr>
	  <td class="catHead" height="28"><a name="login"></a><span class="cattitle">Log in</span></td>
	</tr>
	<tr>
	  <td class="row1" align="center" valign="middle" height="28"><span class="gensmall">Username:
		<input class="post" type="text" name="username" size="10" />
		&nbsp;&nbsp;&nbsp;Password:
		<input class="post" type="password" name="password" size="10" maxlength="32" />
		&nbsp;&nbsp; &nbsp;&nbsp;Log me on automatically each visit
		<input class="text" type="checkbox" name="autologin" />
		&nbsp;&nbsp;&nbsp;
		<input type="submit" class="mainoption" name="login" value="Log in" />
		</span> </td>
	</tr>
  </table>
</form>

<br clear="all" />

<table cellspacing="3" border="0" align="center" cellpadding="0">
  <tr>
	<td width="20" align="center"><img src="templates/subSilver/images/folder_new_big.gif" alt="New posts"/></td>
	<td><span class="gensmall">New posts</span></td>
	<td>&nbsp;&nbsp;</td>
	<td width="20" align="center"><img src="templates/subSilver/images/folder_big.gif" alt="No new posts" /></td>
	<td><span class="gensmall">No new posts</span></td>
	<td>&nbsp;&nbsp;</td>
	<td width="20" align="center"><img src="templates/subSilver/images/folder_locked_big.gif" alt="Forum is locked" /></td>
	<td><span class="gensmall">Forum is locked</span></td>
  </tr>
</table>


<div align="center"><span class="copyright"><br /><br />
<!--
	We request you retain the full copyright notice below including the link to www.phpbb.com.
	This not only gives respect to the large amount of time given freely by the developers
	but also helps build interest, traffic and use of phpBB 2.0. If you cannot (for good
	reason) retain the full copyright we request you at least leave in place the
	Powered by phpBB line, with phpBB linked to www.phpbb.com. If you refuse
	to include even this then support on our forums may be affected.

	The phpBB Group : 2002
// -->
Powered by <a href="http://www.phpbb.com/" target="_phpbb" class="copyright">phpBB</a> &copy; 2001, 2005 phpBB Group<br /></span></div>
		</td>
	</tr>
</table>

</body>
</html>

