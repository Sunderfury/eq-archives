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

</body>
</html>
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
<hr><font size=+1 color="#ff0000"><b>Wine�`</b></font>�@���e�ҁF<font color="#555555"><b>�߂���[��</b></font>
<font size=-1>�@���e���F01��16��(��)10��00��58�b</font><p>
<blockquote><pre>��������[�B���݂₰�A���݂₰�B: )�͏�k�Ƃ��āA�킽�����\Rare Pop�ɂȂ�\�肾����A�����~�����A�C�e�������āAENC need�Ȃ�BBS�ɂł���������ł���B<!--remote_host�Fjyocd-01p92.ppp.odn.ad.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>�����A��������[</b></font>�@���e�ҁF<font color="#555555"><b>Winday</b></font>
<font size=-1>�@���e���F01��15��(�y)21��12��42�b</font><p>
<blockquote><pre>�@Wine�����A��������[�B�@��ӂ�Naggy�O�]�[���N���b�V��FG�S���|�b�v�ŁALv2��exp���������ۂ���^^;;�@����Lv48�ł��A����Ȃɗ���ĂȂ����B��������Ƀ��n�r������^^;�@�䂤������A���Ђ����Ԃ�[�A���߂łƂ��ł��B�@SIKAX�A�o�[�W�����A�b�v�������ł��A�ł��A�����ݒ�ł������@�W���[�N�\�t�g�łȂ��Ȃ��Ă��܂��\��(w�@�X�N���[���Z�[�o�[�܂����g�p���ł���^^;;���͐S���Ɉ����̂Ŏg���Ă܂���(w�@���܂ɂ�Zhilla�ɉ�����ȁ[(w �R������A�@ �A�C�R����ł��ˁA�L���b�V���Ƃ��F�X����ł����A�L���b�V���̃N���A�����@ ���C�ɓ��肩��폜���āA���߂ău�b�N�}�[�N����ƁA�����肵����B�@ ���܁AEQ�̃g�b�v�y�[�W�ɂ�EQT�̃A�C�R������Ă݂Ă����ł�����(w<!--remote_host�Fh091.p111.iij4u.or.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>��������</b></font>�@���e�ҁF<font color="#555555"><b>Wine</b></font>
<font size=-1>�@���e���F01��15��(�y)13��48��10�b</font><p>
<blockquote><pre>Winday�̂��o�����@�������܂�B�@����ɂł��������낵���ˁB�ł�LV�͂Ȃ��ꂽ�ۂ�����A�V�ׂȂ��ˁB���������A�ǂ����ɂ����琺�����ĂˁB<!--remote_host�F1cust89.tnt15.sfo3.da.uu.net--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>��[��</b></font>�@���e�ҁF<b><a href="mailto:virgil7@sda.att.ne.jp">�䂤��</a></b>
<font size=-1>�@���e���F01��14��(��)13��09��30�b</font><p>
<blockquote><pre>���Ђ����Ԃ�ł��A�����܂��Ă��߂łƂ��`��������SIKAX�����Ă܁`���X�N���[���Z�C�o�[�͂��܂���UO�H��̃A���Ł`��<!--remote_host�F20.pool0.sendai.att.ne.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>�A�C�R��</b></font>�@���e�ҁF<b><a href="mailto:viva@hot.hot.co.jp">�R��</a></b>
<font size=-1>�@���e���F01��13��(��)17��52��17�b</font><p>
<blockquote><pre>Winday�ɍ���Ă�������A�C�R���̓Z�b�g���Ă��炾���Ԃ���������URL���Ɍ��������������A�o���o���B�Ȃ񂩂��̋@�\�͉������˂��i��IE5.5������Ōł܂�̂��ȁB<!--remote_host�Fzaqd2bf3b4a.zaq.ne.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>Re��Ӂ[�@�����N�ɂ���</b></font>�@���e�ҁF<font color="#555555"><b>Winday</b></font>
<font size=-1>�@���e���F01��11��(��)18��47��29�b</font><p>
<blockquote><pre>�@�������Ă邤���ɁA�R������̏������݂�(@@�@�������ƃg�b�v�y�[�W��EQ�̓��������Љ���Ă��炢�܂����B �@Wai�ǂ��ł�(^-^)�@�v�X�ɃQ�[�g�A�C�R������(w�@�R������A���܂ɂ�EQ����[(w<!--remote_host�Fh146.p111.iij4u.or.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>�߂������m�点</b></font>�@���e�ҁF<font color="#555555"><b>Winday</b></font>
<font size=-1>�@���e���F01��11��(��)18��40��19�b</font><p>
<blockquote><pre>�@EQ����Ă�PC�Ƃ͕ʂɁA�O����g���Ă�PC�i�J�����j���A�N�����Ȃ��Ȃ�܂���(TT�@�ŁAWindows�ăC���X�g�[���A���[�A�v���݂�ȍăC���X�g�[����(TT�@�������A�l�b�g���[�N�J�[�h�̃h���C�o�f�B�X�N�ǂ߂܂���(w�@���P�F�ӂ�[��FD�͂��܂Ƀ`�F�b�N�����ق�����낵������(^^;;<!--remote_host�Fh146.p111.iij4u.or.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>��Ӂ[�@�����N�ɂ���</b></font>�@���e�ҁF<b><a href="mailto:viva@hot.hot.co.jp">�R��</a></b>
<font size=-1>�@���e���F01��11��(��)18��37��20�b</font><p>
<blockquote><pre>��ف[�@�R�����т��B�����ƃg�b�v�y�[�W��EQ�̓��������Љ���Ă��炢�܂����B�����N�t���[�Ƃ������Ƃ����ǁA�Ƃ肠�����񍐂��B<!--remote_host�Fzaqd2bf3b4a.zaq.ne.jp--></pre><p>

<a href="http://www.mwc.ne.jp/kettya/" target="_top"><img border=0 align=middle src="../../eq/img/eqgate.gif" width=34 height=23 alt="(">http://www.mwc.ne.jp/kettya/<img border=0 align=middle src="../../eq/img/eqgate.gif" width=34 height=23 alt=")"></a><p>
</blockquote>
<hr><font size=+1 color="#ff0000"><b>ReSIKAX�ǂ��ł��I</b></font>�@���e�ҁF<font color="#555555"><b>Winday</b></font>
<font size=-1>�@���e���F01��07��(��)20��28��40�b</font><p>
<blockquote><pre>�@Gengoro����A�͂��߂܂��āB>SIKAX��DL���Ďg���Ă݂܂����B�ƂĂ��C�ɓ����Ă܂��B�@�C�ɓ����Ē����Ă��ꂵ���ł�(^-^)>�L�[���[�h�� become �ɂ��āA�X�L���̃��x���A�b�v�̂��т�>��悤�ɂ��܂����B�@�����A���ꂢ���Ȃ��ANice�ȃA�C�f�A�����B>�ł���΁A�����̃L�[���[�h���o�^�ł��āA>����ɂł���΁A���̃L�[���[�h���ƂɃT�E���h��>�w��ł�����A�����Ƃ��ꂵ����ł����ǁc�c�@��͂�A����������]�������悤�ŁA���l���̕�����t�B�[�h�o�b�N�����Ă܂�(^^;�Ƃ������ƂŁA����Ή��\��ŁA������������Ă܂��B�@�T�[�o�[�_�E������Əo����̑��܂邩��(w<!--remote_host�Fmx-tky207.raidway.ne.jp--></pre><p>

</blockquote>
<hr><font size=+1 color="#ff0000"><b>SIKAX�ǂ��ł��I</b></font>�@���e�ҁF<font color="#555555"><b>Gengoro</b></font>
<font size=-1>�@���e���F01��07��(��)03��39��54�b</font><p>
<blockquote><pre>�͂��߂܂��āBSIKAX��DL���Ďg���Ă݂܂����B�ƂĂ��C�ɓ����Ă܂��B���̃T�[�o�[�ł͎c�O�Ȃ��玭�V���E�g���N����Ȃ��̂ŁA�L�[���[�h�� become �ɂ��āA�X�L���̃��x���A�b�v�̂��т���悤�ɂ��܂����B���Y�n�̏C�Ƃ͂��������P���ɂȂ�̂ŁA�������Ă������ƂĂ���݂ɂȂ�܂��B����ȃ\�t�g�������Ă���āA���肪�Ƃ��������܂����B�ł���΁A�����̃L�[���[�h���o�^�ł��āA����ɂł���΁A���̃L�[���[�h���ƂɃT�E���h���w��ł�����A�����Ƃ��ꂵ����ł����ǁc�c������āA�킪�܂܂ł����H<!--remote_host�Ffunabashi1-20.kcom.ne.jp--></pre><p>

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
19</h4>
</body></html>

