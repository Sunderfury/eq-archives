<HTML><HEAD>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=x-sjis">
<TITLE>DIABLO�U GAME BBS</TITLE></HEAD>
<BODY BGCOLOR=#FFFFFF TEXT=#000000 LINK=#000000 VLINK=#000000 ALINK=#FF3366>
<CENTER><B><I><FONT SIZE=6 COLOR=#FF3366>DIABLO�U GAME BBS</FONT></I></B><BR></CENTER>
<SCRIPT LANGUAGE="JavaScript">
<!--
function check() {
  if (document.F2.name.value == "") {
    alert("���e�Җ������͂���Ă��܂���B");
    document.F2.name.focus();
    return(false);
  }
  if (document.F2.send.value == "") {
    alert("�R�����g�����͂���Ă��܂���B");
    document.F2.send.focus();
    return(false);
  }
  if (document.F2.delkey.value == "") {
    alert("�폜�L�[�����͂���Ă��܂���B");
    document.F2.delkey.focus();
    return(false);
  }
  return(true);
}
// -->
</SCRIPT>
<BR>
<CENTER><TABLE><TR><TD>
<FORM NAME="F2" method="POST" action="/~ikitai/cgi-bin/dia2bbs/dia2bbs.cgi" onSubmit="return check();">
<INPUT type=hidden name=mode value=regist>
<SMALL>
���e�Җ�<INPUT type="text" name="name" value="" size="10">
 �T�[�o�[<SELECT NAME=sava>
<option value="ASIA">ASIA
<option value="USwest">USwest
<option value="USeast">USeast
<option value="Europe">Europe
<option value="Open_BN">Open_BN
<option value="Open_TCP/IP">Open_TCP/IP
</SELECT>
 GAME/�p�X/IP<INPUT type="text" name="game" value="" size="10"> ACT<SELECT NAME=act>
<option value="1">1
<option value="2">2
<option value="3">3
<option value="4">4
</SELECT>
 �폜�L�[<INPUT type=password name=delkey size=5 value=""><BR>
�R�����g <INPUT type="text" name="send"size="70">
<INPUT type="submit" value=" �� �M "> <INPUT type="button" value="RELOAD" onClick='location.href="/~ikitai/cgi-bin/dia2bbs/dia2bbs.cgi"'>
</SMALL>
</FORM>
</TD></TR></TABLE>
<DIV align=center>
<TABLE border=0 width=90%><TR><TD valign=top>
<HR>
<SMALL>[4] NAME�F<B>Hisa@�Ǘ��l</B> SERVER�F<B>Open_BN</B> GAME�F<B>ikitai/akatya</B> ACT�F<B>1</B> DATE�F<B>2000/07/08 22:24:48</B></SMALL><BR>�����̐������ł��B���@�x���l�͏���ɓ����ė��ā[<HR>
<SMALL>[3] NAME�F<B>Hisa@�Ǘ��l</B> SERVER�F<B>Open_BN</B> GAME�F<B>ikitai/ikitai</B> ACT�F<B>3</B> DATE�F<B>2000/07/06 22:03:24</B></SMALL><BR>�����g���Ă݂邩�BOPEN��BN��ikitai�`�����l���ɂ��܂���GAME���p�X�́��̒ʂ藼��ikitai�BACT�R�n�߂��΂���ł��B<HR>
<SMALL>[2] NAME�F<B>Hisa@�Ǘ��l</B> SERVER�F<B>ASIA</B> GAME�F<B></B> ACT�F<B>1</B> DATE�F<B>2000/07/06 10:26:51</B></SMALL><BR>����Ȋ����Ŏg�p����BBS�ł��BTest���Ԃ��I�������p�X���[�h�����ɂȂ�܂��B�ǂ��ł��傤�H<HR>
<SMALL>[1] NAME�F<B>Hisa@�Ǘ��l</B> SERVER�F<B>ASIA</B> GAME�F<B>ikitai/sika</B> ACT�F<B>4</B> DATE�F<B>2000/07/06 10:12:33</B></SMALL><BR>Play���`�B�N���ꏏ��Diablo��|���ɂ����[�B<HR>
</TD></TR></TABLE>
<SCRIPT LANGUAGE="JavaScript">
<!--
function sakujo() {
  if (document.F3.delcode.value == "") {
    alert("�폜No�����͂���Ă��܂���B");
    document.F3.delcode.focus();
    return(false);
  }
  if (document.F3.delkey.value == "") {
    alert("�폜�L�[�����͂���Ă��܂���B");
    document.F3.delkey.focus();
    return(false);
  }
  return(true);
}
// -->
</SCRIPT>

<FORM NAME=F3 method=POST ACTION=/~ikitai/cgi-bin/dia2bbs/dia2bbs.cgi onSubmit="return sakujo()">
<INPUT type=hidden name=type value=bbs>
<INPUT type=hidden name=mode value=delete>
�폜No <INPUT size=5 type=text name=delcode>
�폜�L�[ <INPUT size=5 type=password name=delkey value=>
<INPUT type=submit value= �폜 >
</FORM>
</DIV>
<BR><BR>
<SCRIPT LANGUAGE="JavaScript">
<!--
document.F2.send.focus();
// -->
</SCRIPT>
</BODY></HTML>
