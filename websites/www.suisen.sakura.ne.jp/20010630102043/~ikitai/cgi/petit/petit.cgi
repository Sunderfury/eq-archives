<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<META http-equiv="Content-Script-Type" content="text/javascript">
<META http-equiv="Content-Style-Type" content="text/css">
<title>Roll BBS</title>
<STYLE type="text/css">
<!--
body,tr,td,th { font-size: 10pt }
a { text-decoration:none; }
a:hover { color: #FF0000 }
big  { font-size: 12pt }
small { font-size: 8pt }
input.btn { background-color:#FF3366; color:#FFFFFF; cursor:hand; font-size: 10pt; }
textarea,input.txt { color:#000000; background-color:#FFFBF0; font-size: 10pt; }
select,option { color:#000000; background-color:#FFFBF0; font-size: 10pt; }
UL.mnu { margin-top:0px; font-size: 10pt }
BLOCKQUOTE.howto { margin-left:25px; }
-->
</STYLE>
</head>
<body background="" bgcolor="#E1F0F0" text="#000000" link="#0066FF" vlink="#0066FF" alink="#FF0000">
<SCRIPT language="JavaScript" type="text/javascript">
<!--
var cWin = window; var ie=!!document.all; var n4=!!document.layers; var gk=(navigator.userAgent.match(/Gecko/i)!=null);
function viewForm(bf,name) { var obj; if (ie) { obj = document.all(name).style; } else if (gk) { obj = document.forms[name].style; } if(obj){ if (obj.display == 'block') { obj.display = 'none'; if(name == "newmsg") { bf.value="�V �K �� �e"; } else { bf.value="�� �M"; } } else { obj.display = 'block'; bf.value="���e��������"; } if (document.all) bf.blur(); } }
function rollChange(fm) { if (fm.rollSys.selectedIndex == 1) { fm.rollMin.value = "---"; fm.rollMax.value = "---"; if (ie || gk) { fm.rollMin.disabled = true; fm.rollMax.disabled = true; } } else { fm.rollMin.value = "0"; fm.rollMax.value = "100"; if (document.all || document.getElementById) { fm.rollMin.disabled = false; fm.rollMax.disabled = false; } } }
function inputRandom(myform,rtype,rno,rmin,rmax) { fm = document.forms[myform]; if (fm.comment.value) { fm.comment.value += '\n'; } if (rtype) { fm.comment.value += '/' + rtype + rno; if (rmin != "") { fm.comment.value += ' ' + rmin; } if (rmax != "") { fm.comment.value += ' ' + rmax; } } else { var no = fm.rollNo.options[fm.rollNo.selectedIndex].value; if (fm.rollSys.selectedIndex == 0) { var min = fm.rollMin.value, max = fm.rollMax.value; fm.comment.value += '/random' + no + ' ' + min + ' ' + max; } else { fm.comment.value += '/slot' + no; } } }
function wOpen(myform){ if (document.forms[myform].name.value == '') { alert('���O�����͂���Ă܂���'); return false; } if (document.forms[myform].pwd.value == '') { alert('�p�X���[�h�����͂���Ă܂���'); return false; } cmt = document.forms[myform].comment.value; re1 = new RegExp("[^\\\\\\]\\/slot","i"); re2 = new RegExp("[^\\\\\\]\\/(ran|rand|rando|random)(\\d*) (\\d+) *(\\d*)","i"); if (cmt.search(/^\/slot/i) != -1 || cmt.search(re1) != -1) { rollform = myform; w = 300; h = 200; if (ie) {w = 220; h = 170;} if (gk) {w = 250; h = 180;} l = (screen.availWidth-w) / 2; t = 150; url = "slot.html"; if (cWin == window || cWin.closed) { cWin = window.open(url,"_blank","width="+w+",height="+h+",top="+t+",left="+l); } else { if (cWin.location.href.indexOf(url) == -1) { cWin.location.href = url; } cWin.focus(); } return false; } else if (cmt.match(/^\/(ran|rand|rando|random)(\d*) (\d+) *(\d*)/i) || cmt.match(re2)) { min = eval(RegExp.$3); max = eval(RegExp.$4); if (!max) { max = min; min = 0; } if (max < min) { var temp = min; min = max; max = min; } if (max == min) { alert("�����_���͈̔͂��s���ł��B"); return false; } if (!min && !max) { alert("�����_���͈̔͂��s���ł��B"); return false; } rollform = myform; w = 200; h = 150; l = (screen.availWidth-w) / 2; t = 150; url = "dice.html "; if (cWin == window || cWin.closed) { cWin = window.open(url,"_blank","width="+w+",height="+h+",top="+t+",left="+l); } else { if (cWin.location.href.indexOf(url) == -1) { cWin.location.href = url; } cWin.focus(); } return false; } else { return true; } }
// -->
</SCRIPT>
<A name="top"></A><TABLE width="100%" border=0 cellspacing=0 cellpadding=0><TR><TD nowrap>
<b><font color=#008080 style="font-size:16pt" face="�l�r �o�S�V�b�N">Roll BBS</font></b>
</TD><TD align="right" nowrap>
[<a href="http://www.suisen.sakura.ne.jp/~ikitai/cgi/rollbbs.html" target='_top'>�g�b�v�ɖ߂�</a>]
[<a href="./petit.cgi?mode=howto">�g����</a>]
[<a href="./petit.cgi?mode=find">���[�h����</a>]
[<a href="./petit.cgi?mode=admin">�Ǘ��p</a>]
</TD></TR></TABLE>
<HR>
<UL class=mnu>
<LI>ROLL�ɂ�<B>DICE</B>��<B>SLOT</B>�̂Q��ނ�����R�����g����Roll�R�}���h����͂��邱�Ƃɂ����Roll���鎖���o���܂��B
<LI>ROLL�R�}���h�̓R�����g�L�����̏㕔�ɂ���t�H�[����ݒ肵�}���{�^����������<B>�R�����g�̍Ō�</B>�ɃR�}���h��<B>�}��</B>����܂��B<BR>(�������񐔂����}�������̂ŉ��������ɒ��ӁB�R�}���h�̑}�������ł��̂œ��e����܂�Roll�͍s���܂���B)
<LI>�P������Dice�͉���ł�Slot�͂P��̂ݗL���ł��B��������Window�ł�Roll�͍ŏ��̂P�݂̂�Dice��Slot�����݂��Ă�ꍇ��Slot���D�悳��܂��B
<LI>�E��̃����N�u�g�����v�ɂ�ROLL�̐���������܂��B
</UL>
<blockquote>
<NOSCRIPT><H1 align=center>����BBS��JavaScript��ON�ł����p������</H1></NOSCRIPT>
<FORM method="POST" action="./petit.cgi">
 <INPUT type="submit" class="btn" value="�� �� ��"></FORM>
