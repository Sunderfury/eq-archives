<HTML>
<HEAD>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=euc-jp">
<TITLE>EverGreen GEM BANK</TITLE>
<STYLE type="text/css">
<!--
TD A,TH A {
	text-decoration:none;
}
A:hover {
	color:#FF3366;
}
INPUT.btn {
	background-color:#FFFFCC;
	color:#000000;
}
TD,TH {
	font-size:10pt;
}
INPUT.gem {
	text-align:center;
	height:13pt;
	font-size:10pt;
}
-->
</STYLE>
</HEAD>
<BODY BGCOLOR=#FFFFFF TEXT=#000000 LINK=#000000 VLINK=#000000 ALINK=#FF3366>
<SCRIPT language="JavaScript">
<!--
function check1(fm) {
	if (fm.pass.value == "") {
		alert("�ѥ���ɤ����Ϥ��Ƥ���������");
		return false;
	}
	for (i=0; i<27; i++) {
		if (i == 27-1) {
			if (fm.elements["way"+i].value.match(/^([0-9]{1,3}|[Dd])$/) == null) {
				alert("���顼�����Ϥ�����å����Ƥ�������");
				return false;
			}
		} else {
			if (fm.elements["way"+i].value.match(/^[0-9]{1,3}$/) == null) {
				alert("���顼�����Ϥ�����å����Ƥ�������");
				return false;
			}
		}
	}
	return true;
}
// -->
</SCRIPT>

<TABLE width=100%><TR>
<TD width=30%></TD>
<TH nowrap align=center width=40%><FONT style="font-size:20pt;color:#FF3366">EverGreen GEM BANK</FONT></TH>
<TD nowrap width=30% align=right>[<a href="http://www.everquest.jp/guild/index.php" target='_top'>�ȥåפ����</a>]
[<a href="gem.cgi?cmd=howto">�Ȥ���</a>]
[<a href="gem.cgi?cmd=data">Base Armor</a>]</TD>
</TR></TABLE>


<FORM method="POST" action="gem.cgi" onsubmit="return check1(this)" style="page-break-before:always;page-break-after:always">
<INPUT type="hidden" name="cmd" value="gemRegist">

