
<html>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=big5">
<link REL="STYLESHEET" TYPE="text/css" HREF="b-style.css">
<title>�K�X���</title>
</head>

<body background="/image/base.jpg">
<body link="white" vlink="white" alink="white">
<BODY TEXT=black >


<body>
<script LANGUAGE="VbScript">
<!--
function chk_data
if len(ltrim(form_chk.id_no.value)) = 0 then 
   alert("�b�����i��J�ť�,�п�J���!")
   form_chk.id_no.focus
   exit function
end if 
if len(ltrim(form_chk.password.value)) = 0 then 
   alert("�K�X���i��J�ť�,�п�J���!")
   form_chk.password.focus
   exit function
end if
form_chk.submit
end function
-->
</script>

<p align="center"><font color=white>�m<a href="index.htm">���}</a>�n</font></p>


<form method="POST" name="form_chk">
  <div align="center"><center><table border="1" cellspacing="1" cellpadding="2">
    <tr>
      <td bgcolor="925F38" width="100%" colspan="2"><font color="ffffff"><div align="center"><center><p>�޲z�̧@�~</font></td>
    </tr>
    <tr align="center">
      <td align="right" bgcolor="cyan">*�b��:</td>
      <td align="left"><input type="text" name="id_no" size="8" maxlength="8"></td>
    </tr>
    <tr align="center">
      <td align="right" bgcolor="cyan">*�K�X:</td>
      <td align="left"><input type="password" name="password" size="8" maxlength="8"></td>
    </tr>
  </table>
  </center></div><div align="center"><center><p><input type="button" value="�K�X���"
  name="SEND" onclick="chk_data">&nbsp; <input type="reset" value="�M�����g"
  name="clear"></p>
  </center></div>
</form>
</body>
</html>
