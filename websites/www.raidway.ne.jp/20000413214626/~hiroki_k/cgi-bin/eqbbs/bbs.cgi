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
<hr><font size=+1 color="#ff0000"><b>Shiald</b></font>�@���e�ҁF<font color="#555555"><b>Ikura</b></font>
<font size=-1>�@���e���F04��06��(��)21��35��39�b</font><p>
<blockquote><pre>@@CLR�Ȃ̂��B�s���������ǖ����炠���������A�ł��o���Ă���Ȃ����ȁB<!--remote_host�F1cust61.tnt17.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>Down</b></font>�@���e�ҁF<font color="#555555"><b>IKURA</b></font>
<font size=-1>�@���e���F04��06��(��)21��34��27�b</font><p>
<blockquote><pre>�܂�DOWN���您�������������̂����肳�߂Ƃ��n�߂���̂���P�OMIN��Mess�������Ȃ��̂ł݂�Ȃ���GG�Ԃ�̂�����DD�̗��ł����BKill���Ă���Loot���đ�GG�@Random�ł̂�����Ⴆ�܂����B<!--remote_host�F1cust61.tnt17.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>�h���������l</b></font>�@���e�ҁF<b><a href="mailto:o-yo@wta.att.ne.jp">�i�t�m</a></b>
<font size=-1>�@���e���F04��06��(��)01��38��42�b</font><p>
<blockquote><pre>paw�̃V�[���h�͂m���������b�k�q�������̂ˁi�����x���ɍs�����ˁ`<!--remote_host�F77.pool0.nishitokyo.att.ne.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>��ꂽ�`</b></font>�@���e�ҁF<b><a href="mailto:o-yo@wta.att.ne.jp">�i�t�m</a></b>
<font size=-1>�@���e���F04��05��(��)06��40��28�b</font><p>
<blockquote><pre>�T�[�o�[�t�o���Q�W���ԓ���ւ�藧�����`�q�L�����v���Ă����ǂs�a�a����o�Ȃ��������؁`�i�s�s���₷�݂Ȃ����E�E�E�E�E�i����<!--remote_host�F187.pool0.nishitokyo.att.ne.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>NewSong</b></font>�@���e�ҁF<font color="#555555"><b>Wine</b></font>
<font size=-1>�@���e���F03��30��(��)01��10��58�b</font><p>
<blockquote><pre>http://eq.castersrealm.com/spells/bard/�@NewSong�ł����ǁA����ܗ~�����̂Ȃ���BNweSkill2����ۂ����ǎg����̂��ȁH�Ȃ�ɂ���LV50��Full�ɂ��Ƃ��Ȃ��Ǝn�܂��ȁB<!--remote_host�F1cust99.tnt15.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>Jyooooookiiiiiiin lv 40</b></font>�@���e�ҁF<font color="#555555"><b>Wine</b></font>
<font size=-1>�@���e���F03��29��(��)14��30��21�b</font><p>
<blockquote><pre>�@lv40�s���܂����B���Ȃ�sERORI�����ɂ���Ԃɕ������ł����BPaw��Boss�̂Ƃ��ɂ��ꂱ��5����Camp���Ă܂������ۂ������B�������Boss�ɁB�@Junn����ցB�@������ServerDown����BChat�ő҂��Ă܂��܂��ˁ[�[�[�B<!--remote_host�F1cust254.tnt17.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>����ň�</b></font>�@���e�ҁF<font color="#555555"><b>Wine</b></font>
<font size=-1>�@���e���F03��28��(��)09��04��30�b</font><p>
<blockquote><pre>��������ň��Ȃ�BEQ�쓮���Ă�ƁA�����Ȃ������Ɨ�����B������������Ȋ����ł��Ȃ�h���BTTJunn����E�������Ă��߂�ˁB<!--remote_host�F1cust154.tnt17.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>Jyakiiiiin�@LV39</b></font>�@���e�ҁF<font color="#555555"><b>Wine</b></font>
<font size=-1>�@���e���F03��24��(��)00��50��56�b</font><p>
<blockquote><pre>LV39�ɂȂ����Ȃ�BMinnawanko�쓮�ł���Wan<!--remote_host�F1cust11.tnt21.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>Wine�l</b></font>�@���e�ҁF<b><a href="mailto:o-yo@wta.att.ne.jp">�i�t�m</a></b>
<font size=-1>�@���e���F03��22��(��)03��14��05�b</font><p>
<blockquote><pre>������Ɨp��������Ă���Ȏ��ԂɂȂ��Ă��܂����̂������}���œ��낤�ɂ��Ȃ���EQ�ɓ���Ȃ��i���z���g���߂�Ȃ����`�A�����͕K���s���܂��`m(__)m<!--remote_host�F74.pool0.nishitokyo.att.ne.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>�����ς�</b></font>�@���e�ҁF<font color="#555555"><b>Wine</b></font>
<font size=-1>�@���e���F03��21��(��)00��17��34�b</font><p>
<blockquote><pre>�@Loc����Ǝv��,�K����Feerrot���U�����Ă���OgerTown��Zone���������W������ƕ|�������ȁB�@WAR��SKILL�͂����ɘa��ڂ��Ă��̂ł����������Ƃ��܂��B���񂢂����Skill������̂��āB<!--remote_host�F1cust77.tnt15.sfo3.da.uu.net--></pre><p>

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
1,106</h4>
</body></html>

