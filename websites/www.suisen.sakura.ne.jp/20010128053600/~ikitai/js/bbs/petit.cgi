<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=x-sjis">
<title>JavaScript �T�|�[�g BBS</title>
<SCRIPT language="JavaScript">
<!--
function viewForm(bf,name) {
  var obj;
  if (document.all) { obj = document.all(name).style; }
  else if (document.getElementById) { obj = document.getElementById(name).style; }
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
<body bgcolor=#FFFFFF text=#000000 link=#0000FF vlink=#0000FF alink=#FF0000>
<A name="0"></A><TABLE width="100%" border=0 cellspacing=0><TR><TD>
<font color=#DD0000 size=5 face="�l�r �o�S�V�b�N"><b>JavaScript �T�|�[�g BBS</b></font>
</TD><TD align="right" nowrap><SMALL> 
[<a href="http://www.suisen.sakura.ne.jp/~ikitai/js/" target='_top'>���ǂ�</a>]
[<a href="./petit.cgi?mode=howto">�g����</a>]
[<a href="./petit.cgi?mode=find">���[�h����</a>]
[<a href="./petit2.cgi">�ߋ����O</a>]
[<a href="./petit.cgi?mode=msg_del">�L���폜</a>]
[<a href="./petit.cgi?mode=admin">�Ǘ��p</a>]
</SMALL></TD></TR></TABLE><HR><blockquote>
<FORM>
 <INPUT type="button" class="btn" value="�� �� ��" onclick="location.href='/~ikitai/js/bbs/petit.cgi'"></FORM>
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

<center><A name="1"></A><TABLE border=1 width=95% cellpadding=5 cellspacing=0 bgcolor=#FFFFFF>
<TR><TD bgcolor=#FFFBF0>
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
[<b>159</b>]�@<font color=#0000FF><b>�͂��߂܂���</b></font>
�@���e�ҁF<font color=#0000FF><b>naomama</b></font>
�@<small>���e���F2001�N01��25�� 22��52��12�b</small> <a href="http://www.joy.hi-ho.ne.jp/naomama/" target=_top><img src="./home.gif" border=0 align=top HSPACE=10 WIDTH="25" HEIGHT="22"></a></TD>
<TD align="right" nowrap><A href="#0">��</A> <A href="#2">��</A>
 <A href="#0">��</A> <A href="#100">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="800000" size=2>�͂��߂܂��āAHTML�̃��[���f�ނ�HP�����Ă���Anaomama�ƌ����܂��B<br>�O����JavaScript���g���ă��[���f�ނ���肽���āAJava��HP��T����<br>���܂����B�������HP�ɏo����āA���ꂾ�I���Ďv���A���ꂵ���Ȃ��Ă��܂��܂����B<br>���܂��ẮA���[���Ŏg����悤�ɂ��Ă���T���v�����܂߂āA���낢��<br>�g�킹�Ă��������A����HP�Ƀ��[���f�ނƂ��čڂ������Ă������������̂ł����A<br>��낵���ł��傤���H�ǂ�����낵�����肢���܂��B<br><br>ps.�����N�t���[�Ƃ̂��Ƃł����̂ő��������N�����Ă��������܂��B(^^)</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>Script�̓]�ڂ�OK�ł����摜�͎����ŗp�ӂ��Ă��������B<br>�g�p���Ă�摜�͂���Ƃ��Ȃ��Ă�̂�OK�ł��B<br>���͎��삶��Ȃ��̂őʖڂł��B<br><br>����Ɩw�ǂ̂��͉̂������Ȃ���HTML���[���ł͎g���܂���B<br>�����̎d���͐�~��TIPS�ɂ����Ă���̂ł���������Ă��������B </FONT><FONT size=1><EM>(2001/01/26 20:27:25)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>naomama</B></FONT></TD>
<TD valign=top><FONT color=800000 size=2>�L���������܂��B<br>�����ł��Ȃ��A�����ł��Ȃ��Ƃ���Ă݂܂��B </FONT><FONT size=1><EM>(2001/01/26 22:03:14)</EM></FONT></TD></TR>

</TABLE>

<form name="res_159" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="159">
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
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
[<b>160</b>]�@<font color=#0000FF><b>���v���Ԃ�ł���</b></font>
�@���e�ҁF<font color=#0000FF><b>����</b></font>
�@<small>���e���F2001�N01��26�� 05��08��03�b</small> <a href="http://www3.ocn.ne.jp/~smile123/" target=_top><img src="./home.gif" border=0 align=top HSPACE=10 WIDTH="25" HEIGHT="22"></a></TD>
<TD align="right" nowrap><A href="#1">��</A> <A href="#3">��</A>
 <A href="#0">��</A> <A href="#100">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="FF80C0" size=2>���v���Ԃ�ł���@Hisa�����<br>��N�A�u�Ԃт�~�炵�v�ł����b�ɂȂ��������ł���i�o���Ă܂����H�j<br>�����́A�u���������̖��Q�v�̃\�[�X�𒸂��ɎQ��܂�����<br>����́A�����������܂���������<br>���N���X������肢�v���܂��B�i�͂��Ɓj</font></blockquote>

<form name="res_160" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="160">
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
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
[<b>158</b>]�@<font color=#0000FF><b>������܂����B</b></font>
�@���e�ҁF<font color=#0000FF><b><a href=mailto:aaf26770@pop06.odn.ne.jp>���V</a></b></font>
�@<small>���e���F2001�N01��25�� 19��55��11�b</small> </TD>
<TD align="right" nowrap><A href="#2">��</A> <A href="#4">��</A>
 <A href="#0">��</A> <A href="#100">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="800000" size=2>���̓��e�̃��V�ł��A�������킩��܂�����̖��œ����Ă��邶��Ȃ���ł���<br>��������̖���gif�łł��Ă���̂�������܂����A����������o�Ă��Ȃ�������ł��B</font></blockquote>

<form name="res_158" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="158">
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
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
[<b>157</b>]�@<font color=#0000FF><b>�}�E�X��ǂ�������摜�Ȃ�ł����ǁ@</b></font>
�@���e�ҁF<font color=#0000FF><b><a href=mailto:aaf26770@pop06.odn.ne.jp>���V</a></b></font>
�@<small>���e���F2001�N01��25�� 14��11��59�b</small> </TD>
<TD align="right" nowrap><A href="#3">��</A> <A href="#5">��</A>
 <A href="#0">��</A> <A href="#100">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="800000" size=2>�}�E�X��ǂ�������摜�Ȃ�ł����ǁA�}�E�X��gif�摜�͂ǂ̃t�H���_�ɓ����̂ł��傤��<br>�ǂ̃t�H���_�ɂ���Ă��v���r���[�ŏo�Ă���̂ł����}�E�X�������Ă�����<br>�����Ă��܂��܂��B���S�҂Ȃ̂ł��������������A��낵���B�@</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>�S��html�t�@�C���Ɠ����Ƃ���ɒu���Ă��������B </FONT><FONT size=1><EM>(2001/01/25 16:18:47)</EM></FONT></TD></TR>

</TABLE>

<form name="res_157" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="157">
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
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
[<b>156</b>]�@<font color=#0000FF><b>�͂��߂܂���!</b></font>
�@���e�ҁF<font color=#0000FF><b><a href=mailto:myrtille27@freesurf.fr>Puko</a></b></font>
�@<small>���e���F2001�N01��21�� 07��05��26�b</small> </TD>
<TD align="right" nowrap><A href="#4">��</A> <A href="#6">��</A>
 <A href="#0">��</A> <A href="#100">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="C100C1" size=2>JAVA���S�҂ł��B���̃T�C�g�ɗ��Ă��낢��׋������Ă��������Ă܂��B<br><br>�����u����~�点��v�̃X�N���v�g���g���Ă݂܂����BNN4.7, IE5�ł͂����ƌ������̂ł����A���NN6�𓱓����ă`�F�b�N���Ă݂���A���삵�Ă��Ȃ��̂ł��B<br>NN6�ɂ��Ή�������ɂ͂ǂ�������悢�ł��傤���H���邢�͎��̃~�X�ł��傤���H<br>�u����+���~��v�̉��ǔł�NN6�ł������ƌ����Ă���̂�...�B<br><br>�ǂ����A�h���@�C�X����낵�����肢���܂���@</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2><a href=http://www.nob21.com/javanavi/ target=_top>http://www.nob21.com/javanavi/</a><br>�����̂�NN6�ɑΉ����Ă܂����B<br>�����̂͂܂����Ή��B�ʓ|�Ȃ̂�(��) </FONT><FONT size=1><EM>(2001/01/21 21:06:58)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>Puko</B></FONT></TD>
<TD valign=top><FONT color=C100C1 size=2>�ǂ������肪�Ƃ��������܂��I�I�����g���Ă݂܂����B<br>NN6�ł͐�̍~��X�s�[�h��4.7���x���悤�ȋC�����܂����A���߂��Ă݂܂��B </FONT><FONT size=1><EM>(2001/01/22 12:36:31)</EM></FONT></TD></TR>

</TABLE>

<form name="res_156" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="156">
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
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
[<b>155</b>]�@<font color=#0000FF><b>���߂܂���</b></font>
�@���e�ҁF<font color=#0000FF><b>�܂�</b></font>
�@<small>���e���F2001�N01��19�� 09��04��19�b</small> </TD>
<TD align="right" nowrap><A href="#5">��</A> <A href="#7">��</A>
 <A href="#0">��</A> <A href="#100">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="0000FF" size=2>������ɗ���悤�ɂȂ��Ă���i�`�u�`�ɋ��������������̂ł��B<br>�ł��A�p�\�R���o�������Ȃ��ׁA�킩��Ȃ����������̂ł����c<br>�u�X�V���\���v���g���Ă݂����ĉ��x���������̂ł����A�����^�C���E�G���[�ƂȂ�܂��B<br>�ǂ�������o����̂ł��傤���H<br>�����I�Ȏ���Ő\���󂠂�܂���B<br>�X�������肢�v���܂��B</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>���̏�肭�s���Ȃ��̂������Ă��������B </FONT><FONT size=1><EM>(2001/01/19 13:01:58)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>�܂�</B></FONT></TD>
<TD valign=top><FONT color=0000FF size=2>���ꂪ�c�^�O���R�s�[���ē\��t���Ă݂�ƁA�����^�C���E�G���[�ƂȂ��āA<br>�f�o�b�N�̉�ʁH�ɂ����what's new(�N�A���A���A�P�j�̕��������F�ɂȂ��ĕ\�������̂ł����c<br>�Ȃ̂Ńy�[�W�\�����A�܂��o���Ă��Ȃ��̂ł��B<br>��������A�ǂ�����΂����̂�����Ȃ��̂ł�(T_T)<br>2001.1.18������X�V�����n�߂����̂ł����c�B </FONT><FONT size=1><EM>(2001/01/19 13:39:00)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>3</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>Head����Script�͓���܂����H�B </FONT><FONT size=1><EM>(2001/01/19 14:56:06)</EM></FONT></TD></TR>

</TABLE>

<form name="res_155" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="155">
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
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
[<b>152</b>]�@<font color=#0000FF><b>����ɂ���</b></font>
�@���e�ҁF<font color=#0000FF><b>�P�C�~����</b></font>
�@<small>���e���F2001�N01��17�� 23��41��31�b</small> </TD>
<TD align="right" nowrap><A href="#6">��</A> <A href="#8">��</A>
 <A href="#0">��</A> <A href="#100">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="000080" size=2>�u�{�^�����g�����_�C�i�~�b�N���j���[�v��<br>�w�i�╶���F�͕ς�����̂ł����E�E<br>�O���̘g�̕����̐F��ς��邱�Ƃ͏o���Ȃ��ł��傤���H<br>�����Ă��������@</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>�X�^�C���V�[�g�Ɉȉ���ǉ��B<br>border:1 solid blue;<br>�����瑾�� ���� �F�ł��B<br>�ڂ����̓X�^�C���V�[�g�̕׋������Ă��������B </FONT><FONT size=1><EM>(2001/01/18 22:45:42)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>�P�C�~����</B></FONT></TD>
<TD valign=top><FONT color=000080 size=2>���肪�Ƃ��������܂���<br>�X�^�C���V�[�g�̖{�͌�����ł����i�p���p�����Ɓj�킩��܂���ł���<br>�܂��Ȃɂ��������狳���Ă��������B<br>���x�͂����ƒ��ׂĂ��炻��ł��킩��Ȃ������玿�₵�܂��i�G�P���P�` </FONT><FONT size=1><EM>(2001/01/19 09:45:01)</EM></FONT></TD></TR>

</TABLE>

<form name="res_152" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="152">
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
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
[<b>153</b>]�@<font color=#0000FF><b>�͂��߂܂���_(._.)_</b></font>
�@���e�ҁF<font color=#0000FF><b><a href=mailto:anzu@mug.biglobe.ne.jp>anzu</a></b></font>
�@<small>���e���F2001�N01��18�� 13��35��27�b</small> </TD>
<TD align="right" nowrap><A href="#7">��</A> <A href="#9">��</A>
 <A href="#0">��</A> <A href="#100">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="000080" size=2>HTML�Ŏg�������̃v���[���g�T���^���g�킹�Ē��������ĉ摜��<br>stationery�ɕۑ����ă\�|�X���R�s�|���ă��|���̃\�|�X�ɓ\����܂�����<br>�摜���~�ɂȂ��Ă��܂��܂��ǂ����Ăł��傤���H<br>���|���̓A�E�g���b�N�łh�d��5.01�ł�<br>���w����낵�����肢�������܂�</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>���[���ł͉������Ȃ��Ǝg���܂���B<br>�����̎d���͐�~��TIPS�����Ă��������B </FONT><FONT size=1><EM>(2001/01/18 22:46:25)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>anzu</B></FONT></TD>
<TD valign=top><FONT color=000080 size=2>���e���Ă�����������܂����ł��܂����g�킹�Ă��������܂�<br>���肪�Ƃ��������܂��� </FONT><FONT size=1><EM>(2001/01/18 23:10:21)</EM></FONT></TD></TR>

</TABLE>

<form name="res_153" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="153">
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
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
[<b>154</b>]�@<font color=#0000FF><b>�͂��߂܂���</b></font>
�@���e�ҁF<font color=#0000FF><b>���ڂ���</b></font>
�@<small>���e���F2001�N01��18�� 20��15��43�b</small> </TD>
<TD align="right" nowrap><A href="#8">��</A> <A href="#10">��</A>
 <A href="#0">��</A> <A href="#100">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="800000" size=2>�t�B���^�[�̃g�����W�V�����@���g�킳���ĖႢ�܂��B<br>��������낢�남���b�ɂȂ�Ǝv���܂�<br>��낵����肢���܂��B</font></blockquote>

<form name="res_154" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="154">
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
<TABLE border=0 width=100% cellpadding=0 cellspacing=0><TR><TD>
[<b>151</b>]�@<font color=#0000FF><b>�͂��߂܂��āI</b></font>
�@���e�ҁF<font color=#0000FF><b>�Ƃ���</b></font>
�@<small>���e���F2001�N01��16�� 18��00��43�b</small> <a href="http://www.geocities.co.jp/SweetHome-Green/8802/" target=_top><img src="./home.gif" border=0 align=top HSPACE=10 WIDTH="25" HEIGHT="22"></a></TD>
<TD align="right" nowrap><A href="#9">��</A> <A href="#11">��</A>
 <A href="#0">��</A> <A href="#100">��</A></TD></TR></TABLE><TR><TD colspan=2>
<BR><blockquote><font color="008040" size=2>�����̉Ԃ̃X�N���v�g�����؂肵�܂����I<br>���ǁE�E�E<br>flash�̑f�ނ��ꏏ�ɒu���Ă邹�����E�E�E<br>����ɍ쓮���Ă܂���(T^T)���<br>�ǂ����Ăł��傤�E�E�E�H�I<br><br>����ƁE�E�E�p���[�T�[�`�̃^�O�̌��J�͍��゠��܂��񂩁H�I</font></blockquote>

<P><hr width=95% size=1>

<TABLE border=0 cellpadding=3>
<TR><TD align=right valign=top nowrap><FONT size=2>[<B>1</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>hana.js�̓_�E�����܂������H�B<br>hana.js��ۑ�����html�Ɠ������ɒu���Ă��������B<br><br>�p���[�T�[�`�͒��ڃ\�[�X�����Ă��������B<br>JavaScript Navigator�̂��Q�l�ɁB<br><a href=http://www.nob21.com/javanavi/ target=_top>http://www.nob21.com/javanavi/</a> </FONT><FONT size=1><EM>(2001/01/17 08:58:15)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>2</B>]</FONT></TD><TD valign=top><FONT size=2><B>�Ƃ���</B></FONT></TD>
<TD valign=top><FONT color=FF80C0 size=2>���X�L���������܂��B<br>hana.js�͓����Ƃ���ɒu���Ă��ł����ǁA<br>�X�N���[�����A�������Y��ɓ����ĂȂ����Ă������E�E�E�B<br><br>�p���[�T�[�`�̃\�[�X�������Ă����������Ƃ�����ł����A<br>�t���[���ɂȂ��ĂČ���Ȃ���ł��E�E�E�B<br>�ǂ�����āA����΂�����ł��傤�E�E�E�E�H(T^T)��� </FONT><FONT size=1><EM>(2001/01/17 12:27:49)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>3</B>]</FONT></TD><TD valign=top><FONT size=2><B>Hisa���Ǘ��l</B></FONT></TD>
<TD valign=top><FONT color=008040 size=2>���[��A�t���b�V���͊֌W�Ȃ��Ǝv��html�̍�肪���������H<br>�t�H�[���ƕ������t�ɔz�u����Ă邵�B<br>���̃\�t�g�ō�������m��Ȃ����\�[�X���������ɂ����̂ł킩���B<br><br>�\�[�X��<br>�t���[���̎��͉E�N���b�N�Ō���܂��B </FONT><FONT size=1><EM>(2001/01/17 20:36:11)</EM></FONT></TD></TR>

<TR><TD align=right valign=top nowrap><FONT size=2>[<B>4</B>]</FONT></TD><TD valign=top><FONT size=2><B>�Ƃ���</B></FONT></TD>
<TD valign=top><FONT color=FF80C0 size=2>���萔���������ăX�~�}�Z���ł���m(_ _)m<br>FrontPageExpress�ƃz�[���y�[�W�r���_�[2001�Ƃō������ł�����<br>���܂����z�[���y�[�W�r���_�[�̕����g������ĂȂ��āE�E�E�B<br>������񂫂���ƍ�蒼���Ă݂܂��B<br>�L���������܂����B </FONT><FONT size=1><EM>(2001/01/17 22:01:25)</EM></FONT></TD></TR>

</TABLE>

<form name="res_151" method="POST" action="./petit.cgi">
<input type=hidden name=mode value="msg">
<input type=hidden name=resno value="151">
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
<input type=hidden name=page value="10">
<input type=hidden name=mode value="page">
<input type=submit value="����10��">
</form></TD>
</TR></TABLE><A name="100"></A>
<br><br><center><small><!-- PETIT v4.4 -->
- <a href="http://www.kent-web.com/" target=_top>Petit Board</a> -<BR>
Script arranged by <a href="http://www.suisen.sakura.ne.jp/~ikitai/" target="_blank"><B>Hisa</B></a>
</small></center>
</body></html>
