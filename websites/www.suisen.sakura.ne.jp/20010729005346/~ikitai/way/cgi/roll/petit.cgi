<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<META http-equiv="Content-Script-Type" content="text/javascript">
<META http-equiv="Content-Style-Type" content="text/css">
<title>Way Station Roll BBS</title>
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
<b><font color=#008080 style="font-size:16pt" face="�l�r �o�S�V�b�N">Way Station Roll BBS</font></b>
</TD><TD align="right" nowrap>
[<a href="http://www.suisen.sakura.ne.jp/~ikitai/way/" target='_top'>�g�b�v�ɖ߂�</a>]
[<a href="./petit.cgi?mode=howto">�g����</a>]
[<a href="./petit.cgi?mode=find">���[�h����</a>]
[<a href="./petit.cgi?mode=past">�ߋ����O</a>]
[<a href="./petit.cgi?mode=admin">�Ǘ��p</a>]
</TD></TR></TABLE>
<HR>
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
<TR align=center bgcolor=#FFFBF0><TH nowrap width=1%><B>NO</B></TH><TH nowrap width=5%>���񓊍e��</TH><TH nowrap width=5%>�ŏI���e��</TH><TH nowrap width=5%>�ŏI���e����</TH><TH width=84%>�^ �C �g ��</TH></TR><TR><TD nowrap><A href="#1" style="color:black">[933]</A></TD><TD nowrap><A href="#1" style="color:black">Shizuho</A></TD><TD nowrap><A href="#1" style="color:black">Shizuho</A></TD><TD nowrap><A href="#1" style="color:black">2001/07/28 14:00</A></TD><TD><A href="#1" style="color:black">7/22 DNP�@<FONT color="#0066FF"><B><SMALL>NEW</SMALL></B></FONT></A></TD></TR>
<TR><TD nowrap><A href="#2" style="color:black">[920]</A></TD><TD nowrap><A href="#2" style="color:black">Deid</A></TD><TD nowrap><A href="#2" style="color:black">Shizuho</A></TD><TD nowrap><A href="#2" style="color:black">2001/07/28 13:58</A></TD><TD><A href="#2" style="color:black">7/20-21�@Sebi �L�m�R�̉��l�@<FONT color="#0066FF"><B><SMALL>NEW</SMALL></B></FONT></A></TD></TR>
<TR><TD nowrap><A href="#3" style="color:black">[915]</A></TD><TD nowrap><A href="#3" style="color:black">Shizuho</A></TD><TD nowrap><A href="#3" style="color:black">Adien@Mirage</A></TD><TD nowrap><A href="#3" style="color:black">2001/07/27 22:06</A></TD><TD><A href="#3" style="color:black">7/20Chardok King&Queen</A></TD></TR>
<TR><TD nowrap><A href="#4" style="color:black">[894]</A></TD><TD nowrap><A href="#4" style="color:black">Bokuden</A></TD><TD nowrap><A href="#4" style="color:black">Shizuho</A></TD><TD nowrap><A href="#4" style="color:black">2001/07/20 14:20</A></TD><TD><A href="#4" style="color:black">7/12����Severilous Roll</A></TD></TR>
<TR><TD nowrap><A href="#5" style="color:black">[878]</A></TD><TD nowrap><A href="#5" style="color:black">Infey</A></TD><TD nowrap><A href="#5" style="color:black">Infey</A></TD><TD nowrap><A href="#5" style="color:black">2001/07/16 13:24</A></TD><TD><A href="#5" style="color:black">7/9Keal�iPA�����ł��グ�j��</A></TD></TR>
<TR><TD nowrap><A href="#6" style="color:black">[858]</A></TD><TD nowrap><A href="#6" style="color:black">Gafus</A></TD><TD nowrap><A href="#6" style="color:black">Gafus</A></TD><TD nowrap><A href="#6" style="color:black">2001/07/14 15:53</A></TD><TD><A href="#6" style="color:black">6/24 in PoS</A></TD></TR>
<TR><TD nowrap><A href="#7" style="color:black">[874]</A></TD><TD nowrap><A href="#7" style="color:black">Lilit</A></TD><TD nowrap><A href="#7" style="color:black">Infey</A></TD><TD nowrap><A href="#7" style="color:black">2001/07/13 20:28</A></TD><TD><A href="#7" style="color:black">Xneko�����Help��Hole�s�������i7/8�j</A></TD></TR>
<TR><TD nowrap><A href="#8" style="color:black">[745]</A></TD><TD nowrap><A href="#8" style="color:black">Sleip</A></TD><TD nowrap><A href="#8" style="color:black">Bokuden</A></TD><TD nowrap><A href="#8" style="color:black">2001/07/10 22:11</A></TD><TD><A href="#8" style="color:black">28-29</A></TD></TR>
<TR><TD nowrap><A href="#9" style="color:black">[679]</A></TD><TD nowrap><A href="#9" style="color:black">Shizuho</A></TD><TD nowrap><A href="#9" style="color:black">Gafus_CLR</A></TD><TD nowrap><A href="#9" style="color:black">2001/07/10 02:39</A></TD><TD><A href="#9" style="color:black">Siren�ɂ�</A></TD></TR>
<TR><TD nowrap><A href="#10" style="color:black">[764]</A></TD><TD nowrap><A href="#10" style="color:black">Gafus</A></TD><TD nowrap><A href="#10" style="color:black">Gafus_CLR</A></TD><TD nowrap><A href="#10" style="color:black">2001/07/08 18:25</A></TD><TD><A href="#10" style="color:black">6/30�� - 7/1�� in Kael</A></TD></TR></TABLE>
<TABLE border=0 width=95%><TR><TD><SMALL><FONT color="#FF3366"><B>NEW</B></FONT> : �Ԃ͐e�L�����A�͎q�L���݂̂�24���Ԉȓ��ɓ��e���ꂽ�ꍇ�ł��B</SMALL></TD><TD align=right>
<table cellpadding=0 cellspacing=0><tr>
<form action="./petit.cgi" method="POST"><td>
<input type=hidden name=page value="10">
&nbsp;<input type=submit value="����10��">
</td></form>
</tr></table></TD></TR></TABLE></center><BR>
<center>

<!------------------------------------ ---------------------------------------------->
<A name="1"></A><TABLE BORDER=1 WIDTH='95%' BGCOLOR="#FFFFFF" CELLSPACING=1 CELLPADDING=5><TR><TD bgcolor=#FFFBF0 colspan=2>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
<BIG><b>[933]�@<font color="#006400">7/22 DNP</font></b> ���e�ҁF<b>Shizuho</b> ���e���F2001/07/22(Sun) 14:04 &nbsp;  </BIG></TD>
<TD align="right" nowrap><BIG><A href="#0" title="�O" style="color:black">��</A> <A href="#2" title="��" style="color:black">��</A>
 <A href="#top" title="�ŏ�" style="color:black">��</A> <A href="#btm" title="�Ō�" style="color:black">��</A></BIG></TD></TR></TABLE></TD></TR>
<TR><TD valign=top><BR><blockquote><font color="0000FF">1.Recurved Velium Bow<br>  MAGIC LORE<br>  Damage: 30 Dly: 39  Wt: 2<br>  Classes: WAR PAL RNG SHD ROG <br>  Race   : ALL<br><br>2.Tempered Velium Warsword<br>  MAGIC LORE  <br>  Damage: 10 Dly: 20  Wt: 2.5<br>  Classes: WAR PAL RNG SHD BRD ROG <br>  Race   : ALL<br><br>�̂Q��Keep�����B<br></font><BR></blockquote>
<hr size=1 width='95%'>
<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[934]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">2��1HS�ł��B<br> </FONT><small>(2001/07/22 14:05)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[936]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">3.Batfang Headband ���Q<br>MAGIC<br>Slot:HEAD<br>AC:2<br>WIS+3 INT+3<br>WT:1.5<br>Size:SMALL<br>Class:ALL<br>Race:ALL<br><br>4.Netted Kelp Bracelet<br>MAGIC<br>Slot:WRIST<br>AC:4<br>STR+4 STA+1 CHA-3 INT+4 SVF+2<br>WT:0.3<br>Size:SMALL<br>Class:ALL<br>Race:ALL<br><br>�ȏ�Keep�� </FONT><small>(2001/07/22 14:43)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[938]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Xneko</B></FONT></TD>
<TD valign=top><font color="800000">5.Chetari Bonecrafted Dhield x 3<br>MAGIC LORE<br>Slot:BACK SECONDARY<br>AC:19<br>SVF+10<br>WT:6.5<br>Size:LARGE<br>Class:WAR CLR PAL RNG SHD DRU BRD ROG SHM<br>Race:HUM ERU ELF HIE DEF HEF DWF HFL GNM IKS<br>TOTAl�R�o�Ă܂����ˁB�P�a�����Ă܂��B<br><br>6.Velium Knuckledusters<br>MAGIC LORE <br>Damage: 10 Dly: 25 Wt: 1.0<br>Slot:PRA SEC<br>Classes: WAR ROG MNK<br>Race : HUM BAR ELF DEF HEF DWF TRL OGR HFL GNM IKS<br><br> </FONT><small>(2001/07/22 21:08)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[939]</B></FONT></TD>
<TD valign=top><font color="800000"><B>issue@NPC�ɐ���������j</B></FONT></TD>
<TD valign=top><font color="800000">Chetari Bonecrafted Shield ��1�a�����Ă܂��B </FONT><small>(2001/07/22 23:31)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[940]</B></FONT></TD>
<TD valign=top><font color="800080"><B>BIS</B></FONT></TD>
<TD valign=top><font color="800080">���񂾂����ȁB<br>�~�������̈�I���Slot��GO<br>������EventBBS�ɏ������悤��Xneko�͏�1�m��Ƃ��܂��B<br>����肱�����̂��~�������Ă̂������Slot���Ă��������B<br>���������������̂��E����Nob����Oka�����Slot�i�V�ŁB<br>���ߐ؂�7/23 </FONT><small>(2001/07/23 02:17)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[943]</B></FONT></TD>
<TD valign=top><font color="800000"><B>sesu</B></FONT></TD>
<TD valign=top><font color="800000">������-�|���H���������ȁ[<br>���Ă��Ƃŋ|����<br><br><FONT color="FF0000"><B>[1��]</B></FONT> �X���b�g<B>0</B>�� <B>585</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/07/23 05:35)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="008000"><B>[945]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Yaminin</B></FONT></TD>
<TD valign=top><font color="008000">���������|�������ȁB�|��Kael�̂��邵�A���ŁB<br><FONT color="008000"><B>[2��]</B></FONT> �X���b�g<B>2</B>�� <B>104</B> ���o���� </FONT><small>(2001/07/23 11:58)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[946]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Infey</B></FONT></TD>
<TD valign=top><font color="0000FF">Tempered Velium Warsword��]�I<br><FONT color="008000"><B>[1��]</B></FONT> �X���b�g<B>2</B>�� <B>867</B> ���o���� </FONT><small>(2001/07/23 16:08)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF0000"><B>[949]</B></FONT></TD>
<TD valign=top><font color="FF0000"><B>issue@NPC�ɐ���������j</B></FONT></TD>
<TD valign=top><font color="FF0000"><FONT color="0000FF"><B>[1��]</B></FONT> �X���b�g<B>5</B>�� <B>695</B> ���o����<br>�k���邼�AHeart!!�R���s�������Heat!!<br>���ʂɋP�����F��OverDraive��������!! </FONT><small>(2001/07/23 22:03)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[950]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">all pass��(^^;; </FONT><small>(2001/07/24 02:27)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[951]</B></FONT></TD>
<TD valign=top><font color="800080"><B>BIS</B></FONT></TD>
<TD valign=top><font color="800080">���ƕ��͂Ɍ�����������͗l�B<br>EventBBS���������Ă��������B<br>���ߐ؂�7/24�ɉ��� </FONT><small>(2001/07/24 05:23)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[959]</B></FONT></TD>
<TD valign=top><font color="800080"><B>BIS</B></FONT></TD>
<TD valign=top><font color="800080">���΂炭BBS����܂���ł�����&gt;&lt;<br>�Ăщ���7/27<br>���x�������ߐ؂�&gt;&lt; </FONT><small>(2001/07/26 04:44)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[965]</B></FONT></TD>
<TD valign=top><font color="800080"><B>BIS</B></FONT></TD>
<TD valign=top><font color="800080">�m��B�������l�A�a�����Ă�l�ɒ��ڐ����� </FONT><small>(2001/07/28 06:19)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[967]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">�ł͋|��Sese����ɁA����Infey����ɁB<br>�������玝�������̂ŁA��������n���܂���[�B<br> </FONT><small>(2001/07/28 14:00)�@<FONT color="#FF3366"><B>NEW</B></FONT></small></TD></TR>