<TABLE border="1" cellpadding="1" cellspacing="0" align="center">
<TR align="center" bgcolor="#FFFFCC">
<TH>GEM̾</TH>
<TH>��</TH>
<TH><A href="gem.cgi?cmd=vewitem&class=WAR&slot=ALL">WAR</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=PAL&slot=ALL">PAL</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=SHD&slot=ALL">SHD</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=RNG&slot=ALL">RNG</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=MNK&slot=ALL">MNK</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=ROG&slot=ALL">ROG</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=BRD&slot=ALL">BRD</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=CLR&slot=ALL">CLR</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=DRU&slot=ALL">DRU</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=SHM&slot=ALL">SHM</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=ENC&slot=ALL">ENC</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=MAG&slot=ALL">MAG</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=NEC&slot=ALL">NEC</A></TH>
<TH><A href="gem.cgi?cmd=vewitem&class=WIZ&slot=ALL">WIZ</A></TH>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Black Marble</TD>
<TD><input type="text" size="3" class="gem" name="way0" value="10" onFocus="this.select()" tabindex="1"></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=CLR&slot=Chest">Chest</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=DRU&slot=Chest">Chest</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHM&slot=Chest">Chest</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Chipped Onyx Sapphire</TD>
<TD><input type="text" size="3" class="gem" name="way1" value="13" onFocus="this.select()" tabindex="2"></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=CLR&slot=Legs">Legs</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=DRU&slot=Legs">Legs</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHM&slot=Legs">Legs</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Black Marble</TD>
<TD><input type="text" size="3" class="gem" name="way2" value="9" onFocus="this.select()" tabindex="3"></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WAR&slot=Feet">Feet</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=PAL&slot=Feet">Feet</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHD&slot=Feet">Feet</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=RNG&slot=Feet">Feet</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MNK&slot=Feet">Feet</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ROG&slot=Feet">Feet</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=BRD&slot=Feet">Feet</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Coral</TD>
<TD><input type="text" size="3" class="gem" name="way3" value="12" onFocus="this.select()" tabindex="4"></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WAR&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=PAL&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHD&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=RNG&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MNK&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ROG&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=BRD&slot=Head">Head</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Flame Emerald</TD>
<TD><input type="text" size="3" class="gem" name="way4" value="16" onFocus="this.select()" tabindex="5"></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WAR&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=PAL&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHD&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=RNG&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MNK&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ROG&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=BRD&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=CLR&slot=Feet">Feet</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=DRU&slot=Feet">Feet</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHM&slot=Feet">Feet</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Flame Opal</TD>
<TD><input type="text" size="3" class="gem" name="way5" value="8" onFocus="this.select()" tabindex="6"></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ENC&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MAG&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=NEC&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WIZ&slot=Head">Head</A></TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Jaundice</TD>
<TD><input type="text" size="3" class="gem" name="way6" value="19" onFocus="this.select()" tabindex="7"></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ENC&slot=Feet">Feet</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MAG&slot=Feet">Feet</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=NEC&slot=Feet">Feet</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WIZ&slot=Feet">Feet</A></TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Lava Ruby</TD>
<TD><input type="text" size="3" class="gem" name="way7" value="24" onFocus="this.select()" tabindex="8"></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=CLR&slot=Hands">Hands</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=DRU&slot=Hands">Hands</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHM&slot=Hands">Hands</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Onyx Sapphire</TD>
<TD><input type="text" size="3" class="gem" name="way8" value="2" onFocus="this.select()" tabindex="9"></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=CLR&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=DRU&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHM&slot=Head">Head</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ENC&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MAG&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=NEC&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WIZ&slot=Wrist">Wrist</A></TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Opal</TD>
<TD><input type="text" size="3" class="gem" name="way9" value="11" onFocus="this.select()" tabindex="10"></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=CLR&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=DRU&slot=Wrist">Wrist</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHM&slot=Wrist">Wrist</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Topaz</TD>
<TD><input type="text" size="3" class="gem" name="way10" value="15" onFocus="this.select()" tabindex="11"></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WAR&slot=Hands">Hands</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=PAL&slot=Hands">Hands</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHD&slot=Hands">Hands</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=RNG&slot=Hands">Hands</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MNK&slot=Hands">Hands</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ROG&slot=Hands">Hands</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=BRD&slot=Hands">Hands</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ENC&slot=Hands">Hands</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MAG&slot=Hands">Hands</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=NEC&slot=Hands">Hands</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WIZ&slot=Hands">Hands</A></TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Flawed Emerald</TD>
<TD><input type="text" size="3" class="gem" name="way11" value="11" onFocus="this.select()" tabindex="12"></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WAR&slot=Arms">Arms</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=PAL&slot=Arms">Arms</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHD&slot=Arms">Arms</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=RNG&slot=Arms">Arms</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MNK&slot=Arms">Arms</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ROG&slot=Arms">Arms</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=BRD&slot=Arms">Arms</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Flawed Sea Sapphire</TD>
<TD><input type="text" size="3" class="gem" name="way12" value="11" onFocus="this.select()" tabindex="13"></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WAR&slot=Legs">Legs</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=PAL&slot=Legs">Legs</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHD&slot=Legs">Legs</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=RNG&slot=Legs">Legs</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MNK&slot=Legs">Legs</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ROG&slot=Legs">Legs</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=BRD&slot=Legs">Legs</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Flawed Topaz</TD>
<TD><input type="text" size="3" class="gem" name="way13" value="9" onFocus="this.select()" tabindex="14"></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ENC&slot=Arms">Arms</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MAG&slot=Arms">Arms</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=NEC&slot=Arms">Arms</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WIZ&slot=Arms">Arms</A></TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Flawless Diamond</TD>
<TD><input type="text" size="3" class="gem" name="way14" value="17" onFocus="this.select()" tabindex="15"></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WAR&slot=Chest">Chest</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=PAL&slot=Chest">Chest</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHD&slot=Chest">Chest</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=RNG&slot=Chest">Chest</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MNK&slot=Chest">Chest</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ROG&slot=Chest">Chest</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=BRD&slot=Chest">Chest</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Jaundice Gem</TD>
<TD><input type="text" size="3" class="gem" name="way15" value="10" onFocus="this.select()" tabindex="16"></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=CLR&slot=Arms">Arms</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=DRU&slot=Arms">Arms</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=SHM&slot=Arms">Arms</A></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Nephrite</TD>
<TD><input type="text" size="3" class="gem" name="way16" value="12" onFocus="this.select()" tabindex="17"></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ENC&slot=Legs">Legs</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MAG&slot=Legs">Legs</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=NEC&slot=Legs">Legs</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WIZ&slot=Legs">Legs</A></TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Pristine Emerald</TD>
<TD><input type="text" size="3" class="gem" name="way17" value="10" onFocus="this.select()" tabindex="18"></TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD>&nbsp;</TD>
<TD><A href="gem.cgi?cmd=vewitem&class=ENC&slot=Chest">Chest</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=MAG&slot=Chest">Chest</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=NEC&slot=Chest">Chest</A></TD>
<TD><A href="gem.cgi?cmd=vewitem&class=WIZ&slot=Chest">Chest</A></TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Chipped Black Marble</TD>
<TD><input type="text" size="3" class="gem" name="way18" value="0" onFocus="this.select()"></TD>
<TD colspan="14">��������</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Chrysolite</TD>
<TD><input type="text" size="3" class="gem" name="way19" value="0" onFocus="this.select()"></TD>
<TD colspan="14">��������</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Emerald</TD>
<TD><input type="text" size="3" class="gem" name="way20" value="0" onFocus="this.select()"></TD>
<TD colspan="14">��������</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Nephirite</TD>
<TD><input type="text" size="3" class="gem" name="way21" value="0" onFocus="this.select()"></TD>
<TD colspan="14">��������</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Crushed Sea Sapphire</TD>
<TD><input type="text" size="3" class="gem" name="way22" value="0" onFocus="this.select()"></TD>
<TD colspan="14">��������</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Flawless Aquamarine</TD>
<TD><input type="text" size="3" class="gem" name="way23" value="0" onFocus="this.select()"></TD>
<TD colspan="14">��������</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Flawed Opal</TD>
<TD><input type="text" size="3" class="gem" name="way24" value="0" onFocus="this.select()"></TD>
<TD colspan="14">��������</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Flawed Flame Opal</TD>
<TD><input type="text" size="3" class="gem" name="way25" value="0" onFocus="this.select()"></TD>
<TD colspan="14">��������</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC">Flawed Lava Ruby</TD>
<TD><input type="text" size="3" class="gem" name="way26" value="0" onFocus="this.select()"></TD>
<TD colspan="14">��������</TD>
</TR>
<TR align="center">
<TD align="left" bgcolor="#FFFFCC"><INPUT size="20" type="text" name="addgem"></TD>
<TD><input type="text" size="3" class="gem" name="way27" value="" onFocus="this.select()"></TD>
<TD colspan="14">���ιԤ���������GEM���ɲä���������Ϥ��Ƥ���������</TD>
</TR>
<TR align="center">
<TD colspan="18">�ѥ���� <INPUT size="10" type="password" name="pass"> <INPUT class="btn" type="submit" value="�ѡ���"></TD>
</TR>
</Table>

