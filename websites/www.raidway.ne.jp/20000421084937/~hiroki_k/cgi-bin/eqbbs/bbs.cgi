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
<hr><font size=+1 color="#ff0000"><b>12�lParty</b></font>�@���e�ҁF<b><a href="mailto:o-yo@wta.att.ne.jp">JUN</a></b>
<font size=-1>�@���e���F04��20��(��)14��16��22�b</font><p>
<blockquote><pre>���ꌈ�肵���́H�\�͕����Ă����ǃz���g�ɂȂ�̂��ȁH���O���ǂ��ɕ\������邩���ɋC�ɂȂ�ˁ`�o����΁A���̑���������łP�Q�l�������Ɨǂ��Ȃ������g���ǂ���͉����ǂ�����Ȃ���ɁA�S�Œ��O�Ɏg���������u�������I�������I�I�v���Ă����̖�����Ă݂����C������񂾂�����l��Paw�s���Ă鎞�͂��������Ȃ����ȂƁi���ł����肷��ƁA�g�p����Ikura�{�l�̂ݎ��S�Ƃ����邩��HealTaunt������������ˁO�O�G�܂�����Paw�Ŏg�����Ƃ���HealTaunt��Ikura�����񂶂�����牴���P�O�O�����ʂ񂾂��ǂˁi�����Օi�Ƃ��Ă݂��Ȃ�퓬��̕����ǂ��̂��ȁH���̘r�����ɂ͂ǂ̂��炢���l��������̂Ȃ̂��ǂ��킩��Ȃ��̂��ǂ�Ȃ̂�������g���[�hOK�Ȃ̂����x�ڂ��������Ă��������i��kettya�̂Ƃ��ɏ����O�ɒ��Ղ��Č����Ă����΂��������ۂ��񂾂��O�O�G�������������ĕ������̂ŏ�������ł��܂��܂����i���߂񂿂Ⴂ���������Nox�E�������ǂǂ������r�ւ������A�n�Y���̓��[�u�������H�����������ł����[�u�i�����x�ꏏ�ɍs���Ă݂邶������������Ȃ���������O�O�G<!--remote_host�F100.pool0.nishitokyo.att.ne.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>�����[�[�[�[�iW</b></font>�@���e�ҁF<font color="#555555"><b>Ikura</b></font>
<font size=-1>�@���e���F04��20��(��)07��31��01�b</font><p>
<blockquote><pre>�@To�@Junn�����@�����i���@�g�����Ǝv���Ă��̂ɁA��Ɍ���ꂽ���ۂ��B����ς肱����āAPoX�Ƃ��őS�łƂ��̎��Ɏg���̂��ǂ��̂��ȁH����Ƃ��P�Q�lParty�ɂȂ��Ă���g���Ƃ��ˁHIcon�ς���Ă邩�獡�x�����Ă�����B�@�Ƃ���ŁA���F�r��Get���Ă�̂ˁB�������ˁB���߂łƁB����(w<!--remote_host�F1cust107.tnt15.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>�h���S�����`</b></font>�@���e�ҁF<b><a href="mailto:o-yo@wta.att.ne.jp">JUN</a></b>
<font size=-1>�@���e���F04��20��(��)07��25��35�b</font><p>
<blockquote><pre>����Get���߂łƂ��IAE��CH���T�񂾂����H����������������Q�����Ă݂����ȉ����A�X��ITEM���炦����ō����������l���̒�ITEM�ł�Get�Ȃ�ăz���g�����Ǝv�����A����Ɓi��Paw�ɓ�l�ōs���Ă鎞�Ɏg���̂͂��������Ȃ��̂ł�߂܂��傤�i��<!--remote_host�F135.pool0.nishitokyo.att.ne.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>��������������B</b></font>�@���e�ҁF<font color="#555555"><b>Ikura</b></font>
<font size=-1>�@���e���F04��20��(��)03��37��18�b</font><p>
<blockquote><pre>�@Naggy��ގ����ɍs������A���������炦����B�Ȃ�Word�@Of�@Healing�����̌��ʕt���Ă��B���͂Ƃ�������炦�Ċ����������ł��B<!--remote_host�F2cust8.tnt15.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>LAST�@Hell�ۂ�</b></font>�@���e�ҁF<font color="#555555"><b>Ikura</b></font>
<font size=-1>�@���e���F04��19��(��)23��22��46�b</font><p>
<blockquote><pre>�@LastHell�ɂȂ����ۂ���B<!--remote_host�F2cust8.tnt15.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>SeverDown</b></font>�@���e�ҁF<font color="#555555"><b>Wine</b></font>
<font size=-1>�@���e���F04��19��(��)23��22��03�b</font><p>
<blockquote><pre>�@Eci��Down�������ł��B�ق��ق��ł��ˁB�@<!--remote_host�F2cust8.tnt15.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>�����f�d�s���āE�E�E</b></font>�@���e�ҁF<b><a href="mailto:o-yo@wta.att.ne.jp">JUN</a></b>
<font size=-1>�@���e���F04��18��(��)08��43��36�b</font><p>
<blockquote><pre>��l��Named MAG�ގ��܂Ő��������킯�����x��BookGet����i���撣��܂��傤�i��<!--remote_host�F153.pool0.nishitokyo.att.ne.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>grats</b></font>�@���e�ҁF<font color="#555555"><b>Winday</b></font>
<font size=-1>�@���e���F04��17��(��)19��39��03�b</font><p>
<blockquote><pre>�@���߂łƁ[�@�S�������A�������ɂ�^^;;<!--remote_host�Fh082.p112.iij4u.or.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>�������������Sorry</b></font>�@���e�ҁF<font color="#555555"><b>Wine</b></font>
<font size=-1>�@���e���F04��16��(��)14��45��40�b</font><p>
<blockquote><pre>�@Junn����Winday�����Haru�����Ryuzi���񂠂肪�ƁBPaw�ɂ���ł͂�S�����B���x���AGet���݂邯�ǂ���B�����@�����Ă��ɏo��Get�o���܂����ق�Ƃ����肪�Ƃ��������܂����B<!--remote_host�F1cust119.tnt15.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>Shiald</b></font>�@���e�ҁF<font color="#555555"><b>Ikura</b></font>
<font size=-1>�@���e���F04��06��(��)21��35��39�b</font><p>
<blockquote><pre>@@CLR�Ȃ̂��B�s���������ǖ����炠���������A�ł��o���Ă���Ȃ����ȁB<!--remote_host�F1cust61.tnt17.sfo3.da.uu.net--></pre><p>

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
1,390</h4>
</body></html>