</TABLE>
<form name="res_933" method="POST" action="./petit.cgi" onsubmit="return wOpen('res_933')">
<input type=hidden name=mode value=regist>
<input type=hidden name=reno value="933">
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
<input type=button value="�R�}���h�}��" onClick="inputRandom('res_933')" class="btn"><BR>
<textarea name=comment cols=56 rows=3 wrap="off"></textarea></TD>
<TD><input type=password name=pwd size=4 value="" class="txt"> PASS<BR>
<input type=submit value='�ԁ@�@�M' class="btn"></TD></TR></TABLE></CENTER></form>
</TD>
<TD width=1% rowspan=2 valign=top nowrap><B>Slot0</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="FF0000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;685</TD><TD nowrap>&nbsp;sesu</TD></TR>
</TABLE><BR>
<B>Slot2</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="008000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;867</TD><TD nowrap>&nbsp;Infey</TD></TR>
<TR><TD align=right><FONT color="008000"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;104</TD><TD nowrap>&nbsp;Yaminin</TD></TR>
</TABLE><BR>
<B>Slot5</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="0000FF"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;695</TD><TD nowrap>&nbsp;issue@NPC�ɐ���������j</TD></TR>
</TABLE></TD>
</TR></TABLE><BR>


<!------------------------------------ ---------------------------------------------->
<A name="2"></A><TABLE BORDER=1 WIDTH='95%' BGCOLOR="#FFFFFF" CELLSPACING=1 CELLPADDING=5><TR><TD bgcolor=#FFFBF0 colspan=2>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
<BIG><b>[920]�@<font color="#006400">7/20-21�@Sebi �L�m�R�̉��l</font></b> ���e�ҁF<b>Deid</b> ���e���F2001/07/21(Sat) 14:03 &nbsp;  </BIG></TD>
<TD align="right" nowrap><BIG><A href="#1" title="�O" style="color:black">��</A> <A href="#3" title="��" style="color:black">��</A>
 <A href="#top" title="�ŏ�" style="color:black">��</A> <A href="#btm" title="�Ō�" style="color:black">��</A></BIG></TD></TR></TABLE></TD></TR>
