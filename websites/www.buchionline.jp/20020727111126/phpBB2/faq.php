<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<!-- DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd" -->
<html dir="LTR">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<meta http-equiv="Content-Style-Type" content="text/css">

<link rel="top" href="index.php" title="" />
<link rel="search" href="search.php" title="" />
<link rel="help" href="faq.php" title="" />
<link rel="author" href="memberlist.php" title="" />

<title>BuchiOnline :: FAQ</title>
<link rel="stylesheet" href="templates/DarkEQ/DarkEQ.css" type="text/css" />
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
 	background-color: #111111;
 	scrollbar-face-color: #602C72;
 	scrollbar-highlight-color: #602C72;
 	scrollbar-shadow-color: #602C72;
 	scrollbar-3dlight-color: #602C72;
 	scrollbar-arrow-color:  #E3DDFF;
 	scrollbar-track-color: #333355;
 	scrollbar-darkshadow-color: #98AAB1;
}

/* General font families for common tags */
font,th,td,p { font-family: 'MS P�S�V�b�N', Verdana, Arial, Helvetica, sans-se }
a:link,a:active,a:visited { color : #E3DDFF; }
a:hover		{ text-decoration: underline; color : #E3DDFF; }
hr	{ height: 0px; border: solid #c2cdd6 0px; border-top-width: 1px;}


/* This is the border line & background colour round the entire page */
.bodyline	{ background-color: #111133; border: 1px #602C72 solid; }

/* This is the outline round the main forum tables */
.forumline	{ background-color: #000000; border: 1px #602C72 solid; }


/* Main table cell colours and backgrounds */
td.row1	{ background-color: #222233; }
td.row2	{ background-color: #2C2B3C; }
td.row3	{ background-color: #333344; }


/*
  This is for the table cell above the Topics, Post & Last posts on the index.php page
  By default this is the fading out gradiated silver background.
  However, you could replace this with a bitmap specific for each forum
*/
td.rowpic {
		background-color: #ffffff;
		background-image: url(templates/DarkEQ/images/cellpic2.jpg);
		background-repeat: repeat-y;
}

/* Header cells - the blue and silver gradient backgrounds */
th	{
	color: #E3DDFF; font-size: 11px; font-weight : bold;
	background-color: #E3DDFF; height: 25px;
	background-image: url(templates/DarkEQ/images/cellpic3.gif);
}

td.cat,td.catHead,td.catSides,td.catLeft,td.catRight,td.catBottom {
			background-image: url(templates/DarkEQ/images/cellpic1.gif);
			background-color:#333344; border: #FFFFFF; border-style: solid; height: 28px;
}


/*
  Setting additional nice inner borders for the main table cells.
  The names indicate which sides the border will be on.
  Don't worry if you don't understand this, just ignore it :-)
*/
td.cat,td.catHead,td.catBottom {
	height: 29px;
}
th.thHead,th.thSides,th.thTop,th.thLeft,th.thRight,th.thBottom,th.thCornerL,th.thCornerR {
	font-weight: bold; border: #ffffff; border-style: solid; height: 28px; }
td.row3Right,td.spaceRow {
	background-color: #333344; border: #FFFFFF; border-style: solid; }

th.thHead,td.catHead { font-size: 12px; border-width: 0px 0px 0px 0px; }
th.thSides,td.catSides,td.spaceRow	 { border-width: 0px 0px 0px 0px; }
th.thRight,td.catRight,td.row3Right	 { border-width: 0px 0px 0px 0px; }
th.thLeft,td.catLeft	  { border-width: 0px 0px 0px 0px; }
th.thBottom,td.catBottom  { border-width: 0px 0px 0px 0px; }
th.thTop	 { border-width: 0px 0px 0px 0px; }
th.thCornerL { border-width: 0px 0px 0px 0px; }
th.thCornerR { border-width: 0px 0px 0px 0px; }


/* The largest text used in the index page title and toptic title etc. */
.maintitle	{
	font-family: "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;
	font-size : 22px;
	font-weight : bold;
	text-decoration : none;
	line-height : 120%;
	color : #FFFFFF;
}



/* General text */
.gen { font-size : 12px; }
.genmed { font-size : 11px; }
.gensmall { font-size : 10px; }
.gen,.genmed,.gensmall { color : #FFE8FF; }
a.gen,a.genmed,a.gensmall { color: #AF95DF; text-decoration: none; }
a.gen:hover,a.genmed:hover,a.gensmall:hover	{ color: #AF95DF; text-decoration: underline; }


/* The register, login, search etc links at the top of the page */
.mainmenu		{ font-size : 11px; color : #FFE8FF }
a.mainmenu		{ text-decoration: none; color : #E3DDFF;  }
a.mainmenu:hover{ text-decoration: underline; color : #E3DDFF; }


/* Forum category titles */
.cattitle		{ font-weight: bold; font-size: 12px ; letter-spacing: 1px; color : #E3DDFF}
a.cattitle		{ text-decoration: none; color : #E3DDFF; }
a.cattitle:hover{ text-decoration: underline; }


/* Forum title: Text and link to the forums used in: index.php */
.forumlink		{ font-weight: bold; font-size: 12px; color : #E3DDFF; }
a.forumlink 	{ text-decoration: none; color : #E3DDFF; }
a.forumlink:hover{ text-decoration: underline; color : #E3DDFF; }


/* Used for the navigation text, (Page 1,2,3 etc) and the navigation bar when in a forum */
.nav			{ font-weight: bold; font-size: 11px; color : #FFE8FF;}
a.nav			{ text-decoration: none; color : #E3DDFF; }
a.nav:hover		{ text-decoration: underline; }


/* titles for the topics: could specify viewed link colour too */
.topictitle,h1,h2	{ font-weight: bold; font-size: 11px; color : #FFE8FF; }
a.topictitle:link   { text-decoration: none; color : #E3DDFF; }
a.topictitle:visited { text-decoration: none; color : #9C96B6; }
a.topictitle:hover	{ text-decoration: underline; color : #E3DDFF; }



/* Name of poster in viewmsg.php and viewtopic.php and other places */
.name			{ font-size : 11px; color : #FFE8FF;}

/* Location, number of posts, post date etc */
.postdetails		{ font-size : 10px; color : #E3DDFF; }


/* The content of the posts (body of text) */
.postbody { font-size : 12px; line-height: 18px}
a.postlink:link	{ text-decoration: underline; color : #D8B7FF }
a.postlink:visited { text-decoration: underline; color : #D8B7FF; }
a.postlink:hover { text-decoration: underline; color : #D8B7FF}


/* Quote & Code blocks */
.code {
	font-family: 'MS P�S�V�b�N', Courier, 'Courier New', sans-serif; font-size: 11px; color: #EBE5FF;
	background-color: #676579; border: #333344; border-style: solid;
	border-left-width: 1px; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px
}

.quote {
	font-family: 'MS P�S�V�b�N', Verdana, Arial, Helvetica, sans-se; font-size: 11px; color: #EBE5FF; line-height: 125%;
	background-color: #676579; border: #333344; border-style: solid;
	border-left-width: 1px; border-top-width: 1px; border-right-width: 1px; border-bottom-width: 1px
}


/* Copyright and bottom info */
.copyright		{ font-size: 10px; font-family: 'MS P�S�V�b�N', Verdana, Arial, Helvetica, sans-se; color: #BBBBDD; letter-spacing: -1px;}
a.copyright		{ color: #BBBBDD; text-decoration: none;}
a.copyright:hover { color: #FFE8FF; text-decoration: underline;}


/* Form elements */
input,textarea, select {
	color : #000000;
	font: normal 11px 'MS P�S�V�b�N', Verdana, Arial, Helvetica, sans-se;
	border-color : #000000;
}

/* The text input fields background colour */
input.post, textarea.post, select {
	background-color : #ffffff;
}

input { text-indent : 2px; }

/* The buttons used for bbCode styling in message post */
input.button {
	background-color : #efefef;
	color : #000000;
	font-size: 11px; font-family: 'MS P�S�V�b�N', Verdana, Arial, Helvetica, sans-se;
}

/* The main submit button option */
input.mainoption {
	background-color : #fafafa;
	font-weight : bold;
}

/* None-bold submit button */
input.liteoption {
	background-color : #fafafa;
	font-weight : normal;
}

/* This is the line in the posting page which shows the rollover
  help line. This is actually a text box, but if set to be the same
  colour as the background no one will know ;)
*/
.helpline { background-color: #DEE3E7; border-style: none; }


/* Import the fancy styles for IE only (NS4.x doesn't use the @import function) */
@import url("templates/DarkEQ/formIE.css");
-->
</style>

</head>

<body bgcolor="#111111" text="#FFE8FF" link="#E3DDFF" vlink="#9C96B6">
<span class="gen"><a name="top"></a></span><table width="100%" border="0" cellspacing="0" cellpadding="10" align="center">
<tr>
	<td class="bodyline">
		  <table width="100%" border="0" cellspacing="0" cellpadding="0">
			<tr>


		<td> <a href="index.php?sid=ca85e553d65bb0c19caf3adc8f902e91"><img src="templates/DarkEQ/images/logo_phpBB.gif" border="0" alt="BuchiOnline �t�H�[�����C���f�b�N�X" vspace="1" /></a>
		</td>


		<td align="center" width="100%" valign="middle"><span class="maintitle">BuchiOnline</span><br />
		  <span class="gen">Online Game Databases<br />&nbsp; </span>

		  <table cellspacing="0" cellpadding="2" border="0">
			<tr>
			  <td valign="top" nowrap="nowrap" align="center"><span class="mainmenu">&nbsp;<a href="faq.php?sid=ca85e553d65bb0c19caf3adc8f902e91" class="mainmenu"><img src="templates/DarkEQ/images/icon_mini_faq.gif" width="12" height="13" border="0" alt="FAQ" hspace="3" />FAQ</a></span><span class="mainmenu">&nbsp;&nbsp;&nbsp;<a href="search.php?sid=ca85e553d65bb0c19caf3adc8f902e91" class="mainmenu"><img src="templates/DarkEQ/images/icon_mini_search.gif" width="12" height="13" border="0" alt="����" hspace="3" />����</a>&nbsp;&nbsp;&nbsp;<a href="memberlist.php?sid=ca85e553d65bb0c19caf3adc8f902e91" class="mainmenu"><img src="templates/DarkEQ/images/icon_mini_members.gif" width="12" height="13" border="0" alt="�����o�[���X�g" hspace="3" />�����o�[���X�g</a>&nbsp;&nbsp;&nbsp;<a href="groupcp.php?sid=ca85e553d65bb0c19caf3adc8f902e91" class="mainmenu"><img src="templates/DarkEQ/images/icon_mini_groups.gif" width="12" height="13" border="0" alt="���[�U�O���[�v" hspace="3" />���[�U�O���[�v</a>&nbsp;&nbsp;&nbsp;<a href="profile.php?mode=register&amp;sid=ca85e553d65bb0c19caf3adc8f902e91" class="mainmenu"><img src="templates/DarkEQ/images/icon_mini_register.gif" width="12" height="13" border="0" alt="�o�^" hspace="3" />�o�^</a></span></td>
			</tr>
			<tr>
			  <td nowrap="nowrap" valign="top" height="25" align="center"><span class="mainmenu">&nbsp;<a href="profile.php?mode=editprofile&amp;sid=ca85e553d65bb0c19caf3adc8f902e91" class="mainmenu"><img src="templates/DarkEQ/images/icon_mini_profile.gif" width="12" height="13" border="0" alt="�v���t�B�[��" hspace="3" />�v���t�B�[��</a>&nbsp;&nbsp;&nbsp;<a href="privmsg.php?folder=inbox&amp;sid=ca85e553d65bb0c19caf3adc8f902e91" class="mainmenu"><img src="templates/DarkEQ/images/icon_mini_message.gif" width="12" height="13" border="0" alt="�v���C�x�[�g���b�Z�[�W���݂�ɂ̓��O�C�����K�v�ł�" hspace="3" />�v���C�x�[�g���b�Z�[�W���݂�ɂ̓��O�C�����K�v�ł�</a>&nbsp;&nbsp;&nbsp;<a href="login.php?sid=ca85e553d65bb0c19caf3adc8f902e91" class="mainmenu"><img src="templates/DarkEQ/images/icon_mini_login.gif" width="12" height="13" border="0" alt=" ���O�C�� " hspace="3" /> ���O�C�� </a></span></td>
			</tr>
		  </table>
			</td>
			</tr>
		  </table>
<span class="mainmenu"> <br /> </span>


<table width="100%" cellspacing="2" cellpadding="2" border="0">
  <tr>
	<td align="left" valign="bottom" nowrap><span class="nav"><a href="index.php?sid=ca85e553d65bb0c19caf3adc8f902e91" class="nav">BuchiOnline �t�H�[�����C���f�b�N�X</a></span></td>
  </tr>
</table>

<table border="0" cellpadding="3" cellspacing="1" width="100%" class="forumline" align="center">
	<tr>
		<th class="thHead">FAQ</th>
	</tr>
	<tr><td class="row1">
<span class="gen"><b>���O�C���Ɠo�^�ɂ���</b><br /> </span>
<span class="gen"><a href="#0" class="postlink">���O�C���ł��Ȃ���ł����H</a></span><br />
<span class="gen"><a href="#1" class="postlink">�Ȃ��o�^����K�v������܂����H</a></span><br />
<span class="gen"><a href="#2" class="postlink">�Ȃ������I�Ƀ��O�I�t����Ă��܂��H</a></span><br />
<span class="gen"><a href="#3" class="postlink">�I�����C�����[�U�Ɏ����̃��[�U���������Ȃ��悤�ɂ���ɂ́H</a></span><br />
<span class="gen"><a href="#4" class="postlink">�p�X���[�h��Y��Ă��܂����I</a></span><br />
<br />
<span class="gen"><b>���[�U�����ݒ�ɂ���</b><br /> </span>
<span class="gen"><a href="#5" class="postlink">�ǂ�����Ď����̐ݒ��ύX����H</a></span><br />
<span class="gen"><a href="#6" class="postlink">�ǂ�����ă��[�U���̉��ɉ摜���͂����H</a></span><br />
<span class="gen"><a href="#7" class="postlink">�ǂ�����Ď����̃����N��ύX����H</a></span><br />
<span class="gen"><a href="#8" class="postlink">���[�U��Email�����N���N���b�N����ƁA���O�C������悤�ɂ����܂�</a></span><br />
<br />
<span class="gen"><b>�L���̓��e�ɂ���</b><br /> </span>
<span class="gen"><a href="#9" class="postlink">�ǂ�����ċL���𓊍e����H</a></span><br />
<span class="gen"><a href="#10" class="postlink">�ǂ�����ċL����ҏW������폜����H</a></span><br />
<span class="gen"><a href="#11" class="postlink">�ǂ�����Ď����̋L���ɏ���������H</a></span><br />
<span class="gen"><a href="#12" class="postlink">�ǂ�����ăA���P�[�g������H</a></span><br />
<span class="gen"><a href="#13" class="postlink">�Ȃ����[�ł��Ȃ��H</a></span><br />
<br />
<span class="gen"><b>�t�H�[�}�b�g�ƃg�s�b�N�`��</b><br /> </span>
<span class="gen"><a href="#14" class="postlink">BBCode �Ƃ́H</a></span><br />
<span class="gen"><a href="#15" class="postlink">HTML�͎g���܂����H</a></span><br />
<span class="gen"><a href="#16" class="postlink">Smiles�Ƃ́H</a></span><br />
<span class="gen"><a href="#17" class="postlink">�摜�𓊍e�ł��܂����H</a></span><br />
<span class="gen"><a href="#18" class="postlink">�A�i�E���X�Ƃ́H</a></span><br />
<span class="gen"><a href="#19" class="postlink">Sticky �Ƃ́H</a></span><br />
<span class="gen"><a href="#20" class="postlink">���b�N���ꂽ�g�s�b�N�X�Ƃ́H</a></span><br />
<br />
<span class="gen"><b>���[�U���x���ƃO���[�v</b><br /> </span>
<span class="gen"><a href="#21" class="postlink">�Ǘ��҂Ƃ́H</a></span><br />
<span class="gen"><a href="#22" class="postlink">���f���[�^�Ƃ́H</a></span><br />
<span class="gen"><a href="#23" class="postlink">���[�U�O���[�v�Ƃ́H</a></span><br />
<span class="gen"><a href="#24" class="postlink">�Ƃ�����ă��[�U�O���[�v�֎Q������H</a></span><br />
<span class="gen"><a href="#25" class="postlink">�Ƃ�����ă��[�U�O���[�v�̃��f���[�^�ɂȂ�H</a></span><br />
<br />
<span class="gen"><b>�v���C�x�[�g���b�Z�[�W</b><br /> </span>
<span class="gen"><a href="#26" class="postlink">�v���C�x�[�g���b�Z�[�W�𑗐M�ł��܂���I</a></span><br />
<br />
<span class="gen"><b>phpBB 2 �ɂ���</b><br /> </span>
<span class="gen"><a href="#27" class="postlink">���̌f���͒N���������́H</a></span><br />
<br />
</td><tr>
<td height="28" class="catBottom">&nbsp;</td>
	</tr>
</table>

<br clear="all" />

<table border="0" cellpadding="3" cellspacing="1" width="100%" class="forumline" align="center">
	<tr>
		<td height="28" class="catHead" align="center"><span class="cattitle">���O�C���Ɠo�^�ɂ���</span></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="0"></a><b>���O�C���ł��Ȃ���ł����H</b></span><br /><span class="postbody">�o�^�͂��ς݂ł����H���O�C������ɂ͓o�^���K�v�ł��B�A�N�Z�X���ۂ���Ă��܂��񂩁H���Ȃ��̋L���͕\������Ă��܂����H�����A���Ȃ��̋L�����폜����Ă���悤�ł���ΊǗ��҂ɂ��A���������B�o�^���Ă��āA�A�N�Z�X���ۂ�����Ă��Ȃ��ꍇ�́A���[�U���ƃp�X���[�h����������Ɗm�F���ĉ������B�������������ΊǗ��҂ɂ��A���������B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row2"><span class="postbody"><a name="1"></a><b>�Ȃ��o�^����K�v������܂����H</b></span><br /><span class="postbody">�L���𓊍e���邽�߂ɓo�^����K�v�����邩�ǂ����́A�Ǘ��҂̐ݒ�ɂ��܂��B�������A�o�^����΁A�t�H�[�����̒ǉ��@�\�𗘗p���邱�Ƃ��ł��܂��BAvatar�摜�A�v���C�x�[�g���b�Z�[�W�A���̃��[�U�ւ̃��[�����M�A���[�U�O���[�v�ւ̎Q���ȂǁB�o�^�͐����Ŋ������܂��̂ŁA����o�^���ĉ������B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="2"></a><b>�Ȃ������I�Ƀ��O�I�t����Ă��܂��H</b></span><br /><span class="postbody">���O�C�����鎞�� <i>�����I�Ƀ��O�C������</i> �Ƀ`�F�b�N����ꂸ�Ƀ��O�C������ƁA�A�N�Z�X���Ă��鎞�������O�C����ԂɂȂ�܂��B����͂��Ȃ��ȊO�̕������Ȃ��̖��O�Ńt�H�[�����֎Q�����Ȃ��悤�ɂ��邽�߂ł��B�`�F�b�N��t���ă��O�C������ƃA�N�Z�X���鎞�͏�Ƀ��O�C��������ԂƂȂ�܂��B�����̃��[�U���g�p����p�\�R���ł̓`�F�b�N��t���Ȃ��ŉ������B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row2"><span class="postbody"><a name="3"></a><b>�I�����C�����[�U�Ɏ����̃��[�U���������Ȃ��悤�ɂ���ɂ́H</b></span><br /><span class="postbody">�����ݒ�ŁA <i>�I�����C����Ԃ��B�� </i>�� <i>on</i> �ɂ���ƁA�Ǘ��҂Ƃ��Ȃ����g�����Ɍ�����悤�ɂȂ�A�B��o�^�҂Ƃ��ăJ�E���g����܂��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="4"></a><b>�p�X���[�h��Y��Ă��܂����I</b></span><br /><span class="postbody">���O�C����ʂɂ��� <u>�p�X���[�h��Y�ꂽ</u> ���N���b�N���ĉ������B���[�U���ƃ��[���A�h���X����͂���΁A�V�����p�X���[�h�����[���ő��M���܂��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
</table>

<br clear="all" />
<table border="0" cellpadding="3" cellspacing="1" width="100%" class="forumline" align="center">
	<tr>
		<td height="28" class="catHead" align="center"><span class="cattitle">���[�U�����ݒ�ɂ���</span></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="5"></a><b>�ǂ�����Ď����̐ݒ��ύX����H</b></span><br /><span class="postbody">���ɓo�^���Ă���ꍇ�A���Ȃ��̐ݒ�͂��ׂăf�[�^�x�[�X�ɕۑ�����Ă��܂��B��ʉE��ɂ��� <u>�v���t�B�[��</u> ���N���b�N���ĉ������B�����őS�Ă̐ݒ��ύX�ł��܂��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row2"><span class="postbody"><a name="6"></a><b>�ǂ�����ă��[�U���̉��ɉ摜���͂����H</b></span><br /><span class="postbody">�L���������ʂŁA���[�U���̉��ɂQ�̉摜�����邩������܂���B�����N��\���摜�i����ȂǂŃ��[�U�̓��e���ɉ����ă����N�����j�ƁAAvatar�摜�i���[�U�̔��ʂ𖾂炩�ɂ��邽�߂̉摜�j�ł��B�摜��t�����邩�ǂ����́A�Ǘ��҂����肵�Ă��܂��B�摜��t������悤�ɐݒ肳��Ă���΁A�v���t�B�[���ҏW��ʂ̈�ԉ��̍��ڂŁA�摜���A�b�v���[�h�ł��܂��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="7"></a><b>�ǂ�����Ď����̃����N��ύX����H</b></span><br /><span class="postbody">���Ȃ��͒��ڃ����N��ύX���邱�Ƃ͂ł��܂���B�����N�͓��e���ȂǂŌ��肳��Ă��܂��̂ŁA�������񓊍e����΃����N�͏㏸���܂��B�����N��\�����邩�ǂ����́A�Ǘ��҂̐ݒ莟��ł��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row2"><span class="postbody"><a name="8"></a><b>���[�U��Email�����N���N���b�N����ƁA���O�C������悤�ɂ����܂�</b></span><br /><span class="postbody">���[���t�H�[������́A�o�^�҂݂̂��A���̃��[�U�փ��[���𑗐M���邱�Ƃ��ł��܂��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
</table>

<br clear="all" />
<table border="0" cellpadding="3" cellspacing="1" width="100%" class="forumline" align="center">
	<tr>
		<td height="28" class="catHead" align="center"><span class="cattitle">�L���̓��e�ɂ���</span></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="9"></a><b>�ǂ�����ċL���𓊍e����H</b></span><br /><span class="postbody">�V�K�g�s�b�N���쐬���鎞�́Anewtopic �{�^���A�ԐM���鎞�́Apostreply �{�^�����N���b�N���ĉ������B���e����ꍇ�͓o�^����K�v�����邩������܂���i�Ǘ��҂̐ݒ莟��ł��j�B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row2"><span class="postbody"><a name="10"></a><b>�ǂ�����ċL����ҏW������폜����H</b></span><br /><span class="postbody">���Ȃ����Ǘ��҂܂��̓��f���[�^�łȂ���΁A�����̋L��������ҏW�A�폜���邱�Ƃ��ł��܂��B���Ȃ��̋L����ҏW����ꍇ�́A���̋L���� <i>edit</i> �{�^�����N���b�N���ĉ������B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="11"></a><b>�ǂ�����Ď����̋L���ɏ���������H</b></span><br /><span class="postbody">�L���ɏ���������ɂ́A�܂��v���t�B�[���ҏW��ʂŏ������쐬���ĉ������B���̌�A���e���鎞��[
����������v�Ƀ`�F�b�N������ē��e���ĉ������B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row2"><span class="postbody"><a name="12"></a><b>�ǂ�����ăA���P�[�g������H</b></span><br /><span class="postbody">�V�K�g�s�b�N���쐬���鎞�ɁA�A���P�[�g�����鍀�ڂŎ���ƃI�v�V��������͂��ĉ������B�Q�ȏ�̃I�v�V�������K�v�Ȃ̂ŁA�I�v�V�����ǉ����N���b�N���Ēǉ����ĉ������B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="13"></a><b>�Ȃ����[�ł��Ȃ��H</b></span><br /><span class="postbody">�o�^���[�U���������[�ł��܂��B�o�^���Ă��āA���̃A���P�[�g�ɂ܂����[���Ă��Ȃ��ꍇ�́A�A�N�Z�X��������Ă��܂���B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
</table>

<br clear="all" />
<table border="0" cellpadding="3" cellspacing="1" width="100%" class="forumline" align="center">
	<tr>
		<td height="28" class="catHead" align="center"><span class="cattitle">�t�H�[�}�b�g�ƃg�s�b�N�`��</span></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="14"></a><b>BBCode �Ƃ́H</b></span><br /><span class="postbody">BBCode ��HTML�Ɏ����\�����@�ł��BBBCode ���g�p�ł��邩�ǂ����͊Ǘ��҂̐ݒ莟��ł��B�g�p�\�ƂȂ��Ă��Ă��A�L���𓊍e���鎞�ɁA�g�p����A���Ȃ���I���ł��܂��BBBCode�^�O�́A&lt; �� &gt; �ł͂Ȃ� [ �� ] �ł͂��܂�Ă��܂��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row2"><span class="postbody"><a name="15"></a><b>HTML�͎g���܂����H</b></span><br /><span class="postbody">�Ǘ��҂̐ݒ莟��ł��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="16"></a><b>Smiles�Ƃ́H</b></span><br /><span class="postbody">�����\���������ȃA�C�R���̂��Ƃł��B���e��ʂ̍����Ɉꗗ�\������Ă��܂��̂ŁA�N���b�N���邱�ƂŋL���ɑ}�����邱�Ƃ��ł��܂��B�܂��A�L���̒��Ŏg�p���Ȃ��悤�ɂ��邱�Ƃ��\�ł��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row2"><span class="postbody"><a name="17"></a><b>�摜�𓊍e�ł��܂����H</b></span><br /><span class="postbody">�L���̒��ɉ摜��\�������邱�Ƃ͉\�ł����A�t�H�[�����։摜�t�@�C�����A�b�v���[�h���邱�Ƃ͂ł��܂���B���̃T�[�o�ɂ���摜��URL���g�p���Ă��������B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="18"></a><b>�A�i�E���X�Ƃ́H</b></span><br /><span class="postbody">�A�i�E���X�́A�d�v�ȏ����܂�ł��܂��̂ŁA�ł��邾�������ǂ�ŉ������B�A�i�E���X�̓g�s�b�N�X�ꗗ�̃g�b�v�ɕ\������܂��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row2"><span class="postbody"><a name="19"></a><b>Sticky �Ƃ́H</b></span><br /><span class="postbody">Sticky �̓A�i�E���X�قǏd�v�ł͂Ȃ��ł����A������Əd�v�Ȃ��m�点�ł��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="20"></a><b>���b�N���ꂽ�g�s�b�N�X�Ƃ́H</b></span><br /><span class="postbody">���b�N���ꂽ�g�s�b�N�X�̓��f���[�^�܂��͊Ǘ��҂��ݒ肵�Ă��܂��B���̃g�s�b�N�ɂ͕ԐM���邱�Ƃ͂ł��܂���B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
</table>

<br clear="all" />
<table border="0" cellpadding="3" cellspacing="1" width="100%" class="forumline" align="center">
	<tr>
		<td height="28" class="catHead" align="center"><span class="cattitle">���[�U���x���ƃO���[�v</span></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="21"></a><b>�Ǘ��҂Ƃ́H</b></span><br /><span class="postbody">�Ǘ��҂́A�f���S�̂��Ǘ�����l�ł��B�p�[�~�b�V�����̐ݒ�A���[�U�̃A�N�Z�X�����A���[�U�O���[�v�⃂�f���[�^�̍쐬�ȂǑS�Ă̌����������Ă��܂��B�܂��A�S�Ẵt�H�[�����ł̃��f���[�^�����˂Ă��܂��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row2"><span class="postbody"><a name="22"></a><b>���f���[�^�Ƃ́H</b></span><br /><span class="postbody">���f���[�^�͂P�t�H�[�������Ǘ�����l�̂��Ƃł��B�t�H�[�����ł̋c���I�Ȗ��������܂��B�P�t�H�[�����̒��ŋL����ҏW������폜�����肷�邱�Ƃ��ł��܂��B.<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="23"></a><b>���[�U�O���[�v�Ƃ́H</b></span><br /><span class="postbody">���[�U�O���[�v�́A�Ǘ��҂����[�U���ЂƂ܂Ƃ܂�ɂ��邽�߂̂��̂ł��B���[�U�͂������̃O���[�v�֎Q�����邱�Ƃ��ł��܂��B�O���[�v���ɃA�N�Z�X������^�����肷�邱�Ƃ��\�ł��B�v���C�x�[�g�t�H�[�����Ȃǂւ̐����ȂǁA�Ǘ��҂��Ǘ����₷���悤�ɂ���@�\�ł��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row2"><span class="postbody"><a name="24"></a><b>�Ƃ�����ă��[�U�O���[�v�֎Q������H</b></span><br /><span class="postbody">���[�U�O���[�v�֎Q������ɂ́A��ʉE��̃��[�U�O���[�v�ւ̃����N���N���b�N���ĉ������B�S�Ẵ��[�U�O���[�v���m�F���邱�Ƃ��ł��܂����A�S�ẴO���[�v�ɃA�N�Z�X�ł���Ƃ͌���܂���B�I�[�v���ȃO���[�v�ɎQ������ɂ͎Q���{�^�����N���b�N���ĉ������B�Ǘ��҂܂��̓��f���[�^�����F��A�O���[�v�ւ̎Q���ƂȂ�܂��B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="25"></a><b>�Ƃ�����ă��[�U�O���[�v�̃��f���[�^�ɂȂ�H</b></span><br /><span class="postbody">���[�U�O���[�v�͌f���Ǘ��҂��쐬���A���f���[�^��ݒ肵�܂��B���Ȃ������[�U�O���[�v���쐬���A���f���[�^�ɂȂ肽���ꍇ�́A�v���C�x�[�g���b�Z�[�W�ɂĊǗ��҂ւ��A���������B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
</table>

<br clear="all" />
<table border="0" cellpadding="3" cellspacing="1" width="100%" class="forumline" align="center">
	<tr>
		<td height="28" class="catHead" align="center"><span class="cattitle">�v���C�x�[�g���b�Z�[�W</span></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="26"></a><b>�v���C�x�[�g���b�Z�[�W�𑗐M�ł��܂���I</b></span><br /><span class="postbody">�R�̗��R���l�����܂��F�P�ڂ́A���Ȃ����o�^���Ă��Ȃ��A�܂��̓��O�C�����Ă��Ȃ��ꍇ�B�Q�ڂ͊Ǘ��҂��v���C�x�[�g���b�Z�[�W�������Ă��Ȃ��ꍇ�B�R�ڂ͊Ǘ��҂����Ȃ��Ƀv���C�x�[�g���b�Z�[�W�������Ă��Ȃ��ꍇ�B�R�ڂ̗��R�̏ꍇ�͊Ǘ��҂ɂ����˂ĉ������B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
</table>

<br clear="all" />
<table border="0" cellpadding="3" cellspacing="1" width="100%" class="forumline" align="center">
	<tr>
		<td height="28" class="catHead" align="center"><span class="cattitle">phpBB 2 �ɂ���</span></td>
	</tr>
	<tr>
		<td align="left" valign="top" class="row1"><span class="postbody"><a name="27"></a><b>���̌f���͒N���������́H</b></span><br /><span class="postbody">���̃\�t�g�E�F�A (�J�X�^�}�C�Y���Ă��Ȃ�����) ���쐬�����쌠�������Ă���̂́A<a href="http://www.phpbb.com/" target="_blank">phpBB Group</a> �ł��BGNU General Public Licence �̂��ƂŎ��R�ɍĔz�z�\�ł��B�ڂ����̓����N���N���b�N���ĉ������B<br /><a href="#Top" class="postlink">�g�b�v�ւ��ǂ�</a></span></td>
	</tr>
	<tr>
		<td height="1" class="spaceRow"><img src="templates/DarkEQ/images/spacer.gif" alt="" width="1" height="1" /></td>
	</tr>
</table>

<br clear="all" />

<table width="100%" cellspacing="2" border="0" align="center">
  <tr>
	  <td align="right" valign="middle" nowrap><span class="gensmall">���Ԑݒ�́A GMT + 9 ����</span><br /><br />
<form method="GET" name="jumpbox" action="viewforum.php?sid=ca85e553d65bb0c19caf3adc8f902e91">
  <table cellspacing="0" cellpadding="0" border="0">
	<tr>
	  <td nowrap="nowrap"><span class="gensmall">�ړ��F:&nbsp;<select name="f" onChange="if(this.options[this.selectedIndex].value != -1){ forms['jumpbox'].submit() }"><option value="-1">�t�H�[������I��</option><option value="-1">&nbsp;</option><option value="-1">Public</option><option value="-1">----------------</option><option value="1">General Forum</option><option value="-1">&nbsp;</option><option value="-1">EverQuest</option><option value="-1">----------------</option><option value="2">EverQuest Players</option><option value="-1">&nbsp;</option><option value="-1">FINAL FANTASY XI ONLINE</option><option value="-1">----------------</option><option value="3">FF11 Pub</option></select><input type="hidden" name="sid" value="sid=ca85e553d65bb0c19caf3adc8f902e91" />&nbsp;
		<input type="submit" value="Go" class="liteoption" />
		</span></td>
	</tr>
  </table>
</form>

</td>
  </tr>
</table>


<div align="center"> <span class="copyright"><br /><br />
  <!--

	Please note that the following copyright notice
	MUST be displayed on each and every page output
	by phpBB. You may alter the font, colour etc. but
	you CANNOT remove it, nor change it so that it be,
	to all intents and purposes, invisible. You may ADD
	your own notice to it should you have altered the
	code but you may not replace it. The hyperlink must
	also remain intact. These conditions are part of the
	licence this software is released under. See the
	LICENCE and README files for more information.

	The phpBB Group : 2001

// -->
  Powered by phpBB 2.0.0 &copy; 2001 <a href="http://www.phpbb.com/" target="_phpbb" class="copyright">phpBB
  Group</a><br> -- Theme by <a href="mailto:Shady@ShadyNeighbor.com" class="copyright">ShadyNeighbor</a> - EQ graphic from <a href="http://www.freeclipart.nu/" class="copyright">www.freeclipart.nu/</a> -- <br /></span></div>
	</td>
  </tr>
</table>
&nbsp;
</body>
</html>

