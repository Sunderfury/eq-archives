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
<B>�^�[��<FONT COLOR="royalblue">1340</FONT>�܂�&nbsp;<IMG name="_hour1" src="http://www.geocities.co.jp/Playtown-King/3466/hakora/0.gif" align="middle"><IMG name="_hour0" src="http://www.geocities.co.jp/Playtown-King/3466/hakora/1.gif" align="middle">&nbsp;����&nbsp;<IMG name="_min1"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/4.gif" align="middle"><IMG name="_min0"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/3.gif" align="middle">&nbsp;��&nbsp;<IMG name="_sec1"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/0.gif" align="middle"><IMG name="_sec0"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/4.gif" align="middle">&nbsp;�b&nbsp;&nbsp;(1/11 17:50)</B>
<P>
<SCRIPT language="JavaScript">
<!--
// �c�莞��
var day  = 0;
var hour = 1;
var min  = 43;
var sec  = 4;

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
<H1><FONT COLOR="#4444ff">�^�[��1339</FONT></H1>
<FORM name="RemainForm"><INPUT name="RemainTime" size="30" type="text" readonly></FORM><SCRIPT language="JavaScript">
<!--
nextTurn = 6184; loadDate = new Date();
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
<OPTION VALUE="13" >�q�b�v���L����
<OPTION VALUE="6" >������_�̓�
<OPTION VALUE="5" >��铇
<OPTION VALUE="12" >���I��
<OPTION VALUE="1" >���X�g�}��
<OPTION VALUE="23" >�a�e�c�{����
<OPTION VALUE="18" >����
<OPTION VALUE="2" >Sara��RealHell��

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
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=13" "alt="ID=13"><FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT></TD></TR>
<TR><TD ALIGN="center">3563800�l</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�_��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=13" "alt="ID=13"><FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT></TD></TR>
<TR><TD ALIGN="center">1343000�l�K��</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�E��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=6" "alt="ID=6"><FONT COLOR="#a06040"><B>������_�̓�</B></FONT></TD></TR>
<TR><TD ALIGN="center">4897000�l�K��</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�̌@��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=18" "alt="ID=18"><FONT COLOR="#a06040"><B>����</B></FONT></TD></TR>
<TR><TD ALIGN="center">595000�l�K��</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�X��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=2" "alt="ID=2"><FONT COLOR="#a06040"><B>Sara��RealHell��</B></FONT></TD></TR>
<TR><TD ALIGN="center">527300�{</TD></TR>
</TABLE>
</TABLE>
<br>
<TABLE ALIGN="center" width="100%">
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�ɂ�Ƃ萔NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">2612���H</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�Ԃ���NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">1369����</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>������NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=6" "alt="ID=6"><FONT COLOR="#a06040"><B>������_�̓�</B></FONT></TD></TR>
<TR><TD ALIGN="center">6587����</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>���b�o����NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">25�C</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>���b�ގ���NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">2077�C</TD></TR>
</TABLE>
</TABLE>
<br>
<TABLE ALIGN="center" width="100%">
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�����xNO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=18" "alt="ID=18"><FONT COLOR="#a06040"><B>����</B></FONT></TD></TR>
<TR><TD ALIGN="center">�O�^�[���{5241pts.</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�l������NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=12" "alt="ID=12"><FONT COLOR="#a06040"><B>���I��</B></FONT></TD></TR>
<TR><TD ALIGN="center">�O�^�[���{12200�l</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>����NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=6" "alt="ID=6"><FONT COLOR="#a06040"><B>������_�̓�</B></FONT></TD></TR>
<TR><TD ALIGN="center">�O�^�[���{30846���~</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�L�O�萔NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=1" "alt="ID=1"><FONT COLOR="#a06040"><B>���X�g�}��</B></FONT></TD></TR>
<TR><TD ALIGN="center">24����</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�R���Z�pNO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">�k��601</TD></TR>
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
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=13" "alt="ID=13">
<FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">65147</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-18.24%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[��-79pts.-6400�l-6637���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>3563800�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>28700����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1343000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>2871000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��431</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT>(n3@705)</NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>Nonota : </font>540���l�󂯓��ꏀ������</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font>�@<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">43%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">39%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">51%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">10%<IMG SRC="prize0.gif" ALT="1200�^�[���t 1300�^�[���t " WIDTH=16 HEIGHT=16> <IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster23.gif" ALT="[���b���̂�] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] [�V�g�E���G��] " WIDTH=16 HEIGHT=16>1522�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>2</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=6" "alt="ID=6">
<FONT COLOR="#a06040"><B>������_�̓�</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">55351</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-104.68%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{333pts.�{800�l�{30846���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>2641700�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>15600����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>510000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>4897000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��531</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT></NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>Saldia : </font>�܂�����ƁB</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font><IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">6587����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">97%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">8%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">21%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">15%<IMG SRC="bouei.gif" ALT="�h�q�q��" WIDTH=16 HEIGHT="16">21%<IMG SRC="ire.gif" ALT="�C���M�����[" WIDTH=16 HEIGHT="16">90%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster16.gif" ALT="[�l�����J���̂�] [���b�T���W��] [���b���b�h���̂�] [��b���̂�S�[�X�g] [���b�L���O���̂�] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] [���b�͂˂͂�] " WIDTH=16 HEIGHT=16>1616�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>3</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=5" "alt="ID=5">
<FONT COLOR="#a06040"><B>��铇</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">45924</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-124.19%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{98pts.�{3400�l�{6824���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1662900�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>17400����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1054000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>2674000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��393</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT></NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>Rarue : </font>�ԈႦ�����^���D���A���݂܂���c</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font>�@<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">44%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">27%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">63%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">33%<IMG SRC="bouei.gif" ALT="�h�q�q��" WIDTH=16 HEIGHT="16">42%<IMG SRC="ire.gif" ALT="�C���M�����[" WIDTH=16 HEIGHT="16">195%<IMG SRC="prize0.gif" ALT="100�^�[���t 200�^�[���t " WIDTH=16 HEIGHT=16> <IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="monster16.gif" ALT="[���b���̂�] [���b�T���W��] [���b���b�h���̂�] [���b�N�W��] [���b�L���O���̂�] [���b�o�����A] [��b�X���C��] [���b�͂˂͂�] " WIDTH=16 HEIGHT=16>1187�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>4</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=12" "alt="ID=12">
<FONT COLOR="#a06040"><B>���I��</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">45525</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-26.02%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{249pts.�{12200�l�{11855���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1945800�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>12300����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1030000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1407000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>15000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��335</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT>(n3@512)</NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>kumi : </font>�������Ȃ��Ȃ����@�����ڂ�</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><IMG SRC="monster17.gif" ALT="[��b�X���C��] [�V�g�~�J�G��] " WIDTH=16 HEIGHT=16> <font color="hotpink">22�C�o����!!</font>�@<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">45%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">50%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">71%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">74%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster27.gif" ALT="[�l�����J���̂�] [���b���̂�] [���b�T���W��] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [���b�L���O���̂�] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] [���b�N�C�[�����̂�] [�V�g�E���G��] [�V�g�C�Z���A] [�����T�^��] " WIDTH=16 HEIGHT=16>1064�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>5</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=1" "alt="ID=1">
<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">45174</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-91.00%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{3711pts.-11000�l�{3615���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>2033500�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>24000����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1024000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>2860000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��117</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT>(n3@828)�i���o�[�Y�\�z�͊��ʂł�����ׂ��I</NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>�ׂ� : </font>���E���E�E</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><IMG SRC="monster14.gif" ALT="[��b�X���C��] " WIDTH=16 HEIGHT=16> <font color="hotpink">11�C�o����!!</font>�@<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">96%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">72%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">93%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">96%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster16.gif" ALT="[�l�����J���̂�] [���b���̂�] [���b�T���W��] [���b���b�h���̂�] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [���b�L���O���̂�] [���b�o�����A] [��b�X���C��] [���b�͂˂͂�] " WIDTH=16 HEIGHT=16>280�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>6</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23">
<FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">43280</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-60.58%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{107pts.�{1700�l�{7610���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1826500�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>24300����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>110000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>2803000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>20000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��601</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT>(n3@510)</NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>SONG : </font>�N�̒���ł��󂯂�I�@��P���n�j�I</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><IMG SRC="monster14.gif" ALT="[��b�X���C��] " WIDTH=16 HEIGHT=16> <font color="hotpink">25�C�o����!!</font><IMG SRC="niwatori.gif" ALT="�ɂ�Ƃ�" WIDTH=16 HEIGHT="16">2612���H<IMG SRC="buta.gif" ALT="�Ԃ�" WIDTH=16 HEIGHT="16">1369����<IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">3921����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">57%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">45%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">99%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">69%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize4.gif" ALT="���a��" WIDTH=16 HEIGHT=16> <IMG SRC="prize5.gif" ALT="�����a��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster22.gif" ALT="[���b���b�h���̂�] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [���b�L���O���̂�] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] [���b�͂˂͂�] [���b���C�W��] " WIDTH=16 HEIGHT=16>2077�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>7</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=18" "alt="ID=18">
<FONT COLOR="#a06040"><B>����</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">30431</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-55.51%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{5241pts.�{000�l-405���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>980000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>21000����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>618000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>311000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>595000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��41</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT></NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>�����ҁ` : </font>Pet���璆�B�����߂Ȃ��łˁB�@�@��</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font><IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">504����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">75%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">80%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="monster14.gif" ALT="[�l�����J���̂�] [���b���̂�] [���b�T���W��] [���b���b�h���̂�] [���b�_�[�N���̂�] [���b�N�W��] [���b�o�����A] [��b�X���C��] " WIDTH=16 HEIGHT=16>281�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>8</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=2" "alt="ID=2">
<FONT COLOR="#a06040"><B>Sara��RealHell��</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">26153</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-38.16%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{3719pts.�{000�l-200���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>760000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>21000����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9648500�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>120000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>930000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��14</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT></NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>Doramon : </font>�Ȃ񂩍Г�������[�[�[</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font>�@<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">28%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">54%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="monster14.gif" ALT="[���b���̂�] [���b�T���W��] [���b���b�h���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [��b�X���C��] " WIDTH=16 HEIGHT=16>40�C�ގ�</font></font></NOBR></TD>
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
<OPTION VALUE="13" >�q�b�v���L����
<OPTION VALUE="6" >������_�̓�
<OPTION VALUE="5" >��铇
<OPTION VALUE="12" >���I��
<OPTION VALUE="1" >���X�g�}��
<OPTION VALUE="23" >�a�e�c�{����
<OPTION VALUE="18" >����
<OPTION VALUE="2" >Sara��RealHell��

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
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�q�b�v���L����(2, 6)</B></FONT>��<B>�V���n</B>����A<B>2356���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�q�b�v���L����(18, 14)</B></FONT>��<B>�C����c</B>����A<B>3423���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�q�b�v���L����(3, 11)</B></FONT>��<B>�V���n</B>����A<B>2356���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���I��(5, 9)</B></FONT>��<B>�V�g�~�J�G��</B>�������炵���L��ɂ��A�����<B>97000�g��</B>�̐H�����o���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���I��(5, 9)</B></FONT>��<B>�V�g�~�J�G��</B>�����Ƃ����H����<B>2907���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���I��(3, 17)</B></FONT>��<B>�V���n</B>����A<B>1273���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���I��(19, 14)</B></FONT>��<B>�C���݂�</B>����A<B>797���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���I��(14, 11)</B></FONT>��<B>�C����c</B>����A<B>3216���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���I��(7, 6)</B></FONT>��<B>�V���n</B>����A<B>1273���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���I��(17, 11)</B></FONT>��<B>�C����c</B>����A<B>2649���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(17, 14)</B></FONT>��<B>���A�C�L�O�����</B>�̂��y�Y�����񂩂�<B>13���~</B>�̎���������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(2, 16)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(2, 15)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(11, 4)</B></FONT>��<B>�C����c</B>����A<B>3272���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(3, 16)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(3, 15)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(3, 19)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(2, 18)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(3, 17)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(2, 17)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(6, 19)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(5, 19)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(15, 6)</B></FONT>��<B>�C����c</B>����A<B>3260���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(13, 5)</B></FONT>��<B>�C����c</B>����A<B>3214���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�(9, 17)</B></FONT>��<B>�C��T���D�E��</B>������𔭌��I<B>33020���~</B>�̉��l�����邱�Ƃ��킩��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�(15, 15)</B></FONT>��<B>�C���݂�</B>�ŃC�x���g���J�Â���A<B>528000�g��</B>�̐H���������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(0, 5)</B></FONT>��<B>�C����c</B>����A<B>3293���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(4, 13)</B></FONT>��<B>���^���D</B>�́A<B>31600�g��</B>�̐H���𓾂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(16, 15)</B></FONT>��<B>����</B>�������炵���L��ɂ��A�����<B>166000�g��</B>�̐H�����o���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(0, 7)</B></FONT>��<B>�C����c</B>����A<B>3317���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(9, 5)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(9, 6)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(12, 3)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(11, 4)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(3, 7)</B></FONT>��<B>�C����c</B>����A<B>2860���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(18, 15)</B></FONT>��<B>�s�s</B>��<FONT COLOR="#ff0000"><B>�΍�</B></FONT>�ɂ���ł��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(8, 16)</B></FONT>��<B>�s�s</B>��<FONT COLOR="#ff0000"><B>�΍�</B></FONT>�ɂ���ł��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(13, 5)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(12, 5)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(10, 5)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(10, 4)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(10, 6)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(11, 6)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>����(4, 5)</B></FONT>��<B>���DMASTER</B>�́A<B>72300�g��</B>�̐H���𓾂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>����(3, 5)</B></FONT>��<B>���DMASTER</B>�́A<B>69500�g��</B>�̐H���𓾂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�q�b�v���L����(18, 19)</B></FONT>��<FONT COLOR="#d08000"><B>�C���݂㌚��</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�q�b�v���L����(4, 17)</B></FONT>��<FONT COLOR="#d08000"><B>���n</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�q�b�v���L����(11, 14)</B></FONT>��<FONT COLOR="#d08000"><B>���n</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�q�b�v���L����(3, 13)</B></FONT>��<FONT COLOR="#d08000"><B>���n</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�q�b�v���L����(8, 18)</B></FONT>��<FONT COLOR="#d08000"><B>���n</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���I��</B></FONT>��<FONT COLOR="#d08000"><B>�U�v����</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(13, 1)</B></FONT>��<FONT COLOR="#d08000"><B>���D�E�o�q</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�(8, 16)</B></FONT>��<FONT COLOR="#d08000"><B>���D�E�o�q</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(10, 4)</B></FONT>��<FONT COLOR="#d08000"><B>�@��</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>Sara��RealHell��(17, 15)</B></FONT>��<FONT COLOR="#d08000"><B>�@��</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(11, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(10, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(10, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(12, 3)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(10, 6)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(12, 4)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(10, 3)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(10, 3)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(11, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(12, 7)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(9, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(11, 3)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(9, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(10, 6)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(12, 7)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(10, 7)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(10, 3)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(11, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(10, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(12, 3)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(10, 3)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(10, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(10, 3)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(12, 6)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(13, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(12, 4)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(10, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(12, 6)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(10, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(11, 3)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(13, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(10, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(12, 3)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(12, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(9, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(12, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(9, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(9, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(9, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(9, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(11, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(10, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(9, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(9, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(13, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(12, 4)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(12, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<FONT COLOR="#a06040"><B>���X�g�}��(11, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(9, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>����(13, 6)</B></FONT>��<FONT COLOR="#d08000"><B>�H�ꌚ��</B></FONT>���s���܂����B</NOBR><BR>
<H1><FONT COLOR="#4444ff">�����̋L�^</FONT></H1>
<NOBR><FONT COLOR="#800000"><B>�^�[��1339</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�</B></FONT>��<B>�C��T���D�E��</B>������𔭌��I</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1332</B></FONT>�F<FONT COLOR="#a06040"><B>��铇</B></FONT>��<B>�C��T���D�E��</B>������𔭌��I</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1331</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<B>�C��T���D�E��</B>������𔭌��I</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1330</B></FONT>�F<FONT COLOR="#a06040"><B>��1330�^�[�� Numbers4</B></FONT> <B>�F 4879</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1323</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<B>�C��T���D�E��</B>������𔭌��I</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1320</B></FONT>�F<FONT COLOR="#a06040"><B>��1320�^�[�� Numbers3</B></FONT> <B>�F 755</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1320</B></FONT>�F<FONT COLOR="#a06040"><B>��铇</B></FONT>��<B>�C��T���D�E��</B>������𔭌��I</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1318</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>��<B>�C��T���D�E��</B>������𔭌��I</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1316</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT>��<B>�C��T���D�E��</B>������𔭌��I</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��1310</B></FONT>�F<FONT COLOR="#a06040"><B>��1310�^�[�� Numbers4</B></FONT> <B>�F 9474</B></NOBR><BR>
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
