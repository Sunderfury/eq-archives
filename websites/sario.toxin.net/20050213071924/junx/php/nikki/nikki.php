<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=Shift_JIS">
<title>Junx eq</title>
</head>
<style type="text/css">
p {margin-left:30}

<!--
BODY {
scrollbar-face-color:      #FFFFFF;
scrollbar-shadow-color:    #99cccc;
scrollbar-highlight-color: #99cccc;
scrollbar-3dlight-color:   #99cccc;
scrollbar-darkshadow-color:;
scrollbar-track-color:     #99cccc;
scrollbar-arrow-color:     #99cccc; }

</style>
<body>
<DIV ALIGN="center">
<IMG src="../../img/img-box/img20031015121218.jpg" border="0" width="400" height="100" >
</DIV>
<BR>
<blockquote>

<?php
/*******************************
 *    
 *    ���L����[�I�@by ToR
 *
 *            http://php.s3.to/
 *******************************
 * 2002/04/09 v2.0
 * 2002/07/13 v2.0 ����(���O�`���ύX�j
 *
 *NO	�����������	���t��		�薼	�{��
 * 3	1003935600	2001/10/25(��)	dai��	��honbun
 * �@�@����
 *�����������	�薼	�{��
 *1003935600	dai��	��honbun
 *
 * ���O����茏���𒴂���Ɖߋ��ިڸ�؂ɑ����
 * �����ƂɃ��O�t�@�C��������܂��B
 * �D���ȓ��t���ŏ������߁A�V�������ɕ��т܂��B�ߋ����O�͌Â����ł��B
 * �����O�ŌÓ��L���Â����L���������ꍇ�́A�����O�ŌÓ��L���ߋ����O�ɍs���܂�
 *
 * ��̃��O�t�@�C���Ɖߋ����O�p�ިڸ�؂��쐬���A
 * ���O�t�@�C����666�A�ߋ��ިڸ�؂�777���߰Я��݂�ݒ肵�ĉ������B
 * �ߋ����O�͎����쐬���܂�
 *
 */
/*--------�ݒ�-----------*/
$page_def = 10;			//�P�y�[�W�ɕ\�����錏��
$logfile  = "nikki.txt";	//���O�t�@�C����
$password = "upiupi";		//�Ǘ��p�p�X���[�h
$logdir   = "./log/";		//�ߋ����O�p�ިڸ��(777)
$ext      = ".dat";		//�ߋ����O�g���q
$mudai    = "(����)";//����̏ꍇ�̃^�C�g��

$t_size   = 65;				//�薼���͕�
$cols     = 75;				//�{���G���A���͕�
$rows     = 10;				//�{���G���A���͍���
$jisa     = 0;				//�����i?���ԁj

//echo "���ݎ���:".strftime("%Y/%m/%d %H:%M:%S",time()+$jisa*3600);

/*���L�e���v���[�gHTML�@<%IN_DATE%>�@�����t  <%IN_TITLE%>���薼
�@�@�@�@�@�@�@�@�@�@	<%IN_MESSAGE%>���{�� <%DEL_FORM%>���폜�ҏW�{�^��
�@�킩��͈͂ŕύX���Ă��������B���t���̐F�͂���������Ɖ��̕��ɂ���܂�
*/
//���C��
$main = <<<MAIN
<TABLE BORDER=0 WIDTH=90%>
<TR><TD BGCOLOR=#99cccc><FONT COLOR=#ffffff>��</FONT>
<FONT COLOR=#ffffff><%IN_TITLE%></FONT>
</TD></TR><%DEL_FORM%></TABLE>
&nbsp;&nbsp;<FONT COLOR=#000000 size="2"> <%IN_DATE%> </FONT>
<p><FONT size="2"><%IN_MESSAGE%></FONT></p>
MAIN;

//�ҏW�E�폜�{�^���i���<%DEL_FORM%>�����ƒu���j
$delform = <<<DEL
<tr align=right><td>
<input type=radio name=editno value=<%NO%>>�ҏW 
<input type=checkbox name=del[<%NO%>] value=on>�폜
</td></tr>
DEL;

//�t�b�^
$foot = <<<FOOT
</blockquote>
<p align="right"><small><a href="http://php.s3.to" target=_blank>���b�cPHP�I</a>
</body></html>
FOOT;

/*------------------------*/
//PHP4.1.0�ȍ~�Ή��͈ȉ�3�s�́^�^�����
extract($_POST);
extract($_GET);
extract($_SERVER);

$utime = time()+$jisa*3600;
$today = getdate($utime);

// ���t���\���֐�
function day_print($stamp) {

  $today = getdate($stamp);
  $youbi = array('Sun','Mon','Tue','Wed','Thu','Fri','Sat');
  // ���t������yyyy/mm/dd(�j)
  $date_out = strftime("%Y/%m/%d(".$youbi[$today[wday]].")", $stamp);
  $date_out2 = strftime("%Y/%m/%d", $stamp);
  // �y�j�͐F�A���j�͐ԐF
  if ($today[wday]==0) {
    return "$date_out2<font color=red>(".$youbi[$today[wday]].")</font>";
  } elseif($today[wday]==6) {
    return "$date_out2<font color=blue>(".$youbi[$today[wday]].")</font>";
  }
  return $date_out;
}
// �\�[�g�֐�
function day_cmp($a, $b) {
  list($aa,) = explode("\t", $a);
  list($bb,) = explode("\t", $b);
  
  if ($aa == $bb) return 0;
  return ($aa > $bb) ? -1 : 1;
}

// �ߋ��t�@�C����
if (ereg("^[0-9]{6}",$logno)) $logfile = $logdir.$logno.$ext;

// �t�@�C���ǂݍ���
$lines = @file($logfile);
usort($lines, "day_cmp");

/* �ߋ����O�\�����[�h */
if ($mode=="past") {
  echo "<center><H3>�ߋ��̓��L</H3>���t���N���b�N����Ɖߋ��̓��L�������܂��B<BR><BR>";

  //���O�f�B���N�g������
  $d = dir($logdir);
  while ($ent = $d->read()) {
    if (ereg("^[0-9]{6}$ext$", $ent))
      $entarr[] = $ent;
  }
  $d->close();

  if (!is_array($entarr)) die("�ߋ��̓��L�͂���܂���");
  //�V�������̂���\�[�g
  arsort($entarr);
  foreach ($entarr as $name) {
    printf("<a href=\"%s?logno=%s\">%1d�N%1d���̓��L</a><br><br>\n",
         $PHP_SELF,substr($name, 0, 6),substr($name, 0, 4),substr($name, 4, 2));
  }
echo <<<EOA
<form action="$PHP_SELF"><input type=submit value="  �� ��  "></form>
<br><br></center></blockquote><p align=right><small><a href=http://php.s3.to target=_blank>���b�cPHP�I</a>
</body></html>
EOA;
  exit;
}

/* ���O�C�� */
if ($act) {
  if ($REQUEST_METHOD != "POST") die("�s���ȓ��e�����Ȃ���");
  if (!$pass) die("�p�X���[�h�����Ă�������");
  if (isset($pass) && $pass != $password) die("�p�X���[�h���Ⴄ��");
}

switch ($act) {
case 'prev':
  $utime = mktime(date("H")+$jisa,date("i"),date("s"),$mon,$day,$year);
  if (!checkdate($mon, $day, $year)) $err = "<font color=red>���t���L���ł͂���܂���</font>";

  if (empty($com)) $err="<font color=red><b>�������͂���Ă܂���</b></font>";
  if (empty($sub)) $sub = $mudai;

  if (get_magic_quotes_gpc()) {
    $com = stripslashes($com);
    $sub = stripslashes($sub);
  }

  $com = str_replace("\r\n", "\r", $com);
  $com = str_replace("\r", "\n", $com);
  $com = str_replace("\n", "<br>", $com);
  $com = str_replace("\t", "    ", $com);

  // �u��
  $mes = str_replace("<%IN_DATE%>", day_print($utime), $main);
  $mes = str_replace("<%IN_TITLE%>", $sub, $mes);
  $mes = str_replace("<%IN_MESSAGE%>", $com, $mes);
  $sub = htmlspecialchars($sub);
  $com = htmlspecialchars($com);
  // �v���r���[
  echo $mes;

echo <<<EOB
<hr size=1><center>$err
<table><tr><td>
<form action="$PHP_SELF" method="POST">
<input type=hidden name=act value=regi>
<input type=hidden name=pass value="$pass">
<input type=hidden name=sub value="$sub">
<input type=hidden name=com value="$com">
<input type=hidden name=wtime value="$utime">
<input type=hidden name=lineno value="$lineno">
<input type=submit value="�@���̓��e�œ��e�@"></form>
</td><td>
<form action="$PHP_SELF" method="POST">
<input type=hidden name=act value=edit>
<input type=hidden name=pass value="$pass">
<input type=hidden name=esub value="$sub">
<input type=hidden name=ecom value="$com">
<input type=submit value="�@�߂�@"></form>
</td></tr></table>
</center></body></html>
EOB;
  break;

case 'regi':
  if (get_magic_quotes_gpc()) {
    $com = stripslashes($com);
    $sub = stripslashes($sub);
  }

  $newline = "$wtime\t$sub\t$com\n";

  if ($lineno) {
    // �ҏW�̏ꍇ�A����No�̕��ƒu��������
    $find = false;
    for ($i = 0; $i < count($lines); $i++) {
      list($lno,) = explode("\t", $lines[$i]);
      if ($lno == $lineno) {
        $lines[$i] = $newline;
        $find = true;
        break;
      }
    }
    if ($find == false) die("�Y���L����������܂���");
  } else {
    // ���O�̐擪�ɋL���ǉ�
    array_unshift($lines, $newline);
    if (count($lines) > $page_def) {
      for ($j = count($lines); $j > $page_def; $j--) {
        list($p_wtime,) = explode("\t", $lines[$j-1]);
        $pastlog = $logdir.date("Ym",$p_wtime).$ext;
        $pp = @fopen($pastlog, "a") or die("$pastlog�̉ߋ����O�ɏ������߂܂���<br>�߰Я��݂��m�F���Ă�������");
        flock($pp, LOCK_EX);
        fputs($pp, $lines[$j-1]);
        fclose($pp);
        // ��������폜
        array_pop($lines);
      }
    }
  }

  // ���O�X�V
  $fp = fopen($logfile, "w");
  flock($fp, LOCK_EX);
  fputs($fp, implode('', $lines));
  fclose($fp);

case 'edit':
  // �u�߂�v�̎�
  if (get_magic_quotes_gpc()) {
    $ecom = stripslashes($ecom);
    $esub = stripslashes($esub);
    $ecom = str_replace("<br>", "\n", $ecom);
  }
  // �ҏW���폜NO���w�肳�ꂽ��
  $find = false;
  if (is_array($del) || isset($editno)) {
    for ($i = 0; $i < count($lines); $i++) {
      list($e_time,$e_sub,$e_com) = explode("\t", $lines[$i]);
      if ($del[$e_time] == "on") {
        $lines[$i] = "";
        $find = true;
      }
      if ($editno == $e_time) {
        $etime = $e_time;
        $esub = $e_sub;
        $ecom = $e_com;
        break;
      }
    }
  }
  // �ҏW�̏ꍇ�i���t���Ɖ��s�ϊ��j
  if (isset($editno)) {
    $today = getdate($etime);
    $ecom = str_replace("<br>", "\n", $ecom);
  }
  // �폜�̏ꍇ�i���O���������j
  if ($find == true) {
    $fp = fopen($logfile, "w");
    flock($fp, LOCK_EX);
    fputs($fp, implode('', $lines));
    fclose($fp);

    unset($editno);
  }

case 'admin':
  $title = (isset($editno)) ? "�ҏW" : "�V�K��������";

//�������݃w�b�_
echo <<<EOC
<hr size=1>[<a href="$PHP_SELF?">&lt;&lt;�߂�</a>]
<form action="$PHP_SELF" method="POST">
<input type=hidden name=act value=prev>
<input type=hidden name=pass value="$pass">
<input type=hidden name=lineno value="$etime">

<table align=center>
<tr><td align=center><h4>$title</h4></td></tr>
<tr><td align=left>
EOC;

  //�N�̃Z���N�g�{�b�N�X�i�}2�N�j
  echo "<select name=year>\n";
  for ($y=$today[year]+2; $y>=$today[year]-2; $y--) {
    $sel = ($y == $today[year]) ? " selected" : "";
    echo "<option value=\"$y\"$sel>$y</option>\n";
  }
  echo "</select>/\n";
  //���̃Z���N�g�{�b�N�X(12-1���j
  echo "<select name=mon>\n";
  for ($m=12; $m>=1; $m--) {
   $sel = ($m == $today[mon]) ? " selected" : "";
   echo "<option value=\"$m\"$sel>$m</option>\n";
  }
  echo "</select>/\n";
  //���̃Z���N�g�{�b�N�X(31-1��)
  echo "<select name=day>\n";
  for ($d=31; $d>=1; $d--) {
    $sel = ($d == $today[mday]) ? " selected" : "";
    echo "<option value=\"$d\"$sel>$d</option>\n";
  }
  echo "</select>\n";

  //�������݃t�H�[��
  echo <<<EOD
 �薼 <input type=text size="$t_size" name=sub value="$esub"><br>
<textarea name="com" cols="$cols" rows="$rows">$ecom</textarea></td></tr>
<tr><td align=center><input type=submit value=" �v���r���[ ">
<input type=reset value="clear"></form>
</td></tr></table><hr>
<form action="$PHP_SELF" method=POST>
EOD;

default:
  //�ߋ����O�\���̏ꍇ�A�^�C�g��
  if ($logno) printf("<center><h3>%4d�N%1d���̓��L</h3></center>\n", substr($logno, 0, 4),substr($logno, 4, 2));

  /*�@�P�y�[�W���\�� */
  if ($page) {
    $st = ($page-1) * $page_def;
  } else {
    $page = 1;
    $st = 0; 
  }
  $lines = @file($logfile);
  usort($lines, "day_cmp");

  for ($i = $st; $i < $st+$page_def; $i++) {
    if($lines[$i]=="") continue;
    list($wtime, $sub, $com) = explode("\t", $lines[$i]);
    $mes = str_replace("<%IN_DATE%>", day_print($wtime), $main);
    $mes = str_replace("<%IN_TITLE%>", $sub, $mes);
    $mes = str_replace("<%IN_MESSAGE%>", $com, $mes);
    $form = str_replace("<%NO%>", $wtime, $delform);
    $mes = ($act) ? ereg_replace("<%DEL_FORM%>", $form, $mes) : ereg_replace("<%DEL_FORM%>","",$mes);
    echo $mes;
  }
  // �y�[�W���O�쐬
  if ($logno && count($lines) > $page_def) {
    if ($page > 1) $next = sprintf("<a href=\"%s?page=%s&logno=%s\">&lt;&lt;</a> ", $PHP_SELF,$page-1,$logno);
    for ($i = 1; $i*$page_def < count($lines)+$page_def; $i++) {
      if ($page == $i) {
        $next .= " $i ";
      } else {
        $next .= " <a href=\"$PHP_SELF?page=$i&logno=$logno\">$i</a> ";
      }
    }
    if($i > $page+1) $next .= sprintf(" <a href=\"%s?page=%s&logono=%s\">&gt;&gt;</a>", $PHP_SELF,$page+1,$logno);

    echo "<p><br>[ $page_def �����\�� : $next ]�@�@�@[<a href=\"$PHP_SELF\">���݂̓��L��</a>]";
  }
  echo "<hr size=1>";
  // �ҏW�E�폜�{�^��
  if ($act) {
    echo "<p align=center><input type=hidden name=act value=edit>
          <input type=hidden name=page value=\"$page\">
          <input type=hidden name=pass value=\"$pass\">
          <input type=submit value=\" �ҏW / �폜 \"></form>";
  // �ߋ��փ{�^�����߽���͗�
  } elseif(!$logno) {
    echo "<p align=right><form action=\"$PHP_SELF\">
          <input type=hidden name=mode value=past>
          <input type=submit value='�ߋ��̓��L'></form>
          <form action=\"$PHP_SELF\" method=POST>
          <input type=hidden name=act value=admin>
          <input type=password name=pass size=8>
          <input type=submit value=\" �Ǘ� \"></form></p>";
  }
}
echo $foot;
?>
