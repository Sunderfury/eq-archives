<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=x-sjis">
<title>��Ȃ��Ƃ������� JavaScript BBS</title>
<SCRIPT language="JavaScript">
<!--
function viewForm(bf,name) {
  var obj;
  if (document.all) { obj = document.all(name).style; }
  else if (document.getElementById) { obj = document.forms[name].style; }
  if(obj){
    if (obj.display == 'block') {
      obj.display = 'none';
      if(name == "newmsg") { bf.value="�V �K �� �e"; } else { bf.value="�� �M"; }
    } else {
      obj.display = 'block';
      bf.value="���e��������";
    }
    if (document.all) bf.blur();
  }
}
// -->
</SCRIPT>
<STYLE>
<!--
A {
text-decoration:none;
}
input.btn {
background-color:#FF3366;
color:#FFFFFF;
}
textarea,input.txt {
background-color:#FFFBF0;
}
-->
</STYLE>
</HEAD>
<body bgcolor=#E1F0F0 text=#000000 link=#0000FF vlink=#0000FF alink=#FF0000>
<A name="top"></A><TABLE width="100%" border=0 cellspacing=0><TR><TD>
<font color=#DD0000 size=5 face="�l�r �o�S�V�b�N"><b>��Ȃ��Ƃ������� JavaScript BBS</b></font>
</TD><TD align="right" nowrap><SMALL> 
[<a href="http://www.suisen.sakura.ne.jp/~ikitai/js/" target='_top'>���ǂ�</a>]
[<a href="./petit.cgi?mode=howto">�g����</a>]
[<a href="./petit.cgi?mode=find">���[�h����</a>]
[<a href="./petit2.cgi">�ߋ����O</a>]
[<a href="./petit.cgi?mode=msg_del">�L���폜</a>]
[<a href="./petit.cgi?mode=admin">�Ǘ��p</a>]
</SMALL></TD></TR></TABLE><HR><blockquote>
<FORM method="POST" action="./petit.cgi">
 <INPUT type="submit" class="btn" value="�� �� ��"></FORM>
<form name="newmsg" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">

<TABLE border=0 cellspacing=0>
<TR><TD nowrap><b>���Ȃ܂�</b></TD>
<TD><input type=text name=name size="20" value="" class="txt"></TD></TR>
<TR><TD nowrap><b>�d���[��</b></TD>
<TD><input type=text name=email size="20" value="" class="txt"></TD></TR>
<TR><TD nowrap><b>��@�@��</b></TD>
<TD><input type=text name=subj size="25" class="txt"> <input type=submit value="���e����" class="btn"> <input type=reset value="���Z�b�g" class="btn"></TD></TR>
<TR><TD colspan=2><b>�R�����g</b><br><textarea cols="56" rows=7 name=comment wrap="off"></textarea></TD></TR>
<TR><TD nowrap><b>�t�q�k</b></TD>
<TD><input type=text size="50" name=url value="http://" class="txt"></TD></TR>
<TR><TD nowrap><b>�폜�L�[</b></TD>
<TD><input type=password name=pwd size=8 maxlength=8 value="" class="txt"><small>(�����̋L�����폜���Ɏg�p�B�p������8�����ȓ�)</small></TD></TR>
<TR><TD nowrap><b>�����F</b></TD>
<TD>
<input type=radio name=color value="800000" checked><font color=800000>��</font>
<input type=radio name=color value="DF0000"><font color=DF0000>��</font>
<input type=radio name=color value="008040"><font color=008040>��</font>
<input type=radio name=color value="0000FF"><font color=0000FF>��</font>
<input type=radio name=color value="C100C1"><font color=C100C1>��</font>
<input type=radio name=color value="FF80C0"><font color=FF80C0>��</font>
<input type=radio name=color value="FF8040"><font color=FF8040>��</font>
<input type=radio name=color value="000080"><font color=000080>��</font>
</TD></TR></TABLE></form></blockquote>

<center><A name="0"></A><TABLE WIDTH=95% BORDER=1 CELLPADDING=3 CELLSPACING=0 bgcolor=#FFFFFF>
<TR align=center bgcolor=#FFFBF0><TD nowrap width=1%><B>NO</B></TD><TD nowrap width=5%><small><B>���񓊍e��</B></small></TD><TD nowrap width=5%><small><B>�ŏI���e��</B></small></TD><TD nowrap width=5%><small><B>�ŏI���e����</B></small></TD><TD width=84%><small><B>�^ �C �g ��</B></small></TD></TR><TR>
<TD nowrap width=1%><A href="#1" style="color:black"><small>[331]</small></A></TD><TD nowrap width=5%><A href="#1" style="color:black"><small>������</small></A></TD><TD nowrap width=5%><A href="#1" style="color:black"><small>������</small></A></TD><TD nowrap width=5%><A href="#1" style="color:black"><small>2001/07/26 11:01:26</small></A></TD>
<TD width=84%><A href="#1" style="color:black"><small>�ԉ΁E�摜�őł��グ��ʂ��E�E</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#2" style="color:black"><small>[338]</small></A></TD><TD nowrap width=5%><A href="#2" style="color:black"><small>akig</small></A></TD><TD nowrap width=5%><A href="#2" style="color:black"><small>akig</small></A></TD><TD nowrap width=5%><A href="#2" style="color:black"><small>2001/07/24 20:24:19</small></A></TD>
<TD width=84%><A href="#2" style="color:black"><small>���������ɗ��܂�����</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#3" style="color:black"><small>[337]</small></A></TD><TD nowrap width=5%><A href="#3" style="color:black"><small>�U�L��</small></A></TD><TD nowrap width=5%><A href="#3" style="color:black"><small>�U�R�m</small></A></TD><TD nowrap width=5%><A href="#3" style="color:black"><small>2001/07/23 23:12:09</small></A></TD>
<TD width=84%><A href="#3" style="color:black"><small>�����o���ɂ���</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#4" style="color:black"><small>[335]</small></A></TD><TD nowrap width=5%><A href="#4" style="color:black"><small>����ӂ�</small></A></TD><TD nowrap width=5%><A href="#4" style="color:black"><small>����ӂ�</small></A></TD><TD nowrap width=5%><A href="#4" style="color:black"><small>2001/07/22 22:42:10</small></A></TD>
<TD width=84%><A href="#4" style="color:black"><small>Web Player�̌��ł�</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#5" style="color:black"><small>[336]</small></A></TD><TD nowrap width=5%><A href="#5" style="color:black"><small>J.S</small></A></TD><TD nowrap width=5%><A href="#5" style="color:black"><small>Hisa���Ǘ��l</small></A></TD><TD nowrap width=5%><A href="#5" style="color:black"><small>2001/07/22 06:28:42</small></A></TD>
<TD width=84%><A href="#5" style="color:black"><small>��������</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#6" style="color:black"><small>[332]</small></A></TD><TD nowrap width=5%><A href="#6" style="color:black"><small>Mika</small></A></TD><TD nowrap width=5%><A href="#6" style="color:black"><small>Hisa���Ǘ��l</small></A></TD><TD nowrap width=5%><A href="#6" style="color:black"><small>2001/07/21 15:58:13</small></A></TD>
<TD width=84%><A href="#6" style="color:black"><small>Hisa�l��</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#7" style="color:black"><small>[333]</small></A></TD><TD nowrap width=5%><A href="#7" style="color:black"><small>�I�W�W</small></A></TD><TD nowrap width=5%><A href="#7" style="color:black"><small>�I�W�W</small></A></TD><TD nowrap width=5%><A href="#7" style="color:black"><small>2001/07/20 23:24:52</small></A></TD>
<TD width=84%><A href="#7" style="color:black"><small>���������̖��Ɛ�~�肨�؂肵�܂���</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#8" style="color:black"><small>[330]</small></A></TD><TD nowrap width=5%><A href="#8" style="color:black"><small>�e��</small></A></TD><TD nowrap width=5%><A href="#8" style="color:black"><small>Hisa���Ǘ��l</small></A></TD><TD nowrap width=5%><A href="#8" style="color:black"><small>2001/07/19 15:05:49</small></A></TD>
<TD width=84%><A href="#8" style="color:black"><small>�\�������t�@�C���������ɏ��X�ɏ������@������΁E�E</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#9" style="color:black"><small>[329]</small></A></TD><TD nowrap width=5%><A href="#9" style="color:black"><small>������������</small></A></TD><TD nowrap width=5%><A href="#9" style="color:black"><small>������������</small></A></TD><TD nowrap width=5%><A href="#9" style="color:black"><small>2001/07/16 14:46:47</small></A></TD>
<TD width=84%><A href="#9" style="color:black"><small>�ԉΉ摜�ł̐F�ɂ��Ă��������܂��B</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#10" style="color:black"><small>[328]</small></A></TD><TD nowrap width=5%><A href="#10" style="color:black"><small>���i</small></A></TD><TD nowrap width=5%><A href="#10" style="color:black"><small>���i</small></A></TD><TD nowrap width=5%><A href="#10" style="color:black"><small>2001/07/15 23:44:45</small></A></TD>
<TD width=84%><A href="#10" style="color:black"><small>�^�C�v���C�^�[�ŁE�E�E</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#11" style="color:black"><small>[327]</small></A></TD><TD nowrap width=5%><A href="#11" style="color:black"><small>�݂�</small></A></TD><TD nowrap width=5%><A href="#11" style="color:black"><small>�݂�</small></A></TD><TD nowrap width=5%><A href="#11" style="color:black"><small>2001/07/15 22:33:19</small></A></TD>
<TD width=84%><A href="#11" style="color:black"><small>���肢���܂��I</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#12" style="color:black"><small>[325]</small></A></TD><TD nowrap width=5%><A href="#12" style="color:black"><small>Youske</small></A></TD><TD nowrap width=5%><A href="#12" style="color:black"><small>Youske</small></A></TD><TD nowrap width=5%><A href="#12" style="color:black"><small>2001/07/13 21:36:38</small></A></TD>
<TD width=84%><A href="#12" style="color:black"><small>���E�B���h�E</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#13" style="color:black"><small>[326]</small></A></TD><TD nowrap width=5%><A href="#13" style="color:black"><small>����</small></A></TD><TD nowrap width=5%><A href="#13" style="color:black"><small>����</small></A></TD><TD nowrap width=5%><A href="#13" style="color:black"><small>2001/07/13 14:30:46</small></A></TD>
<TD width=84%><A href="#13" style="color:black"><small>�ԉ΁E�摜�łɂ���</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#14" style="color:black"><small>[324]</small></A></TD><TD nowrap width=5%><A href="#14" style="color:black"><small>�}����</small></A></TD><TD nowrap width=5%><A href="#14" style="color:black"><small>Hisa���Ǘ��l</small></A></TD><TD nowrap width=5%><A href="#14" style="color:black"><small>2001/07/12 14:13:27</small></A></TD>
<TD width=84%><A href="#14" style="color:black"><small>�u�摜��TABLE�̒��Łv</small></A></TD></TR>
<TR>
<TD nowrap width=1%><A href="#15" style="color:black"><small>[323]</small></A></TD><TD nowrap width=5%><A href="#15" style="color:black"><small>��鈨</small></A></TD><TD nowrap width=5%><A href="#15" style="color:black"><small>Hisa���Ǘ��l</small></A></TD><TD nowrap width=5%><A href="#15" style="color:black"><small>2001/07/10 23:30:45</small></A></TD>
<TD width=84%><A href="#15" style="color:black"><small>�͂��߂܂��ā�</small></A></TD></TR>
</TABLE></center>
<TABLE border=0 width=95%><TR><TD align=right><TABLE border=0><TR>
<TD><form method="POST" action="./petit.cgi">
<input type=hidden name=page value="15">
<input type=hidden name=mode value="page">
<input type=submit class="btn" value="����15��">
</form></TD>
</TR></TABLE></TD></TR></TABLE>
<center><A name="1"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>331</b>]�@<font color=#0000FF><b>�ԉ΁E�摜�őł��グ��ʂ��E�E</b></font>�@���e�ҁF<font color=#0000FF><b><a href=mailto:azuki@osano.design.co.jp>������</a></b></font>�@<small>���e���F2001�N07��19�� 18��26��27�b</small> </TD>
<TD align="right" nowrap><A href="#0" title="�O">��</A> <A href="#2" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="0000FF" size=2>Hisa����A����ɂ��́B<br>�����������b�ɂȂ��Ă܂��B<br>�����ɁC�A�j���́h�ԉ΁E�摜�Łh�ŐF���ύX�ł��܂��񂪁C<br>����1���肢���Ă��X�����ł��傤���H<br>���̉ԉΉ摜�łŁC�ԉ΂��J���O�ɁC�n�ォ��ԉ΂̋ʂ���ɏオ���Ă���<br>�ƌ����摜���ǉ��ł��Ȃ��ł��傤���B<br><br>�ԉ΂̋ʂ��n�ォ��オ���Ă����C�ԉ΂��J���ƌ��������Ȃ�ł����E�E<br><br>�C���^�[�l�b�g��ŁC����Ȃ̂��Ȃ����ȂƎv���������Ă݂܂������C<br>�����p�ꂪ�����̂��C�Ȃ��Ȃ������鎖���o���܂���ł����̂ŁC<br>�����܂����Ǝv���̂ł����X�������肢�������܂��B</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>�ł��グ�����͖ʓ|�œ���Ȃ������̂ł��B<br>�C�������������悤�Ǝv���Ă��񂾂��ǖY��Ă�(^^;<br>�b�����҂����ߓ����ɓ���Ă݂܂��B </FONT><FONT size=1><EM>(2001/07/21 16:02:50)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>�������ɁC�A�j���́h�ԉ΁E�摜�Łh�ŐF���ύX�ł��܂��񂪁C<br>�o�����猩���ĖႦ�܂��񂩁H<br>�����Ƃ����A�h�o�C�X�ł��邩������܂���B </FONT><FONT size=1><EM>(2001/07/21 16:03:53)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>3</B>]</FONT></TD><TD valign=top><FONT size=2><B>������</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>Hisa����A����ɂ��́B<br>�����������b�����Đ\���󂠂�܂���B<br><br>���Z�����Ƃ͎v���܂����C�ł��グ�ԉ΋X�������肢�������܂��B<br>�y���݂ɂ��Ă���܂��B<br><br>����ƁA�摜�E�ԉ΂̐F�̌��Ȃ�ł����C<br>IE�ł͂Ȃ��COE5.5�̃��[����ʂŐF���ω����܂���B<br>Hisa�����HTML���[���Ŏg�����Q�l�ɃX�N���v�g��ύX���Ă܂����E�E�E<br>�Ȃ����F���ω����܂���B<br><br>[329]�̓��e�ҁF������������������ω����Ȃ��l�ł����E�E�E�B<br>�ԉ΂Ɏg���摜��,�Ⴆ�ΐ��̉摜���g���ꍇ�@���̉��̘g�����̂��́@<br>���g��Ȃ��Ƃ����Ȃ��̂ł��傤���H<br>�g�̒����ԂƂ��̐F�œh��Ԃ����摜���ʖڂȂ̂ł��傤���B<br>�X�������肢�������܂� </FONT><FONT size=1><EM>(2001/07/22 11:17:28)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>4</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>&gt;IE�ł͂Ȃ��COE5.5�̃��[��<br>IE�œ����Ȃ�OE�̎d�l�����H�B<br><br>���Ȃ݂ɉ摜�Ƃ��𓮂����Ɛ���CPU�p���[��H���̂�<br>�摜�̃A�j���ɗ]��p���[�����Ȃ��̂ł�ł��B<br>�ł�����gif�A�j���̃A�j���X�s�[�h�͐����������Ȃ��ƐF���ς��܂���B<br>�����̊��ł���gif�A�j���̃X�s�[�h�͎��ۂ̑�����1/10�ȉ����炢�ɂȂ�܂��B<br><br>���g�̒����ԂƂ��̐F�œh��Ԃ���<br>�ǂ��Ӗ���������܂���(^^;<br>�w�i�̂��Ƃ��ȁH </FONT><FONT size=1><EM>(2001/07/22 19:19:10)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>5</B>]</FONT></TD><TD valign=top><FONT size=2><B>������</B></FONT></TD>
<TD valign=top><FONT color=FF80C0 size=2>Hisa����A����ɂ��́B<br>���̐���������ł����܂���ł����B<br><br>���g�̒����ԂƂ��̐F�œh��Ԃ����E�E�E�E�E<br>�̐����ł���,�w�i�̎��ł͂Ȃ�,�摜�̎��Ȃ�ł����B<br>�܂�A���̉摜�̏ꍇ�g�ƌ������֊s�̎��ł��B���̉摜���֊s�����̉摜��<br>���̒��̐F���h��Ԃ��ĂȂ��摜�ƌ��������������������̂ł����B<br>�����܂���ł����B<br><br>����ƁA<br>&gt;�ł�����gif�A�j���̃A�j���X�s�[�h�͐����������Ȃ��ƐF���ς��܂���B<br>�A�j���X�s�[�h�͉�����ύX����Ηǂ��̂��������Ē����Ȃ��ł��傤���B<br>var speed = 5;�̂T��ύX����Ηǂ��̂ł��傤���B<br>�X�������肢�������܂��B </FONT><FONT size=1><EM>(2001/07/25 14:06:03)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>6</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>���[����������GIF�A�j�����������ĂȂ��H<br><br>�摜�̐F�̕ω���JavaScript�̋@�\����Ȃ�����Ȃ�GIF�A�j���ł���B<br>�����畁�ʂ̉摜�͑ʖڂł���B<br><br>GIF�A�j����<br><a href=http://www.suisen.sakura.ne.jp/~ikitai/js/anime/images/star.gif target=_top>http://www.suisen.sakura.ne.jp/~ikitai/js/anime/images/star.gif</a><br><a href=http://www.suisen.sakura.ne.jp/~ikitai/js/anime/images/star2.gif target=_top>http://www.suisen.sakura.ne.jp/~ikitai/js/anime/images/star2.gif</a><br><a href=http://www.suisen.sakura.ne.jp/~ikitai/js/anime/images/ball.gif target=_top>http://www.suisen.sakura.ne.jp/~ikitai/js/anime/images/ball.gif</a> </FONT><FONT size=1><EM>(2001/07/25 17:46:43)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>7</B>]</FONT></TD><TD valign=top><FONT size=2><B>������</B></FONT></TD>
<TD valign=top><FONT color=FF8040 size=2>Hisa����A����ɂ��́B<br><br>�ԉ΁E�摜�ŏo���܂����B<br>Hisa���񂪌�����Ƃ���GIF�摜���������Ă܂���ł����B<br>�摜�̐F��,JavaScript�ŕύX���Ă���Ǝv���Ă܂����̂�,�ω����Ȃ��̂�������܂��ł��ˁB<br>�ǂ����L���������܂����B����Ƃ��X�������肢�������܂��B </FONT><FONT size=1><EM>(2001/07/26 11:01:26)</EM></FONT></TD></TR>

</TABLE>

<form name="res_331" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="331">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="2"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>338</b>]�@<font color=#0000FF><b>���������ɗ��܂�����</b></font>�@���e�ҁF<font color=#0000FF><b><a href=mailto:aki@pp.104.net>akig</a></b></font>�@<small>���e���F2001�N07��24�� 20��24��19�b</small> <a href="http://www2.ocn.ne.jp/~akit/" target=_top><img src="./home.gif" border=0 align=top HSPACE=10 WIDTH="25" HEIGHT="22"></a></TD>
<TD align="right" nowrap><A href="#1" title="�O">��</A> <A href="#3" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="FF80C0" size=2>����ɂ��́A���v���Ԃ�ł��E�E�E���Č����Ă��o���Ă���������Ȃ��Ǝv���܂����E�E�E<br>�����́A�ԉ΂̉摜�ł𒸂��čs���܂���<br>�i�v���Ԃ�ɓ��ӂłȂ�JS�Ɗi�����悤�Ǝv���܂��āE�E�E�j<br>�܂����܂������撣���Ă���������</font></blockquote>

<form name="res_338" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="338">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="3"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>337</b>]�@<font color=#0000FF><b>�����o���ɂ���</b></font>�@���e�ҁF<font color=#0000FF><b><a href=mailto:nisekisi935@geocities.co.jp>�U�L��</a></b></font>�@<small>���e���F2001�N07��22�� 22��47��14�b</small> </TD>
<TD align="right" nowrap><A href="#2" title="�O">��</A> <A href="#4" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="FF8040" size=2>�͂��߂܂��āA�g�������l�B<br>������̃X�N���v�g���Q�l�ɂ��ăy�[�W������Č��܂����B<br>�����̃p�\�R���ł͓����̂ł����A�A�b�v��������X�N���v�g�G���[���o�Ă��܂��܂��B<br>�ǂ����ɊԈႢ������Ǝv���̂ł����A���Ȃ����Ă݂Ă�����܂���B<br>�\���󂲂����܂��񂪁A���Ă��������܂���ł��傤���H<br><br><a href=http://cocofree.com/nisekisi/gallery/totugeki.html target=_top>http://cocofree.com/nisekisi/gallery/totugeki.html</a><br><br>�����ł��B<br>��낵�����肢���܂��B</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>�J�n�^�O��&lt;SCRIPT&gt;�������ł��ˁB </FONT><FONT size=1><EM>(2001/07/23 08:07:53)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>�U�R�m</B></FONT></TD>
<TD valign=top><FONT color=0000FF size=2>���肪�Ƃ��������܂��A��{�I�ȊԈႢ�ł����i�O�O�G�j<br>���Z�����Ƃ���A�{���Ɍ䐢�b�ɂȂ�܂����B </FONT><FONT size=1><EM>(2001/07/23 23:12:09)</EM></FONT></TD></TR>

</TABLE>

<form name="res_337" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="337">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="4"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>335</b>]�@<font color=#0000FF><b>Web Player�̌��ł�</b></font>�@���e�ҁF<font color=#0000FF><b><a href=mailto:s_minami@cty-net.ne.jp>����ӂ�</a></b></font>�@<small>���e���F2001�N07��21�� 14��08��07�b</small> <a href="http://www6.tkcity.net/~tail/player/player.html" target=_top><img src="./home.gif" border=0 align=top HSPACE=10 WIDTH="25" HEIGHT="22"></a></TD>
<TD align="right" nowrap><A href="#3" title="�O">��</A> <A href="#5" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="000080" size=2>Web Player�A���؂肵�܂����B<br>�ł����̂��A�G���[���o�Ă��܂��܂��B<br>���S�҂Ȃ̂ŋȏ����������ɁA�����~�X�����Ă���ɈႢ�Ȃ��̂ł����A<br>���x���Ă�������܂���B<br>���݂܂���B�����Ă��������Ȃ��ł��傤���H<br>�Ƃ肠�������Ă���������悤�AWeb��ɏo���Ă݂܂����B<br><br><a href=http://www6.tkcity.net/~tail/player/player.html target=_top>http://www6.tkcity.net/~tail/player/player.html</a><br>�ł��B<br>���肢���܂��B<br>�@</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>""http://�`�`�`"<br>�̐擪��"���Q���邽�߂ł��ˁB </FONT><FONT size=1><EM>(2001/07/21 15:51:15)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>����ӂ�</B></FONT></TD>
<TD valign=top><FONT color=000080 size=2>�����I�ȃ~�X�ł��ˁi���j�B<br>���݂܂���A���肪�Ƃ��������܂��B<br>�ł��A���x�͍Đ����悤�Ƃ���ƃG���[���o���ł����c�c�c�B<br>�܂��A�������������Ă��ł��傤���H </FONT><FONT size=1><EM>(2001/07/21 20:53:34)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>3</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>mid�t�@�C�����A�b�v���[�h����ĂȂ��݂����ł����B<br>�܂���URL���Ԉ���Ă邩�ł��ˁB </FONT><FONT size=1><EM>(2001/07/22 06:30:43)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>4</B>]</FONT></TD><TD valign=top><FONT size=2><B>����ӂ�</B></FONT></TD>
<TD valign=top><FONT color=000080 size=2>���肪�Ƃ��������܂��B<br>URL�ԈႢ�ł���(^^;)�B<br>�Ȃ�����̃t�H���_�ɁE�E�E�i���j<br>���������܂ŁA���x�͂����Ɠ����܂�����<br>�����A���Ƃ͐ݒu���[���I </FONT><FONT size=1><EM>(2001/07/22 22:42:10)</EM></FONT></TD></TR>

</TABLE>

<form name="res_335" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="335">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="5"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>336</b>]�@<font color=#0000FF><b>��������</b></font>�@���e�ҁF<font color=#0000FF><b>J.S</b></font>�@<small>���e���F2001�N07��21�� 21��23��11�b</small> </TD>
<TD align="right" nowrap><A href="#4" title="�O">��</A> <A href="#6" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="800000" size=2>���Ђ��`�AHisa����m���Ă��狳���āI<br>JS����<br>	print "Content-type: text/html\n\n";<br>	print &lt;&lt;"EOF";<br>	&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN"&gt;<br>	&lt;HTML&gt;<br>        &lt;META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=euc-jp"&gt;<br>�ƌ���������print��html���o�͂����Ƃ��A�u���E�U�̐ݒ�𕶎��R�[�h�Z�b�g�������ɂ��Ă��Ă�EUC�𔻕ʂ��Ă���܂���B<br>reload�����肷��Ɖ��������̂ł����B���Ȃ݂Ƀu���E�U��NN4.7�ł��BIE�̏ꍇ�����������܂���B<br>NN�ł͂����������̂Ȃ̂��AJS����HTML���o�͂��鎞�ɍl���_������̂��킩��܂���B<br>��낵�����肢���܂��B</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>�ǂ��A���Ђ�<br><a href=http://tohoho.wakusei.ne.jp/wwwxx005.htm target=_top>http://tohoho.wakusei.ne.jp/wwwxx005.htm</a><br>�������Q�l�ɂȂ�܂����B </FONT><FONT size=1><EM>(2001/07/22 06:27:44)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>���Ȃ݂ɂ����ł͂����������ɂ͂Ȃ������Ɠ��ł��ˁB<br>�Ȃ�ł��낤�H </FONT><FONT size=1><EM>(2001/07/22 06:28:42)</EM></FONT></TD></TR>

</TABLE>

<form name="res_336" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="336">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="6"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>332</b>]�@<font color=#0000FF><b>Hisa�l��</b></font>�@���e�ҁF<font color=#0000FF><b>Mika</b></font>�@<small>���e���F2001�N07��20�� 11��15��45�b</small> <a href="http://homepage1.nifty.com/thama/" target=_top><img src="./home.gif" border=0 align=top HSPACE=10 WIDTH="25" HEIGHT="22"></a></TD>
<TD align="right" nowrap><A href="#5" title="�O">��</A> <A href="#7" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="DF0000" size=2>����ɂ��́B���������b�ɂȂ��Ă���܂��Bm(__)m<br><br>����̌ߑO���Ƀh�C�c����A���Ă��܂����B<br><br>�������j���[�̃f�X�N�g�b�vPC.Me��PAGE�̍X�V�Ȃǂ��Ă܂����B<br>XP�͗��N�ɂ������̂悤�ł��ˁB(^_^;)<br><br>IBM�̉t���f�B�X�v���C�c�C�ɂȂ�h�^�񒆂Ƀh�b�g�R�ꂪ����A<br>�����^�����������悤�ȋC�����܂��B(^_^;)<br>LAM��256�ɂ��A�˂ɃV�X�e�����\�[�X���`�F�b�N���A70�`80����<br>���ɂ������Ă��܂��B<br><br>����ƁA���F���u���v�ɂȂ��Ă��܂��A�A�A�z�R�����߂����āA�A�A<br>���́[�AHisa�l�̃T�C�g�ɍ��10�����炢�ɃA�N�Z�X�����̂ł����A<br>�u�y�[�W���\������܂���v�Əo�܂����B���x�����킵���̂ł����A<br>(^_^;)�c�_���ł����B(^_^;;<br><br>�Y�[���̃X�N���v�g���R�s�[���悤�Ǝv�����̂ł����c(^_^;;</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Mika</B></FONT></TD>
<TD valign=top><FONT color=FF8040 size=2>Hisa�l�A����ɂ��́B<br><br>���́A���j���[��PC�ł̍X�V�̍ۂ��uLINKS.1.2.3�v��PAGE�́A<br>�u�^�C���Y �G���[���������܂���!�f�o�b�N���܂���?�v�Əo��<br>���܂�����������܂���B<br><br>��͂�\�[�X�ɖ�肪����̂ł��傤��? </FONT><FONT size=1><EM>(2001/07/21 14:19:21)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>���A��`(^^)<br>������ƁA���F���u���v�ɂȂ��Ă��܂�<br>�́A�������������Ă܂���(^^)<br>�����ڗ������łȂ����i�G��Ƃ���͉����o�Ă��āE�E�E�E(&gt;&lt;)<br><br>�����10�����炢�ɃA�N�Z�X�����̂ł����A<br>������22������25�����炢�܂ł͉���d���ł��ˁB<br>�����z�������Ƃ��l���e���̂ł����Ȃ��Ȃ��ǂ��Ƃ��낪������<br><br>���u�^�C���Y �G���[���������܂���!�f�o�b�N���܂���?�v�Əo��<br>�����ł͏o�Ȃ��̂ł�����Ɣ���܂���HTML�I�ɕs�����Ƃ��낪����̂�<br>����������Ύ��邩���H�B<br>�F�X����̂Ō��MAIL���܂��́B </FONT><FONT size=1><EM>(2001/07/21 15:58:13)</EM></FONT></TD></TR>

</TABLE>

<form name="res_332" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="332">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="7"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>333</b>]�@<font color=#0000FF><b>���������̖��Ɛ�~�肨�؂肵�܂���</b></font>�@���e�ҁF<font color=#0000FF><b><a href=mailto:ogg@abelia.ocn.ne.jp>�I�W�W</a></b></font>�@<small>���e���F2001�N07��20�� 23��24��52�b</small> <a href="http://www6.ocn.ne.jp/~ogg/" target=_top><img src="./home.gif" border=0 align=top HSPACE=10 WIDTH="25" HEIGHT="22"></a></TD>
<TD align="right" nowrap><A href="#6" title="�O">��</A> <A href="#8" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="800000" size=2>�͂��߂܂��ăI�W�W�Ƃ����܂��B<br>�z�[���y�[�W�ɓ������~�����Ǝv���Ă���܂����Ƃ���A<br>�^�ǂ������ɂ��ǂ蒅���v���Ă������̂������葁��<br>���������̖��Ɛ�~�肨�؂肵�܂����B<br>�{���ɗL��������܂����B</font></blockquote>

<form name="res_333" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="333">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="8"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>330</b>]�@<font color=#0000FF><b>�\�������t�@�C���������ɏ��X�ɏ������@������΁E�E</b></font>�@���e�ҁF<font color=#0000FF><b>�e��</b></font>�@<small>���e���F2001�N07��19�� 00��43��25�b</small> </TD>
<TD align="right" nowrap><A href="#7" title="�O">��</A> <A href="#9" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="0000FF" size=2>����ɂ��̓e���Ɛ\���܂��B<br>�����Ō����̂��o���Ă��Ȃ��̂ł����A�����̃T�C�g�ł�<br>Flash�iswf�j��\�����āA�A�j���[�V�������I���<br>���X�ɏ����čs���܂����B�X�[�[�ƌ��������ŏ��X�ɔw�i��������<br>�s���悤�Ȋ����ɂł��B<br><br>�����Flash�쐬�ɂ��Ă̎��₪�o���鎿��f���Ŏ��₵����<br>�W���o�X�N���v�g�������Ɏg���Ώo����悤�Ȏ��������Ă���܂����B<br>�����ł����A�����u�\�����Ă��镨�����b��ɏ��X�ɏ����v<br>�ƌ��������̖��ߕ��ł����Ǝv���̂ł���<br>�������̐����ŕ�����悤�ł������낵�����w�����������B</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>TOP�ɒǉ����܂����B<br><a href=http://www.suisen.sakura.ne.jp/~ikitai/js/filter/alpha4.shtml target=_top>http://www.suisen.sakura.ne.jp/~ikitai/js/filter/alpha4.shtml</a> </FONT><FONT size=1><EM>(2001/07/19 15:05:49)</EM></FONT></TD></TR>

</TABLE>

<form name="res_330" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="330">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="9"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>329</b>]�@<font color=#0000FF><b>�ԉΉ摜�ł̐F�ɂ��Ă��������܂��B</b></font>�@���e�ҁF<font color=#0000FF><b>������������</b></font>�@<small>���e���F2001�N07��16�� 07��55��26�b</small> <a href="http://ww2.wt.tiki.ne.jp/~mafumin/" target=_top><img src="./home.gif" border=0 align=top HSPACE=10 WIDTH="25" HEIGHT="22"></a></TD>
<TD align="right" nowrap><A href="#8" title="�O">��</A> <A href="#10" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="000080" size=2>����ɂ��́B<br>����͂��肪�Ƃ��������܂����B<br><br>�ԉΉ摜�ł̐F�ɂ��Ă������������̂ł����E�E�E<br>�摜���w�肵�Ă����{�̂悤�ȐF�ɕω����܂���B<br>���Ƃ̉摜�̐F�̂܂܃`�J�`�J���܂��B<br><br>�{���ɏ����I�Ȏ���Ő\���󂠂�܂���<br>�����Ă��������܂��񂩁H<br><br>���ʂȉ摜���g���Ă���̂ł��傤���H<br>���萔�����������܂�����낵�����肢�v���܂��B</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>���[��A���ʂ̃A�j��gif���g���Ă邾���ł����B<br>�����A�j������Speed�͉��葁�����Ă܂��B<br>��������Speed�̏��ׂ��Ǝv���܂��B </FONT><FONT size=1><EM>(2001/07/16 13:26:24)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>������������</B></FONT></TD>
<TD valign=top><FONT color=000080 size=2>����ɂ��́B<br>�����̂��Ԏ����肪�Ƃ��������܂��B<br><br>�����ł����`�`�A���ʂ̃A�j���Ȃ�ł����E�E�E<br>�܂����낢��Ǝ����Ă݂܂���<br>�ǂ������肪�Ƃ��������܂���m(u u)m </FONT><FONT size=1><EM>(2001/07/16 14:46:47)</EM></FONT></TD></TR>

</TABLE>

<form name="res_329" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="329">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="10"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>328</b>]�@<font color=#0000FF><b>�^�C�v���C�^�[�ŁE�E�E</b></font>�@���e�ҁF<font color=#0000FF><b>���i</b></font>�@<small>���e���F2001�N07��14�� 13��15��44�b</small> </TD>
<TD align="right" nowrap><A href="#9" title="�O">��</A> <A href="#11" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="C100C1" size=2>�͂��߂܂��āB<br>�u�^�C�v���C�^�[�v�����������Đݒu���Ă݂��̂ł����A<br>�ӂ��߂̃Z���e���X�ist[1]�j��ύX����ƃG���[��<br>�o�ē����Ȃ��Ȃ��Ă��܂��܂��B�ЂƂ߁i[st0]�j����<br>��ύX�����ꍇ�ɂ͂��܂������̂ł����E�E�E�B<br>��낵�����肢�������܂��B</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>�ǂ̗l�ɕύX���܂������H<br>���������Ȃ����ᕪ����܂��� </FONT><FONT size=1><EM>(2001/07/15 06:05:31)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>���i</B></FONT></TD>
<TD valign=top><FONT color=C100C1 size=2>�Ȃ�Ƃ������悤�ɂȂ����݂����ł��B<br>���肪�Ƃ��������܂����B </FONT><FONT size=1><EM>(2001/07/15 23:44:45)</EM></FONT></TD></TR>

</TABLE>

<form name="res_328" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="328">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="11"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>327</b>]�@<font color=#0000FF><b>���肢���܂��I</b></font>�@���e�ҁF<font color=#0000FF><b><a href=mailto:daizy@titan.ocn.ne.jp>�݂�</a></b></font>�@<small>���e���F2001�N07��14�� 08��21��48�b</small> </TD>
<TD align="right" nowrap><A href="#10" title="�O">��</A> <A href="#12" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="000080" size=2>���g�o���쐬���ł����A������̂g�o�����Ăi�r�𒸂�����΂��Ă��܂��B<br>���肪���������܂��B<br>�����I�Ȏ���ł����悢�ł��傤���H<br>�u����~�点��v�͏o���܂����B�����Ă��̏�Ƀ��C���[���̂�����ł����A<br>�Ⴊ�ǂ����Ă����C���[�̏�ɍ~���ł��B�z�[���y�[�W�r���_�[��<br>�쐬���Ă��ł����E�E�E�E�ǂ����Ăł��傤�H<br>��낵�����肢���܂��B</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>script��z-index���w�肵�Ă邽�߂ł��B<br>�`�` Z-INDEX: "+ i +";�`�`<br>��<br>�`�` Z-INDEX: ?;�`�`<br>�ƕς��Ă݂Ă��������B<br>�H��z-index�̒l�B </FONT><FONT size=1><EM>(2001/07/15 06:04:37)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>�݂�</B></FONT></TD>
<TD valign=top><FONT color=000080 size=2>���Ԏ����肪�Ƃ��������܂��B<br>���������Ă݂܂��B </FONT><FONT size=1><EM>(2001/07/15 22:17:23)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>3</B>]</FONT></TD><TD valign=top><FONT size=2><B>�݂�</B></FONT></TD>
<TD valign=top><FONT color=000080 size=2>�o���܂�����ق�Ƃɂ��肪�Ƃ��������܂����B<br>�g�o�o�������莟��A���񍐁������N�\�点�Ă��������܂��B<br>���̂��Ƃ��A�T�b�p���킩��܂��񂪁E�E�E����΂�܂��B<br>�܂���������΂��肢���܂��B </FONT><FONT size=1><EM>(2001/07/15 22:33:19)</EM></FONT></TD></TR>

</TABLE>

<form name="res_327" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="327">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="12"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>325</b>]�@<font color=#0000FF><b>���E�B���h�E</b></font>�@���e�ҁF<font color=#0000FF><b><a href=mailto:fumio.takizawa@nifty.com>Youske</a></b></font>�@<small>���e���F2001�N07��11�� 23��14��17�b</small> </TD>
<TD align="right" nowrap><A href="#11" title="�O">��</A> <A href="#13" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="C100C1" size=2>���v���Ԃ�ł��B<br>������ƕ��������̂ł����A<br>&lt;script language="JavaScript"&gt;<br>&lt;!--<br>function MM_openBrWindow(theURL,winName,features) { //v2.0<br>  window.open(theURL,winName,features);<br>}<br>// --&gt;<br>&lt;/script&gt;<br>�������āA<br>&lt;a href="#" onclick="MM_openBrWindow('sub.htm','sub','scrollbars=yes,width=400,height=225')"&gt;<br>���y�[�W�̉��̂ق��Ŏ��s����ƁA����Ƀy�[�W���X�N���[�����Ă��܂��̂͂Ȃ��ł���?<br>����������ł����܂��񂪁A�����Ă��������B</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>onclick="�`�`�`;return false"<br>�Ƃ��Ȃ���<br>href="#"<br>����������ł��B<br><br>������ɂ������ȁH<br>�悤��onclick�̍Ō��return false�����Ȃ���<br>#�ƌ��������N���N���b�N�������ƂɂȂ�̂ł��B </FONT><FONT size=1><EM>(2001/07/12 14:11:36)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>Youske</B></FONT></TD>
<TD valign=top><FONT color=C100C1 size=2>�ł���悤�ɂȂ�܂����B<br>�������肪�Ƃ��������܂��B </FONT><FONT size=1><EM>(2001/07/13 21:36:38)</EM></FONT></TD></TR>

</TABLE>

<form name="res_325" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="325">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="13"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>326</b>]�@<font color=#0000FF><b>�ԉ΁E�摜�łɂ���</b></font>�@���e�ҁF<font color=#0000FF><b>����</b></font>�@<small>���e���F2001�N07��12�� 22��22��32�b</small> <a href="http://uo.net/i/k-ao" target=_top><img src="./home.gif" border=0 align=top HSPACE=10 WIDTH="25" HEIGHT="22"></a></TD>
<TD align="right" nowrap><A href="#12" title="�O">��</A> <A href="#14" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="800000" size=2>�����b�l�ł��B<br>�ԉ΁E�摜�ł��g�킹�Ē����܂������A���Ɏg���Ă���MARQUEE�̓�����<br>�ԉ΂̕\�����͎~�܂莟�ɉԉ΂��\�������Ԃ��������A�Ƃ�����Ԃ�<br>�Ȃ��Ă��܂��A�ԉ΂̎g�p���~�߂܂����B<br>���P�􂪗L��܂����狳���Ē����܂��ł��傤���H</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>���P��͑���CPU�ɕς���Ώ����́E�E�E </FONT><FONT size=1><EM>(2001/07/13 03:15:47)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>���<br>var fireNo = 6;<br>var wa = 4;<br>�̐���������������Ώ����́E�E�E </FONT><FONT size=1><EM>(2001/07/13 03:17:32)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>3</B>]</FONT></TD><TD valign=top><FONT size=2><B>����</B></FONT></TD>
<TD valign=top><FONT color=800000 size=2>m(_ _)m���݂܂���@�������܂����B�E�E�E<br>�g�����y�[�W�̓��͕����������̈�MARQUEE�͕ʂ̂����t�@�C���̒��ɏ��������ėL�������̂ŁA�����ɉԉ΂̂����t�@�C����\�����ׂɋN�����Ǐ�ł����B<br>��̃t�@�C���ɂ�����A�ǂ������薳�������Ă���܂����B<br>���̊Ԉ�����g�p�@�ł��������������܂����B���l�ѐ\���グ�܂��B </FONT><FONT size=1><EM>(2001/07/13 14:30:46)</EM></FONT></TD></TR>

</TABLE>

<form name="res_326" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="326">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="14"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>324</b>]�@<font color=#0000FF><b>�u�摜��TABLE�̒��Łv</b></font>�@���e�ҁF<font color=#0000FF><b><a href=mailto:mamuchi_s@hotmail.com>�}����</a></b></font>�@<small>���e���F2001�N07��10�� 14��06��15�b</small> <a href="http://www.kitanet.ne.jp/~kono/" target=_top><img src="./home.gif" border=0 align=top HSPACE=10 WIDTH="25" HEIGHT="22"></a></TD>
<TD align="right" nowrap><A href="#13" title="�O">��</A> <A href="#15" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="000080" size=2>�͂��߂܂��āB<br>�����u����~�点��v�̂��낢��ȉ��p���g�킹�Ē����Ă܂��B<br>�����͐V�����A�b�v�����u�摜��TABLE�̒��Łv��<br>�u��(�E)����E(��)�֓������v�Ƒg�ݍ��킹��<br>�g�킹�ĖႨ���Ǝv�����̂ł����Ascript�̃\�[�X�̐^�񒆓������<br><br>document.write("&lt;layer name=\"dot"+ i +"\" left=\"15\" top=\"15\" <br>visibility=\"show\"&gt;��&lt;img src=\"" + snow[j][0] + "\" <br>border=\"0\"&gt;&lt;/layer&gt;");<br><br>�����́��̏��� &lt;/HEAD&gt;&lt;BODY&gt; ������ɓ����Ă��܂��܂��B<br>&lt;img src&gt;������Ƃg�o�쐬�\�t�g�������I�ɓ���Ă��܂���ł��傤���H<br>�ǂ̗l�ɂ�����ǂ��ł��傤���H<br>��낵�����肢���܂��B</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>�g�o�쐬�\�t�g�̎�ނɂ���ĐF�X����͈Ⴄ�̂ŕ�����܂���B<br>����ȂƂ��̓������Ƃ��ł��܂��傤 </FONT><FONT size=1><EM>(2001/07/10 23:28:42)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>�}����</B></FONT></TD>
<TD valign=top><FONT color=000080 size=2>���Ԏ����肪�Ƃ��������܂����B<br>�������ł������o���܂����B<br><br>����ǁA���̃y�[�W�̑��̕�������������<br>���Ȃ���΂Ȃ�Ȃ���ł��ˁE�E�E<br>����΂�܂��I�I�@���肪�Ƃ��������܂����B </FONT><FONT size=1><EM>(2001/07/11 15:52:05)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>3</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>JavaScript���O���t�@�C���ɂ���̂���ł��B<br><a href=http://www.oitaweb.ne.jp/hp/tatsuya/java/js.htm target=_top>http://www.oitaweb.ne.jp/hp/tatsuya/java/js.htm</a> </FONT><FONT size=1><EM>(2001/07/12 14:13:27)</EM></FONT></TD></TR>

</TABLE>

<form name="res_324" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="324">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<center><A name="15"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR>
<TD>[<b>323</b>]�@<font color=#0000FF><b>�͂��߂܂��ā�</b></font>�@���e�ҁF<font color=#0000FF><b>��鈨</b></font>�@<small>���e���F2001�N07��09�� 16��49��32�b</small> <a href="http://mebius.cside2.jp/" target=_top><img src="./home.gif" border=0 align=top HSPACE=10 WIDTH="25" HEIGHT="22"></a></TD>
<TD align="right" nowrap><A href="#14" title="�O">��</A> <A href="#16" title="��">��</A>
 <A href="#top" title="�ŏ�">��</A> <A href="#100" title="�Ō�">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="000080" size=2>�͂��߂܂��Ăł���<br>���������^���������HP���炫�܂�����<br>KOKE- GAME������������点�Ă��������܂�����<br>�iaoi_Y�͎��ł��j<br>���`��c�^�u���b�g�̎g�������������ԈႦ�Ă���悤�ȋC���c�i��<br>�ł͂���ɂĂł���</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>�^�u���b�g�g���ƊȒP�Ȃ̂��ȁH<br>�Ȃ��Ȃ��ǂ��_��(^^)<br>���Ȃ݂Ƀn�[�h�̍ō���100�_��12�b���Ă̂��ߋ��ɂ���܂��B<br>���̂͂P�x�f�[�^�폜��Ȃ�Ŏc���Ă܂��񂪁B<br>�撣���Ă݂�(^^) </FONT><FONT size=1><EM>(2001/07/10 23:30:45)</EM></FONT></TD></TR>

</TABLE>

<form name="res_323" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="323">
<input type=hidden name=page value="">
<input type=hidden name=email value="">
<input type=hidden name=url value="">
<CENTER><TABLE border=0 bgcolor=#FFFBF0>
<TR><TD nowrap align="right"><FONT size=2>���O <input type=text name=name size=10 value="" class="txt"><BR>
�����F <select name=color>
<option value="800000" selected style="color:#FFFFFF; background-color:#800000;">��
<option value="DF0000" style="color:#FFFFFF; background-color:#DF0000;">��
<option value="008040" style="color:#FFFFFF; background-color:#008040;">�݂ǂ�
<option value="0000FF" style="color:#FFFFFF; background-color:#0000FF;">��
<option value="C100C1" style="color:#FFFFFF; background-color:#C100C1;">��
<option value="FF80C0" style="color:#FFFFFF; background-color:#FF80C0;">�s���N
<option value="FF8040" style="color:#FFFFFF; background-color:#FF8040;">�I�����W
<option value="000080" style="color:#FFFFFF; background-color:#000080;">�����F
</SELECT></FONT></TD>
<TD><FONT size=2><textarea cols="56" rows=3 name=comment wrap="off"></textarea></FONT></TD>
<TD><FONT size=2><input type=password name=pwd size=4 value="" class="txt"> �폜�L�[<BR>
<INPUT type=submit value="�ԐM����" class="btn"></FONT></TD></TR></TABLE>
</CENTER></FORM>
</TD></TR></TABLE></CENTER><BR>

<TABLE border=0><TR>
<TD><form method="POST" action="./petit.cgi">
<input type=hidden name=page value="15">
<input type=hidden name=mode value="page">
<input type=submit class="btn" value="����15��">
</form></TD>
</TR></TABLE><A name="100"></A>
<br><br><center><small><!-- PETIT v4.4 -->
- <a href="http://www.kent-web.com/" target=_top>Petit Board</a> -<BR>
Script arranged by <a href="http://www.suisen.sakura.ne.jp/~ikitai/" target="_blank"><B>Hisa</B></a>
</small></center>
</body></html>
