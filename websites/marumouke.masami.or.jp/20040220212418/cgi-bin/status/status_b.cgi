<!doctype html public "-//IETF//DTD HTML//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=x-sjis">
<title></title>
<!-- <link rel="stylesheet" href="tst.css" type="text/css"> -->
</head>

<body bgcolor="snow"><BR>

<p align="center"><font FACE="Verdana" SIZE="6"><b>Login</b></font></p>

<hr WIDTH="300" align="center">

<p align="center"><small><strong>�� <font color="tomato">Please enter your name and password.</font> ��</strong></small></p>

<form METHOD="POST" ACTION="status_b.cgi">
  <input type="hidden" name="mode" value="check">
  <table BORDER="0" align="center">
    <tr>
      <td>���[�U�[���F</td>
      <td><input TYPE="TEXT" NAME="name" SIZE="20"></td>
    </tr>
    <tr>
      <td>�p�X���[�h�F</td>
      <td><input TYPE="PASSWORD" NAME="pwd" SIZE="20"></td>
    </tr>
  </table>
  <div align="center"><center><p><input TYPE="SUBMIT" VALUE="���O�C��"> <input TYPE="RESET" VALUE="���Z�b�g"> </p>

�V�K�o�^����ꍇ�̓`�F�b�N���Ă��������B<input type="checkbox" name="reg_flag">

  </center></div>
</form>

<hr WIDTH="300" align="center">

<div align="right">
<form action="status_b.cgi" method="post">
  <input type="hidden" name="mode" value="master_list">
  <input TYPE="PASSWORD" NAME="pwd" SIZE="10">
  <input type="submit" value="�Ǘ��҃��[�h">
</form>
</div>


</body>
</html>