</FORM>
<DIV align=center style="font-size:10pt">
<FORM method="POST" action="gem.cgi">
<INPUT type="hidden" name="cmd" value="inputComment">
<INPUT type=submit class=btn value="��������Ͽ">
</FORM>
</DIV>
<TABLE BORDER=1 CELLSPACING=0 CELLPADDING=5 width=85% align=center>
<TR><TD bgcolor=#FFFFCC>[6] �� <B><A href="mailto:gambar@everquest.jp">Gambar</A></B> �� <SMALL>2002/10/06 10:29:15</SMALL> </TD></TR>
<TR><TD>Makitan���󡢤�ä�Passľ���ޤ���(^_^;</TD></TR>
<TR><TD bgcolor=#FFFFCC>[5] �� <B>Maki</B> �� <SMALL>2002/09/23 14:21:53</SMALL> </TD></TR>
<TR><TD>�Ȥ����ĤĹ�����</TD></TR>
<TR><TD bgcolor=#FFFFCC>[4] �� <B>Maki</B> �� <SMALL>2002/09/23 14:13:19</SMALL> </TD></TR>
<TR><TD>�Ǥ��ʤ���</TD></TR>
<TR><TD bgcolor=#FFFFCC>[3] �� <B>Maki</B> �� <SMALL>2002/09/23 14:12:44</SMALL> </TD></TR>
<TR><TD>������</TD></TR>
<TR><TD bgcolor=#FFFFCC>[2] �� <B>sizimi</B> �� <SMALL>2001/11/25 18:19:42</SMALL> </TD></TR>
<TR><TD>NEWGEM���٤��ޤ�������</TD></TR>
<TR><TD bgcolor=#FFFFCC>[1] �� <B>Sizimi</B> �� <SMALL>2001/11/21 16:03:26</SMALL> </TD></TR>
<TR><TD>�������ޤ�������</TD></TR>
</TABLE>
<TABLE border=0 align=center><TR>
</TR></TABLE>
<HR WIDTH=95%>
<CENTER><A class=menu HREF="http://www.suisen.sakura.ne.jp/~ikitai/cgi/gem.html" TARGET="_blank">GEM BANK</A> v1.32 - Script written by <A class=menu HREF="mailto:ito@e-mail.ne.jp">Hisa</A></CENTER>
</BODY>
</HTML>
