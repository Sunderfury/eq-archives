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
<B>�^�[��<FONT COLOR="royalblue">2473</FONT>�܂�&nbsp;<IMG name="_min1"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/1.gif" align="middle"><IMG name="_min0"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/6.gif" align="middle">&nbsp;��&nbsp;<IMG name="_sec1"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/0.gif" align="middle"><IMG name="_sec0"  src="http://www.geocities.co.jp/Playtown-King/3466/hakora/9.gif" align="middle">&nbsp;�b&nbsp;&nbsp;(6/2 08:50)</B>
<P>
<SCRIPT language="JavaScript">
<!--
// �c�莞��
var day  = 0;
var hour = 0;
var min  = 16;
var sec  = 9;

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
<H1><FONT COLOR="#4444ff">�^�[��2472</FONT></H1>
<FORM name="RemainForm"><INPUT name="RemainTime" size="30" type="text" readonly></FORM><SCRIPT language="JavaScript">
<!--
nextTurn = 969; loadDate = new Date();
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
<OPTION VALUE="23" >�a�e�c�{����
<OPTION VALUE="1" >���X�g�}��
<OPTION VALUE="6" >������_�̓�
<OPTION VALUE="5" >��铇
<OPTION VALUE="12" >���I��
<OPTION VALUE="18" >����
<OPTION VALUE="2" >��_������

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
<TR><TD ALIGN="center">9075500�l</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�_��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=13" "alt="ID=13"><FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT></TD></TR>
<TR><TD ALIGN="center">3660000�l�K��</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�E��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">10220000�l�K��</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�̌@��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=18" "alt="ID=18"><FONT COLOR="#a06040"><B>����</B></FONT></TD></TR>
<TR><TD ALIGN="center">625000�l�K��</TD></TR>
</TABLE><td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�X��NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=5" "alt="ID=5"><FONT COLOR="#a06040"><B>��铇</B></FONT></TD></TR>
<TR><TD ALIGN="center">275300�{</TD></TR>
</TABLE>
</TABLE>
<br>
<TABLE ALIGN="center" width="100%">
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�ɂ�Ƃ萔NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">8000���H</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�Ԃ���NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">9585����</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>������NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">11913����</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>���b�o����NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=18" "alt="ID=18"><FONT COLOR="#a06040"><B>����</B></FONT></TD></TR>
<TR><TD ALIGN="center">74�C</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>���b�ގ���NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">4044�C</TD></TR>
</TABLE>
</TABLE>
<br>
<TABLE ALIGN="center" width="100%">
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�����xNO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=5" "alt="ID=5"><FONT COLOR="#a06040"><B>��铇</B></FONT></TD></TR>
<TR><TD ALIGN="center">�O�^�[���{2685pts.</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�l������NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">�O�^�[���{8900�l</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>����NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=5" "alt="ID=5"><FONT COLOR="#a06040"><B>��铇</B></FONT></TD></TR>
<TR><TD ALIGN="center">�O�^�[���{21646���~</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�L�O�萔NO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=5" "alt="ID=5"><FONT COLOR="#a06040"><B>��铇</B></FONT></TD></TR>
<TR><TD ALIGN="center">18����</TD></TR>
</TABLE>
<td width="9%"><TABLE BORDER=1 width="100%">
<TR><TD BGCOLOR="lightsteelblue" ALIGN="center" COLSPAN="2">
<FONT COLOR="#ffffff"><B>�R���Z�pNO.1</B></FONT></TD></TR>
<TR><TD ALIGN="center"><A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23"><FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT></TD></TR>
<TR><TD ALIGN="center">�k��745</TD></TR>
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
<NOBR>Points:<font color="royalblue">130894</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-20.19%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[��-316pts.�{600�l-34874���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9075500�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>33500����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>3660000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>7248000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��372</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT>(n3@705)</NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT>(toto@13.23.1.6.5.00.00.00)</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>Nonota : </font>�j�A1�疜�s�s�I�I</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font><IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">11286����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">31%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">65%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">77%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">73%<IMG SRC="prize0.gif" ALT="1200�^�[���t 1300�^�[���t 1400�^�[���t 1500�^�[���t 1600�^�[���t 1700�^�[���t 1800�^�[���t 1900�^�[���t 2000�^�[���t 2100�^�[���t 2200�^�[���t 2222�^�[���t 2300�^�[���t 2400�^�[���t " WIDTH=16 HEIGHT=16> <IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize4.gif" ALT="���a��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster23.gif" ALT="[���b���̂�] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [���b�L���O���̂�] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] [�V�g�E���G��] " WIDTH=16 HEIGHT=16>2646�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>2</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=23" "alt="ID=23">
<FONT COLOR="#a06040"><B>�a�e�c�{����</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">112828</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-53.58%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{2466pts.�{8900�l-13589���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>7251400�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>31300����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>917000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>10220000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��745</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT>(n3@510)</NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>SONG : </font>�N�̒���ł��󂯂�I�@��P���n�j�I</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font><IMG SRC="niwatori.gif" ALT="�ɂ�Ƃ�" WIDTH=16 HEIGHT="16">8000���H<IMG SRC="buta.gif" ALT="�Ԃ�" WIDTH=16 HEIGHT="16">9585����<IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">11913����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">11%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">49%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">60%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">15%<IMG SRC="bouei.gif" ALT="�h�q�q��" WIDTH=16 HEIGHT="16">96%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize4.gif" ALT="���a��" WIDTH=16 HEIGHT=16> <IMG SRC="prize5.gif" ALT="�����a��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster26.gif" ALT="[���b���b�h���̂�] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [���b�L���O���̂�] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] [���b�͂˂͂�] [���b���C�W��] [�V�g�E���G��] [���p�t�A�[����] [�V�g�C�Z���A] " WIDTH=16 HEIGHT=16>4044�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>3</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=1" "alt="ID=1">
<FONT COLOR="#a06040"><B>���X�g�}��</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">100688</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-49.92%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[��-2pts.�{000�l�{2565���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>6363900�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>27600����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>3420000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>6121000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��347</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT>(n3@828)�i���o�[�Y�\�z�͊��ʂł�����ׂ��I</NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>�ׂ� : </font>���킠����������������A�n�k�Ŕ��󂵂�(�G�L�t���j</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><IMG SRC="monster14.gif" ALT="[��b�X���C��] " WIDTH=16 HEIGHT=16> <font color="hotpink">20�C�o����!!</font><IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">1908����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">32%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">75%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">20%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">80%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster23.gif" ALT="[�l�����J���̂�] [���b���̂�] [���b�T���W��] [���b���b�h���̂�] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [���b�L���O���̂�] [���b�o�����A] [��b�X���C��] [���b�͂˂͂�] [�X���C�����W�F���h] [���b�N�C�[�����̂�] [�V�g�E���G��] " WIDTH=16 HEIGHT=16>825�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>4</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=6" "alt="ID=6">
<FONT COLOR="#a06040"><B>������_�̓�</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">91674</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-14.65%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{130pts.�{3700�l�{4931���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>5539500�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>21900����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1685000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>4666000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��578</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT></NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>Saldia : </font>�܂�����ƁB</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font><IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">9555����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">10%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">69%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">18%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">23%<IMG SRC="bouei.gif" ALT="�h�q�q��" WIDTH=16 HEIGHT="16">20%<IMG SRC="ire.gif" ALT="�C���M�����[" WIDTH=16 HEIGHT="16">210%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster16.gif" ALT="[�l�����J���̂�] [���b�T���W��] [���b���b�h���̂�] [��b���̂�S�[�X�g] [���b�L���O���̂�] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] [���b�͂˂͂�] " WIDTH=16 HEIGHT=16>2442�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>5</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=5" "alt="ID=5">
<FONT COLOR="#a06040"><B>��铇</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">79998</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-35.17%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{2685pts.�{1000�l�{21646���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>4217800�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>11100����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1384000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>4317000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�ۗL����</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��371</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT></NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>Rarue : </font>������葁�����̍ЊQ�������Ƃ��ɁI�@�̂���Ă�D</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font><IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">1439����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">66%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">39%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">77%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">77%<IMG SRC="bouei.gif" ALT="�h�q�q��" WIDTH=16 HEIGHT="16">73%<IMG SRC="prize0.gif" ALT="100�^�[���t 200�^�[���t " WIDTH=16 HEIGHT=16> <IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster16.gif" ALT="[���b���̂�] [���b�T���W��] [���b���b�h���̂�] [���b�N�W��] [���b�L���O���̂�] [���b�o�����A] [��b�X���C��] [���b�͂˂͂�] " WIDTH=16 HEIGHT=16>1187�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>6</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=12" "alt="ID=12">
<FONT COLOR="#a06040"><B>���I��</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">68033</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-19.45%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{20pts.�{2100�l�{5469���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>3645000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>13500����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1929000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>2415000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>10000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��437</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT>(n3@512)</NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT>�F(toto@13.23.6.5.12.00.00.00)</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>kumi : </font>�܂��@�ǐ^�񒆂Ɂ@TT</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font><IMG SRC="niwatori.gif" ALT="�ɂ�Ƃ�" WIDTH=16 HEIGHT="16">4000���H<IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">2786����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">87%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">89%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">85%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">87%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster27.gif" ALT="[�l�����J���̂�] [���b���̂�] [���b�T���W��] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [���b�L���O���̂�] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] [���b�N�C�[�����̂�] [�V�g�E���G��] [�V�g�C�Z���A] [�����T�^��] " WIDTH=16 HEIGHT=16>2038�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>7</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=18" "alt="ID=18">
<FONT COLOR="#a06040"><B>����</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">37647</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-69.61%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{90pts.�{1600�l�{3608���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1212800�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>26600����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>946000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>486000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>625000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��266</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT></NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>�����ҁ` : </font>�X���C���\����!!�@&gt; &lt; /</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><IMG SRC="monster14.gif" ALT="[��b�X���C��] " WIDTH=16 HEIGHT=16> <font color="hotpink">74�C�o����!!</font><IMG SRC="ushi.gif" ALT="����" WIDTH=16 HEIGHT="16">4658����<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">72%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">60%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">71%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">29%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize9.gif" ALT="���ɍГ��" WIDTH=16 HEIGHT=16> <IMG SRC="monster14.gif" ALT="[�l�����J���̂�] [���b���̂�] [���b�T���W��] [���b���b�h���̂�] [���b�_�[�N���̂�] [���b�N�W��] [�d�b�߂��͂�] [���b�o�����A] [��b�X���C��] " WIDTH=16 HEIGHT=16>1096�C�ގ�</font></font></NOBR></TD>
</TR>

<TR>
<TD BGCOLOR="#ccffcc" ROWSPAN=4 align=center nowrap=nowrap><NOBR><FONT COLOR="#800000"><B>8</B></FONT></NOBR></TD>
<TD BGCOLOR="#ccffff" ROWSPAN=4 align=left nowrap=nowrap>
<center><NOBR>
<A STYlE="text-decoration:none" HREF="http://www22.big.or.jp/~eyes/cgi-bin/hako/hako-main.cgi?Sight=2" "alt="ID=2">
<FONT COLOR="#a06040"><B>��_������</B></FONT>
</A><br>
<NOBR>Points:<font color="royalblue">31092</font>pts.</NOBR><br>
<NOBR>���Ɨ�:(<font color="royalblue">-111.70%</font>)</NOBR><br>
<NOBR><font color="hotpink" font size="-1">(�O�^�[���{19pts.�{000�l�{284���~)</font></NOBR></center>
</TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>923000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>32100����</NOBR></TD>

<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>9999900�g��</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>1340000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>364000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>250000�l</NOBR></TD>
<TD BGCOLOR="#ccffff" align=right nowrap=nowrap><NOBR>�k��140</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�P�F</B></FONT></NOBR></TD>
<TD BGCOLOR="WHITE" COLSPAN=4 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>�\�z�Q�F</B></FONT></NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="WHITE" COLSPAN=8 align=left nowrap=nowrap><NOBR><font color=#0000ff>Doramon : </font>�ǂ��܂ōr���΋C���ςނ̂��E�E�E�E</NOBR></TD>
</TR>
<TR>
<TD BGCOLOR="#ccffcc" COLSPAN=8 align=left nowrap=nowrap><NOBR><FONT COLOR="royalblue"><B>info�F<font size="-1"><font color="hotpink"></font>�@<IMG SRC="kisho.gif" ALT="�C�ۉq��" WIDTH=16 HEIGHT="16">13%<IMG SRC="kansoku.gif" ALT="�ϑ��q��" WIDTH=16 HEIGHT="16">15%<IMG SRC="geigeki.gif" ALT="�}���q��" WIDTH=16 HEIGHT="16">31%<IMG SRC="gunji.gif" ALT="�R���q��" WIDTH=16 HEIGHT="16">95%<IMG SRC="bouei.gif" ALT="�h�q�q��" WIDTH=16 HEIGHT="16">53%<IMG SRC="prize1.gif" ALT="�ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize2.gif" ALT="���ɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize3.gif" ALT="���ɔɉh��" WIDTH=16 HEIGHT=16> <IMG SRC="prize7.gif" ALT="�Г��" WIDTH=16 HEIGHT=16> <IMG SRC="prize8.gif" ALT="���Г��" WIDTH=16 HEIGHT=16> <IMG SRC="monster19.gif" ALT="[���b���̂�] [���b�T���W��] [���b���b�h���̂�] [���b�_�[�N���̂�] [��b���̂�S�[�X�g] [���b�N�W��] [��b�X���C��] [�X���C�����W�F���h] " WIDTH=16 HEIGHT=16>604�C�ގ�</font></font></NOBR></TD>
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
<OPTION VALUE="23" >�a�e�c�{����
<OPTION VALUE="1" >���X�g�}��
<OPTION VALUE="6" >������_�̓�
<OPTION VALUE="5" >��铇
<OPTION VALUE="12" >���I��
<OPTION VALUE="18" >����
<OPTION VALUE="2" >��_������

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
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>���I��(1, 15)</B></FONT>��<B>���A�C�L�O�����</B>�̂��y�Y�����񂩂�<B>42���~</B>�̎���������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>���I��(12, 13)</B></FONT>��<B>�V���n</B>����A<B>2402���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>���I��(19, 14)</B></FONT>��<B>�C���݂�</B>����A<B>1591���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(16, 7)</B></FONT>��<B>�V���n</B>����A<B>798���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(0, 6)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(1, 6)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(0, 4)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(0, 3)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(15, 4)</B></FONT>��<B>�C���݂�</B>����A<B>690���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(5, 15)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(4, 14)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(2, 7)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(2, 8)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(1, 3)</B></FONT>��<B>�r�n</B>��<B>��b�X���C��</B>�ɓ��ݍr�炳��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����(2, 3)</B></FONT>��<B>�X���C��</B>�����􂵂܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��_������(11, 19)</B></FONT>��<B>�C����c</B>����A<B>3346���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�(4, 9)</B></FONT>��<B>�V���n</B>�ŃC�x���g���J�Â���A<B>1107000�g��</B>�̐H���������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�(4, 9)</B></FONT>��<B>�V���n</B>����A<B>3653���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(18, 10)</B></FONT>��<B>�C���݂�</B>�ŃC�x���g���J�Â���A<B>1448000�g��</B>�̐H���������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(7, 15)</B></FONT>��<B>�C���݂�</B>�ŃC�x���g���J�Â���A<B>1448000�g��</B>�̐H���������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(11, 5)</B></FONT>��<B>�C���݂�</B>�ŃC�x���g���J�Â���A<B>1448000�g��</B>�̐H���������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(3, 5)</B></FONT>��<B>�C����c</B>����A<B>3370���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(0, 10)</B></FONT>��<B>�C����c</B>����A<B>3415���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(3, 17)</B></FONT>��<B>�V���n</B>����A<B>3540���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(5, 11)</B></FONT>��<B>�C����c</B>����A<B>3380���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(19, 18)</B></FONT>��<B>�C���݂�</B>�ŃC�x���g���J�Â���A<B>843000�g��</B>�̐H���������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(5, 7)</B></FONT>��<B>�C��T���D�E��</B>�̎��̂ɂ��A<B>165���~</B>�̕ی�������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(5, 7)</B></FONT>��<B>�C��T���D�E��</B>�͎��̂��ߒ��v���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(2, 18)</B></FONT>��<B>�V���n</B>����A<B>3287���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(2, 16)</B></FONT>��<B>�V���n</B>����A<B>3287���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(2, 17)</B></FONT>��<B>�V���n</B>����A<B>3540���~</B>�̎��v���オ��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(4, 10)</B></FONT>��<B>�C��T���D�E��</B>�̎��̂ɂ��A<B>35���~</B>�̕ی�������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(4, 10)</B></FONT>��<B>�C��T���D�E��</B>�͎��̂��ߒ��v���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>���I��</B></FONT>��<FONT COLOR="#d08000"><B>�U�v����</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(3, 7)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(2, 6)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(2, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(1, 3)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(2, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(0, 6)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(2, 6)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(1, 7)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(3, 7)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(2, 6)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(0, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(2, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(0, 4)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(2, 6)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(3, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(0, 4)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 3)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(3, 7)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(0, 4)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(4, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(1, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(3, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(3, 7)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(3, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(1, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(0, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(0, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(3, 3)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(2, 7)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(4, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(2, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(3, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(1, 4)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(3, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(2, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(2, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(3, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(4, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(2, 3)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(0, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(0, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(0, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(2, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(4, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 3)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(3, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 3)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(2, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(2, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(0, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(2, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(3, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(3, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(4, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(3, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(1, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(0, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(2, 6)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 7)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(0, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(4, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���܂������A<FONT COLOR="#a06040"><B>(2, 5)</B></FONT>��<B>�r�n</B>�ɗ����܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(3, 3)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<B>��b�X���C��</B>�̎c�[�ɂ́A<B>100���~</B>�̒l���t���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(2, 5)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͗͐s���A�|��܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(0, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>����</B></FONT>��<FONT COLOR="#a06040"><B>����(2, 5)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�~�T�C������</B></FONT>���s���A<FONT COLOR="#a06040"><B>(1, 4)</B></FONT>��<B>��b�X���C��</B>�ɖ����B<B>��b�X���C��</B>�͋ꂵ�����ə��K���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>���X�g�}��(12, 8)</B></FONT>��<FONT COLOR="#d08000"><B>���ߗ���</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>�q�b�v���L����</B></FONT>��<FONT COLOR="#a06040"><B>�q�b�v���L����(2, 9)</B></FONT>�n�_�Ɍ�����<FONT COLOR="#d08000"><B>�q�����[�U�[����</B></FONT>���s���A<B>���b���C�W��</B>�ɖ����A<B>���b���C�W��</B>�͏Ă������܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��_������(16, 4)</B></FONT>��<FONT COLOR="#d08000"><B>�H������������</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�(16, 18)</B></FONT>��<FONT COLOR="#d08000"><B>�j���[�^�E������</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>������_�̓�(16, 18)</B></FONT>��<FONT COLOR="#d08000"><B>���n</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>�a�e�c�{����(15, 8)</B></FONT>��<FONT COLOR="#d08000"><B>�C���݂㌚��</B></FONT>���s���܂����B</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2472</B></FONT>�F<FONT COLOR="#a06040"><B>��铇(3, 17)</B></FONT>��<FONT COLOR="#d08000"><B>�V���n����</B></FONT>���s���܂����B</NOBR><BR>
<H1><FONT COLOR="#4444ff">�����̋L�^</FONT></H1>
<NOBR><FONT COLOR="#800000"><B>�^�[��2470</B></FONT>�F<FONT COLOR="#a06040"><B>��2470�^�[�� Numbers4</B></FONT> <B>�F 8411</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2460</B></FONT>�F<FONT COLOR="#a06040"><B>��2460�^�[�� Numbers3</B></FONT> <B>�F 334</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2450</B></FONT>�F<FONT COLOR="#a06040"><B>��2450�^�[�� Numbers4</B></FONT> <B>�F 5796</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2440</B></FONT>�F<FONT COLOR="#a06040"><B>��2440�^�[�� Numbers3</B></FONT> <B>�F 231</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2430</B></FONT>�F<FONT COLOR="#a06040"><B>��2430�^�[�� Numbers4</B></FONT> <B>�F 5752</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2426</B></FONT>�F<FONT COLOR="#a06040"><B>��铇</B></FONT>��<B>�C��T���D�E��</B>������𔭌��I</NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2420</B></FONT>�F<FONT COLOR="#a06040"><B>��2420�^�[�� Numbers3</B></FONT> <B>�F 16</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2410</B></FONT>�F<FONT COLOR="#a06040"><B>��2410�^�[�� Numbers4</B></FONT> <B>�F 2976</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2400</B></FONT>�F<FONT COLOR="#a06040"><B>��2400�^�[�� Numbers3</B></FONT> <B>�F 224</B></NOBR><BR>
<NOBR><FONT COLOR="#800000"><B>�^�[��2400</B></FONT>�F<FONT COLOR="#a06040"><B>��2400�^�[�� ��������</B></FONT> 8�_�I�����z���� 60000���~</NOBR><BR>
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