<TR><TD valign=top><BR><blockquote><font color="008000">���[���ƁA<br>Tunic�͂P��Chatsubo�s����<br>�����P��ALL Roll�ŏ������l���ǂ����邩���߂���Ă��Əo�ǂ��ł��傤���H�B<br>�����OK�Ȑl��Roll 100�ŐU���Ă��������B<br>���΂̐l�͂ǂ�ȕ��@�������������Ă��������B</font><BR></blockquote>
<hr size=1 width='95%'>
<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><font color="008000"><B>[921]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Deid</B></FONT></TD>
<TD valign=top><font color="008000"><FONT color="FF0000"><B>[8��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>47</B> ���o�� </FONT><small>(2001/07/21 14:04)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="008000"><B>[925]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Yaminin</B></FONT></TD>
<TD valign=top><font color="008000"><FONT color="FF0000"><B>[3��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>79</B> ���o�� </FONT><small>(2001/07/21 17:54)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[926]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000"><FONT color="FF0000"><B>[6��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>70</B> ���o�� </FONT><small>(2001/07/21 19:39)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[928]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Bokuden</B></FONT></TD>
<TD valign=top><font color="800000"><FONT color="FF0000"><B>[7��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>51</B> ���o�� </FONT><small>(2001/07/21 20:03)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[929]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF"><FONT color="FF0000"><B>[2��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>87</B> ���o�� </FONT><small>(2001/07/21 22:44)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[930]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Infey</B></FONT></TD>
<TD valign=top><font color="0000FF"><FONT color="FF0000"><B>[5��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>73</B> ���o�� </FONT><small>(2001/07/21 23:16)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[932]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Okanoan@���W�X�g�}�j�A</B></FONT></TD>
<TD valign=top><font color="800000"><FONT color="FF0000"><B>[1��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>89</B> ���o�� </FONT><small>(2001/07/22 07:28)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[947]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Xneko</B></FONT></TD>
<TD valign=top><font color="800000"><FONT color="FF0000"><B>[9��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>31</B> ���o��<br> </FONT><small>(2001/07/23 19:38)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF69B4"><B>[948]</B></FONT></TD>
<TD valign=top><font color="FF69B4"><B>asako</B></FONT></TD>
<TD valign=top><font color="FF69B4"><FONT color="FF0000"><B>[3��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>79</B> ���o�� </FONT><small>(2001/07/23 20:36)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="008000"><B>[961]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Deid</B></FONT></TD>
<TD valign=top><font color="008000">�Ȃ񂩐U���Ă�l�����Ȃ�����<br>�Pweek�߂����̂Œ��ߐ؂�܂��B </FONT><small>(2001/07/27 03:23)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[966]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">Tunic��Oka����ɓn���܂����B<br>���߁[(^^/<br> </FONT><small>(2001/07/28 13:58)�@<FONT color="#FF3366"><B>NEW</B></FONT></small></TD></TR>

</TABLE>
<form name="res_920" method="POST" action="./petit.cgi" onsubmit="return wOpen('res_920')">
<input type=hidden name=mode value=regist>
<input type=hidden name=reno value="920">
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
<input type=button value="�R�}���h�}��" onClick="inputRandom('res_920')" class="btn"><BR>
<textarea name=comment cols=56 rows=3 wrap="off"></textarea></TD>
<TD><input type=password name=pwd size=4 value="" class="txt"> PASS<BR>
<input type=submit value='�ԁ@�@�M' class="btn"></TD></TR></TABLE></CENTER></form>
</TD>
<TD width=1% rowspan=2 valign=top nowrap><B>Dice0&nbsp;0-100</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="FF0000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;89</TD><TD nowrap>&nbsp;Okanoan@���W�X�g�}�j�A</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;87</TD><TD nowrap>&nbsp;Shizuho</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>3</B></FONT></TD><TD nowrap align=right>&nbsp;79</TD><TD nowrap>&nbsp;asako</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>3</B></FONT></TD><TD nowrap align=right>&nbsp;79</TD><TD nowrap>&nbsp;Yaminin</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>5</B></FONT></TD><TD nowrap align=right>&nbsp;73</TD><TD nowrap>&nbsp;Infey</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>6</B></FONT></TD><TD nowrap align=right>&nbsp;70</TD><TD nowrap>&nbsp;Gafus</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>7</B></FONT></TD><TD nowrap align=right>&nbsp;51</TD><TD nowrap>&nbsp;Bokuden</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>8</B></FONT></TD><TD nowrap align=right>&nbsp;47</TD><TD nowrap>&nbsp;Deid</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>9</B></FONT></TD><TD nowrap align=right>&nbsp;31</TD><TD nowrap>&nbsp;Xneko</TD></TR>
</TABLE></TD>
</TR></TABLE><BR>


<!------------------------------------ ---------------------------------------------->
<A name="3"></A><TABLE BORDER=1 WIDTH='95%' BGCOLOR="#FFFFFF" CELLSPACING=1 CELLPADDING=5><TR><TD bgcolor=#FFFBF0 colspan=2>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
<BIG><b>[915]�@<font color="#006400">7/20Chardok King&Queen</font></b> ���e�ҁF<b>Shizuho</b> ���e���F2001/07/20(Fri) 14:25 &nbsp;  </BIG></TD>
<TD align="right" nowrap><BIG><A href="#2" title="�O" style="color:black">��</A> <A href="#4" title="��" style="color:black">��</A>
 <A href="#top" title="�ŏ�" style="color:black">��</A> <A href="#btm" title="�Ō�" style="color:black">��</A></BIG></TD></TR></TABLE></TD></TR>
<TR><TD valign=top><BR><blockquote><font color="0000FF">��King&Queen���Ă����f�B�X�R����܂����ȁE�E�E�E�����f�B�X�R���Č��t�����ꂩ��(^^;<br><br>Diamond x1 �o�Ă܂��B<br><br>���ƁAZurnalk's Animation(Lv55 ENC Spell)��Lilit����s���ł��B<br>���x��������n���܂��ˁB�펞�g�т����B<br></font><BR></blockquote>
<hr size=1 width='95%'>
<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><font color="800000"><B>[916]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Bokuden</B></FONT></TD>
<TD valign=top><font color="800000">���́A�f�B�X�R�̓_���X�z�[�����ČĂԂ̂���ʓI(�f��)�B<br><br>Queen����ł�Dagger(10/28�E�E)��Xneko�ɓn���ς݁B<br>���ƁAForitude(CLR��55Spell)�o�Ă邯��Bank�s�����ȁH </FONT><small>(2001/07/20 17:13)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF69B4"><B>[917]</B></FONT></TD>
<TD valign=top><font color="FF69B4"><B>asako</B></FONT></TD>
<TD valign=top><font color="FF69B4">����King����Argent Defender ��Keep���Ă܂��B<br>33/49 Mana: +20  Weight: 10.0 <br>Weapon Skill: Two Hand Slash <br>Classes: Ranger Paladin Shadowknight Warrior  <br>Races: All Races  <br>Inventory Slot: Primary Melee�@<br><br> </FONT><small>(2001/07/20 21:46)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[918]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">�ꉞ�ŏ��̕񍐂����Ȃ̂ŏ���Ɏd�؂��Ă����ŃX�J�B<br>���T27�����j�����ŁY�܂��̂ŁA�݂�ȐU���ĂˁB<br> </FONT><small>(2001/07/21 05:29)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[919]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">�Ƃ������ƂŊF����~����ITEM����������Slot�Ń����B<br>2HS�͂�͂�g�p�\�̕��ł��肢���܂��B<br><br>�[���ƂŎ�DIA�~�����ȁB<br><br><br><br><FONT color="800080"><B>[9��]</B></FONT> �X���b�g<B>0</B>�� <B>193</B> ���o���� </FONT><small>(2001/07/21 05:36)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="008000"><B>[922]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Deid</B></FONT></TD>
<TD valign=top><font color="008000">Dia��<br><FONT color="FF0000"><B>[1��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>59</B> ���o�� </FONT><small>(2001/07/21 14:05)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="008000"><B>[923]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Deid</B></FONT></TD>
<TD valign=top><font color="008000">�Ԉ����(����)<br>slot��<br><FONT color="800080"><B>[3��]</B></FONT> �X���b�g<B>0</B>�� <B>736</B> ���o���� </FONT><small>(2001/07/21 14:06)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="008000"><B>[924]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Yaminin</B></FONT></TD>
<TD valign=top><font color="008000">DIA�ŁBArgent Defender�͎����Ă違�g���Ă�̂Ńp�X�B<br><FONT color="800080"><B>[4��]</B></FONT> �X���b�g<B>0</B>�� <B>730</B> ���o���� </FONT><small>(2001/07/21 17:53)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[927]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">all pass �ł� </FONT><small>(2001/07/21 19:40)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[931]</B></FONT></TD>
<TD valign=top><font color="800080"><B>BIS</B></FONT></TD>
<TD valign=top><font color="800080">GolemTearRing���o���o���������ł����B<br>�N��Keep���Ă܂���?? </FONT><small>(2001/07/22 06:19)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[937]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Aden@Mirage</B></FONT></TD>
<TD valign=top><font color="800000">BD 1, Dia 1<br>Water Sprinkler of the Forgiven<br> 2HS 11/24 Atone<br> CLR/All<br>�o�Ă܂��B�x���Ȃ�܂����B </FONT><small>(2001/07/22 20:11)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[941]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">�ʂ�(^^;;<br>������ǉ����E�E�E�����U������ǂ��납Pass�����܂�����(���<br><br>&gt;Water Sprinkler of the Forgiven<br>&gt;2HS 11/24 Atone<br>&gt;CLR/All<br>�������2HB�̊ԈႢ�łȂ��H�H<br>����item�ׂ݂̈̂�2HB Skil�������Ă���͓̂���(w<br>Delay�����Ԃ�CLR�������ł���2HB�ł��ő��̑㕨�Ǝv���܂��B<br>�E�E�E�o�k��p�B�_�E�E�EChardok�ŏo��̂�(^Q^ �W����<br> </FONT><small>(2001/07/23 02:54)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[942]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Adien@Mirage</B></FONT></TD>
<TD valign=top><font color="0000FF">�ǉ��`(&gt;.&lt;)/<br>Golem Tear Ring<br>Finger AC2 STR2 WIS6 Mana10 All/All<br><br>Edge of Cabilis<br>2HS 25/50 WAR,PAL,RNG,SHD/All<br><br>�����o�Ă��Ȃ����낤�ȁc </FONT><small>(2001/07/23 03:16)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF00FF"><B>[944]</B></FONT></TD>
<TD valign=top><font color="FF00FF"><B>Makos</B></FONT></TD>
<TD valign=top><font color="FF00FF">Atone��������邯�ǁABD���m�P�������ĂȂ����Ȃ��i��<br>Auc�Ŕ��������Ȃ����BBD�ŁB<br><br><FONT color="800080"><B>[7��]</B></FONT> �X���b�g<B>0</B>�� <B>454</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/07/23 11:40)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF0000"><B>[952]</B></FONT></TD>
<TD valign=top><font color="FF0000"><B>Rainsama</B></FONT></TD>
<TD valign=top><font color="FF0000">GolemTearRing de!<br><FONT color="800080"><B>[6��]</B></FONT> �X���b�g<B>0</B>�� <B>724</B> ���o���� </FONT><small>(2001/07/25 09:11)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[953]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">��[�ƁA���΂炭�l���Ă���ł����E�E�E�B<br>�ォ��ǉ���Item������܂��āA������BD����܂�����ˁB<br>�U��Ȃ����̂��A�������B�i�傫���̏o�Ă��������̏o�Ă��X�b�L�����Ȃ��C���j<br>�Ƃ������ƂŐ�ɐU�����l�A�Ώ�Item�w�肵�Ȃ����Ă������Ǝv���܂����ǂ��ł��傤�H<br>�Ƃ������A��ɐU��������Deid����Yami����́A�݂��DIA-�����Ă܂����A<br>BD��������BD�ł������ρi�΁jGaf�����BD��������Pass���Ȃ������ł��傤���B<br>����BD����DIA���~�����̂Ȃ�ύX���Ȃ��Ă�Ok�ł��B<br>������ɂ��Ă��A������Slot�񂷑O�̐S���ł��肢���܂��B<br><br>���ᎄ��BD�ɕύX���Ƃ��܂��B�������肵�Ă܂����i��<br><br><br><br><br><br><br><br><br><br> </FONT><small>(2001/07/25 14:44)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[954]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Sleip</B></FONT></TD>
<TD valign=top><font color="800000">BD de<br><br><FONT color="800080"><B>[2��]</B></FONT> �X���b�g<B>0</B>�� <B>861</B> ���o���� </FONT><small>(2001/07/25 17:55)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF69B4"><B>[955]</B></FONT></TD>
<TD valign=top><font color="FF69B4"><B>asako</B></FONT></TD>
<TD valign=top><font color="FF69B4">Golem Tear Ring de :)<br><br><FONT color="800080"><B>[10��]</B></FONT> �X���b�g<B>0</B>�� <B>136</B> ���o���� </FONT><small>(2001/07/25 20:50)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF00FF"><B>[956]</B></FONT></TD>
<TD valign=top><font color="FF00FF"><B>Makos</B></FONT></TD>
<TD valign=top><font color="FF00FF">&gt;��[�ƁA���΂炭�l���Ă���ł����E�E�E�B<br>&gt;�ォ��ǉ���Item������܂��āA������BD����܂�����ˁB<br>&gt;�U��Ȃ����̂��A�������B�i�傫���̏o�Ă��������̏o�Ă��X�b�L�����Ȃ��C���j<br>&gt;�Ƃ������ƂŐ�ɐU�����l�A�Ώ�Item�w�肵�Ȃ����Ă������Ǝv���܂����ǂ��ł��傤�H<br><br>���̂��߂�slot�Ȃ�ŁA���R��̐l����BD����Ă����ėǂ����ƁB </FONT><small>(2001/07/25 20:56)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[957]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">&gt; Gaf�����BD��������Pass���Ȃ������ł��傤��<br>�����Ɍ�����BD���Atone��(w<br>�����ăR�C�c���U�肪�����̂Ȃ����AAuction�ŏo�Ă��Ȃ���(^^;;<br><br>but ���΂炭EQ�ŗV�Ԃ̂��ϑ��I(������V�ׂȂ�)�̂�<br>����ς� all pass �ł�(^^;;<br>�N���ɗL�����p���Ă��炤�����C�����ǂ��̂ŁB </FONT><small>(2001/07/26 03:44)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[958]</B></FONT></TD>
<TD valign=top><font color="800080"><B>BIS</B></FONT></TD>
<TD valign=top><font color="800080">BD�������̂��E�E�E(w<br><FONT color="800080"><B>[1��]</B></FONT> �X���b�g<B>0</B>�� <B>899</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/07/26 04:43)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[960]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">���傢�ƁY���������܂����B<br>30���܂ł��Ă��Ƃł�낵���B<br>�Ƃ���łb�l�̕��X��Roll���Ȃ���ł��傤���[�B<br> </FONT><small>(2001/07/26 05:25)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[962]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Drie</B></FONT></TD>
<TD valign=top><font color="800000">�Ȃ񂩂���񂪐U���Ă����� =)<br>��Όn��BD<br><br><FONT color="800080"><B>[8��]</B></FONT> �X���b�g<B>0</B>�� <B>528</B> ���o���� </FONT><small>(2001/07/27 18:30)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[963]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Adien@Mirage</B></FONT></TD>
<TD valign=top><font color="0000FF">Golem Tear Ring�~�������ǖ������낤�ȁB<br><FONT color="800080"><B>[4��]</B></FONT> �X���b�g<B>0</B>�� <B>730</B> ���o���� </FONT><small>(2001/07/27 22:04)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[964]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Adien@Mirage</B></FONT></TD>
<TD valign=top><font color="0000FF">Mirage��Loot item�͎���Bank char��FP�Ŏ����Ă܂��B<br>���܂�����Tell��낵���B </FONT><small>(2001/07/27 22:06)</small></TD></TR>

</TABLE>
<form name="res_915" method="POST" action="./petit.cgi" onsubmit="return wOpen('res_915')">
<input type=hidden name=mode value=regist>
<input type=hidden name=reno value="915">
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
<input type=button value="�R�}���h�}��" onClick="inputRandom('res_915')" class="btn"><BR>
<textarea name=comment cols=56 rows=3 wrap="off"></textarea></TD>
<TD><input type=password name=pwd size=4 value="" class="txt"> PASS<BR>
<input type=submit value='�ԁ@�@�M' class="btn"></TD></TR></TABLE></CENTER></form>
</TD>
<TD width=1% rowspan=2 valign=top nowrap><B>Dice0&nbsp;0-100</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="FF0000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;59</TD><TD nowrap>&nbsp;Deid</TD></TR>
</TABLE><BR><B>Slot0</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="800080"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;999</TD><TD nowrap>&nbsp;BIS</TD></TR>
<TR><TD align=right><FONT color="800080"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;861</TD><TD nowrap>&nbsp;Sleip</TD></TR>
<TR><TD align=right><FONT color="800080"><B>3</B></FONT></TD><TD nowrap align=right>&nbsp;736</TD><TD nowrap>&nbsp;Deid</TD></TR>
<TR><TD align=right><FONT color="800080"><B>4</B></FONT></TD><TD nowrap align=right>&nbsp;730</TD><TD nowrap>&nbsp;Yaminin</TD></TR>
<TR><TD align=right><FONT color="800080"><B>4</B></FONT></TD><TD nowrap align=right>&nbsp;730</TD><TD nowrap>&nbsp;Adien@Mirage</TD></TR>
<TR><TD align=right><FONT color="800080"><B>6</B></FONT></TD><TD nowrap align=right>&nbsp;724</TD><TD nowrap>&nbsp;Rainsama</TD></TR>
<TR><TD align=right><FONT color="800080"><B>7</B></FONT></TD><TD nowrap align=right>&nbsp;554</TD><TD nowrap>&nbsp;Makos</TD></TR>
<TR><TD align=right><FONT color="800080"><B>8</B></FONT></TD><TD nowrap align=right>&nbsp;528</TD><TD nowrap>&nbsp;Drie</TD></TR>
<TR><TD align=right><FONT color="800080"><B>9</B></FONT></TD><TD nowrap align=right>&nbsp;193</TD><TD nowrap>&nbsp;Shizuho</TD></TR>
<TR><TD align=right><FONT color="800080"><B>10</B></FONT></TD><TD nowrap align=right>&nbsp;136</TD><TD nowrap>&nbsp;asako</TD></TR>
</TABLE></TD>
</TR></TABLE><BR>


<!------------------------------------ ---------------------------------------------->
<A name="4"></A><TABLE BORDER=1 WIDTH='95%' BGCOLOR="#FFFFFF" CELLSPACING=1 CELLPADDING=5><TR><TD bgcolor=#FFFBF0 colspan=2>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
<BIG><b>[894]�@<font color="#006400">7/12����Severilous Roll</font></b> ���e�ҁF<b>Bokuden</b> ���e���F2001/07/12(Thu) 05:39 &nbsp;  </BIG></TD>
<TD align="right" nowrap><BIG><A href="#3" title="�O" style="color:black">��</A> <A href="#5" title="��" style="color:black">��</A>
 <A href="#top" title="�ŏ�" style="color:black">��</A> <A href="#btm" title="�Ō�" style="color:black">��</A></BIG></TD></TR></TABLE></TD></TR>
<TR><TD valign=top><BR><blockquote><font color="800000">Severilous��Drop Item����<br><br>�P�AShield of Green Dragon<br><a href="http://eqdb.allakhazam.com/item.html?item=1133" target='_top'>http://eqdb.allakhazam.com/item.html?item=1133</a><br><br>�Q�AForm of the Hunter (DRU Spell) x 2��(1��Asako�m��)<br>�R�ATalisman of the Raptor�iSHM Spell)�@Can����m��<br>�S�AMala�iMAG Spell)<br>�T�APal Epic��Naggy Book(Deidrit�a����)<br><br>Shield�͎g�p�\Class��Race��Roll�ADRU Spell,Mag Spell,Pal Book��<br>�Q�����Ă��ꂽGuild������Need�ȊY��Class�̐l��Slot�Ƃ����Ē����܂��B<br>Need��Item�̔ԍ�(Or���O)�𖾋L�̏�Slot��U���Ă��������B<br>���ߐ؂�͗��T�̖ؗj�̒�9:00�Ƃ����Ă��������܂��B</font><BR></blockquote>
<hr size=1 width='95%'>
<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><font color="800000"><B>[900]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Vognus</B></FONT></TD>
<TD valign=top><font color="800000"><FONT color="FF69B4"><B>[7��]</B></FONT> �X���b�g<B>0</B>�� <B>122</B> ���o�����B <B>Congratulations! +100�_</B><br>Shield�@�ق�����<br> </FONT><small>(2001/07/13 10:35)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[901]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Vognus</B></FONT></TD>
<TD valign=top><font color="800000">�����A�I������c(;.;)<br>���A�ԍ��͂������P�ł� </FONT><small>(2001/07/13 10:37)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[904]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">Shield�ŐU���Ƃ��܂��B<br><br><FONT color="FF69B4"><B>[1��]</B></FONT> �X���b�g<B>0</B>�� <B>800</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/07/13 22:46)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF0000"><B>[905]</B></FONT></TD>
<TD valign=top><font color="FF0000"><B>Candra</B></FONT></TD>
<TD valign=top><font color="FF0000"><FONT color="FF69B4"><B>[2��]</B></FONT> �X���b�g<B>0</B>�� <B>771</B> ���o�����B <B>Congratulations! +100�_</B><br><br>���ŁASpell�L�邩�疳�����Ęb�Ȃ�Pass�ŁB </FONT><small>(2001/07/13 23:18)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[906]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Xneko</B></FONT></TD>
<TD valign=top><font color="800000">����<br><FONT color="FF69B4"><B>[5��]</B></FONT> �X���b�g<B>0</B>�� <B>406</B> ���o����<br> </FONT><small>(2001/07/13 23:40)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[907]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">Shield���ق������[<br><br><FONT color="FF69B4"><B>[6��]</B></FONT> �X���b�g<B>0</B>�� <B>242</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/07/14 04:50)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[908]</B></FONT></TD>
<TD valign=top><font color="800080"><B>Neath</B></FONT></TD>
<TD valign=top><font color="800080">�ʂ������������I�I�I<br><br><FONT color="FF69B4"><B>[4��]</B></FONT> �X���b�g<B>0</B>�� <B>594</B> ���o����<br> </FONT><small>(2001/07/14 12:32)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[912]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Infey</B></FONT></TD>
<TD valign=top><font color="0000FF">�������P�I<br><FONT color="FF69B4"><B>[3��]</B></FONT> �X���b�g<B>0</B>�� <B>843</B> ���o���� </FONT><small>(2001/07/19 02:16)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[913]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Bokuden</B></FONT></TD>
<TD valign=top><font color="800000">�m��ŁI<br>Shizu�����Shield of Green Dragon���A�󂯓n����NFP�ɂāB<br><br>���ƁADRU��MAG��Spell�̓I�C���̕����獡��Q�����Ă����������eGuild�̐l�o�R�ŕ����Ă݂܂��ˁB </FONT><small>(2001/07/19 21:14)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[914]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">�����E�E�E�v���Ԃ�ɑ啨��Roll���Ă��Ȃ��B<br>���肪�����g�킹�Ē����܂��Bm(_ _)m<br><br> </FONT><small>(2001/07/20 14:20)</small></TD></TR>

</TABLE>
<form name="res_894" method="POST" action="./petit.cgi" onsubmit="return wOpen('res_894')">
<input type=hidden name=mode value=regist>
<input type=hidden name=reno value="894">
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
<input type=button value="�R�}���h�}��" onClick="inputRandom('res_894')" class="btn"><BR>
<textarea name=comment cols=56 rows=3 wrap="off"></textarea></TD>
<TD><input type=password name=pwd size=4 value="" class="txt"> PASS<BR>
<input type=submit value='�ԁ@�@�M' class="btn"></TD></TR></TABLE></CENTER></form>
</TD>
<TD width=1% rowspan=2 valign=top nowrap><B>Slot0</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="FF69B4"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;900</TD><TD nowrap>&nbsp;Shizuho</TD></TR>
<TR><TD align=right><FONT color="FF69B4"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;871</TD><TD nowrap>&nbsp;Candra</TD></TR>
<TR><TD align=right><FONT color="FF69B4"><B>3</B></FONT></TD><TD nowrap align=right>&nbsp;843</TD><TD nowrap>&nbsp;Infey</TD></TR>
<TR><TD align=right><FONT color="FF69B4"><B>4</B></FONT></TD><TD nowrap align=right>&nbsp;594</TD><TD nowrap>&nbsp;Neath</TD></TR>
<TR><TD align=right><FONT color="FF69B4"><B>5</B></FONT></TD><TD nowrap align=right>&nbsp;406</TD><TD nowrap>&nbsp;Xneko</TD></TR>
<TR><TD align=right><FONT color="FF69B4"><B>6</B></FONT></TD><TD nowrap align=right>&nbsp;342</TD><TD nowrap>&nbsp;Gafus</TD></TR>
<TR><TD align=right><FONT color="FF69B4"><B>7</B></FONT></TD><TD nowrap align=right>&nbsp;222</TD><TD nowrap>&nbsp;Vognus</TD></TR>
</TABLE></TD>
</TR></TABLE><BR>


<!------------------------------------ ---------------------------------------------->
<A name="5"></A><TABLE BORDER=1 WIDTH='95%' BGCOLOR="#FFFFFF" CELLSPACING=1 CELLPADDING=5><TR><TD bgcolor=#FFFBF0 colspan=2>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
<BIG><b>[878]�@<font color="#006400">7/9Keal�iPA�����ł��グ�j��</font></b> ���e�ҁF<b>Infey</b> ���e���F2001/07/10(Tue) 20:41 &nbsp;  </BIG></TD>
<TD align="right" nowrap><BIG><A href="#4" title="�O" style="color:black">��</A> <A href="#6" title="��" style="color:black">��</A>
 <A href="#top" title="�ŏ�" style="color:black">��</A> <A href="#btm" title="�Ō�" style="color:black">��</A></BIG></TD></TR></TABLE></TD></TR>
<TR><TD valign=top><BR><blockquote><font color="0000FF">1.Diamond<br><br>2.Giant�@Scalemail Tunic<br>Ac18 Hp40 WT20<br>Classes�FWar Rog Brd Shd Pal Clr Shm Ran  <br>Races�FHuman Half Elf High Elf Wood Elf Erudite Barbarian<br>Dark Elf Troll Ogre Iksar</font><BR></blockquote>
<hr size=1 width='95%'>
<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><font color="800080"><B>[881]</B></FONT></TD>
<TD valign=top><font color="800080"><B>BIS</B></FONT></TD>
<TD valign=top><font color="800080">Diamond�ǉ� </FONT><small>(2001/07/11 00:54)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF0000"><B>[882]</B></FONT></TD>
<TD valign=top><font color="FF0000"><B>Infey</B></FONT></TD>
<TD valign=top><font color="FF0000">�Q�������lDice0��Max100�ł�낵��<br>���������o�����l�������Ă������Ƃɂ��܂��B<br><br>�܂��ALootItem�����ĂȂ��l�����瑁�������Ă��������B </FONT><small>(2001/07/11 15:13)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF0000"><B>[883]</B></FONT></TD>
<TD valign=top><font color="FF0000"><B>Infey</B></FONT></TD>
<TD valign=top><font color="FF0000">Dia�����I<br><FONT color="FF0000"><B>[4��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>61</B> ���o�� </FONT><small>(2001/07/11 15:14)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[884]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Bokuden@���</B></FONT></TD>
<TD valign=top><font color="800000">����1��Dia Need���ȁ[�B<br><br><FONT color="008000"><B>[1��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B>1</B> ��U���� <B>47</B> ���o�� </FONT><small>(2001/07/11 17:59)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="000080"><B>[885]</B></FONT></TD>
<TD valign=top><font color="000080"><B>�g����������</B></FONT></TD>
<TD valign=top><font color="000080">�_�C�����낦�Ȃ��Ɓ���<br><FONT color="FF0000"><B>[3��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>66</B> ���o�� </FONT><small>(2001/07/11 18:45)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[886]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">�������[<br><br><FONT color="FF0000"><B>[5��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>48</B> ���o�� </FONT><small>(2001/07/11 22:44)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[887]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Infey</B></FONT></TD>
<TD valign=top><font color="800000">�Y�؏����Y��Ă�<br>7��15���܂łƂ��܂��B�i��������Item������킯�ł��Ȃ����A�T�N�b�ƏI��点�܂��傗<br> </FONT><small>(2001/07/12 00:05)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[888]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">Diamond-<br>No1����ˁH�H�H<br><br><FONT color="008000"><B>[2��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B>1</B> ��U���� <B>45</B> ���o�� </FONT><small>(2001/07/12 00:13)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[890]</B></FONT></TD>
<TD valign=top><font color="800000"><B>sesu</B></FONT></TD>
<TD valign=top><font color="800000">watasi nimo daia tyo<br><FONT color="FF0000"><B>[2��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>85</B> ���o�� </FONT><small>(2001/07/12 02:04)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[891]</B></FONT></TD>
<TD valign=top><font color="800000"><B>kong</B></FONT></TD>
<TD valign=top><font color="800000"><FONT color="008000"><B>[4��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B>1</B> ��U���� <B>22</B> ���o��<br><br>daia </FONT><small>(2001/07/12 02:24)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[892]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Sleip</B></FONT></TD>
<TD valign=top><font color="800000">���̂�I<br><FONT color="FF0000"><B>[1��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>93</B> ���o�� </FONT><small>(2001/07/12 04:43)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="008000"><B>[893]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Deid</B></FONT></TD>
<TD valign=top><font color="008000"><FONT color="FF0000"><B>[7��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>32</B> ���o�� </FONT><small>(2001/07/12 05:10)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="008000"><B>[895]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Keropyon</B></FONT></TD>
<TD valign=top><font color="008000">dia-- de<br><FONT color="008000"><B>[3��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B>1</B> ��U���� <B>27</B> ���o�� </FONT><small>(2001/07/12 06:10)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF69B4"><B>[896]</B></FONT></TD>
<TD valign=top><font color="FF69B4"><B>asako</B></FONT></TD>
<TD valign=top><font color="FF69B4">Dia�z�V�C�B<br><FONT color="FF0000"><B>[6��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>43</B> ���o�� </FONT><small>(2001/07/12 06:23)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[897]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>issue@��Ђœ����Ă���ӂ�i�e�v�H�j��Skill�𖁂����̒j</B></FONT></TD>
<TD valign=top><font color="0000FF"><FONT color="FF0000"><B>[8��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B></B> ��U���� <B>26</B> ���o��<br>Dia�z�V�C�B </FONT><small>(2001/07/12 12:27)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="008000"><B>[898]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Keropyon</B></FONT></TD>
<TD valign=top><font color="008000">issue���񖼑O�A�����`�i�� </FONT><small>(2001/07/12 21:35)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF0000"><B>[911]</B></FONT></TD>
<TD valign=top><font color="FF0000"><B>Infey</B></FONT></TD>
<TD valign=top><font color="FF0000">�Y�؂ł��B<br>Diamond�iSleip�Esesu<br>Giant�@Scalemail Tunic�iHekate<br>�Ɍ��܂�܂����B���߂łƂ��I<br>Tunic�́A������~�����ЂƂ��Ȃ��l�Ȃ̂�3�Ԗڂ�Hekate����s���Ƃ��܂��B<br>���H�������Ȃ��H�� </FONT><small>(2001/07/16 13:24)</small></TD></TR>

</TABLE>
<form name="res_878" method="POST" action="./petit.cgi" onsubmit="return wOpen('res_878')">
<input type=hidden name=mode value=regist>
<input type=hidden name=reno value="878">
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
<input type=button value="�R�}���h�}��" onClick="inputRandom('res_878')" class="btn"><BR>
<textarea name=comment cols=56 rows=3 wrap="off"></textarea></TD>
<TD><input type=password name=pwd size=4 value="" class="txt"> PASS<BR>
<input type=submit value='�ԁ@�@�M' class="btn"></TD></TR></TABLE></CENTER></form>
</TD>
<TD width=1% rowspan=2 valign=top nowrap><B>Dice0&nbsp;0-100</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="FF0000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;93</TD><TD nowrap>&nbsp;Sleip</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;85</TD><TD nowrap>&nbsp;sesu</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>3</B></FONT></TD><TD nowrap align=right>&nbsp;66</TD><TD nowrap>&nbsp;�g����������</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>4</B></FONT></TD><TD nowrap align=right>&nbsp;61</TD><TD nowrap>&nbsp;Infey</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>5</B></FONT></TD><TD nowrap align=right>&nbsp;48</TD><TD nowrap>&nbsp;Shizuho</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>6</B></FONT></TD><TD nowrap align=right>&nbsp;43</TD><TD nowrap>&nbsp;asako</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>7</B></FONT></TD><TD nowrap align=right>&nbsp;32</TD><TD nowrap>&nbsp;Deid</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>8</B></FONT></TD><TD nowrap align=right>&nbsp;26</TD><TD nowrap>&nbsp;issue@��Ђœ����Ă���ӂ�i�e�v�H�j��Skill�𖁂����̒j</TD></TR>
</TABLE><BR>
<B>Dice1&nbsp;0-100</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="008000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;47</TD><TD nowrap>&nbsp;Bokuden@���</TD></TR>
<TR><TD align=right><FONT color="008000"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;45</TD><TD nowrap>&nbsp;Gafus</TD></TR>
<TR><TD align=right><FONT color="008000"><B>3</B></FONT></TD><TD nowrap align=right>&nbsp;27</TD><TD nowrap>&nbsp;Keropyon</TD></TR>
<TR><TD align=right><FONT color="008000"><B>4</B></FONT></TD><TD nowrap align=right>&nbsp;22</TD><TD nowrap>&nbsp;kong</TD></TR>
</TABLE></TD>
</TR></TABLE><BR>


<!------------------------------------ ---------------------------------------------->
<A name="6"></A><TABLE BORDER=1 WIDTH='95%' BGCOLOR="#FFFFFF" CELLSPACING=1 CELLPADDING=5><TR><TD bgcolor=#FFFBF0 colspan=2>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
<BIG><b>[858]�@<font color="#006400">6/24 in PoS</font></b> ���e�ҁF<b>Gafus</b> ���e���F2001/07/06(Fri) 02:41 &nbsp;  </BIG></TD>
<TD align="right" nowrap><BIG><A href="#5" title="�O" style="color:black">��</A> <A href="#7" title="��" style="color:black">��</A>
 <A href="#top" title="�ŏ�" style="color:black">��</A> <A href="#btm" title="�Ō�" style="color:black">��</A></BIG></TD></TR></TABLE></TD></TR>
<TR><TD valign=top><BR><blockquote><font color="800000">�N���n�߂Ȃ��̂ŏ���ɐi�߂܂�(&gt;&lt;/<br>DICE��0-1000���Ă��������B<br>�ォ�珇�ɕ��z���Ă����܂��B<br>�����Ɋ֌W�Ȃ�Class��item���s���l�������Ȃ肻���ł���<br>�֌W����l��get�����l�Ō����ď�肭����Ă�������(��<br><br>�������ォ�珇�Ɋ֌W�̂���Class��item���番�z�͂��Ă����܂��B<br><br>���ꂮ���100�ŐU��Ȃ��悤��(��<br>���Ɓu���O�̌���Class�v�������Ă����Ă��������B<br>���肢���܂�(&gt;&lt;/<br>���܂��`��(?) Class���Ⴂ����̂ŁB<br>�ŏIroll���u24h�v�ŁY����܂��B</font><BR></blockquote>
<hr size=1 width='95%'>
<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><font color="800000"><B>[859]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus_CLR</B></FONT></TD>
<TD valign=top><font color="800000">�݂�ȑ����U���Ă�(��<br><br><FONT color="FF0000"><B>[1��]</B></FONT> 0 ���� 1000 �܂ł� �T�C�R��<B></B> ��U���� <B>995</B> ���o��<br> </FONT><small>(2001/07/06 02:43)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[860]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus_CLR</B></FONT></TD>
<TD valign=top><font color="800000">���E�E�E�ڂ�����(^^;;<br> </FONT><small>(2001/07/06 02:44)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[861]</B></FONT></TD>
<TD valign=top><font color="800080"><B>BIS@WayStation.GM</B></FONT></TD>
<TD valign=top><font color="800080">�m��Ȃ̂ŐU��܂���(w </FONT><small>(2001/07/06 06:04)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="008000"><B>[864]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Keropyon_MNK</B></FONT></TD>
<TD valign=top><font color="008000">kyaa!<br><FONT color="FF0000"><B>[4��]</B></FONT> 0 ���� 1000 �܂ł� �T�C�R��<B></B> ��U���� <B>318</B> ���o�� </FONT><small>(2001/07/06 17:09)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF0000"><B>[866]</B></FONT></TD>
<TD valign=top><font color="FF0000"><B>Deidrit</B></FONT></TD>
<TD valign=top><font color="FF0000"><FONT color="FF0000"><B>[5��]</B></FONT> 0 ���� 1000 �܂ł� �T�C�R��<B></B> ��U���� <B>298</B> ���o�� </FONT><small>(2001/07/07 02:53)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[867]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Bokuden</B></FONT></TD>
<TD valign=top><font color="800000"><FONT color="FF0000"><B>[3��]</B></FONT> 0 ���� 1000 �܂ł� �T�C�R��<B></B> ��U���� <B>641</B> ���o�� </FONT><small>(2001/07/07 06:38)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[868]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Okanoan@���W�X�g�}�j�A</B></FONT></TD>
<TD valign=top><font color="800000"><FONT color="FF0000"><B>[6��]</B></FONT> 0 ���� 1000 �܂ł� �T�C�R��<B></B> ��U���� <B>47</B> ���o�� </FONT><small>(2001/07/07 09:50)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="000080"><B>[869]</B></FONT></TD>
<TD valign=top><font color="000080"><B>�g����������</B></FONT></TD>
<TD valign=top><font color="000080">������Ƃ��^���X���Ă����E�E<br><FONT color="FF0000"><B>[2��]</B></FONT> 0 ���� 1000 �܂ł� �T�C�R��<B></B> ��U���� <B>993</B> ���o�� </FONT><small>(2001/07/07 16:31)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[875]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus_CLR</B></FONT></TD>
<TD valign=top><font color="800000">�Y��24h���߂��Ă邯�ǁA�z���g�ɂ���ŁY������ėǂ��̂��H<br>CM������N��roll���ɗ��ĂȂ����E�E�E(CM��BBS�ɂ̓J�L�R�ς�) </FONT><small>(2001/07/10 02:36)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[899]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus_CLR</B></FONT></TD>
<TD valign=top><font color="800000">�Y�܂��B<br>�W�v�͌��(���炭�y�j�̒�)�s���āA�����ɏ����܂��B<br>���łɎ����Ă��镨�ƃ_�u�邩������Ȃ��̂ŏW�v���ʂ��������<br>���̐l�ƌ������鎖���l���܂��傤(^^;; </FONT><small>(2001/07/13 03:01)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[909]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">�W�v���ʁ`<br><br>Spiroc Feather(Nec                Rainy �� Oka<br>Silver Disc(Enc Nec               Rainy �� Oka<br>Gem of Empowerment(Mag            Rainy �� Oka<br><br>Ivory Tessera (War,Rog)           Asako �� Boku<br>Red Race Paint (Rog)              Asako �� Boku<br><br>Verdant Tessera(MNK�w���ANEC���  Gafus �� Oka<br>Gridelin Globe(RNG��              Gafus �� Kero<br>Iron Disc(MAG��AWIZ��            Gafus �� Bis<br>Red Face Paint(ROG��              Gafus �� Heka<br>Spiroc Feather(NEC�w��            Gafus �� Deid<br>Azure Tessera(DRU��AWIZ��        Gafus �� Bis<br>Ethereal Opal(WIZ��               Gafus �� Bis<br>Auburn Tessera(RNG��ASHM��       Gafus �� Gaf<br>Platinum Disc(BRD���ASHM���      Gafus �� Gaf<br>Gem of Empowerment(MAG��          Gafus �� Gaf<br><br>Phosphoric globe(brd              Kuantaku �� Heka<br><br>Gold Disc(CLR                     Hekate �� Gaf<br><br>Ebon Tessera (Shd)                Shizuho �� Kero<br><br>Silver Disc:Enc Nec               Bis �� Deid<br>Platinum Disc:Brd Shm             Bis �� Boku<br>Ebon Tessera:Shd                  Bis �� Heka<br><br>Bronze Disc(ROG��EWAR��j        U7 �� Heka<br>Ochre Tessera�iBRD��ECLR���j     U7 �� Gaf<br>Harpy Tongue�iRNG�w���j           U7 �� Boku<br>Tiny Ruby�iMNK��EWAR�w�j         U7 �� Boku<br>Platinum Disc(BRD���ESHM���j    U7 �� Kero<br>Ebon Tessera(SHD��j              U7 �� Kero<br>Verdant Tessera(MNK�w���ENEC���) U7 �� Kero<br><br>Black Face Paint(dru              Candra �� Deid<br>Songbird Statuette(brd            Candra �� Deid<br>Music Box(brd                     Candra �� Deid<br><br>Platinum Disc(BRD                 Driestis ��Heka<br><br>����Ȃ��񂶂��`<br>�z���v�Z�ɓ񎞊Ԃ����������܂�����(�� </FONT><small>(2001/07/14 15:52)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[910]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">���႟�`<br>Q Item���Ǝ�����̊ԂɃX�y�[�X����Č��₷��(�����₩�Ȓ�R)�����̂Ɂ[<br>�S�������Ă那�` </FONT><small>(2001/07/14 15:53)</small></TD></TR>

</TABLE>
<form name="res_858" method="POST" action="./petit.cgi" onsubmit="return wOpen('res_858')">
<input type=hidden name=mode value=regist>
<input type=hidden name=reno value="858">
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
<input type=button value="�R�}���h�}��" onClick="inputRandom('res_858')" class="btn"><BR>
<textarea name=comment cols=56 rows=3 wrap="off"></textarea></TD>
<TD><input type=password name=pwd size=4 value="" class="txt"> PASS<BR>
<input type=submit value='�ԁ@�@�M' class="btn"></TD></TR></TABLE></CENTER></form>
</TD>
<TD width=1% rowspan=2 valign=top nowrap><B>Dice0&nbsp;0-1000</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="FF0000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;995</TD><TD nowrap>&nbsp;Gafus_CLR</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;993</TD><TD nowrap>&nbsp;�g����������</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>3</B></FONT></TD><TD nowrap align=right>&nbsp;641</TD><TD nowrap>&nbsp;Bokuden</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>4</B></FONT></TD><TD nowrap align=right>&nbsp;318</TD><TD nowrap>&nbsp;Keropyon_MNK</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>5</B></FONT></TD><TD nowrap align=right>&nbsp;298</TD><TD nowrap>&nbsp;Deidrit</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>6</B></FONT></TD><TD nowrap align=right>&nbsp;47</TD><TD nowrap>&nbsp;Okanoan@���W�X�g�}�j�A</TD></TR>
</TABLE></TD>
</TR></TABLE><BR>


<!------------------------------------ ---------------------------------------------->
<A name="7"></A><TABLE BORDER=1 WIDTH='95%' BGCOLOR="#FFFFFF" CELLSPACING=1 CELLPADDING=5><TR><TD bgcolor=#FFFBF0 colspan=2>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
<BIG><b>[874]�@<font color="#006400">Xneko�����Help��Hole�s�������i7/8�j</font></b> ���e�ҁF<b>Lilit</b> ���e���F2001/07/10(Tue) 02:32 &nbsp;  </BIG></TD>
<TD align="right" nowrap><BIG><A href="#6" title="�O" style="color:black">��</A> <A href="#8" title="��" style="color:black">��</A>
 <A href="#top" title="�ŏ�" style="color:black">��</A> <A href="#btm" title="�Ō�" style="color:black">��</A></BIG></TD></TR></TABLE></TD></TR>
<TR><TD valign=top><BR><blockquote><font color="800000">1.Withered Leather Mask<br>MAGIC ITEM LORE ITEM<br>Slot: FACE<br>AC: 3<br>CHR: +8  WIZ: +2  MANA: +10<br>WT:0.4  Size: SMALL<br>Class: CLR DRU SHM<br>Race: HUM BAR ERU ELF HIE DEF HEF IKS<br><br>2.Withered Leather Cloak<br>MAGIC ITEM LORE ITEM<br>Slot: BACK<br>AC: 3<br>STR: +5  STA: +8  MANA: +15<br>WT:2.0  Size: MIDIUM<br>Class: CLR DRU SHM<br>Race: ALL<br><br>�ȏ�Q�_���P�Âa�����Ă��܂��`<br></font><BR></blockquote>
<hr size=1 width='95%'>
<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><font color="800000"><B>[877]</B></FONT></TD>
<TD valign=top><font color="800000"><B>kong</B></FONT></TD>
<TD valign=top><font color="800000">���������肵�Ȃ��H<br>dice�P�Ŋ�]�҂͂P�O�O��roll���B<br>�����l����D���ȕ����P����Ă������ɂ��܂��B<br>���ߐ؂�͍ŏI�X�����S�W���ԁB<br>�ŏI�X���͒ǉ�item�񍐂̃X�����܂݂܂��B<br><br><FONT color="FF0000"><B>[2��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B>1</B> ��U���� <B>29</B> ���o�� </FONT><small>(2001/07/10 12:36)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[879]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Infey</B></FONT></TD>
<TD valign=top><font color="0000FF">�����ċC�������������̂P<br>�`���v��<br><FONT color="FF0000"><B>[1��]</B></FONT> 0 ���� 100 �܂ł� �T�C�R��<B>1</B> ��U���� <B>88</B> ���o��<br> </FONT><small>(2001/07/10 21:16)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[889]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">Pass </FONT><small>(2001/07/12 00:13)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[902]</B></FONT></TD>
<TD valign=top><font color="800000"><B>kong</B></FONT></TD>
<TD valign=top><font color="800000">���ߐ؂�܂��B<br>infey��]item�������Ă���B </FONT><small>(2001/07/13 12:27)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[903]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Infey</B></FONT></TD>
<TD valign=top><font color="0000FF">Cloak�̕����������܂��B </FONT><small>(2001/07/13 20:28)</small></TD></TR>

</TABLE>
<form name="res_874" method="POST" action="./petit.cgi" onsubmit="return wOpen('res_874')">
<input type=hidden name=mode value=regist>
<input type=hidden name=reno value="874">
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
<input type=button value="�R�}���h�}��" onClick="inputRandom('res_874')" class="btn"><BR>
<textarea name=comment cols=56 rows=3 wrap="off"></textarea></TD>
<TD><input type=password name=pwd size=4 value="" class="txt"> PASS<BR>
<input type=submit value='�ԁ@�@�M' class="btn"></TD></TR></TABLE></CENTER></form>
</TD>
<TD width=1% rowspan=2 valign=top nowrap><B>Dice1&nbsp;0-100</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="FF0000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;88</TD><TD nowrap>&nbsp;Infey</TD></TR>
<TR><TD align=right><FONT color="FF0000"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;29</TD><TD nowrap>&nbsp;kong</TD></TR>
</TABLE></TD>
</TR></TABLE><BR>


<!------------------------------------ ---------------------------------------------->
<A name="8"></A><TABLE BORDER=1 WIDTH='95%' BGCOLOR="#FFFFFF" CELLSPACING=1 CELLPADDING=5><TR><TD bgcolor=#FFFBF0 colspan=2>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
<BIG><b>[745]�@<font color="#006400">28-29</font></b> ���e�ҁF<b>Sleip</b> ���e���F2001/06/29(Fri) 18:12 &nbsp;  </BIG></TD>
<TD align="right" nowrap><BIG><A href="#7" title="�O" style="color:black">��</A> <A href="#9" title="��" style="color:black">��</A>
 <A href="#top" title="�ŏ�" style="color:black">��</A> <A href="#btm" title="�Ō�" style="color:black">��</A></BIG></TD></TR></TABLE></TD></TR>
<TR><TD valign=top><BR><blockquote><font color="800000">1.Imbued Granite Spauldors<br>AC12 SVall10 �́@��<br>�v�����@�b�����@�o�����@�q�����@�r�g�c�@�l�����@�a�����@�r�g�l<br>�g�t�l�@�a�`�q�@�d�q�t�@�d�k�e�@�g�h�d�@�c�d�e�@�g�d�e<br><br>�Q�D�r���������������@�s��������<br>�P�R�E�Q�V�o���������������@�r�s�q�R<br>�v�����@�q�����@�a�����@�q�����@�r�g�c�@�m�����@�l�����@�d�����@�v����<br>�`����<br><br>�R�D�k�������@�d�����������������@�o������������������<br>�`�b�T�@�h�����R�@�`�c�h�W�@�g�o�P�O�@�l�������T�@�r�u�c�P�O<br>�m�����@�v�����@�l�����@�d����<br>�g�t�l�@�d�k�e�@�g�h�d�@�c�d�e�@�f�m�l�@�h�j�r<br><br>���ƂȂ񂩏E��������낵��<br>�q���������@�͂a����������������w����</font><BR></blockquote>
<hr size=1 width='95%'>
<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><font color="800000"><B>[748]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Bokuden</B></FONT></TD>
<TD valign=top><font color="800000">Sleip���񌨂�AC20�ł��ȁB<br>�������͎Q���҂Ŏg�p�\�ҍŗD��A���Ȃ��ꍇ�͎Q���҂��ĂȂ��g�p�\�҂�Slot��<br>���Ƃ̃A�C�e���͎g�p�\�җD��A���Ȃ��ꍇ��ALL Slot��<br>Slot�͊�]�A�C�e�������ɋL�ڂ���Slot�����B<br><br>�����ӁF��q���Ă���"�g�p�\��"��"�g���l"�̈Ӗ��ł��A�g�p�\�҂Ŕ��por�g���[�h�ړI�̏ꍇ�͂��̎|�K�������Ă��������B<br> </FONT><small>(2001/06/29 20:07)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF00FF"><B>[750]</B></FONT></TD>
<TD valign=top><font color="FF00FF"><B>Makos</B></FONT></TD>
<TD valign=top><font color="FF00FF">�S�DBrell's Girdle<br>slot:Waist<br>AC10 STR+10 DEX-5 STA+10 AGI+5 Mana+50<br>all/all<br><br>�T�DRuined Heretic Longsword<br>1HS 2/30 all/all<br>Caster�ł������ł��錕�ł��B<br><br>�U�DLoam encrusetd cap<br>slot:Head<br>AC4 STR+2 CHA+4 INT+5 Mana+5<br>NEC WIZ MAG ENC/HUM ERU HIE DEF GNM IKS<br><br>�V�DSpeckled Granlite Pebble<br>����Gem���s���B<br> </FONT><small>(2001/06/30 03:26)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF69B4"><B>[762]</B></FONT></TD>
<TD valign=top><font color="FF69B4"><B>asako</B></FONT></TD>
<TD valign=top><font color="FF69B4">Sleip�������Ă���R�D�̂k�������@�d�����������������@�o������������������<br>��<br>1�����Ă��܂��B�i���v�Q�ɂȂ�̂��ȁj<br><br>�W.Earthen Blade<br>2HS�@26/50�@Effect�FHaste�@wt�@8.5<br>WAR/ALL </FONT><small>(2001/06/30 20:07)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[778]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Okanoan@���W�X�g�}�j�A</B></FONT></TD>
<TD valign=top><font color="800000">6�ł��B<br><FONT color="FF8C00"><B>[1��]</B></FONT> �X���b�g<B>0</B>�� <B>979</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/07/02 02:17)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[782]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Sleip</B></FONT></TD>
<TD valign=top><font color="800000">�啨�p�ɂo�����������̕���ق��[�@�łQ<br><br><FONT color="FF8C00"><B>[7��]</B></FONT> �X���b�g<B>0</B>�� <B>629</B> ���o���� </FONT><small>(2001/07/02 05:49)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[802]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">���~���[<br><FONT color="FF8C00"><B>[9��]</B></FONT> �X���b�g<B>0</B>�� <B>014</B> ���o����<br><br><br>/slot<br>/slot<br>/slot<br>/slot </FONT><small>(2001/07/02 14:06)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[803]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">����玸��B�������Ⴂ�i��<br> </FONT><small>(2001/07/02 14:07)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF00FF"><B>[805]</B></FONT></TD>
<TD valign=top><font color="FF00FF"><B>Makos</B></FONT></TD>
<TD valign=top><font color="FF00FF">�����\�A�C�e�����E�E�E�B<br>Hole��KC�͂��т������ʌ���������Ȃ��B<br>�ǂ����ɂ���Makos�ɑ��������郂���͖����̂ŁA��ԍŌ�ɐU�낤���ȁB </FONT><small>(2001/07/02 14:12)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF0000"><B>[807]</B></FONT></TD>
<TD valign=top><font color="FF0000"><B>Deidrit</B></FONT></TD>
<TD valign=top><font color="FF0000"><FONT color="000080"><B>[2��]</B></FONT> �X���b�g<B>5</B>�� <B>061</B> ���o����<br>�������p�Ɂi�� </FONT><small>(2001/07/02 15:39)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[819]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Xneko</B></FONT></TD>
<TD valign=top><font color="800000">4��belt��<br><FONT color="FF8C00"><B>[5��]</B></FONT> �X���b�g<B>0</B>�� <B>647</B> ���o����<br> </FONT><small>(2001/07/02 20:48)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[821]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Infey</B></FONT></TD>
<TD valign=top><font color="0000FF"><FONT color="FF8C00"><B>[3��]</B></FONT> �X���b�g<B>0</B>�� <B>964</B> ���o����<br>1�E2�ŐU��t�� </FONT><small>(2001/07/02 21:07)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF0000"><B>[825]</B></FONT></TD>
<TD valign=top><font color="FF0000"><B>issue@NPC�ɐ���������j</B></FONT></TD>
<TD valign=top><font color="FF0000"><FONT color="FF8C00"><B>[2��]</B></FONT> �X���b�g<B>0</B>�� <B>933</B> ���o�����B <B>Congratulations! +100�_</B><br>���������� </FONT><small>(2001/07/03 02:13)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="000080"><B>[826]</B></FONT></TD>
<TD valign=top><font color="000080"><B>�g����������</B></FONT></TD>
<TD valign=top><font color="000080">�T�[�y���g�̉�`��<br><FONT color="FF8C00"><B>[8��]</B></FONT> �X���b�g<B>0</B>�� <B>040</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/07/03 03:42)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="000080"><B>[829]</B></FONT></TD>
<TD valign=top><font color="000080"><B>Lilit</B></FONT></TD>
<TD valign=top><font color="000080">�E�P�_���łT�Ԃ̌����i��<br><br><FONT color="000080"><B>[1��]</B></FONT> �X���b�g<B>5</B>�� <B>679</B> ���o���� </FONT><small>(2001/07/03 10:11)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF00FF"><B>[851]</B></FONT></TD>
<TD valign=top><font color="FF00FF"><B>Makos</B></FONT></TD>
<TD valign=top><font color="FF00FF">2.4�ŐU��܂�<br><FONT color="FF8C00"><B>[6��]</B></FONT> �X���b�g<B>0</B>�� <B>642</B> ���o���� </FONT><small>(2001/07/05 09:29)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[854]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">all pass </FONT><small>(2001/07/06 00:07)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[865]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Bokuden</B></FONT></TD>
<TD valign=top><font color="800000">4 Belt��<br><FONT color="FF8C00"><B>[4��]</B></FONT> �X���b�g<B>0</B>�� <B>787</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/07/07 02:44)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[872]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Bokuden</B></FONT></TD>
<TD valign=top><font color="800000">���̃X���b�h��Roll������21�����ߐ؂�ŁA�܂��U���ĂȂ��l�����瑁�߂Ƀ����B </FONT><small>(2001/07/09 03:48)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[873]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Bokuden</B></FONT></TD>
<TD valign=top><font color="800000">��������21�����჏�J���˂��[���B<br>7��10����21�����ăR�g�łЂƂB </FONT><small>(2001/07/09 03:52)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[880]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Bokuden</B></FONT></TD>
<TD valign=top><font color="800000">�V���B<br>1.Imbued Granite Spauldors�@Sleip��Issue<br>�Q�D�r���������������@�s���������@Sleip��Sleip<br>�R�D�k�������@�d�����������������@�o������������������(�݌ɂQ)�@��]�҂Ȃ�<br>�S�DBrell's Girdle�@Makos��Bokuden<br>�T�DRuined Heretic Longsword�@Makos��Lilit<br>�U�DLoam encrusetd cap�@Makos��Okanoan<br>�V�DSpeckled Granlite Pebble�@��]�҂Ȃ�<br>�W.Earthen Blade�@��]�҂Ȃ�<br><br>��]�҂Ȃ���Item�͗a�����Ă�l�����D���Ȍ`�ŏ����������ŗ~�������m������l�͑��U�ŗa�����Ă�l�ɘA������Get��(�����ҏ���)�B<br> </FONT><small>(2001/07/10 22:11)</small></TD></TR>

</TABLE>
<form name="res_745" method="POST" action="./petit.cgi" onsubmit="return wOpen('res_745')">
<input type=hidden name=mode value=regist>
<input type=hidden name=reno value="745">
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
<input type=button value="�R�}���h�}��" onClick="inputRandom('res_745')" class="btn"><BR>
<textarea name=comment cols=56 rows=3 wrap="off"></textarea></TD>
<TD><input type=password name=pwd size=4 value="" class="txt"> PASS<BR>
<input type=submit value='�ԁ@�@�M' class="btn"></TD></TR></TABLE></CENTER></form>
</TD>
<TD width=1% rowspan=2 valign=top nowrap><B>Slot0</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="FF8C00"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;1079</TD><TD nowrap>&nbsp;Okanoan@���W�X�g�}�j�A</TD></TR>
<TR><TD align=right><FONT color="FF8C00"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;1033</TD><TD nowrap>&nbsp;issue@NPC�ɐ���������j</TD></TR>
<TR><TD align=right><FONT color="FF8C00"><B>3</B></FONT></TD><TD nowrap align=right>&nbsp;964</TD><TD nowrap>&nbsp;Infey</TD></TR>
<TR><TD align=right><FONT color="FF8C00"><B>4</B></FONT></TD><TD nowrap align=right>&nbsp;887</TD><TD nowrap>&nbsp;Bokuden</TD></TR>
<TR><TD align=right><FONT color="FF8C00"><B>5</B></FONT></TD><TD nowrap align=right>&nbsp;647</TD><TD nowrap>&nbsp;Xneko</TD></TR>
<TR><TD align=right><FONT color="FF8C00"><B>6</B></FONT></TD><TD nowrap align=right>&nbsp;642</TD><TD nowrap>&nbsp;Makos</TD></TR>
<TR><TD align=right><FONT color="FF8C00"><B>7</B></FONT></TD><TD nowrap align=right>&nbsp;629</TD><TD nowrap>&nbsp;Sleip</TD></TR>
<TR><TD align=right><FONT color="FF8C00"><B>8</B></FONT></TD><TD nowrap align=right>&nbsp;140</TD><TD nowrap>&nbsp;�g����������</TD></TR>
<TR><TD align=right><FONT color="FF8C00"><B>9</B></FONT></TD><TD nowrap align=right>&nbsp;14</TD><TD nowrap>&nbsp;Shizuho</TD></TR>
</TABLE><BR>
<B>Slot5</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="000080"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;679</TD><TD nowrap>&nbsp;Lilit</TD></TR>
<TR><TD align=right><FONT color="000080"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;61</TD><TD nowrap>&nbsp;Deidrit</TD></TR>
</TABLE></TD>
</TR></TABLE><BR>


<!------------------------------------ ---------------------------------------------->
<A name="9"></A><TABLE BORDER=1 WIDTH='95%' BGCOLOR="#FFFFFF" CELLSPACING=1 CELLPADDING=5><TR><TD bgcolor=#FFFBF0 colspan=2>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
<BIG><b>[679]�@<font color="#006400">Siren�ɂ�</font></b> ���e�ҁF<b>Shizuho</b> ���e���F2001/06/22(Fri) 15:23 &nbsp;  </BIG></TD>
<TD align="right" nowrap><BIG><A href="#8" title="�O" style="color:black">��</A> <A href="#10" title="��" style="color:black">��</A>
 <A href="#top" title="�ŏ�" style="color:black">��</A> <A href="#btm" title="�Ō�" style="color:black">��</A></BIG></TD></TR></TABLE></TD></TR>
<TR><TD valign=top><BR><blockquote><font color="0000FF">�����Siren�ł���Ȃ�o�Ă܂����B<br><br>Netted Kelp Sash<br>Races: ALL - Classes: ALL (LORE - MAGIC)<br>Stats: AC: 5 - Wt: 0.2 - Slot: waist<br>Attributes: STR+6 STA+3 CHA-2 INT+5 SV FIRE+8 <br><br>All Roll �ł��傤���ˁB<br></font><BR></blockquote>
<hr size=1 width='95%'>
<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><font color="800000"><B>[686]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">Seahorse Spine Bracelet<br>MAGIC LORE<br>WRIST<br>AC8<br>STR+5 CHA+10 AGI+5<br>WT0.5<br>Size TINY<br>Class WAR CLR PAL RNG SHD DRU MNK BRD ROG SHM<br>Race ALL<br><br>������o�Ă܂��B�񍐒x��ăX�~�}�Z�� (&gt;&lt;<br><br>Loot�i�͈ȏ�ł����ˁH </FONT><small>(2001/06/23 15:27)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[690]</B></FONT></TD>
<TD valign=top><font color="800080"><B>BIS@WayStation.GM</B></FONT></TD>
<TD valign=top><font color="800080">������������Ȃ����AllSlot��(w<br>�ǂ�����D�悷�邩�����Ƃ��Ă��������B<br>LastSlot����48h���ߐ؂� </FONT><small>(2001/06/23 17:34)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[695]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">Seahorse Spine Bracelet<br>Netted Kelp Sash<br>�̏���<br><br><FONT color="808000"><B>[3��]</B></FONT> �X���b�g<B>0</B>�� <B>675</B> ���o����<br> </FONT><small>(2001/06/24 20:10)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="000080"><B>[697]</B></FONT></TD>
<TD valign=top><font color="000080"><B>�g����������</B></FONT></TD>
<TD valign=top><font color="000080"><FONT color="808000"><B>[5��]</B></FONT> �X���b�g<B>0</B>�� <B>507</B> ���o����<br>��������_���_���ȉ^�E�E<br>�Ƃ肠�����ӂ��Ƃ� </FONT><small>(2001/06/24 21:03)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[698]</B></FONT></TD>
<TD valign=top><font color="800080"><B>Venio</B></FONT></TD>
<TD valign=top><font color="800080">Bracelet�Ńt���t��<br><br><FONT color="808000"><B>[2��]</B></FONT> �X���b�g<B>0</B>�� <B>929</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/06/24 22:24)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[699]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">�����Ƃ��Ď����ŐU��̖Y��Ă���i��<br>Sv���Ă邩��Sash�D��ŁB<br><br><FONT color="808000"><B>[1��]</B></FONT> �X���b�g<B>0</B>�� <B>939</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/06/24 22:40)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[700]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Okanoan@���W�X�g�}�j�A</B></FONT></TD>
<TD valign=top><font color="800000">����camp���ă]�[���ۂŎ��ɂ܂�����camp�������H </FONT><small>(2001/06/25 04:24)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[701]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">Zone�ۂɌ��炸�A�s���ƕK������ł܂��B�܂��Q��ł�������<br> </FONT><small>(2001/06/25 06:31)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[703]</B></FONT></TD>
<TD valign=top><font color="800080"><B>BIS</B></FONT></TD>
<TD valign=top><font color="800080">�������֐i��ŁAInvs�Ő��H��n���ăg�h�Ə������悤�Ƃ�����<br>�o���Ă������g�h��Add���ėF�B�Ă�ł��đS�ł����Ƃ��̂ł�(w<br>���̂Ƃ���Zone�ۂ�Invs�Ńp�X���܂����� </FONT><small>(2001/06/25 17:34)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[707]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">�Q��Q�����Ăǂ�����g�h����ɂ��Ĕ��󁨂r�b�ł��ˁB<br>���̃g�h��ł����܂��傤�B<br>���Ȃ݂�drop����hide��Shawl 7th�Ŏg�p���܂���(�ււ�<br> </FONT><small>(2001/06/26 03:04)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[711]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Okanoan@���W�X�g�}�j�A</B></FONT></TD>
<TD valign=top><font color="800000">������|������ sash de!<br><FONT color="808000"><B>[4��]</B></FONT> �X���b�g<B>0</B>�� <B>554</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/06/26 07:37)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="008000"><B>[716]</B></FONT></TD>
<TD valign=top><font color="008000"><B>Keropyon</B></FONT></TD>
<TD valign=top><font color="008000">���x�������Ƃ��́Aall kill �� &gt;&lt;/ <br> </FONT><small>(2001/06/26 12:44)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[876]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus_CLR</B></FONT></TD>
<TD valign=top><font color="800000">���܂����[�[�[�[<br>�G���N�Y���肷���Ă邶���A����I�I�I<br><br>Netted Kelp Sash �� Shizuho<br>Seahorse Spine Bracelet �� Venio<br>�͂����� Veni����E�E�E���_�͉��Ȃ񂾂��(T-T<br> </FONT><small>(2001/07/10 02:39)</small></TD></TR>

</TABLE>
<form name="res_679" method="POST" action="./petit.cgi" onsubmit="return wOpen('res_679')">
<input type=hidden name=mode value=regist>
<input type=hidden name=reno value="679">
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
<input type=button value="�R�}���h�}��" onClick="inputRandom('res_679')" class="btn"><BR>
<textarea name=comment cols=56 rows=3 wrap="off"></textarea></TD>
<TD><input type=password name=pwd size=4 value="" class="txt"> PASS<BR>
<input type=submit value='�ԁ@�@�M' class="btn"></TD></TR></TABLE></CENTER></form>
</TD>
<TD width=1% rowspan=2 valign=top nowrap><B>Slot0</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="808000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;1039</TD><TD nowrap>&nbsp;Shizuho</TD></TR>
<TR><TD align=right><FONT color="808000"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;1029</TD><TD nowrap>&nbsp;Venio</TD></TR>
<TR><TD align=right><FONT color="808000"><B>3</B></FONT></TD><TD nowrap align=right>&nbsp;675</TD><TD nowrap>&nbsp;Gafus</TD></TR>
<TR><TD align=right><FONT color="808000"><B>4</B></FONT></TD><TD nowrap align=right>&nbsp;654</TD><TD nowrap>&nbsp;Okanoan@���W�X�g�}�j�A</TD></TR>
<TR><TD align=right><FONT color="808000"><B>5</B></FONT></TD><TD nowrap align=right>&nbsp;507</TD><TD nowrap>&nbsp;�g����������</TD></TR>
</TABLE></TD>
</TR></TABLE><BR>


<!------------------------------------ ---------------------------------------------->
<A name="10"></A><TABLE BORDER=1 WIDTH='95%' BGCOLOR="#FFFFFF" CELLSPACING=1 CELLPADDING=5><TR><TD bgcolor=#FFFBF0 colspan=2>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
<BIG><b>[764]�@<font color="#006400">6/30�� - 7/1�� in Kael</font></b> ���e�ҁF<b>Gafus</b> ���e���F2001/07/01(Sun) 05:47 &nbsp;  </BIG></TD>
<TD align="right" nowrap><BIG><A href="#9" title="�O" style="color:black">��</A> <A href="#11" title="��" style="color:black">��</A>
 <A href="#top" title="�ŏ�" style="color:black">��</A> <A href="#btm" title="�Ō�" style="color:black">��</A></BIG></TD></TR></TABLE></TD></TR>
<TR><TD valign=top><BR><blockquote><font color="800000">1.Diamond<br><br>2.Thunder Runed War Spear<br>MAGIC LORE<br>RANGE PRIMARY<br>Piercing<br>Delay30 DMG13<br>AC5<br>HP+25 SVM+5<br>WT9.0<br>Size MIDIUM<br>Class WAR RNG SHD BRD ROG SHM<br>Race ALL<br><br>�ǋL<br>GWH x3<br>Toe x2<br>�ۊǒ��ɕ��ɒǉ��ŕۊǂ��Ă����܂��B<br></font><BR></blockquote>
<hr size=1 width='95%'>
<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><font color="FF69B4"><B>[768]</B></FONT></TD>
<TD valign=top><font color="FF69B4"><B>asako</B></FONT></TD>
<TD valign=top><font color="FF69B4">1.Diamond<br><br>����1��Loot���Ă܂��̂ō��v2�ł��ˁ@�F�j </FONT><small>(2001/07/01 07:37)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[771]</B></FONT></TD>
<TD valign=top><font color="800000"><B>neath</B></FONT></TD>
<TD valign=top><font color="800000">3.  GIANT SCALEMAIL CLOAK <br>Classes:  All Classes<br>Races:  Humans, Erudites, Dark Elfs, High Elfs, Wood Elfs, Half Elfs, Trolls, Ogres, Barbarians, Iksar<br>Stats:  7 AC +10 MANA +30 HP +5 STA<br>Special Attributes:  MAGIC<br>Slot(s):  Back<br>Weight:  5 Stone<br><br>4.  GIANT SCALEMAIL MANTLE<br>Classes:  All Classes<br>Races:  Humans, Erudites, Dark Elfs, High Elfs, Wood Elfs, Half Elfs, Trolls, Ogres, Barbarians, Iksar<br>Stats:  6 AC +10 MANA +10 HP +2 DEX +2 SV COLD +2 SV DISEASE +2 SV FIRE +2 SV MAGIC +2 SV POISON<br>Special Attributes:  MAGIC<br>Slot(s):  Shoulder Slot<br>Weight:  4.4 Stone<br><br>5. GIANT SCALEMAIL LEGGINGS <br>Classes:  All Classes<br>Races:  Humans, Erudites, Dark Elfs, High Elfs, Wood Elfs, Half Elfs, Trolls, Ogres, Barbarians, Iksar<br>Stats:  11 AC +20 HP +3 INT -3 WIS<br>Special Attributes:  MAGIC, NO DROP<br>Slot(s):  Leg Slot<br>Weight:  11 Stone<br> </FONT><small>(2001/07/01 13:05)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[772]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">6. Giant Scalemail Helm<br>AC:8 Slot:Head Wt:5.6<br>Dex+5 HP+10 MANA+10<br>Class:WAR ROG BRD SHD PAL CLR SHM RNG <br>Races:HUM HEF HIE ELF ERU BAR DEF TRL IKS OGR <br>����Q����܂��B<br><br>7.White Bear Pelt Cloak<br>AC:11 Wt:0 Slot:Back<br>STR+5 WIS+5 HP+75 MANA+50 SvM+3<br>Class:PAL<br>Races:All<br>���Ȃ�ǂ�Stats�ł������I�Ǝv��������PAL only�œf�������A�C�e���B<br>���߂�PAL�������Ome!��������ł����B<br>ALL Roll�Ŗ�����l��2nd�ɓn������A�]�������肷��ܑ͖̖̂�����i���Ǝv���̂ł����B<br>�ꏏ�ɍs���Ȃ������Ƃ͂����AMaru�����Flow����ɂ����Ă��������Ȃ��Ɓi�l�I�ӌ��j<br>����Ƃ��A������̃��m�ł͂Ȃ���ł��傤���H���f���܂��ʁB<br><br> </FONT><small>(2001/07/01 14:12)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[773]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Sleip</B></FONT></TD>
<TD valign=top><font color="800000">�o�����b���������͉��x���o�Ă�̂ő����l���������e����������������Ă�͂��ł� </FONT><small>(2001/07/01 19:15)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF0000"><B>[792]</B></FONT></TD>
<TD valign=top><font color="FF0000"><B>Deidrit</B></FONT></TD>
<TD valign=top><font color="FF0000">�Q����slot�Ł@���ߐ؂�ŏI���48h </FONT><small>(2001/07/02 09:04)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[796]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Cammy</B></FONT></TD>
<TD valign=top><font color="0000FF">����o���Ƃ������������ǁA���߂�CLR������OK�ɂ��ė~������ˁB<br>�������[7�ŐU���Ƃ����ǁAPal�̐l�ŗv��̂Ȃ�A���ނ��Ă��ƂŁB<br>���̏ꍇ�́A���̔ԍ���1.Dia�ɓK�pPlz�B�U��Ȃ��������h������(w<br><br><FONT color="FF0000"><B>[1��]</B></FONT> �X���b�g<B>7</B>�� <B>877</B> ���o�����B <B>Congratulations! +100�_</B> </FONT><small>(2001/07/02 13:00)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[797]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Cammy</B></FONT></TD>
<TD valign=top><font color="0000FF">Yami����ɁA�Ȃ񂩌���ꂻ���ȗ\��Soon�c </FONT><small>(2001/07/02 13:01)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[801]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Shibaraku</B></FONT></TD>
<TD valign=top><font color="800000"><FONT color="000000"><B>[2��]</B></FONT> �X���b�g<B>1</B>�� <B>989</B> ���o�����B <B>Congratulations! +100�_</B><br>SV up &gt;&lt; </FONT><small>(2001/07/02 13:44)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[804]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Shizuho</B></FONT></TD>
<TD valign=top><font color="0000FF">��̔@���_�C���[�B<br><br><FONT color="FF00FF"><B>[2��]</B></FONT> �X���b�g<B>0</B>�� <B>527</B> ���o���� </FONT><small>(2001/07/02 14:08)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="FF0000"><B>[806]</B></FONT></TD>
<TD valign=top><font color="FF0000"><B>Deidrit</B></FONT></TD>
<TD valign=top><font color="FF0000"><FONT color="000000"><B>[3��]</B></FONT> �X���b�g<B>1</B>�� <B>805</B> ���o���� </FONT><small>(2001/07/02 15:37)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[808]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Xneko</B></FONT></TD>
<TD valign=top><font color="800000">���ɗǂ�����ł��Ȃ������Ȃ��<br>�}����AC UP�p�ɁB2�ŁB<br><FONT color="800000"><B>[2��]</B></FONT> �X���b�g<B>2</B>�� <B>180</B> ���o���� </FONT><small>(2001/07/02 17:43)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[809]</B></FONT></TD>
<TD valign=top><font color="800080"><B>Neath</B></FONT></TD>
<TD valign=top><font color="800080">1�΂�B<br><br><FONT color="FF00FF"><B>[3��]</B></FONT> �X���b�g<B>0</B>�� <B>439</B> ���o���� </FONT><small>(2001/07/02 19:05)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800080"><B>[810]</B></FONT></TD>
<TD valign=top><font color="800080"><B>Neath</B></FONT></TD>
<TD valign=top><font color="800080">�Ȃ�΁[�킷��@TT </FONT><small>(2001/07/02 19:06)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="000000"><B>[813]</B></FONT></TD>
<TD valign=top><font color="000000"><B>issue@NPC�ɐ���������j</B></FONT></TD>
<TD valign=top><font color="000000">�ɂ�� </FONT><small>(2001/07/02 20:33)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="000000"><B>[814]</B></FONT></TD>
<TD valign=top><font color="000000"><B>issue@NPC�ɐ���������j</B></FONT></TD>
<TD valign=top><font color="000000"><FONT color="000000"><B>[5��]</B></FONT> �X���b�g<B>1</B>�� <B>209</B> ���o����<br> </FONT><small>(2001/07/02 20:34)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="0000FF"><B>[820]</B></FONT></TD>
<TD valign=top><font color="0000FF"><B>Infey</B></FONT></TD>
<TD valign=top><font color="0000FF">Neko�ɂ͏��I������I<br><FONT color="800000"><B>[1��]</B></FONT> �X���b�g<B>2</B>�� <B>793</B> ���o���� </FONT><small>(2001/07/02 20:58)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[824]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus</B></FONT></TD>
<TD valign=top><font color="800000">give me diamond!!<br><br><FONT color="000000"><B>[6��]</B></FONT> �X���b�g<B>1</B>�� <B>038</B> ���o����<br><br>�_�C����No1����ˁE�E�E�H </FONT><small>(2001/07/03 00:14)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="000080"><B>[831]</B></FONT></TD>
<TD valign=top><font color="000080"><B>Lilit</B></FONT></TD>
<TD valign=top><font color="000080">����ς�Diamond�ł����ɂ�`�H </FONT><small>(2001/07/03 12:34)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="000080"><B>[832]</B></FONT></TD>
<TD valign=top><font color="000080"><B>Lilit</B></FONT></TD>
<TD valign=top><font color="000080">�͂��I�U��Y��(T-T)<br><FONT color="000000"><B>[1��]</B></FONT> �X���b�g<B>1</B>�� <B>333</B> ���o�����B <B>Congratulations! +1000�_</B><br> </FONT><small>(2001/07/03 12:35)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="000080"><B>[833]</B></FONT></TD>
<TD valign=top><font color="000080"><B>Lilit</B></FONT></TD>
<TD valign=top><font color="000080">��[���i�� </FONT><small>(2001/07/03 12:35)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[835]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Sleip</B></FONT></TD>
<TD valign=top><font color="800000">���낻��U�낤<br>�c�����I<br><br><FONT color="000000"><B>[4��]</B></FONT> �X���b�g<B>1</B>�� <B>319</B> ���o���� </FONT><small>(2001/07/03 17:32)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[846]</B></FONT></TD>
<TD valign=top><font color="800000"><B>sesu</B></FONT></TD>
<TD valign=top><font color="800000">���ꂢ����ˁH��<br>���Ȃ�������p����<br><FONT color="FF00FF"><B>[1��]</B></FONT> �X���b�g<B>0</B>�� <B>608</B> ���o���� </FONT><small>(2001/07/04 13:21)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[847]</B></FONT></TD>
<TD valign=top><font color="800000"><B>sesu</B></FONT></TD>
<TD valign=top><font color="800000">���P�̂���������ǂ� </FONT><small>(2001/07/04 13:22)</small></TD></TR>

<TR><TD align=right valign=top nowrap><font color="800000"><B>[871]</B></FONT></TD>
<TD valign=top><font color="800000"><B>Gafus_CLR</B></FONT></TD>
<TD valign=top><font color="800000">�Y�܂��B<br>Diamond �� Lilit�AShibaraku<br>Thunder Runed War Spear �� Infey<br>White Bear Pelt Cloak �� Cammy<br>�ȏ�Ŋm��ł��Agratz!!<br><br> </FONT><small>(2001/07/08 18:25)</small></TD></TR>

</TABLE>
<form name="res_764" method="POST" action="./petit.cgi" onsubmit="return wOpen('res_764')">
<input type=hidden name=mode value=regist>
<input type=hidden name=reno value="764">
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
<input type=button value="�R�}���h�}��" onClick="inputRandom('res_764')" class="btn"><BR>
<textarea name=comment cols=56 rows=3 wrap="off"></textarea></TD>
<TD><input type=password name=pwd size=4 value="" class="txt"> PASS<BR>
<input type=submit value='�ԁ@�@�M' class="btn"></TD></TR></TABLE></CENTER></form>
</TD>
<TD width=1% rowspan=2 valign=top nowrap><B>Slot0</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="FF00FF"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;608</TD><TD nowrap>&nbsp;sesu</TD></TR>
<TR><TD align=right><FONT color="FF00FF"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;527</TD><TD nowrap>&nbsp;Shizuho</TD></TR>
<TR><TD align=right><FONT color="FF00FF"><B>3</B></FONT></TD><TD nowrap align=right>&nbsp;439</TD><TD nowrap>&nbsp;Neath</TD></TR>
</TABLE><BR>
<B>Slot1</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="000000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;1333</TD><TD nowrap>&nbsp;Lilit</TD></TR>
<TR><TD align=right><FONT color="000000"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;1089</TD><TD nowrap>&nbsp;Shibaraku</TD></TR>
<TR><TD align=right><FONT color="000000"><B>3</B></FONT></TD><TD nowrap align=right>&nbsp;805</TD><TD nowrap>&nbsp;Deidrit</TD></TR>
<TR><TD align=right><FONT color="000000"><B>4</B></FONT></TD><TD nowrap align=right>&nbsp;319</TD><TD nowrap>&nbsp;Sleip</TD></TR>
<TR><TD align=right><FONT color="000000"><B>5</B></FONT></TD><TD nowrap align=right>&nbsp;209</TD><TD nowrap>&nbsp;issue@NPC�ɐ���������j</TD></TR>
<TR><TD align=right><FONT color="000000"><B>6</B></FONT></TD><TD nowrap align=right>&nbsp;38</TD><TD nowrap>&nbsp;Gafus</TD></TR>
</TABLE><BR>
<B>Slot2</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="800000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;793</TD><TD nowrap>&nbsp;Infey</TD></TR>
<TR><TD align=right><FONT color="800000"><B>2</B></FONT></TD><TD nowrap align=right>&nbsp;180</TD><TD nowrap>&nbsp;Xneko</TD></TR>
</TABLE><BR>
<B>Slot7</B><BR><TABLE border=0 cellspacing=0 cellpadding=0>
<TR><TD align=right><FONT color="FF0000"><B>1</B></FONT></TD><TD nowrap align=right>&nbsp;977</TD><TD nowrap>&nbsp;Cammy</TD></TR>
</TABLE></TD>
</TR></TABLE><BR>
<blockquote><table align=left cellpadding=0 cellspacing=0><tr>
<form action="./petit.cgi" method="POST"><td>
<input type=hidden name=page value="10">
&nbsp;<input type=submit value="����10��">
</td></form>
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
