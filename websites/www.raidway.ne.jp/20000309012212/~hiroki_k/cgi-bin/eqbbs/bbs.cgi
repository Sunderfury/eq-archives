<html>
<head>
<title>EQ�̓������BBS</title>

<SCRIPT LANGUAGE = "JavaScript">

<!--

browserName = navigator.appName;
browserVer = parseInt(navigator.appVersion);

if (browserName == "Netscape" && browserVer >= 3)
	version = "n3";
else
	version = "x";

if (version == "n3") {

	homeoff = new Image(18,80)
	homeon = new Image(18,80)
	homeoff.src = "../../btn/home_off.gif"
	homeon.src  = "../../btn/home_on.gif"

        uooff = new Image(18,80)
        uoon = new Image(18,80)
        uooff.src = "../../btn/uo_off.gif"
        uoon.src  = "../../btn/uo_on.gif"

        uobbsoff = new Image(18,80)
        uobbson = new Image(18,80)
        uobbsoff.src = "../../btn/uobbs_off.gif"
        uobbson.src  = "../../btn/uobbs_on.gif"

        eqoff = new Image(18,80)
        eqon = new Image(18,80)
        eqoff.src = "../../btn/eq_off.gif"
        eqon.src  = "../../btn/eq_on.gif"

        eqbbsoff = new Image(18,80)
        eqbbson = new Image(18,80)
        eqbbsoff.src = "../../btn/eqbbs_now.gif"
        eqbbson.src  = "../../btn/eqbbs_now.gif"

        chatoff = new Image(18,80)
        chaton = new Image(18,80)
        chatoff.src = "../../btn/chat_off.gif"
        chaton.src  = "../../btn/chat_on.gif"
}

function img_act(imgName)
{
        if (version == "n3") 
        {
        imgOn = eval(imgName + "on.src");
        document [imgName].src = imgOn;
        }
}

function img_inact(imgName)
{
        if (version == "n3") 
        {
        imgOff = eval(imgName + "off.src");
        document [imgName].src = imgOff;
        }
}

//-->

</SCRIPT>

</head>

	<body bgcolor="#77BBEE" text="#000000" background="../../common/wall.gif">

<A NAME="top"></A>

<TABLE BORDER="0" CELLPADDING="0" CELLSPACING="0">
<TR>

<TD><A HREF="../../index.html" onMouseOver="img_act('home');
         self.status='�g�b�v�y�[�W';
         return true" onMouseOut="img_inact('home')">
        <IMG SRC="../../btn/home_off.gif" BORDER="0" WIDTH="80" HEIGHT="18" name='home'></A></TD>

<TD><A HREF="../../uo/index.html" onMouseOver="img_act('uo');
         self.status='UO Software';
         return true" onMouseOut="img_inact('uo')">
        <IMG SRC="../../btn/uo_off.gif" BORDER="0" WIDTH="80" HEIGHT="18" name='uo'></A></TD>

<TD><A HREF="/~hiroki_k/cgi-bin/uobbs/bbs.cgi" onMouseOver="img_act('uobbs');
         self.status='UO Software BBS';
         return true" onMouseOut="img_inact('uobbs')">
        <IMG SRC="../../btn/uobbs_off.gif" BORDER="0" WIDTH="80" HEIGHT="18" name='uobbs'></A></TD>

<TD><A HREF="../../eq/index.html" onMouseOver="img_act('eq');
         self.status='EQ�̓������';
         return true" onMouseOut="img_inact('eq')">
        <IMG SRC="../../btn/eq_off.gif" BORDER="0" WIDTH="80" HEIGHT="18" name='eq'></A></TD>

<TD><A HREF="/~hiroki_k/cgi-bin/eqbbs/bbs.cgi" onMouseOver="img_act('eqbbs');
         self.status='EQ�̓������BBS';
         return true" onMouseOut="img_inact('eqbbs')">
        <IMG SRC="../../btn/eqbbs_now.gif" BORDER="0" WIDTH="80" HEIGHT="18" name='eqbbs'></A></TD>

<TD><A HREF="/~hiroki_k/cgi-bin/chat1/index.cgi" onMouseOver="img_act('chat');
	self.status='EQ�̓������`���b�g';
	return true" onMouseOut="img_inact('chat')">
	<IMG SRC="../../btn/chat_off.gif" BORDER="0" WIDTH="80" HEIGHT="18" name='chat'></A></TD>

</TR>
</TABLE>

