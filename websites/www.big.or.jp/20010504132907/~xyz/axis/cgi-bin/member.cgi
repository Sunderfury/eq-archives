<html>
<head>
<title>MemberList</title>
<meta http-equiv="Content-Type" content="text/html; charset=x-sjis">
<style type="text/css">
<!--
a {  color: #006600; text-decoration: none}
a:hover {  color: #0099FF; text-decoration: underline}
a:active {  color: #0099FF; text-decoration: underline}
-->
</style></head>

<SCRIPT language="JavaScript">
<!--
function gourl(n){
if(n != "0"){
self.location.href=n;
}
}
// -->
</SCRIPT>

<body bgcolor="#FFFFFF">
<CENTER>

<br>
<table width="96%" border="0" align="center">
  <tr> 
    <td width="9%" height="32" bgcolor="#D2DEFF"> 
      <div align="center"></div>
    </td>
    <td width="83%" height="32" bgcolor="#ACC1FF"> 
      <div align="center"><font size="4"><b><font color="#FFFFFF" size="5" face="Courier New, Courier, mono">Guild Member</font><FONT size="3" color="#FFFFFF"> (�o�^ 32��)</font></b></font></div>
    </td>
    <td width="8%" height="32" bgcolor="#D2DEFF"> 
      <div align="center"></div>
    </td>
  </tr>
</table>

<br>

<div align="right"><br>
<table><tr>
<td><form name="r">Race:<select name="race" onChange="self.gourl(this.options[this.selectedIndex].value)">
<option value="./member.cgi?race=All&class=All&sort=" SELECTED >All</option>
<option value="./member.cgi?race=Barbarian&class=All&sort=">Barbarian</option>
<option value="./member.cgi?race=Dark Elf&class=All&sort=">Dark Elf</option>
<option value="./member.cgi?race=Dwarf&class=All&sort=">Dwarf</option>
<option value="./member.cgi?race=Erudite&class=All&sort=">Erudite</option>
<option value="./member.cgi?race=Gnome&class=All&sort=">Gnome</option>
<option value="./member.cgi?race=Half Elf&class=All&sort=">Half Elf</option>
<option value="./member.cgi?race=Halfling&class=All&sort=">Halfling</option>
<option value="./member.cgi?race=High Elf&class=All&sort=">High Elf</option>
<option value="./member.cgi?race=Human&class=All&sort=">Human</option>
<option value="./member.cgi?race=Iksar&class=All&sort=">Iksar</option>
<option value="./member.cgi?race=Ogre&class=All&sort=">Ogre</option>
<option value="./member.cgi?race=Troll&class=All&sort=">Troll</option>
<option value="./member.cgi?race=Wood Elf&class=All&sort=">Wood Elf</option>
</select>
</form></td>
<td><form name="c">Class:<select name="class" onChange="self.gourl(this.options[this.selectedIndex].value)">
<option value="./member.cgi?race=All&class=All&sort=" SELECTED >All</option>
<option value="./member.cgi?race=All&class=Bard&sort=">Bard</option>
<option value="./member.cgi?race=All&class=Cleric&sort=">Cleric</option>
<option value="./member.cgi?race=All&class=Druid&sort=">Druid</option>
<option value="./member.cgi?race=All&class=Enchanter&sort=">Enchanter</option>
<option value="./member.cgi?race=All&class=Magician&sort=">Magician</option>
<option value="./member.cgi?race=All&class=Monk&sort=">Monk</option>
<option value="./member.cgi?race=All&class=Necromancer&sort=">Necromancer</option>
<option value="./member.cgi?race=All&class=Paladin&sort=">Paladin</option>
<option value="./member.cgi?race=All&class=Ranger&sort=">Ranger</option>
<option value="./member.cgi?race=All&class=Rogue&sort=">Rogue</option>
<option value="./member.cgi?race=All&class=Shadow Knight&sort=">Shadow Knight</option>
<option value="./member.cgi?race=All&class=Shaman&sort=">Shaman</option>
<option value="./member.cgi?race=All&class=Warrior&sort=">Warrior</option>
<option value="./member.cgi?race=All&class=Wizard&sort=">Wizard</option>
</select>
</form></td>
<td><form action="./member.cgi" method="POST">
<input type=hidden name=race value="All">
<input type=hidden name=class value="All">
<input type=hidden name=sort value="level">
<input type="submit" name="master" value="���x����">
</form>
</td>
<td><form method="POST" action="./member.cgi">
<input type=hidden name=race value="All">
<input type=hidden name=race value="All">
<input type=hidden name=sort value="">
<input type=hidden name=page value="10">
<input type=hidden name=mode value="page">
<input type=submit value="����10��">
</form></td>
<td><form method="POST" action="./member.cgi">
<input type=hidden name=race value="All">
<input type=hidden name=race value="All">
<input type=hidden name=sort value="">
<input type=hidden name=allview value="1">
<input type=submit value="�Ȉ�View">
</form></td>
</tr></table>
</div>
<div align="center">
          <table border="1" width="635">
            <tr> 
              <td colspan="2" height="25" bgcolor="#ACC1FF" width="147"> 
                <div align="left"><b><font size="3">Player</font>
				  <font color="#0000ff" size="2" face="MS UI Gothic, �l�r �o�S�V�b�N">
                  <br>
                  Lincelet</font></b></div>
              </td>
              <td height="25" width="140" bgcolor="#ACC1FF"><b><font size="3">ICQ#</font></b>
                <br>
				<font color="#0000ff" size="3" face="Comic Sans MS">none</font></td>
				<td height="25" width="348" bgcolor="#ACC1FF">
				  <table width="100%">
				    <tr>
					  <td>
						<b><font size="3">HP</font><font color="#0000ff" size="3" face="MS UI Gothic, �l�r �o�S�V�b�N">
	                	<br>
	                	none</font></b>
	                  </td>
					  <td align="right" valign="bottom">
                	    <form action="./member.cgi" method="POST">
                	      <input type="hidden" name="mode" value="edit">
                	      <input type="hidden" name="editno" value="1562">
                	      <input type="submit" name="edit" value="�o�^�ύX">
                	    </form>
					  </td>
				    </tr>
				  </table>
              </td>
            </tr>
            <tr> 
              <td colspan="2" height="25" width="147" bgcolor="#D2DEFF"><b><font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">05��04���X�V�I</font></b></td>
              <td height="25" colspan="2" width="488" bgcolor="#D2DEFF"><b><font size="2">Character 
                </font><font size="3" color="#0000ff" face="MS UI Gothic, �l�r �o�S�V�b�N">Lincelet Chocola
                (<font face="MS UI Gothic, �l�r �o�S�V�b�N">��</font>)</font><font size="4"> 
                </font><font color="#FF3333" size="3" face="Comic Sans MS"></font></b></td>
            </tr>
            <tr> 
              <td colspan="2" height="80" rowspan="4" width="147" align="center" valign="middle" bgcolor="#D2DEFF"><img src="race/Lincelet Chocola.jpg"></td>
              <td width="107" height="25" bgcolor="#D2DEFF"><b><font size="2">LV </font><font size="3" color="#0000ff" face="Comic Sans MS">53</font></b></td>
              <td width="381" height="25" bgcolor="#D2DEFF"><b><font size="2">Race/Class </font><font size="3" color="#0000ff" face="Comic Sans MS">Human/Enchanter</font></b></td>
            </tr>
            <tr valign="top"> 
              <td height="25" width="140" bgcolor="#D2DEFF"> 
                <p><b><font size="2">�M�_</font></b><br>
                  <b><font size="2" color="#0000ff">EROLLISI MARR</font></b><font size="1"><br>(���̐_)</font>
                </p>
              </td>
              <td height="25" width="348" bgcolor="#D2DEFF"><b><font size="2">�������_</font><br>
                <font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">�Z���s�肩���E�E�E�B</font></b></td>
            </tr>





    <TR>
      <TD colspan="2" bgcolor="#D2DEFF"><B><FONT size="3">SV</FONT></B>

<B><FONT size="2">M</FONT></B>
<font face="Comic Sans MS" size="3" color="#800000">86�@</font></b>

<B><FONT size="2">M&F</FONT></B>
<font face="Comic Sans MS" size="3" color="#FF0000">80�@</font></b>

<B><FONT size="2">M&C</FONT></B>
<font face="Comic Sans MS" size="3" color="#0000ff">85�@</font></b>

<B><FONT size="2">M&P</FONT></B>
<font face="Comic Sans MS" size="3" color="#008000">51�@</font></b>

<B><FONT size="2">M&D</FONT></B>
<font face="Comic Sans MS" size="3" color="#404040">59�@</font></b>

    </TD>
    </TR>






            <tr valign="top"> 
              <td colspan="2" height="78" width="488" bgcolor="#D2DEFF">
                <p><b><font size="2">Comment</font> <br>
                  <font face="MS UI Gothic, �l�r �o�S�V�b�N" color="#0000ff" size="3">���΂炭�ǂ����ɏZ�݂������ł��B<br>�i�b�̘b�ɂȂ�Ƃ������C�W���������̂ŁA����n�߂Ă݂܂����B�������܂P�X�Q�I�@�Q�O�O�܂ł��Ƃ�����ƁI<br>���̂���t��t���`�i���B<br><br>Redrouge HIE PAL LVL13</font> 
                </td>
            </tr>
          </table>
          <br>
          <table border="1" width="635">
            <tr> 
              <td colspan="2" height="25" bgcolor="#ACC1FF" width="147"> 
                <div align="left"><b><font size="3">Player</font>
				  <font color="#0000ff" size="2" face="MS UI Gothic, �l�r �o�S�V�b�N">
                  <br>
                  Sayuri</font></b></div>
              </td>
              <td height="25" width="140" bgcolor="#ACC1FF"><b><font size="3">ICQ#</font></b>
                <br>
				<font color="#0000ff" size="3" face="Comic Sans MS">none</font></td>
				<td height="25" width="348" bgcolor="#ACC1FF">
				  <table width="100%">
				    <tr>
					  <td>
						<b><font size="3">HP</font><font color="#0000ff" size="3" face="MS UI Gothic, �l�r �o�S�V�b�N">
	                	<br>
	                	none</font></b>
	                  </td>
					  <td align="right" valign="bottom">
                	    <form action="./member.cgi" method="POST">
                	      <input type="hidden" name="mode" value="edit">
                	      <input type="hidden" name="editno" value="1561">
                	      <input type="submit" name="edit" value="�o�^�ύX">
                	    </form>
					  </td>
				    </tr>
				  </table>
              </td>
            </tr>
            <tr> 
              <td colspan="2" height="25" width="147" bgcolor="#D2DEFF"><b><font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">05��04���X�V�I</font></b></td>
              <td height="25" colspan="2" width="488" bgcolor="#D2DEFF"><b><font size="2">Character 
                </font><font size="3" color="#0000ff" face="MS UI Gothic, �l�r �o�S�V�b�N">Anri
                (<font face="MS UI Gothic, �l�r �o�S�V�b�N">��</font>)</font><font size="4"> 
                </font><font color="#FF3333" size="3" face="Comic Sans MS"></font></b></td>
            </tr>
            <tr> 
              <td colspan="2" height="80" rowspan="4" width="147" align="center" valign="middle" bgcolor="#D2DEFF"><img src="race/Anri.jpg"></td>
              <td width="107" height="25" bgcolor="#D2DEFF"><b><font size="2">LV </font><font size="3" color="#0000ff" face="Comic Sans MS">58</font></b></td>
              <td width="381" height="25" bgcolor="#D2DEFF"><b><font size="2">Race/Class </font><font size="3" color="#0000ff" face="Comic Sans MS">Dark Elf/Warrior</font></b></td>
            </tr>
            <tr valign="top"> 
              <td height="25" width="140" bgcolor="#D2DEFF"> 
                <p><b><font size="2">�M�_</font></b><br>
                  <b><font size="2" color="#0000ff">�Ȃ�</font></b><font size="1"><br>(���̐_)</font>
                </p>
              </td>
              <td height="25" width="348" bgcolor="#D2DEFF"><b><font size="2">�������_</font><br>
                <font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">��W�`�ԋp���I�I�I(�����Ȃ�n��)</font></b></td>
            </tr>





    <TR>
      <TD colspan="2" bgcolor="#D2DEFF"><B><FONT size="3">SV</FONT></B>

<B><FONT size="2">M</FONT></B>
<font face="Comic Sans MS" size="3" color="#800000">130�@</font></b>

<B><FONT size="2">M&F</FONT></B>
<font face="Comic Sans MS" size="3" color="#FF0000">114�@</font></b>

<B><FONT size="2">M&C</FONT></B>
<font face="Comic Sans MS" size="3" color="#0000ff">99�@</font></b>

<B><FONT size="2">M&P</FONT></B>
<font face="Comic Sans MS" size="3" color="#008000">85�@</font></b>

<B><FONT size="2">M&D</FONT></B>
<font face="Comic Sans MS" size="3" color="#404040">85�@</font></b>

    </TD>
    </TR>






            <tr valign="top"> 
              <td colspan="2" height="78" width="488" bgcolor="#D2DEFF">
                <p><b><font size="2">Comment</font> <br>
                  <font face="MS UI Gothic, �l�r �o�S�V�b�N" color="#0000ff" size="3">sayuri (wiz)   52�@GG�ATL�A�h���S���ގ��L����<br>sayu (iks shm) 52�@�ق�̂����`���ɂȂƂ��L����<br>lawson (pal)   35�@���ɂȂƂ��L����<br>axistrack (rng) 3  �Ď��L�����i�T�͗~�����ˁj<br>�攭War�w�c�ɂȂ�Ƃ��ǂ���ed<br>59�́E�E�E�E���Ȃ�邩�ȁE�E�Eepic���啨�̂݁I�啨come...</font> 
                </td>
            </tr>
          </table>
          <br>
          <table border="1" width="635">
            <tr> 
              <td colspan="2" height="25" bgcolor="#ACC1FF" width="147"> 
                <div align="left"><b><font size="3">Player</font>
				  <font color="#0000ff" size="2" face="MS UI Gothic, �l�r �o�S�V�b�N">
                  <br>
                  Hiraga</font></b></div>
              </td>
              <td height="25" width="140" bgcolor="#ACC1FF"><b><font size="3">ICQ#</font></b>
                <br>
				<font color="#0000ff" size="3" face="Comic Sans MS">2541803</font></td>
				<td height="25" width="348" bgcolor="#ACC1FF">
				  <table width="100%">
				    <tr>
					  <td>
						<b><font size="3">HP</font><font color="#0000ff" size="3" face="MS UI Gothic, �l�r �o�S�V�b�N">
	                	<br>
	                	<a href="http://www5.airnet.ne.jp/wolf/" target=_blank>Little PC World</a></font></b>
	                  </td>
					  <td align="right" valign="bottom">
                	    <form action="./member.cgi" method="POST">
                	      <input type="hidden" name="mode" value="edit">
                	      <input type="hidden" name="editno" value="1560">
                	      <input type="submit" name="edit" value="�o�^�ύX">
                	    </form>
					  </td>
				    </tr>
				  </table>
              </td>
            </tr>
            <tr> 
              <td colspan="2" height="25" width="147" bgcolor="#D2DEFF"><b><font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">05��04���X�V�I</font></b></td>
              <td height="25" colspan="2" width="488" bgcolor="#D2DEFF"><b><font size="2">Character 
                </font><font size="3" color="#0000ff" face="MS UI Gothic, �l�r �o�S�V�b�N">Hiraga Gennai
                (<font face="MS UI Gothic, �l�r �o�S�V�b�N">��</font>)</font><font size="4"> 
                </font><font color="#FF3333" size="3" face="Comic Sans MS"></font></b></td>
            </tr>
            <tr> 
              <td colspan="2" height="80" rowspan="4" width="147" align="center" valign="middle" bgcolor="#D2DEFF"><img src="race/Hiraga Gennai.jpg"></td>
              <td width="107" height="25" bgcolor="#D2DEFF"><b><font size="2">LV </font><font size="3" color="#0000ff" face="Comic Sans MS">52</font></b></td>
              <td width="381" height="25" bgcolor="#D2DEFF"><b><font size="2">Race/Class </font><font size="3" color="#0000ff" face="Comic Sans MS">Erudite/Necromancer</font></b></td>
            </tr>
            <tr valign="top"> 
              <td height="25" width="140" bgcolor="#D2DEFF"> 
                <p><b><font size="2">�M�_</font></b><br>
                  <b><font size="2" color="#0000ff">CAZIC-THULE</font></b><font size="1"><br>(���|�̐_)</font>
                </p>
              </td>
              <td height="25" width="348" bgcolor="#D2DEFF"><b><font size="2">�������_</font><br>
                <font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">�ǂ��Ȃ�ł��傤�ˁB</font></b></td>
            </tr>





    <TR>
      <TD colspan="2" bgcolor="#D2DEFF"><B><FONT size="3">SV</FONT></B>

<B><FONT size="2">M</FONT></B>
<font face="Comic Sans MS" size="3" color="#800000">77�@</font></b>

<B><FONT size="2">M&F</FONT></B>
<font face="Comic Sans MS" size="3" color="#FF0000">92�@</font></b>

<B><FONT size="2">M&C</FONT></B>
<font face="Comic Sans MS" size="3" color="#0000ff">92�@</font></b>

<B><FONT size="2">M&P</FONT></B>
<font face="Comic Sans MS" size="3" color="#008000">37�@</font></b>

<B><FONT size="2">M&D</FONT></B>
<font face="Comic Sans MS" size="3" color="#404040">57�@</font></b>

    </TD>
    </TR>






            <tr valign="top"> 
              <td colspan="2" height="78" width="488" bgcolor="#D2DEFF">
                <p><b><font size="2">Comment</font> <br>
                  <font face="MS UI Gothic, �l�r �o�S�V�b�N" color="#0000ff" size="3">SvMFC�͂��������悭�Ȃ��Ă��������B<br>�ł�SvPD������ˁB�܂���A�������󂢂Ă邩��JC�ŉ��Ƃ��������Ƃ��ł��ȁB<br><br>�Εt�������� ���J�� ����(DWF PAL L9)</font> 
                </td>
            </tr>
          </table>
          <br>
          <table border="1" width="635">
            <tr> 
              <td colspan="2" height="25" bgcolor="#ACC1FF" width="147"> 
                <div align="left"><b><font size="3">Player</font>
				  <font color="#0000ff" size="2" face="MS UI Gothic, �l�r �o�S�V�b�N">
                  <br>
                  Bandou</font></b></div>
              </td>
              <td height="25" width="140" bgcolor="#ACC1FF"><b><font size="3">ICQ#</font></b>
                <br>
				<font color="#0000ff" size="3" face="Comic Sans MS">none</font></td>
				<td height="25" width="348" bgcolor="#ACC1FF">
				  <table width="100%">
				    <tr>
					  <td>
						<b><font size="3">HP</font><font color="#0000ff" size="3" face="MS UI Gothic, �l�r �o�S�V�b�N">
	                	<br>
	                	none</font></b>
	                  </td>
					  <td align="right" valign="bottom">
                	    <form action="./member.cgi" method="POST">
                	      <input type="hidden" name="mode" value="edit">
                	      <input type="hidden" name="editno" value="1559">
                	      <input type="submit" name="edit" value="�o�^�ύX">
                	    </form>
					  </td>
				    </tr>
				  </table>
              </td>
            </tr>
            <tr> 
              <td colspan="2" height="25" width="147" bgcolor="#D2DEFF"><b><font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">05��04���X�V�I</font></b></td>
              <td height="25" colspan="2" width="488" bgcolor="#D2DEFF"><b><font size="2">Character 
                </font><font size="3" color="#0000ff" face="MS UI Gothic, �l�r �o�S�V�b�N">Bandou
                (<font face="MS UI Gothic, �l�r �o�S�V�b�N">��</font>)</font><font size="4"> 
                </font><font color="#FF3333" size="3" face="Comic Sans MS"></font></b></td>
            </tr>
            <tr> 
              <td colspan="2" height="80" rowspan="4" width="147" align="center" valign="middle" bgcolor="#D2DEFF"><img src="race/Bandou.jpg"></td>
              <td width="107" height="25" bgcolor="#D2DEFF"><b><font size="2">LV </font><font size="3" color="#0000ff" face="Comic Sans MS">38</font></b></td>
              <td width="381" height="25" bgcolor="#D2DEFF"><b><font size="2">Race/Class </font><font size="3" color="#0000ff" face="Comic Sans MS">Human/Paladin</font></b></td>
            </tr>
            <tr valign="top"> 
              <td height="25" width="140" bgcolor="#D2DEFF"> 
                <p><b><font size="2">�M�_</font></b><br>
                  <b><font size="2" color="#0000ff">EROLLISI MARR</font></b><font size="1"><br>(���̐_)</font>
                </p>
              </td>
              <td height="25" width="348" bgcolor="#D2DEFF"><b><font size="2">�������_</font><br>
                <font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">���[�[���ƁAHK �ɂ��܂������A���̂��т������@�a�ֈړ����܂����B�N���U���ā[�[�[�����B�@�@�@�@</font></b></td>
            </tr>





    <TR>
      <TD colspan="2" bgcolor="#D2DEFF"><B><FONT size="3">SV</FONT></B>

<B><FONT size="2">M</FONT></B>
<font face="Comic Sans MS" size="3" color="#800000">50�@</font></b>

<B><FONT size="2">M&F</FONT></B>
<font face="Comic Sans MS" size="3" color="#FF0000">�@</font></b>

<B><FONT size="2">M&C</FONT></B>
<font face="Comic Sans MS" size="3" color="#0000ff">�@</font></b>

<B><FONT size="2">M&P</FONT></B>
<font face="Comic Sans MS" size="3" color="#008000">�@</font></b>

<B><FONT size="2">M&D</FONT></B>
<font face="Comic Sans MS" size="3" color="#404040">�@</font></b>

    </TD>
    </TR>






            <tr valign="top"> 
              <td colspan="2" height="78" width="488" bgcolor="#D2DEFF">
                <p><b><font size="2">Comment</font> <br>
                  <font face="MS UI Gothic, �l�r �o�S�V�b�N" color="#0000ff" size="3">�V�Ăł��̂ŁA��E��E���E��!<br></font> 
                </td>
            </tr>
          </table>
          <br>
          <table border="1" width="635">
            <tr> 
              <td colspan="2" height="25" bgcolor="#ACC1FF" width="147"> 
                <div align="left"><b><font size="3">Player</font>
				  <font color="#0000ff" size="2" face="MS UI Gothic, �l�r �o�S�V�b�N">
                  <br>
                  Fovos</font></b></div>
              </td>
              <td height="25" width="140" bgcolor="#ACC1FF"><b><font size="3">ICQ#</font></b>
                <br>
				<font color="#0000ff" size="3" face="Comic Sans MS">6844715</font></td>
				<td height="25" width="348" bgcolor="#ACC1FF">
				  <table width="100%">
				    <tr>
					  <td>
						<b><font size="3">HP</font><font color="#0000ff" size="3" face="MS UI Gothic, �l�r �o�S�V�b�N">
	                	<br>
	                	none</font></b>
	                  </td>
					  <td align="right" valign="bottom">
                	    <form action="./member.cgi" method="POST">
                	      <input type="hidden" name="mode" value="edit">
                	      <input type="hidden" name="editno" value="1558">
                	      <input type="submit" name="edit" value="�o�^�ύX">
                	    </form>
					  </td>
				    </tr>
				  </table>
              </td>
            </tr>
            <tr> 
              <td colspan="2" height="25" width="147" bgcolor="#D2DEFF"><b><font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">05��04���X�V�I</font></b></td>
              <td height="25" colspan="2" width="488" bgcolor="#D2DEFF"><b><font size="2">Character 
                </font><font size="3" color="#0000ff" face="MS UI Gothic, �l�r �o�S�V�b�N">Donkee Punchee
                (<font face="MS UI Gothic, �l�r �o�S�V�b�N">��</font>)</font><font size="4"> 
                </font><font color="#FF3333" size="3" face="Comic Sans MS"></font></b></td>
            </tr>
            <tr> 
              <td colspan="2" height="80" rowspan="4" width="147" align="center" valign="middle" bgcolor="#D2DEFF"><img src="race/Donkee Punchee.jpg"></td>
              <td width="107" height="25" bgcolor="#D2DEFF"><b><font size="2">LV </font><font size="3" color="#0000ff" face="Comic Sans MS">58.4</font></b></td>
              <td width="381" height="25" bgcolor="#D2DEFF"><b><font size="2">Race/Class </font><font size="3" color="#0000ff" face="Comic Sans MS">Iksar/Monk</font></b></td>
            </tr>
            <tr valign="top"> 
              <td height="25" width="140" bgcolor="#D2DEFF"> 
                <p><b><font size="2">�M�_</font></b><br>
                  <b><font size="2" color="#0000ff">CAZIC-THULE</font></b><font size="1"><br>(���|�̐_)</font>
                </p>
              </td>
              <td height="25" width="348" bgcolor="#D2DEFF"><b><font size="2">�������_</font><br>
                <font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">anywhere</font></b></td>
            </tr>





    <TR>
      <TD colspan="2" bgcolor="#D2DEFF"><B><FONT size="3">SV</FONT></B>

<B><FONT size="2">M</FONT></B>
<font face="Comic Sans MS" size="3" color="#800000">119�@</font></b>

<B><FONT size="2">M&F</FONT></B>
<font face="Comic Sans MS" size="3" color="#FF0000">148�@</font></b>

<B><FONT size="2">M&C</FONT></B>
<font face="Comic Sans MS" size="3" color="#0000ff">86�@</font></b>

<B><FONT size="2">M&P</FONT></B>
<font face="Comic Sans MS" size="3" color="#008000">114�@</font></b>

<B><FONT size="2">M&D</FONT></B>
<font face="Comic Sans MS" size="3" color="#404040">104�@</font></b>

    </TD>
    </TR>






            <tr valign="top"> 
              <td colspan="2" height="78" width="488" bgcolor="#D2DEFF">
                <p><b><font size="2">Comment</font> <br>
                  <font face="MS UI Gothic, �l�r �o�S�V�b�N" color="#0000ff" size="3">TARGET LOCK-ON ++ Pengin ++<br>GW���ɂ�59�̉��F2bbl�͂��������ł��ȁ[<br><br>2nd : Fovos the Best of Pretty halfling/55ROG</font> 
                </td>
            </tr>
          </table>
          <br>
          <table border="1" width="635">
            <tr> 
              <td colspan="2" height="25" bgcolor="#ACC1FF" width="147"> 
                <div align="left"><b><font size="3">Player</font>
				  <font color="#0000ff" size="2" face="MS UI Gothic, �l�r �o�S�V�b�N">
                  <br>
                  Haru</font></b></div>
              </td>
              <td height="25" width="140" bgcolor="#ACC1FF"><b><font size="3">ICQ#</font></b>
                <br>
				<font color="#0000ff" size="3" face="Comic Sans MS">none</font></td>
				<td height="25" width="348" bgcolor="#ACC1FF">
				  <table width="100%">
				    <tr>
					  <td>
						<b><font size="3">HP</font><font color="#0000ff" size="3" face="MS UI Gothic, �l�r �o�S�V�b�N">
	                	<br>
	                	none</font></b>
	                  </td>
					  <td align="right" valign="bottom">
                	    <form action="./member.cgi" method="POST">
                	      <input type="hidden" name="mode" value="edit">
                	      <input type="hidden" name="editno" value="1557">
                	      <input type="submit" name="edit" value="�o�^�ύX">
                	    </form>
					  </td>
				    </tr>
				  </table>
              </td>
            </tr>
            <tr> 
              <td colspan="2" height="25" width="147" bgcolor="#D2DEFF"><b><font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">05��03���X�V�I</font></b></td>
              <td height="25" colspan="2" width="488" bgcolor="#D2DEFF"><b><font size="2">Character 
                </font><font size="3" color="#0000ff" face="MS UI Gothic, �l�r �o�S�V�b�N">Haruru
                (<font face="MS UI Gothic, �l�r �o�S�V�b�N">��</font>)</font><font size="4"> 
                </font><font color="#FF3333" size="3" face="Comic Sans MS"></font></b></td>
            </tr>
            <tr> 
              <td colspan="2" height="80" rowspan="4" width="147" align="center" valign="middle" bgcolor="#D2DEFF"><img src="race/Haruru.jpg"></td>
              <td width="107" height="25" bgcolor="#D2DEFF"><b><font size="2">LV </font><font size="3" color="#0000ff" face="Comic Sans MS">58</font></b></td>
              <td width="381" height="25" bgcolor="#D2DEFF"><b><font size="2">Race/Class </font><font size="3" color="#0000ff" face="Comic Sans MS">High Elf/Enchanter</font></b></td>
            </tr>
            <tr valign="top"> 
              <td height="25" width="140" bgcolor="#D2DEFF"> 
                <p><b><font size="2">�M�_</font></b><br>
                  <b><font size="2" color="#0000ff">EROLLISI MARR</font></b><font size="1"><br>(���̐_)</font>
                </p>
              </td>
              <td height="25" width="348" bgcolor="#D2DEFF"><b><font size="2">�������_</font><br>
                <font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">�e�u�풓</font></b></td>
            </tr>





    <TR>
      <TD colspan="2" bgcolor="#D2DEFF"><B><FONT size="3">SV</FONT></B>

<B><FONT size="2">M</FONT></B>
<font face="Comic Sans MS" size="3" color="#800000">77�@</font></b>

<B><FONT size="2">M&F</FONT></B>
<font face="Comic Sans MS" size="3" color="#FF0000">75�@</font></b>

<B><FONT size="2">M&C</FONT></B>
<font face="Comic Sans MS" size="3" color="#0000ff">99�@</font></b>

<B><FONT size="2">M&P</FONT></B>
<font face="Comic Sans MS" size="3" color="#008000">88�@</font></b>

<B><FONT size="2">M&D</FONT></B>
<font face="Comic Sans MS" size="3" color="#404040">70�@</font></b>

    </TD>
    </TR>






            <tr valign="top"> 
              <td colspan="2" height="78" width="488" bgcolor="#D2DEFF">
                <p><b><font size="2">Comment</font> <br>
                  <font face="MS UI Gothic, �l�r �o�S�V�b�N" color="#0000ff" size="3">���ƂQ�I<br><br><br>2nd Haru Lv25WAR<br>3rd harutin Lv35DRU</font> 
                </td>
            </tr>
          </table>
          <br>
          <table border="1" width="635">
            <tr> 
              <td colspan="2" height="25" bgcolor="#ACC1FF" width="147"> 
                <div align="left"><b><font size="3">Player</font>
				  <font color="#0000ff" size="2" face="MS UI Gothic, �l�r �o�S�V�b�N">
                  <br>
                  Aoneko</font></b></div>
              </td>
              <td height="25" width="140" bgcolor="#ACC1FF"><b><font size="3">ICQ#</font></b>
                <br>
				<font color="#0000ff" size="3" face="Comic Sans MS">none</font></td>
				<td height="25" width="348" bgcolor="#ACC1FF">
				  <table width="100%">
				    <tr>
					  <td>
						<b><font size="3">HP</font><font color="#0000ff" size="3" face="MS UI Gothic, �l�r �o�S�V�b�N">
	                	<br>
	                	none</font></b>
	                  </td>
					  <td align="right" valign="bottom">
                	    <form action="./member.cgi" method="POST">
                	      <input type="hidden" name="mode" value="edit">
                	      <input type="hidden" name="editno" value="1555">
                	      <input type="submit" name="edit" value="�o�^�ύX">
                	    </form>
					  </td>
				    </tr>
				  </table>
              </td>
            </tr>
            <tr> 
              <td colspan="2" height="25" width="147" bgcolor="#D2DEFF"><b><font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">05��02���X�V�I</font></b></td>
              <td height="25" colspan="2" width="488" bgcolor="#D2DEFF"><b><font size="2">Character 
                </font><font size="3" color="#0000ff" face="MS UI Gothic, �l�r �o�S�V�b�N">Amrui Horkeukamui
                (<font face="MS UI Gothic, �l�r �o�S�V�b�N">��</font>)</font><font size="4"> 
                </font><font color="#FF3333" size="3" face="Comic Sans MS"></font></b></td>
            </tr>
            <tr> 
              <td colspan="2" height="80" rowspan="4" width="147" align="center" valign="middle" bgcolor="#D2DEFF"><img src="race/Amrui Horkeukamui.jpg"></td>
              <td width="107" height="25" bgcolor="#D2DEFF"><b><font size="2">LV </font><font size="3" color="#0000ff" face="Comic Sans MS">60</font></b></td>
              <td width="381" height="25" bgcolor="#D2DEFF"><b><font size="2">Race/Class </font><font size="3" color="#0000ff" face="Comic Sans MS">Wood Elf/Druid</font></b></td>
            </tr>
            <tr valign="top"> 
              <td height="25" width="140" bgcolor="#D2DEFF"> 
                <p><b><font size="2">�M�_</font></b><br>
                  <b><font size="2" color="#0000ff">TUNARE</font></b><font size="1"><br>(��Ȃ�_)</font>
                </p>
              </td>
              <td height="25" width="348" bgcolor="#D2DEFF"><b><font size="2">�������_</font><br>
                <font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">�ǂ��ɂ��邩������</font></b></td>
            </tr>





    <TR>
      <TD colspan="2" bgcolor="#D2DEFF"><B><FONT size="3">SV</FONT></B>

<B><FONT size="2">M</FONT></B>
<font face="Comic Sans MS" size="3" color="#800000">70�@</font></b>

<B><FONT size="2">M&F</FONT></B>
<font face="Comic Sans MS" size="3" color="#FF0000">86�@</font></b>

<B><FONT size="2">M&C</FONT></B>
<font face="Comic Sans MS" size="3" color="#0000ff">86�@</font></b>

<B><FONT size="2">M&P</FONT></B>
<font face="Comic Sans MS" size="3" color="#008000">94�@</font></b>

<B><FONT size="2">M&D</FONT></B>
<font face="Comic Sans MS" size="3" color="#404040">76�@</font></b>

    </TD>
    </TR>






            <tr valign="top"> 
              <td colspan="2" height="78" width="488" bgcolor="#D2DEFF">
                <p><b><font size="2">Comment</font> <br>
                  <font face="MS UI Gothic, �l�r �o�S�V�b�N" color="#0000ff" size="3">Epic���₷���Ȃ����ȁ[�A�Ǝv����<br>�ڂ̑O�ŕʂ̂Ƃ����VSGem�Q�b�g�����<br>�����������̂����������������̍��c�B<br><br>Siriuse�@DWF/�������@�ULv<br>Burnz�@IKS-BRD�i�H�j�WLv</font> 
                </td>
            </tr>
          </table>
          <br>
          <table border="1" width="635">
            <tr> 
              <td colspan="2" height="25" bgcolor="#ACC1FF" width="147"> 
                <div align="left"><b><font size="3">Player</font>
				  <font color="#0000ff" size="2" face="MS UI Gothic, �l�r �o�S�V�b�N">
                  <br>
                  Isse</font></b></div>
              </td>
              <td height="25" width="140" bgcolor="#ACC1FF"><b><font size="3">ICQ#</font></b>
                <br>
				<font color="#0000ff" size="3" face="Comic Sans MS">none</font></td>
				<td height="25" width="348" bgcolor="#ACC1FF">
				  <table width="100%">
				    <tr>
					  <td>
						<b><font size="3">HP</font><font color="#0000ff" size="3" face="MS UI Gothic, �l�r �o�S�V�b�N">
	                	<br>
	                	none</font></b>
	                  </td>
					  <td align="right" valign="bottom">
                	    <form action="./member.cgi" method="POST">
                	      <input type="hidden" name="mode" value="edit">
                	      <input type="hidden" name="editno" value="1554">
                	      <input type="submit" name="edit" value="�o�^�ύX">
                	    </form>
					  </td>
				    </tr>
				  </table>
              </td>
            </tr>
            <tr> 
              <td colspan="2" height="25" width="147" bgcolor="#D2DEFF"><b><font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">05��01���X�V�I</font></b></td>
              <td height="25" colspan="2" width="488" bgcolor="#D2DEFF"><b><font size="2">Character 
                </font><font size="3" color="#0000ff" face="MS UI Gothic, �l�r �o�S�V�b�N">Isse
                (<font face="MS UI Gothic, �l�r �o�S�V�b�N">��</font>)</font><font size="4"> 
                </font><font color="#FF3333" size="3" face="Comic Sans MS"></font></b></td>
            </tr>
            <tr> 
              <td colspan="2" height="80" rowspan="4" width="147" align="center" valign="middle" bgcolor="#D2DEFF"><img src="race/Isse.jpg"></td>
              <td width="107" height="25" bgcolor="#D2DEFF"><b><font size="2">LV </font><font size="3" color="#0000ff" face="Comic Sans MS">44</font></b></td>
              <td width="381" height="25" bgcolor="#D2DEFF"><b><font size="2">Race/Class </font><font size="3" color="#0000ff" face="Comic Sans MS">Wood Elf/Druid</font></b></td>
            </tr>
            <tr valign="top"> 
              <td height="25" width="140" bgcolor="#D2DEFF"> 
                <p><b><font size="2">�M�_</font></b><br>
                  <b><font size="2" color="#0000ff">�Ȃ�</font></b><font size="1"><br>(���̐_)</font>
                </p>
              </td>
              <td height="25" width="348" bgcolor="#D2DEFF"><b><font size="2">�������_</font><br>
                <font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">solB�ɍݏZ</font></b></td>
            </tr>





    <TR>
      <TD colspan="2" bgcolor="#D2DEFF"><B><FONT size="3">SV</FONT></B>

<B><FONT size="2">M</FONT></B>
<font face="Comic Sans MS" size="3" color="#800000">�@</font></b>

<B><FONT size="2">M&F</FONT></B>
<font face="Comic Sans MS" size="3" color="#FF0000">�@</font></b>

<B><FONT size="2">M&C</FONT></B>
<font face="Comic Sans MS" size="3" color="#0000ff">�@</font></b>

<B><FONT size="2">M&P</FONT></B>
<font face="Comic Sans MS" size="3" color="#008000">�@</font></b>

<B><FONT size="2">M&D</FONT></B>
<font face="Comic Sans MS" size="3" color="#404040">�@</font></b>

    </TD>
    </TR>






            <tr valign="top"> 
              <td colspan="2" height="78" width="488" bgcolor="#D2DEFF">
                <p><b><font size="2">Comment</font> <br>
                  <font face="MS UI Gothic, �l�r �o�S�V�b�N" color="#0000ff" size="3">�r�n�u�E�c�k�ɂ́A�قƂ�Ǎs���Ă܂���B������ꏊ�����Ăˁ[</font> 
                </td>
            </tr>
          </table>
          <br>
          <table border="1" width="635">
            <tr> 
              <td colspan="2" height="25" bgcolor="#ACC1FF" width="147"> 
                <div align="left"><b><font size="3">Player</font>
				  <font color="#0000ff" size="2" face="MS UI Gothic, �l�r �o�S�V�b�N">
                  <br>
                  Zarmbuk</font></b></div>
              </td>
              <td height="25" width="140" bgcolor="#ACC1FF"><b><font size="3">ICQ#</font></b>
                <br>
				<font color="#0000ff" size="3" face="Comic Sans MS">none</font></td>
				<td height="25" width="348" bgcolor="#ACC1FF">
				  <table width="100%">
				    <tr>
					  <td>
						<b><font size="3">HP</font><font color="#0000ff" size="3" face="MS UI Gothic, �l�r �o�S�V�b�N">
	                	<br>
	                	<a href="http://www.rr.iij4u.or.jp/~hiraku/shamanofwar/" target=_blank>Shaman of War</a></font></b>
	                  </td>
					  <td align="right" valign="bottom">
                	    <form action="./member.cgi" method="POST">
                	      <input type="hidden" name="mode" value="edit">
                	      <input type="hidden" name="editno" value="1552">
                	      <input type="submit" name="edit" value="�o�^�ύX">
                	    </form>
					  </td>
				    </tr>
				  </table>
              </td>
            </tr>
            <tr> 
              <td colspan="2" height="25" width="147" bgcolor="#D2DEFF"><b><font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">04��30���X�V�I</font></b></td>
              <td height="25" colspan="2" width="488" bgcolor="#D2DEFF"><b><font size="2">Character 
                </font><font size="3" color="#0000ff" face="MS UI Gothic, �l�r �o�S�V�b�N">Zarmbuk
                (<font face="MS UI Gothic, �l�r �o�S�V�b�N">��</font>)</font><font size="4"> 
                </font><font color="#FF3333" size="3" face="Comic Sans MS"></font></b></td>
            </tr>
            <tr> 
              <td colspan="2" height="80" rowspan="4" width="147" align="center" valign="middle" bgcolor="#D2DEFF"><img src="race/Zarmbuk.jpg"></td>
              <td width="107" height="25" bgcolor="#D2DEFF"><b><font size="2">LV </font><font size="3" color="#0000ff" face="Comic Sans MS">54</font></b></td>
              <td width="381" height="25" bgcolor="#D2DEFF"><b><font size="2">Race/Class </font><font size="3" color="#0000ff" face="Comic Sans MS">Ogre/Shaman</font></b></td>
            </tr>
            <tr valign="top"> 
              <td height="25" width="140" bgcolor="#D2DEFF"> 
                <p><b><font size="2">�M�_</font></b><br>
                  <b><font size="2" color="#0000ff">RALLOS ZEK</font></b><font size="1"><br>(�킢�̐_)</font>
                </p>
              </td>
              <td height="25" width="348" bgcolor="#D2DEFF"><b><font size="2">�������_</font><br>
                <font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">Oggok</font></b></td>
            </tr>





    <TR>
      <TD colspan="2" bgcolor="#D2DEFF"><B><FONT size="3">SV</FONT></B>

<B><FONT size="2">M</FONT></B>
<font face="Comic Sans MS" size="3" color="#800000">52�@</font></b>

<B><FONT size="2">M&F</FONT></B>
<font face="Comic Sans MS" size="3" color="#FF0000">54�@</font></b>

<B><FONT size="2">M&C</FONT></B>
<font face="Comic Sans MS" size="3" color="#0000ff">57�@</font></b>

<B><FONT size="2">M&P</FONT></B>
<font face="Comic Sans MS" size="3" color="#008000">30�@</font></b>

<B><FONT size="2">M&D</FONT></B>
<font face="Comic Sans MS" size="3" color="#404040">37�@</font></b>

    </TD>
    </TR>






            <tr valign="top"> 
              <td colspan="2" height="78" width="488" bgcolor="#D2DEFF">
                <p><b><font size="2">Comment</font> <br>
                  <font face="MS UI Gothic, �l�r �o�S�V�b�N" color="#0000ff" size="3">PoF��Ding�`</font> 
                </td>
            </tr>
          </table>
          <br>
          <table border="1" width="635">
            <tr> 
              <td colspan="2" height="25" bgcolor="#ACC1FF" width="147"> 
                <div align="left"><b><font size="3">Player</font>
				  <font color="#0000ff" size="2" face="MS UI Gothic, �l�r �o�S�V�b�N">
                  <br>
                  Shail</font></b></div>
              </td>
              <td height="25" width="140" bgcolor="#ACC1FF"><b><font size="3">ICQ#</font></b>
                <br>
				<font color="#0000ff" size="3" face="Comic Sans MS">none</font></td>
				<td height="25" width="348" bgcolor="#ACC1FF">
				  <table width="100%">
				    <tr>
					  <td>
						<b><font size="3">HP</font><font color="#0000ff" size="3" face="MS UI Gothic, �l�r �o�S�V�b�N">
	                	<br>
	                	none</font></b>
	                  </td>
					  <td align="right" valign="bottom">
                	    <form action="./member.cgi" method="POST">
                	      <input type="hidden" name="mode" value="edit">
                	      <input type="hidden" name="editno" value="1551">
                	      <input type="submit" name="edit" value="�o�^�ύX">
                	    </form>
					  </td>
				    </tr>
				  </table>
              </td>
            </tr>
            <tr> 
              <td colspan="2" height="25" width="147" bgcolor="#D2DEFF"><b><font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">04��30���X�V�I</font></b></td>
              <td height="25" colspan="2" width="488" bgcolor="#D2DEFF"><b><font size="2">Character 
                </font><font size="3" color="#0000ff" face="MS UI Gothic, �l�r �o�S�V�b�N">Shail
                (<font face="MS UI Gothic, �l�r �o�S�V�b�N">��</font>)</font><font size="4"> 
                </font><font color="#FF3333" size="3" face="Comic Sans MS"></font></b></td>
            </tr>
            <tr> 
              <td colspan="2" height="80" rowspan="4" width="147" align="center" valign="middle" bgcolor="#D2DEFF"><img src="race/Shail.jpg"></td>
              <td width="107" height="25" bgcolor="#D2DEFF"><b><font size="2">LV </font><font size="3" color="#0000ff" face="Comic Sans MS">58</font></b></td>
              <td width="381" height="25" bgcolor="#D2DEFF"><b><font size="2">Race/Class </font><font size="3" color="#0000ff" face="Comic Sans MS">Barbarian/Warrior</font></b></td>
            </tr>
            <tr valign="top"> 
              <td height="25" width="140" bgcolor="#D2DEFF"> 
                <p><b><font size="2">�M�_</font></b><br>
                  <b><font size="2" color="#0000ff">�Ȃ�</font></b><font size="1"><br>(���̐_)</font>
                </p>
              </td>
              <td height="25" width="348" bgcolor="#D2DEFF"><b><font size="2">�������_</font><br>
                <font face="MS UI Gothic, �l�r �o�S�V�b�N" size="2" color="#0000ff">NFP�閧�N���u</font></b></td>
            </tr>





    <TR>
      <TD colspan="2" bgcolor="#D2DEFF"><B><FONT size="3">SV</FONT></B>

<B><FONT size="2">M</FONT></B>
<font face="Comic Sans MS" size="3" color="#800000">120�@</font></b>

<B><FONT size="2">M&F</FONT></B>
<font face="Comic Sans MS" size="3" color="#FF0000">118�@</font></b>

<B><FONT size="2">M&C</FONT></B>
<font face="Comic Sans MS" size="3" color="#0000ff">123�@</font></b>

<B><FONT size="2">M&P</FONT></B>
<font face="Comic Sans MS" size="3" color="#008000">89�@</font></b>

<B><FONT size="2">M&D</FONT></B>
<font face="Comic Sans MS" size="3" color="#404040">84�@</font></b>

    </TD>
    </TR>






            <tr valign="top"> 
              <td colspan="2" height="78" width="488" bgcolor="#D2DEFF">
                <p><b><font size="2">Comment</font> <br>
                  <font face="MS UI Gothic, �l�r �o�S�V�b�N" color="#0000ff" size="3">10th Ring�̉\Get�i���ȁ[�[�[��K�Z���ۂ��B���j<br>�œ�Grand Master��񋁂ށI<br><br>Elmire 51/Nec ��������<br>Elpy    38/Dru</font> 
                </td>
            </tr>
          </table>
          <br>
</div>
<div align="right"><br>
<table><tr>
<td><form name="r">Race:<select name="race" onChange="self.gourl(this.options[this.selectedIndex].value)">
<option value="./member.cgi?race=All&class=All&sort=" SELECTED >All</option>
<option value="./member.cgi?race=Barbarian&class=All&sort=">Barbarian</option>
<option value="./member.cgi?race=Dark Elf&class=All&sort=">Dark Elf</option>
<option value="./member.cgi?race=Dwarf&class=All&sort=">Dwarf</option>
<option value="./member.cgi?race=Erudite&class=All&sort=">Erudite</option>
<option value="./member.cgi?race=Gnome&class=All&sort=">Gnome</option>
<option value="./member.cgi?race=Half Elf&class=All&sort=">Half Elf</option>
<option value="./member.cgi?race=Halfling&class=All&sort=">Halfling</option>
<option value="./member.cgi?race=High Elf&class=All&sort=">High Elf</option>
<option value="./member.cgi?race=Human&class=All&sort=">Human</option>
<option value="./member.cgi?race=Iksar&class=All&sort=">Iksar</option>
<option value="./member.cgi?race=Ogre&class=All&sort=">Ogre</option>
<option value="./member.cgi?race=Troll&class=All&sort=">Troll</option>
<option value="./member.cgi?race=Wood Elf&class=All&sort=">Wood Elf</option>
</select>
</form></td>
<td><form name="c">Class:<select name="class" onChange="self.gourl(this.options[this.selectedIndex].value)">
<option value="./member.cgi?race=All&class=All&sort=" SELECTED >All</option>
<option value="./member.cgi?race=All&class=Bard&sort=">Bard</option>
<option value="./member.cgi?race=All&class=Cleric&sort=">Cleric</option>
<option value="./member.cgi?race=All&class=Druid&sort=">Druid</option>
<option value="./member.cgi?race=All&class=Enchanter&sort=">Enchanter</option>
<option value="./member.cgi?race=All&class=Magician&sort=">Magician</option>
<option value="./member.cgi?race=All&class=Monk&sort=">Monk</option>
<option value="./member.cgi?race=All&class=Necromancer&sort=">Necromancer</option>
<option value="./member.cgi?race=All&class=Paladin&sort=">Paladin</option>
<option value="./member.cgi?race=All&class=Ranger&sort=">Ranger</option>
<option value="./member.cgi?race=All&class=Rogue&sort=">Rogue</option>
<option value="./member.cgi?race=All&class=Shadow Knight&sort=">Shadow Knight</option>
<option value="./member.cgi?race=All&class=Shaman&sort=">Shaman</option>
<option value="./member.cgi?race=All&class=Warrior&sort=">Warrior</option>
<option value="./member.cgi?race=All&class=Wizard&sort=">Wizard</option>
</select>
</form></td>
<td><form action="./member.cgi" method="POST">
<input type=hidden name=race value="All">
<input type=hidden name=class value="All">
<input type=hidden name=sort value="level">
<input type="submit" name="master" value="���x����">
</form>
</td>
<td><form method="POST" action="./member.cgi">
<input type=hidden name=race value="All">
<input type=hidden name=race value="All">
<input type=hidden name=sort value="">
<input type=hidden name=page value="10">
<input type=hidden name=mode value="page">
<input type=submit value="����10��">
</form></td>
<td><form method="POST" action="./member.cgi">
<input type=hidden name=race value="All">
<input type=hidden name=race value="All">
<input type=hidden name=sort value="">
<input type=hidden name=allview value="1">
<input type=submit value="�Ȉ�View">
</form></td>
</tr></table>
</div>


<div align="right">
	<form action="./member.cgi" method="POST">
    <input type=hidden name=mode value="admin">
    <input type="submit" name="master" value="�Ǘ��җp�t�H�[����">
    </form>
</div>

</body></html>
