<html>

<head>
	<title>AccessAnalyzer...</title>
	<style><!--
		td   { font-size: 10pt; }
		.big { font-size: 12pt; }
	--></style>
</head>

<body bgcolor="#FFFFFF" link=#000000 vlink=#000000 onload='chkActValue()'>

<script language="JavaScript"><!--

 // mday //

var dd = 10;
mdayEnableText  = new Array(
					'�f�[�^�^�C�v',
					'�S\�f�[�^�\��',
					'�J�X�^��(�v�ݒ�)',
					'�y�[�W���q�b�g',
					'���ԃf�[�^',
					'�z�X�g�f�[�^',
					'�����N���f�[�^',
					'OS�f�[�^',
					'�u���E�U�f�[�^',
					'�T�[�`���[�h'
					);

mdayEnableValue  = new Array(
					'null',
					'all',
					'orig',
					'each',
					'hour',
					'host',
					'reff',
					'os',
					'agent',
					'word'
					);

// mon //

var mm = 9;
monEnableText  = new Array(
					'�f�[�^�^�C�v',
					'��/�j��/����',
					'�J�X�^��(�v�ݒ�)',
					'�y�[�W���q�b�g',
//					'���t�f�[�^',
//					'�j���f�[�^',
//					'���ԃf�[�^',
					'�z�X�g�f�[�^',
					'�����N���f�[�^',
					'OS�f�[�^',
					'�u���E�U�f�[�^',
					'�T�[�`���[�h'
					);

monEnableValue  = new Array(
					'null',
					'main',
					'orig',
					'each',
//					'mday',
//					'wday',
//					'hour',
					'host',
					'reff',
					'os',
					'agent',
					'word'
					);



	function monEnable(){

		if( document.LaunchAnalyzer.Data.selectedIndex > mm-1 ){
			document.LaunchAnalyzer.Data.selectedIndex = 0;
		}	// �󗓖h�~��B

		document.LaunchAnalyzer.mon.disabled  =  0;
		document.LaunchAnalyzer.mday.disabled =  1;
		document.LaunchAnalyzer.Data.disabled =  0;
		document.LaunchAnalyzer.Data.length   = mm;

		for(i = 0; i < mm; i++ ){	// ���f�[�^
			document.LaunchAnalyzer.Data[i].text =  monEnableText[i] ;
			document.LaunchAnalyzer.Data[i].value = monEnableValue[i] ;
		}

	}

	function mdayEnable(){			 // ���f�[�^

		if( document.LaunchAnalyzer.Data.selectedIndex > dd-1 ){
			document.LaunchAnalyzer.Data.selectedIndex = 0;
		}	// �󗓖h�~��B

		document.LaunchAnalyzer.mon.disabled  =  0;
		document.LaunchAnalyzer.mday.disabled =  0;
		document.LaunchAnalyzer.Data.disabled =  0;
		document.LaunchAnalyzer.Data.length   = dd;

		for(i = 0; i < dd; i++ ){
			document.LaunchAnalyzer.Data[i].text =  mdayEnableText[i] ;
			document.LaunchAnalyzer.Data[i].value = mdayEnableValue[i] ;
		}

	}

	function allDisable(){
		document.LaunchAnalyzer.mon.disabled  = 1;
		document.LaunchAnalyzer.mday.disabled = 1;
		document.LaunchAnalyzer.Data.disabled = 1;
	}

	function chkActValue(){
		     if( document.LaunchAnalyzer.Act[0].checked == 1 ){ mdayEnable(); }
		else if( document.LaunchAnalyzer.Act[1].checked == 1 ){ monEnable();  }
		else if( document.LaunchAnalyzer.Act[2].checked == 1 ){ allDisable(); }
	}


// --></script><div align="center"><center>

<table border="0" width="300" height="100%">
  <tr>
	<td nowrap><form method="POST" name="LaunchAnalyzer">

	<p>AccessAnalyzer<br><font size="+1" class=big>�A�N�Z�X�A�i���C�U</font></p>
	<hr size="1">

	<p>
	<input type="radio" name="Act" value="statMday" onclick="mdayEnable()" checked>���ʉ��
	<input type="radio" name="Act" value="statMon" onclick="monEnable()">���ʉ��
	<input type="radio" name="Act" value="catSetup" onclick="allDisable()">�ݒ�ύX
	</p>

	<p><select name="mon">
		<option value=0207>02/07</option>
		<option value=0206>02/06</option>
		<option value=0205>02/05</option>
		<option value=0204>02/04</option>
		<option value=0203>02/03</option>
		<option value=0202>02/02</option>
		<option value=0201>02/01</option>
		<option value=0112>01/12</option>
		<option value=0111>01/11</option>
		<option value=0110>01/10</option>

	</select> /

	<input type="text" size="2" maxlength="2" name="mday" value="27">
	<select name="Data">
		<option value="null" selected>�f�[�^�^�C�v</option>
		<option></option><option></option>
		<option></option><option></option>
		<option></option><option></option>
		<option></option><option></option>
		<option></option><option></option>
		<!-- ��JavaScript�Ő�������B -->
	</select> <input type="submit" value="Start!">
	</p>

	<hr size="1">

	<p align="right">(c) 1999 <a href=http://www.imaginet.ne.jp/~nobu/>Nobutaka Makino</a>.</p>

	</form></td>
	</tr>
</table>
</center></div>
</body>
</html>