<HR><!-- ------------------------------------------------------------------ -->
<FONT COLOR=green><CENTER><H2><B>EQ�̓������BBS</B></H2></CENTER></FONT>
<HR><!-- ------------------------------------------------------------------ -->
<form method=post action="http://www.raidway.ne.jp/~hiroki_k/cgi-bin/eqbbs/bbs.cgi">
<input type=hidden name="action" value="regist">
<table><tr><td align="right">
<FONT COLOR="#BF2323">���e��</FONT></td><td>
<input type=text name="name" size=20 value="" maxlength=19></td></tr><tr><td align="right">
<FONT COLOR="#BF2323">���[��</FONT></td><td>
<input type=text name="email" size=30 value="">
</td></tr><tr><td align="right">
<FONT COLOR="#BF2323">�薼</FONT></td><td>
<input type=text name="subject" size=30>
</td></tr></table><p><table><tr><td>
<FONT COLOR="#BF2323">���e<i>�i�L���ʂ�ɋL�^���܂��̂œK���ɉ��s�����Ă�������
�j</i></FONT>
</td></tr><tr><td>
<textarea name="value" rows=5 cols=70></textarea><p>
</td></tr><tr><td><FONT COLOR="#BF2323">�t�q�k�i�����N����ꂽ���ꍇ�͂����ɋL�����Ăˁj
</FONT></td></tr><tr><td>
<input type=text name="page" size=70 value="http://"><p>
</td></tr></table>
<table><tr><td>
<input type=submit value="    ��  �e    "><p>
</td><td>
<input type=reset value="   ��������   "><p>
</td></tr></table><p>
</form>
<hr><font size=-1><i>�V�����L������\�����܂��B�ō�50���̋L�����L�^����A����𒴂���ƌÂ��L������폜����܂��B<br>
�P��̕\����10�����z����ꍇ�́A���̃{�^�����������ƂŎ��̉�ʂ̋L����\�����܂��B</i></font>

<HR>
<B>���݂�<A HREF="/~hiroki_k/cgi-bin/chat1/index.cgi">�b�g�`�s</A>�Q���҈ꗗ</B><BR>
<UL>
<LI><B>�N���������Ă��܂���B</B><BR>
</UL>
<hr><font size=+1 color="#ff0000"><b>�ŁA�g���Ă݂��B</b></font>�@���e�ҁF<b><a href="mailto:raqia@w3.to">Kapa(Raq)</a></b>
<font size=-1>�@���e���F03��07��(��)14��30��24�b</font><p>
<blockquote><pre>SoundCardDCS���ĂƂ���S817�iYAMAHA��YMF724 Chip�j��SIKAX���삵�܂����B���Ă������^�C�}�[�\�����ꂸ�B�iTTCREATIVE��3D Blaster Banshee�B�I�I���܂ł͕\������Ă��񂾂��ǁA���̎��̂��o�����̊G�ȍ~�\�����ꂸ�B<!--remote_host�Fkobca-0216p51.ppp.odn.ad.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>�������ł̓n�W���}�V�e</b></font>�@���e�ҁF<b><a href="mailto:raqia@w3.to">Kapapa(Raq)</a></b>
<font size=-1>�@���e���F03��07��(��)11��52��54�b</font><p>
<blockquote><pre>Raqia�Ƃ�Raqie�Ƃ�����Ȗ��O�ŗV��ł鈫�ł��B���B�FDTimer�̂��DL���Ă݂܂����B���ꂩ��g���Ă݂܂���BDS�̌��ʎ��ԊǗ��������āB����ł́A�܂��`�B#���[�ALoc�̂�����삷�邩����Test���邩�ȁ`�B<!--remote_host�Fkobca-0116p148.ppp.odn.ad.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>����FA�֘A</b></font>�@���e�ҁF<font color="#555555"><b>Winday</b></font>
<font size=-1>�@���e���F02��29��(��)21��09��22�b</font><p>
<blockquote><pre>�@�ǂ����A�f�}���炵���i���@�悭�l����Ȃ��A���Ȃ�^^;;<!--remote_host�Fhnj0098.bekkoame.ne.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>PoH</b></font>�@���e�ҁF<font color="#555555"><b>Winday</b></font>
<font size=-1>�@���e���F02��29��(��)16��52��25�b</font><p>
<blockquote><pre>�@���Ԃ�����΍s�����������ɂ傧�B�@�������̎��Ԃ���́A�A�Ǝ��Ԃ����ɂ���Ă鎄�ɂ͖������ۂ���i���@�֌W�������ǁA�ӂƁA�C�O�y�[�W�ŁA�e�`�N�G�X�g(Fiery Avenger)���S�e��ڂɂ��܂����B�����x���o�`�k�݂̂Ȃ��܋C������Ă݂�H�i�����Ƀ����N<!--remote_host�Fh093.p112.iij4u.or.jp--></pre><p>

<a href="http://www.everlore.com/default.asp?mode=35&id=83691" target="_top"><img border=0 align=middle src="../../eq/img/eqgate.gif" width=34 height=23 alt="(">http://www.everlore.com/default.asp?mode=35&id=83691<img border=0 align=middle src="../../eq/img/eqgate.gif" width=34 height=23 alt=")"></a><p>
</blockquote>
<hr><font size=+1 color="#ff0000"><b>LOC Navi</b></font>�@���e�ҁF<font color="#555555"><b>Winday</b></font>
<font size=-1>�@���e���F02��29��(��)16��41��26�b</font><p>
<blockquote><pre>�@�V��i���@LOC�����ɁA�ړI�n�̕��p���o���\�t�g�͂����������������Ƃ�����܂����A�d�p�p�̂o�b�Ƃ͕ʂɂo�b��p�ӂ���\�t�g�����������Ɩ����̂ŁASIKAX���������ē��ŁA����PC�ł����p�ł�����̂��쐬���Ă݂܂����B�@�������s�ȕ�����������i���@����̃o�[�W�������̃C���X�g��Windark�����iNEC�P�Q�΁j�ł��i��<!--remote_host�Fh093.p112.iij4u.or.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>�����</b></font>�@���e�ҁF<font color="#555555"><b>Wine</b></font>
<font size=-1>�@���e���F02��25��(��)17��23��29�b</font><p>
<blockquote><pre>�@PoH��ꂽ�BBelivers��EQ��S���爤����l�̏W�܂�ۂ��B�iNOT�@Haijin)�@�˂�������悯��΍s�����B�����납������BChast���炦����B�@DRU�͂R�R���B�T�O�Ƒg��ł�EXP����̊m�F�ς݁B�����Healer�Ȃ��č��邱�ƂȂ��ˁB�@���ꂩ�����낵���ˁB<!--remote_host�F1cust39.tnt15.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>����������</b></font>�@���e�ҁF<font color="#555555"><b>Winday</b></font>
<font size=-1>�@���e���F02��08��(��)22��42��21�b</font><p>
<blockquote><pre>�@�Q�Ă��݂�����(^^;;�@����A�O���A�������Ă��܂�˂ĂȂ������񂾂悧��(TT�@���݂�<!--remote_host�Fh100.p111.iij4u.or.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>��ȃl�G�^��</b></font>�@���e�ҁF<font color="#555555"><b>Wine</b></font>
<font size=-1>�@���e���F02��08��(��)08��43��31�b</font><p>
<blockquote><pre>�@��ȃl�G�^���@�l�G�^���ɉ��xTell�����AFK������Ă��̂���B����Ƃ���������IgnoerList���ꂽ�H�iToT)�@������Junn����Ə����킢��Inu�ƌJ��L���܂����B�a�t�����ɍs�����Ȃ񂩎������G�T�ɂȂ����͗l�B���₵�[--�B�ł����Ȃ肨�����납�����ȁ[-�܂��s�����ˁB<!--remote_host�F1cust108.tnt15.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>thx- w</b></font>�@���e�ҁF<font color="#555555"><b>Hitopi</b></font>
<font size=-1>�@���e���F02��07��(��)04��41��59�b</font><p>
<blockquote><pre>Aisiteru yoooo w<!--remote_host�Fppp88.asahikawa-ap.dti.ne.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>Re���҂���</b></font>�@���e�ҁF<font color="#555555"><b>Winday</b></font>
<font size=-1>�@���e���F02��06��(��)20��00��21�b</font><p>
<blockquote><pre>�@�������̃g�b�v�y�[�W�ɂ̂��Ă��<!--remote_host�Fh014.p112.iij4u.or.jp--></pre><p>

<a href="http://www13.big.or.jp/~pom/" target="_top"><img border=0 align=middle src="../../eq/img/eqgate.gif" width=34 height=23 alt="(">http://www13.big.or.jp/~pom/<img border=0 align=middle src="../../eq/img/eqgate.gif" width=34 height=23 alt=")"></a><p>
</blockquote>
<hr><p>
<font size=-1><i>�ȏ�́A���ݓo�^����Ă���V����1�Ԗڂ���10�Ԗڂ܂ł̋L���ł��B</i></font><p>
<form method=post action="http://www.raidway.ne.jp/~hiroki_k/cgi-bin/eqbbs/bbs.cgi">
<input type=hidden name="page" value="10">
<input type=submit value="���̃y�[�W"></form>
<form action="http://www.raidway.ne.jp/~hiroki_k/eq/"><input type=submit value="�@�I�@���@"></form><p>
<form method=post action="http://www.raidway.ne.jp/~hiroki_k/cgi-bin/eqbbs/bbs.cgi">
<hr size=5><p>�p�X���[�h <input type=password name="pwd" size=10>
<input type=submit value="�Ǘ��ҍ폜"></form>
<h4 align=right><hr size=5><a href="http://www.ask.or.jp/~rescue/" target="_top">MiniBBS v7.5</a> is Free.<br>
51</h4>
</body></html>

