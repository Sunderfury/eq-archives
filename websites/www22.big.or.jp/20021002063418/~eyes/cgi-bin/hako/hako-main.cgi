<HTML>
<HEAD>
<TITLE>
Mithaniel Marr Type R.A.
</TITLE>
<LINK REL="stylesheet" TYPE="text/css" HREF="./hako.css">
<BASE HREF="http://www.geocities.co.jp/Playtown-King/3466/hakora/">
</HEAD>
<BODY BGCOLOR="#EEFFFF">
[<A HREF="http://t.pos.to/hako/" target="_blank">���돔���X�N���v�g�z�z��</A>] [<A HREF="http://www5b.biglobe.ne.jp/~k-e-i/i.html" target="_blank">Hakoniwa R.A.�z�z��</A>] [<a href="henko.html" target="_blank">�ڂ����ύX�_�͂���</A>]
 [<a href="http://www22.big.or.jp/~eyes/cgi-bin/rf/wwwforum.cgi?id=3" target="_blank">�f����</A>]<HR>
<hr WIDTH="100%">
<B>�^�[��<FONT COLOR="royalblue">3452</FONT>�܂�&nbsp;<IMG name="_hour1" src="http://www.geocities.co.jp/Playtown-King/3466/hakora/0.gif" align="middle"><IMG name="_hour0" src="http://www.geocities.co.jp/Playtown-King/3466/hakora/2.gif" align="middle">&nbsp;����&nbsp;<IMG name="_min1"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/1.gif" align="middle"><IMG name="_min0"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/5.gif" align="middle">&nbsp;��&nbsp;<IMG name="_sec1"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/4.gif" align="middle"><IMG name="_sec0"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/2.gif" align="middle">&nbsp;�b&nbsp;&nbsp;(10/2 17:50)</B>
<P>
<SCRIPT language="JavaScript">
<!--
// �c�莞��
var day  = 0;
var hour = 2;
var min  = 15;
var sec  = 42;

// �摜�̐�ǂ�
var img = new Array(10);
var i;
for (i = 0; i < 10; i++) {
    img = new Image();
    img.src = i + ".gif";
}

// �P�b���Ƃ̍X�V����
function update() {
    if (--sec < 0) {
        sec = 59;
        if (--min < 0) {
            min = 59;
            if (--hour < 0) {
                hour = 23;
                if (--day < 0) {
                    sec = min = hour = day = 0;
                }
            }
        }
    }

    if ((day == 0) && (hour == 0) && (min == 0) && (sec == 0)) {
        _min1.src = _min0.src = "0.gif";
        _sec1.src = _sec0.src = "0.gif";
    } else {
        window.setTimeout("update();", 1000);
    }

    var day1  = Math.floor(day / 10);
    var day0  = day % 10;
    var hour1 = Math.floor(hour / 10);
    var hour0 = hour % 10;
    var min1  = Math.floor(min / 10);
    var min0  = min % 10;
    var sec1  = Math.floor(sec / 10);
    var sec0  = sec % 10;

    with (document) {
        if (day > 0) {
            _day1.src  = day1  + ".gif";
            _day0.src  = day0  + ".gif";
        }
        if ((day > 0) || (hour > 0)) {
            _hour1.src = hour1 + ".gif";
            _hour0.src = hour0 + ".gif";
        }
        _min1.src  = min1  + ".gif";
        _min0.src  = min0  + ".gif";
        _sec1.src  = sec1  + ".gif";
        _sec0.src  = sec0  + ".gif";
    }
}
update();
//-->
</SCRIPT>
<FONT SIZE=7 COLOR="#8888ff">Mithaniel Marr Type R.A.</FONT>
<H1><FONT COLOR="#4444ff">�^�[��3451</FONT></H1>
<FORM name="RemainForm"><INPUT name="RemainTime" size="30" type="text" readonly></FORM><SCRIPT language="JavaScript">
<!--
nextTurn = 8142; loadDate = new Date();
timerID = setTimeout('dispRemainTime()', 100);
function dispRemainTime() { clearTimeout(timerID);
document.RemainForm.RemainTime.value = getRemainTime();
timerID = setTimeout('dispRemainTime()', 1000);}
function getRemainTime() {
now = new Date();msec = now.getTime() - loadDate.getTime();
msec -= msec % 1000; msec /= 1000;msec = nextTurn - msec;
if (msec < 0) {msec = 0;}
sec = msec % 60; msec = (msec - sec) / 60;
min = msec % 60; hour = (msec - min) / 60;
if (hour < 10) {hour = "0" + hour;}
if (min < 10) {min = "0" + min;}
if (sec < 10) {sec = "0" + sec;}
return "���̃^�[���܂Ŏc��" + hour + ":" + min + ":" + sec;}
//-->
</SCRIPT>
<HR>
<H1><FONT COLOR="#4444ff">�����̓���</FONT></H1>
<FORM action="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi" method="POST">
���Ȃ��̓��̖��O�́H<BR>
<SELECT NAME="ISLANDID">
<OPTION VALUE="23" >�a�e�c�{����
<OPTION VALUE="13" >�q�b�v���L����
<OPTION VALUE="6" >������_�̓�
<OPTION VALUE="2" >��_������
<OPTION VALUE="18" >����

</SELECT><BR>

�p�X���[�h���ǂ����I�I<BR>
<INPUT TYPE="password" NAME="PASSWORD" VALUE="" SIZE=32 MAXLENGTH=32><BR>
<INPUT TYPE="submit" VALUE="�J�����ɍs��" NAME="OwnerButton"><BR>
</FORM>

<HR>
<script language="javascript">
<!--
function getcookie(tmp1, tmp2, xx1, xx2, xx3,cname,ccolor){
tmp1 = " " + document.cookie + ";";
xx1 = xx2 = ccolor = 0;
cname = "";len = tmp1.length;
while(xx1 < len){
	xx2 = tmp1.indexOf(";", xx1);
	tmp2 = tmp1.substring(xx1 + 1, xx2);
	xx3 = tmp2.indexOf("=");
	if (tmp2.substring(0, xx3) == "cname") {
		cname = (unescape(tmp2.substring(xx3 + 1, xx2 - xx1 - 1)));
		}
	else if (tmp2.substring(0, xx3) == "ccolor") {
		ccolor = (unescape(tmp2.substring(xx3 + 1, xx2 - xx1 - 1)));
		}
	xx1 = xx2 + 1;
	}
if (ccolor == ""){ccolor = 0;}
document.wform.name.value = cname;
document.wform.color.selectedIndex = ccolor;
}

function setcookie(tmp){
tmp = "cname=" + escape(document.wform.name.value) + "; ";
tmp += "expires=Fri, 31-Dec-2030 23:59:59; ";
document.cookie = tmp;
tmp = "ccolor=" + escape(document.wform.color.selectedIndex) + "; ";
tmp += "expires=Fri, 31-Dec-2030 23:59:59; ";
document.cookie = tmp;
}
// -->
</script>
<noscript>
����BBS�𗘗p����ɂ́AJavaScript���K�v�ł��B
</noscript>


<form name="wform" method="post" action="http://www22.big.or.jp/~eyes/cgi-bin/lblightc/lblightc.cgi">

Name:<input type="text" name="name" size=10>

Color:<select name="color">
<option value="#000000">Black
<option value="#8080ff">Blue
<option value="#40a0a0">Pale Blue
</select>

Message:<input type="text" name="msg" size=20>

<input type="submit" value="Write" onclick="setcookie();">

<input type="hidden" name="act" value="write">

<input type="hidden" name="id" value="id1">

</form>

<hr>
<script language="javascript" src="http://www22.big.or.jp/~eyes/cgi-bin/lblightc/id1.js"></script>
<noscript>����BBS������ɂ�JavaScript���K�v�ł��B</noscript>
<hr>
<a href="http://www22.big.or.jp/~eyes/cgi-bin/lblightc/lblightc.cgi?act=pastlog&id=id1">�ߋ����O�\��</a>

<H1><FONT COLOR="#4444ff">�e����ʂm�n.�P</FONT></H1>
<P>
�ڎw��<B>�`�k�k �m�n.�P</B>�I�I�N���b�N����ƁA<B>�ό�</B>���邱�Ƃ��ł��܂��B
</P>
<TABLE ALIGN="center" width="100%"><tr><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�l��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">11412500�l</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�_��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=13" "alt="ID=13"><FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT></TD></TR>
<TR><TD ALIGN="center">3461000�l�K��</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�E��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">12857000�l�K��</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�̌@��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=18" "alt="ID=18"><FONT COLOR="#a06040"><B>����</B></FONT></TD></TR>
<TR><TD ALIGN="center">185000�l�K��</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�X��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=13" "alt="ID=13"><FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT></TD></TR>
<TR><TD ALIGN="center">000�{</TD></TR>
</TABLE>
</TABLE>
<br>
<TABLE ALIGN="center" width="100%">
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�ɂ�Ƃ萔NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">4000���H</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�Ԃ���NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">12000����</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>������NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=6" "alt="ID=6"><FONT COLOR="#a06040"><B>������_�̓�</B></FONT></TD></TR>
<TR><TD ALIGN="center">37169����</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>���b�o����NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=18" "alt="ID=18"><FONT COLOR="#a06040"><B>����</B></FONT></TD></TR>
<TR><TD ALIGN="center">51�C</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>���b�ގ���NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=13" "alt="ID=13"><FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT></TD></TR>
<TR><TD ALIGN="center">6398�C</TD></TR>
</TABLE>
</TABLE>
<br>
<TABLE ALIGN="center" width="100%">
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�����xNO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">�O�^�[���{187pts.</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�l������NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">�O�^�[���{13800�l</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>����NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=6" "alt="ID=6"><FONT COLOR="#a06040"><B>������_�̓�</B></FONT></TD></TR>
<TR><TD ALIGN="center">�O�^�[���{16505���~</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�L�O�萔NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=13" "alt="ID=13"><FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT></TD></TR>
<TR><TD ALIGN="center">16����</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�R���Z�pNO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=13" "alt="ID=13"><FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT></TD></TR>
<TR><TD ALIGN="center">�k��684</TD></TR>
</TABLE>
</TABLE>
</table>

<hr>

<H1><FONT COLOR="#4444ff">�����̏�</FONT></H1>
<P>
���̖��O���N���b�N����ƁA<B>�ό�</B>���邱�Ƃ��ł��܂��B
</P>
<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=0 WIDTH=100% BGCOLOR="#000000"><TR><TD>
<TABLE BORDER=0 CELLPADDING=1 CELLSPACING=1 WIDTH=100%>
<TR>
<TH BGCOLOR="#ccffcc" align=center nowrap=nowrap><NOBR><FONT COLOR="#C00000"><B>����</B></FONT></NOBR></TH>
<TH BGCOLOR="#ccffcc" align=center nowrap=nowrap><NOBR><FONT COLOR="#C00000"><B>��</B></FONT></NOBR></TH>
<TH BGCOLOR="#ccffcc" align=center nowrap=nowrap><NOBR><FONT COLOR="#C00000"><B>�l��</B></FONT></NOBR></TH>
<TH BGCOLOR="#ccffcc" align=center nowrap=nowrap><NOBR><FONT COLOR="#C00000"><B>�ʐ�</B></FONT></NOBR></TH>

<TH BGCOLOR="#ccffcc" align=center nowrap=nowrap><NOBR><FONT COLOR="#C00000"><B>�H��</B></FONT></NOBR></TH>
<TH BGCOLOR="#ccffcc" align=center nowrap=nowrap><NOBR><FONT COLOR="#C00000"><B>�_��</B></FONT></NOBR></TH>
<TH BGCOLOR="#ccffcc" align=center nowrap=nowrap><NOBR><FONT COLOR="#C00000"><B>�E��</B></FONT></NOBR></TH>
<TH BGCOLOR="#ccffcc" align=center nowrap=nowrap><NOBR><FONT COLOR="#C00000"><B>�̌@��</B></FONT></NOBR></TH>
<TH BGCOLOR="#ccffcc" align=center nowrap=nowrap><NOBR><FONT COLOR="#C00000"><B>�R���Z�p</B></FONT></NOBR></TH>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>1</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23">
<FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">158542</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-32.17%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{187pts.�{13800�l-1100���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>11412500�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>34600����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9641500�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>2227000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>12857000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��562</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT>(n3@510)</NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>SONG : </font>�N�̒���ł��󂯂�I�@��P���n�j�I</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font><IMG SRC="niwatori.gif" ALT="�ɂ�Ƃ�" WIDTH=16 HEIGHT="16">4000���H<IMG SRC="buta.gif" ALT="�Ԃ�" WIDTH=16 HEIGHT="16">12000����<IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">12444����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">71%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">28%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">44%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">42%<IMG SRC="ire.gif" ALT="�C���M�����[" WIDTH=16 HEIGHT="16">27%<IMG SRC="prize0.gif" ALT="2600�^�[���t 2700�^�[���t 2800�^�[���t 2900�^�[���t 3000�^�[���t 3100�^�[���t 3200�^�[���t 3300�^�[���t 3333�^�[���t 3400�^�[���t " WIDTH=16 HEIGHT=16> <IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize4.gif" ALT="���a��" WIDTH=16 HEIGHT=16> <IMG SRC="prize5.gif" ALT="�����a��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster26.gif" ALT="[���b���b�h���̂�] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [���b�L���O���̂�] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] [���b�͂˂͂�] [���b���C�W��] [�V�g�E���G��] [���p�t�A�[����] [�V�g�C�Z���A] " WIDTH=16 HEIGHT=16>4144�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>2</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=13" "alt="ID=13">
<FONT COLOR="#808080"><B>�q�b�v���L����(8)</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">139652</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-17.51%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[��-19pts.�{000�l�{8547���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9503800�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>31700����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>3461000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>7707000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��684</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT>(n3@705)</NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT>(toto@23.13.6.5.2.00.00.00)</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>Nonota : </font>�j�A1�疜�s�s�I�I</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><IMG SRC="monster13.gif" ALT="[���b�o�����A] " WIDTH=16 HEIGHT=16> <font color="hotpink">1�C�o����!!</font><IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">23270����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">19%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">62%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">59%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">21%<IMG SRC="bouei.gif" ALT="�h�q�q��" WIDTH=16 HEIGHT="16">62%<IMG SRC="ire.gif" ALT="�C���M�����[" WIDTH=16 HEIGHT="16">169%<IMG SRC="prize0.gif" ALT="1200�^�[���t 1300�^�[���t 1400�^�[���t 1500�^�[���t 1600�^�[���t 1700�^�[���t 1800�^�[���t 1900�^�[���t 2000�^�[���t 2100�^�[���t 2200�^�[���t 2222�^�[���t 2300�^�[���t 2400�^�[���t 2500�^�[���t " WIDTH=16 HEIGHT=16> <IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize4.gif" ALT="���a��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster3.gif" ALT="[���b���̂�] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [���b�L���O���̂�] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] [�V�g�E���G��] [�V�g�C�Z���A] [�����T�^��] [���b�L���O���̂�] " WIDTH=16 HEIGHT=16>6398�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>3</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=6" "alt="ID=6">
<FONT COLOR="#a06040"><B>������_�̓�</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">131828</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-23.11%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[��-114pts.-8600�l�{16505���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>8596500�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>26700����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>2411000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>8172000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��502</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT></NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>Saldia : </font>�܂�����ƁB</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><IMG SRC="monster22.gif" ALT="[���b���C�W��] " WIDTH=16 HEIGHT=16> <font color="hotpink">1�C�o����!!</font><IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">37169����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">40%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">34%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">40%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">46%<IMG SRC="bouei.gif" ALT="�h�q�q��" WIDTH=16 HEIGHT="16">51%<IMG SRC="ire.gif" ALT="�C���M�����[" WIDTH=16 HEIGHT="16">186%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster16.gif" ALT="[�l�����J���̂�] [���b�T���W��] [���b���b�h���̂�] [��b���̂�S�[�X�g] [���b�L���O���̂�] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] [���b�͂˂͂�] " WIDTH=16 HEIGHT=16>2711�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>4</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=2" "alt="ID=2">
<FONT COLOR="#a06040"><B>��_������</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">101661</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-24.67%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[��-162pts.�{600�l-19335���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>7158200�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>32800����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>3300000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>5574000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>50000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��85</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT></NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>Doramon : </font>�r���E�o�i��</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font>�@<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">82%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">61%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">70%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">87%<IMG SRC="bouei.gif" ALT="�h�q�q��" WIDTH=16 HEIGHT="16">19%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster19.gif" ALT="[���b���̂�] [���b�T���W��] [���b���b�h���̂�] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [��b�X���C��] [�X���C�����W�F���h] " WIDTH=16 HEIGHT=16>604�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>5</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=18" "alt="ID=18">
<FONT COLOR="#a06040"><B>����</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">14165</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-1145.49%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[��-423pts.-33400�l-2402���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>27700�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>29600����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>110000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>50000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>185000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��1</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT></NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>�����ҁ` : </font>�X���C���\����!!�@&gt; &lt; /</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><IMG SRC="monster14.gif" ALT="[��b�X���C��] " WIDTH=16 HEIGHT=16> <font color="hotpink">51�C�o����!!</font>�@<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">20%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">29%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">40%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">97%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster14.gif" ALT="[�l�����J���̂�] [���b���̂�] [���b�T���W��] [���b���b�h���̂�] [���b�_�[�N���̂�] [���b�N�W��] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] " WIDTH=16 HEIGHT=16>4558�C�ގ�</font></font></NOBR></TD>
</TR>
</TABLE>
</td></tr></table>

<HR>
<H1><FONT COLOR="#4444ff">�V��������T��</FONT></H1><FONT COLOR=red><B>
�����́A�l�b�g���[�N�Q�[��EverQuest��Mithaniel Marr�T�[�o�[�ŗV��ł������ΏۂƂ����A���֌�������ł��B<BR>
MM�ݏZ�҂���Ȃ����͓o�^�ł��܂���B�������������B<BR>���ɓo�^�������́A���̂܂ܗV��Œ����Ė�肠��܂���B</B></FONT>
        ���̐����ő吔�ł��E�E�E���ݓo�^�ł��܂���B
<HR>
<H1><FONT COLOR="#4444ff">���̖��O�ƃp�X���[�h�̕ύX</FONT></H1>
<P>
(����)���O�̕ύX�ɂ�500���~������܂��B
</P>
<FORM action="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi" method="POST">
�ǂ̓��ł����H<BR>
<SELECT NAME="ISLANDID">
<OPTION VALUE="23" >�a�e�c�{����
<OPTION VALUE="13" >�q�b�v���L����
<OPTION VALUE="6" >������_�̓�
<OPTION VALUE="2" >��_������
<OPTION VALUE="18" >����

</SELECT>
<BR>
�ǂ�Ȗ��O�ɕς��܂����H(�ύX����ꍇ�̂�)<BR>
<INPUT TYPE="text" NAME="ISLANDNAME" SIZE=32 MAXLENGTH=32>��<BR>
�I�[�i�[���́H(�ύX����ꍇ�̂�)<BR>
<INPUT TYPE="text" NAME="OWNERNAME" SIZE=32 MAXLENGTH=32><BR>
�p�X���[�h�́H(�K�{)<BR>
<INPUT TYPE="password" NAME="OLDPASS" SIZE=32 MAXLENGTH=32><BR>
�V�����p�X���[�h�́H(�ύX���鎞�̂�)<BR>
<INPUT TYPE="password" NAME="PASSWORD" SIZE=32 MAXLENGTH=32><BR>
�O�̂��߃p�X���[�h���������(�ύX���鎞�̂�)<BR>
<INPUT TYPE="password" NAME="PASSWORD2" SIZE=32 MAXLENGTH=32><BR>

<INPUT TYPE="submit" VALUE="�ύX����" NAME="ChangeInfoButton">
</FORM>


</TD>

<TD VALIGN=TOP WIDTH=350>
<H1><FONT COLOR="#4444ff">�摜�̃��[�J���ݒ�</FONT></H1>
���݂̐ݒ�<B>[</b> <FONT COLOR=RED>���ݒ�</FONT> <B>]</B>
�@�@<A HREF=e.html target=_BLANK><FONT SIZE=+1> �� �� </FONT></A>
<form action=http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi method=POST>
<INPUT TYPE=file NAME="IMGLINE">
<INPUT TYPE="submit" VALUE="�ݒ�" name=IMGSET>
</form>

<form action=http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi method=POST>
Mac���[�U�[�p<BR>
<INPUT TYPE=text NAME="IMGLINEMAC">
<INPUT TYPE="submit" VALUE="�ݒ�" name=IMGSET><BR>
<FONT SIZE=-1>Mac�̕��́A��������g�p���ĉ������B</FONT>
</form>
</TD></TR>

<TR HEIGHT=100><TD ALIGN=CENTER>
<form action=http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi method=POST>
<INPUT TYPE=hidden NAME="IMGLINE" value="deletemodenow">
<INPUT TYPE="submit" VALUE="�ݒ����������" name=IMGSET>
</form>
</TD></TR>
</TABLE>
<HR>

<H1><FONT COLOR="#4444ff">�ŋ߂̏o����</FONT></H1>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�</B></FONT>��<B>�C���M�����[</B>��<B>���b���C�W��</B>���U����<FONT COLOR="#ff0000"><B>5</B></FONT>�̃_���[�W��^���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�</B></FONT>��<B>���b���C�W��</B>�o���I�I<FONT COLOR="#a06040"><B>(9, 11)</B></FONT>��<B>�s�s</B>�����ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT>��<B>�C���M�����[</B>��<B>���b�o�����A</B>���U����<FONT COLOR="#ff0000"><B>6</B></FONT>�̃_���[�W��^���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT>��<B>���b�o�����A</B>�o���I�I<FONT COLOR="#a06040"><B>(9, 11)</B></FONT>��<B>��</B>�����ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>��_������(12, 17)</B></FONT>��<B>�V���n</B>����A<B>4722���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>��_������(8, 18)</B></FONT>��<B>�C����c</B>����A<B>2783���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>��_������(9, 18)</B></FONT>��<B>�C����c</B>����A<B>2806���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>��_������(13, 0)</B></FONT>��<B>�V���n</B>����A<B>5151���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>��_������(9, 19)</B></FONT>��<B>�V���n</B>����A<B>4722���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>��_������(19, 0)</B></FONT>��<B>�V���n</B>����A<B>4722���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�(1, 12)</B></FONT>��<B>�V���n</B>����A<B>5679���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�(14, 7)</B></FONT>��<B>�d�b�߂��͂�</B>�����͂ȗ͏�ɉ����ׂ���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(2, 13)</B></FONT>��<B>�C���݂�</B>�ŃC�x���g���J�Â���A<B>2279000�g��</B>�̐H���������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(14, 2)</B></FONT>��<B>�C���݂�</B>�ŃC�x���g���J�Â���A<B>2279000�g��</B>�̐H���������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(13, 10)</B></FONT>��<B>�C���݂�</B>�ŃC�x���g���J�Â���A<B>2279000�g��</B>�̐H���������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(19, 8)</B></FONT>��<B>�r�n</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(15, 4)</B></FONT>��<B>�C���݂�</B>����A<B>50���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(19, 7)</B></FONT>��<B>�h�Гs�s</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(19, 5)</B></FONT>��<B>���P�b�g</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(19, 1)</B></FONT>��<B>��</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(0, 3)</B></FONT>��<B>��b�X���C��</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(16, 11)</B></FONT>��<B>�r�n</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(17, 11)</B></FONT>��<B>�j���[�^�E��</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(18, 0)</B></FONT>��<B>��</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(19, 4)</B></FONT>��<B>�h�Гs�s</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(0, 1)</B></FONT>��<B>��b�X���C��</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(0, 2)</B></FONT>��<B>��b�X���C��</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(16, 10)</B></FONT>��<B>�h�Гs�s</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(17, 9)</B></FONT>��<B>�R</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(18, 8)</B></FONT>��<B>��</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(18, 6)</B></FONT>��<B>��</B>��<B>���C</B>�Ɉ��ݍ��܂�܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<B>���C</B>�����ݏo����<B>�E�q</B>��<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#ff0000"><B>�u�a</B></FONT>�������炵���悤�ł��I�I</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>��_������(3, 13)</B></FONT>��<FONT COLOR="#d08000"><B>����s�s����</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>��_������</B></FONT>�ŗ\�肳��Ă���<FONT COLOR="#d08000"><B>����s�s����</B></FONT>�́A�\��n��<FONT COLOR="#a06040"><B>(15, 6)</B></FONT>�������𖞂����Ă��Ȃ�<B>�j���[�^�E��</B>�̂��ߒ��~����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>��_������</B></FONT>�ŗ\�肳��Ă���<FONT COLOR="#d08000"><B>����s�s����</B></FONT>�́A�\��n��<FONT COLOR="#a06040"><B>(10, 11)</B></FONT>�������𖞂����Ă��Ȃ�<B>�j���[�^�E��</B>�̂��ߒ��~����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>��_������</B></FONT>�ŗ\�肳��Ă���<FONT COLOR="#d08000"><B>����s�s����</B></FONT>�́A�\��n��<FONT COLOR="#a06040"><B>(11, 11)</B></FONT>�������𖞂����Ă��Ȃ�<B>�j���[�^�E��</B>�̂��ߒ��~����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>��_������</B></FONT>�ŗ\�肳��Ă���<FONT COLOR="#d08000"><B>����s�s����</B></FONT>�́A�\��n��<FONT COLOR="#a06040"><B>(15, 7)</B></FONT>�������𖞂����Ă��Ȃ�<B>�j���[�^�E��</B>�̂��ߒ��~����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�</B></FONT>��<FONT COLOR="#d08000"><B>�U�v����</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT>��<FONT COLOR="#d08000"><B>�U�v����</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3451</B></FONT>�F<FONT COLOR="#a06040"><B>����(17, 19)</B></FONT>��<FONT COLOR="#d08000"><B>�H������������</B></FONT>���s���܂����B</NOBR><BR>
<H1><FONT COLOR="#4444ff">�����̋L�^</FONT></H1>
<NOBR><FONT COLOR="#800000"><B>�^�[��3450</B></FONT>�F<FONT COLOR="#a06040"><B>��3450�^�[�� Numbers4</B></FONT> <B>�F 6072</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3444</B></FONT>�F<FONT COLOR="#a06040"><B>��_������</B></FONT>��<B>�C��T���D�E��</B>������𔭌��I</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3440</B></FONT>�F<FONT COLOR="#a06040"><B>��3440�^�[�� Numbers3</B></FONT> <B>�F 272</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3438</B></FONT>�F<FONT COLOR="#a06040"><B>��_������</B></FONT>��<B>�C��T���D�E��</B>������𔭌��I</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3430</B></FONT>�F<FONT COLOR="#a06040"><B>��3430�^�[�� Numbers4</B></FONT> <B>�F 5939</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3420</B></FONT>�F<FONT COLOR="#a06040"><B>��3420�^�[�� Numbers3</B></FONT> <B>�F 552</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3410</B></FONT>�F<FONT COLOR="#a06040"><B>��3410�^�[�� Numbers4</B></FONT> <B>�F 999</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3400</B></FONT>�F<FONT COLOR="#a06040"><B>��3400�^�[�� Numbers3</B></FONT> <B>�F 180</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3400</B></FONT>�F<FONT COLOR="#a06040"><B>��3400�^�[�� ��������</B></FONT> 6�_�I�����z���� 2000���~</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��3400</B></FONT>�F<FONT COLOR="#a06040"><B>��3400�^�[�� ��������</B></FONT> <B>�F 23 13 6 2 18 0 0 0</B></NOBR><BR>
<HR>
<P align=center>
�Ǘ���:eyes(<A HREF="mailto:eyes@big.or.jp">eyes@big.or.jp</A>)<BR>
�f����(<A HREF="http://www22.big.or.jp/~eyes/cgi-bin/rf/wwwforum.cgi?id=3">http://www22.big.or.jp/~eyes/cgi-bin/rf/wwwforum.cgi?id=3</A>)<BR>
�g�b�v�y�[�W(<A HREF=""></A>)<BR>
���돔���̃y�[�W(<A HREF="http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html">http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html</A>)<BR>
Hakoniwa R.A.�̃y�[�W(<A HREF="http://www5b.biglobe.ne.jp/~k-e-i/i.html">http://www5b.biglobe.ne.jp/~k-e-i/i.html</A>)<BR>

      <CENTER>
      <TABLE BORDER="0">
      <TR>
      <TD ALIGN="CENTER" VALIGN="top">
      <a href="http://www5b.biglobe.ne.jp/~k-e-i/i.html" TARGET="_blank">
      <IMG src="http://www14.freeweb.ne.jp/photo/keikun18/rhako.gif" width="200" height="40" alt="Hakoniwa R.A." border="0"></A><BR>
      <FONT size="-1">
      <a href="http://www.webring.ne.jp/cgi-bin/webring?ring=renas;id=4;prev5" target="_blank">[�O5��]</A>
      <a href="http://www.webring.ne.jp/cgi-bin/webring?ring=renas;id=4;sprev" target="_blank">[2�O]</A>
      <a href="http://www.webring.ne.jp/cgi-bin/webring?ring=renas;id=4;prev" target="_blank">[�O]</A>
      <a href="http://www.webring.ne.jp/cgi-bin/webring?ring=renas;id=4;next" target="_blank">[��]</A>
      <a href="http://www.webring.ne.jp/cgi-bin/webring?ring=renas;id=4;skip" target="_blank">[2��]</A>
      <a href="http://www.webring.ne.jp/cgi-bin/webring?ring=renas;id=4;next5" target="_blank">[��5��]</A><BR>
      <a href="http://www.webring.ne.jp/cgi-bin/webring?ring=renas;random" target="_blank">[Random]</A>
      <a href="http://www.webring.ne.jp/cgi-bin/webring?ring=renas;list" target="_blank">[LIST]</A>
      <a href="http://www.webring.ne.jp/cgi-bin/webring?ring=renas;edit" target="_blank">[EDIT]</A>
      <a href="http://www.webring.ne.jp/cgi-bin/webring?ring=renas;addform" target="_blank">[ENTRY]</FONT><BR>      </TD>
      </TR>
      </TABLE>
      </CENTER>
</P>
</BODY>
</HTML>