<form name="newmsg" method="POST" action="./petit.cgi" onsubmit="return wOpen('newmsg')">
<input type=hidden name=mode value="regist">
<input type=hidden name=roll value="">
<input type=hidden name="slot0" value="">
<input type=hidden name="slot1" value="">
<input type=hidden name="slot2" value="">
<table border=0 cellspacing=0>
<tr>
<td nowrap><b>���Ȃ܂�</b></td>
<td><input type=text name=name size="20" value="" class="txt"></td>
</tr>
<tr>
<td nowrap><b>�d���[��</b></td>
<td><input type=text name=email size="20" value="" class="txt"></td>
</tr>
<tr>
<td nowrap><b>��@�@��</b></td>
<td nowrap>
<input type=text name=sub size="25" class="txt">
�@  <input type=submit value="���e����" class="btn"> <input type=reset value="���Z�b�g" class="btn"></td>
</tr>
<tr>
<td nowrap><b>ROLL</b></td>
<td nowrap><select name="rollSys" onChange="rollChange(this.form)">
<option value="1">DICE
<option value="2">SLOT
</select>
No<select name="rollNo">
<option value="">--
<option value=1>01
<option value=2>02
<option value=3>03
<option value=4>04
<option value=5>05
<option value=6>06
<option value=7>07
<option value=8>08
<option value=9>09
<option value=10>10
<option value=11>11
<option value=12>12
<option value=13>13
<option value=14>14
<option value=15>15
<option value=16>16
<option value=17>17
<option value=18>18
<option value=19>19
<option value=20>20
</select>
Min<input type="text" name="rollMin" size=4 class="txt" value="0">
Max<input type="text" name="rollMax" size=4 class="txt" value="100">
<input type=button value="�R�}���h�}��" onClick="inputRandom('newmsg')" class="btn">
</td>
</tr>
<tr>
<td colspan=2><b>�R�����g</b><br>
<textarea cols="56" rows=7 name=comment wrap="off"></textarea>
</td>
</tr>
<tr>
<td nowrap><b>�t�q�k</b></td>
<td><input type=text size="50" name=url value="http://" class="txt"></td>
</tr>
<tr><td nowrap><b>PASS</b></td>
<td><input type=password name=pwd size=8 maxlength=8 value="" class="txt">
<small>(�����̋L�����폜���Ɏg�p�B�p������8�����ȓ�)</small></td></tr>
<tr><td nowrap><b>�����F</b></td><td>
<input type=radio name=color value="800000" checked><font color="800000">��</font>
<input type=radio name=color value="FF0000"><font color="FF0000">��</font>
<input type=radio name=color value="008000"><font color="008000">��</font>
<input type=radio name=color value="0000FF"><font color="0000FF">��</font>
<input type=radio name=color value="800080"><font color="800080">��</font>
<input type=radio name=color value="FF69B4"><font color="FF69B4">��</font>
<input type=radio name=color value="FF8C00"><font color="FF8C00">��</font>
<input type=radio name=color value="000080"><font color="000080">��</font>
<input type=radio name=color value="808000"><font color="808000">��</font>
<input type=radio name=color value="FF00FF"><font color="FF00FF">��</font>
<input type=radio name=color value="000000"><font color="000000">��</font>
</td></tr></table></form>
</blockquote>
<center><A name="0"></A><TABLE WIDTH=95% BORDER=1 CELLPADDING=3 CELLSPACING=0 bgcolor=#FFFFFF>
<TR align=center bgcolor=#FFFBF0><TH nowrap width=1%><B>NO</B></TH><TH nowrap width=5%>���񓊍e��</TH><TH nowrap width=5%>�ŏI���e��</TH><TH nowrap width=5%>�ŏI���e����</TH><TH width=84%>�^ �C �g ��</TH></TR><TR><TD nowrap><A href="#1" style="color:black">[1]</A></TD><TD nowrap><A href="#1" style="color:black">Hisa</A></TD><TD nowrap><A href="#1" style="color:black">----</A></TD><TD nowrap><A href="#1" style="color:black">2001/04/29 22:50</A></TD><TD><A href="#1" style="color:black">TEST</A></TD></TR></TABLE>
<TABLE border=0 width=95%><TR><TD><SMALL><FONT color="#FF3366"><B>NEW</B></FONT> : �Ԃ͐e�L�����A�͎q�L���݂̂�24���Ԉȓ��ɓ��e���ꂽ�ꍇ�ł��B</SMALL></TD><TD align=right>
<table cellpadding=0 cellspacing=0><tr>
</tr></table></TD></TR></TABLE></center><BR>
<center>

<!------------------------------------ ---------------------------------------------->
<A name="1"></A><TABLE BORDER=1 WIDTH='95%' BGCOLOR="#FFFFFF" CELLSPACING=1 CELLPADDING=5><TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
<BIG><b>[1]�@<font color="#006400">TEST</font></b> ���e�ҁF<b><a href="mailto:ito@e-mail.ne.jp">Hisa</a></b> ���e���F2001/04/29(Sun) 22:50 &nbsp;  </BIG></TD>
<TD align="right" nowrap><BIG><A href="#0" title="�O" style="color:black">��</A> <A href="#2" title="��" style="color:black">��</A>
 <A href="#top" title="�ŏ�" style="color:black">��</A> <A href="#btm" title="�Ō�" style="color:black">��</A></BIG></TD></TR></TABLE></TD></TR>
<TR><TD valign=top><BR><blockquote><font color="008040">TEST</font><BR></blockquote>
<form name="res_1" method="POST" action="./petit.cgi" onsubmit="return wOpen('res_1')">
<input type=hidden name=mode value=regist>
<input type=hidden name=reno value="1">
<input type=hidden name=email value="">
<input type=hidden name=roll value="">
<input type=hidden name="slot0" value="">
<input type=hidden name="slot1" value="">
<input type=hidden name="slot2" value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0>
<TR><TD nowrap align="right">NAME <input type=text name=name size=10 value="" class="txt"><BR>
COLOR <select name=color>
<option value="800000" selected style="color:#800000;">Maroon
<option value="FF0000" style="color:#FF0000;">Red
<option value="008000" style="color:#008000;">Green
<option value="0000FF" style="color:#0000FF;">Blue
<option value="800080" style="color:#800080;">Purple
<option value="FF69B4" style="color:#FF69B4;">Pink
<option value="FF8C00" style="color:#FF8C00;">Orange
<option value="000080" style="color:#000080;">Navy
<option value="808000" style="color:#808000;">Olive
<option value="FF00FF" style="color:#FF00FF;">Fuchsia
<option value="000000" style="color:#000000;">Black
</SELECT></TD>
<td><select name="rollSys" onChange="rollChange(this.form)">
<option value="1">DICE
<option value="2">SLOT
</select>
No<select name="rollNo">
<option value="">--
<option value=1>01
<option value=2>02
<option value=3>03
<option value=4>04
<option value=5>05
<option value=6>06
<option value=7>07
<option value=8>08
<option value=9>09
<option value=10>10
<option value=11>11
<option value=12>12
<option value=13>13
<option value=14>14
<option value=15>15
<option value=16>16
<option value=17>17
<option value=18>18
<option value=19>19
<option value=20>20
</select>
Min<input type=text name=rollMin size=4 class="txt" value="0">
Max<input type=text name=rollMax size=4 class="txt" value="100">
<input type=button value="�R�}���h�}��" onClick="inputRandom('res_1')" class="btn"><BR>
<textarea name=comment cols=56 rows=3 wrap="off"></textarea></TD>
<TD><input type=password name=pwd size=4 value="" class="txt"> PASS<BR>
<input type=submit value='�ԁ@�@�M' class="btn"></TD></TR></TABLE></CENTER></form>
</TD>
</TR></TABLE><BR>
<blockquote><table align=left cellpadding=0 cellspacing=0><tr>
</tr></table>
<table align=right><tr>
<td nowrap align=center><form action="./petit.cgi" method="POST">
<font color="#006400">�y�L���폜�ERoll No�C���t�H�[���z</font><br>
<input type=radio name=mode value="usr_del" checked>�폜
<input type=radio name=mode value="usr_ran">�C��
�@�L��No<input type=text name=no size=3>
PASS<input type=password name=pwd size=4 maxlength=8 value="">
<input type=submit value="���M">
</form></td>
</tr></table></blockquote><br clear=all><A name="btm"></A>
<!-- ���� --><P><!-- PETIT BOARD v5.22 -->
- <a href='http://www.kent-web.com/' target='_top'>PetitBoard</a> -<BR>
Script arranged by <a href="http://www.suisen.sakura.ne.jp/~ikitai/cgi/rollbbs.html" target="_blank"><B>Hisa</B></a>
</center>
</body></html>
