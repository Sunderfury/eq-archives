

<HTML>
<HEAD>
<META HTTP-EQUIV="Content-Type" content="text/html; charset=x-sjis">

<script language="JavaScript">
<!--
function SetColor(){
    window.parent.frames[0].document.bgColor = "#"
                     + document.login.R.options[document.login.R.selectedIndex].value
                     + document.login.G.options[document.login.G.selectedIndex].value
                     + document.login.B.options[document.login.B.selectedIndex].value;
}
// -->
</script>

</HEAD>
<BODY bgcolor=black onLoad='SetColor()' text=white>

<table border=0 cellspacing=0>

<form name='login' method='post' action='room.asp' target='_parent'>

    <tr>
        <td nowrap>���O
            <input type='text' name='handle' size=20 maxlength=20 value=''>
            ���[���A�h���X
            <input type='text' name='mail' size=30 maxlength=50 value=''></td></tr>
    <tr>
        <td nowrap>���O�̐F�@
        �� <select name='R' onchange='SetColor()'>
        
            <option value='00'>  0
            <option value='1A' selected>  1
            <option value='33'>  2
            <option value='4C'>  3
            <option value='66'>  4
            <option value='80'>  5
            <option value='99'>  6
            <option value='B2'>  7
            <option value='CC'>  8
            <option value='E6'>  9
            <option value='FF'> 10</select>

        �� <select name='G' onchange='SetColor()'>
        
            <option value='00'>  0
            <option value='1A'>  1
            <option value='33'>  2
            <option value='4C'>  3
            <option value='66' selected>  4
            <option value='80'>  5
            <option value='99'>  6
            <option value='B2'>  7
            <option value='CC'>  8
            <option value='E6'>  9
            <option value='FF'> 10</select>

        �� <select name='B' onchange='SetColor()'>
        
            <option value='00'>  0
            <option value='1A'>  1
            <option value='33'>  2
            <option value='4C' selected>  3
            <option value='66'>  4
            <option value='80'>  5
            <option value='99'>  6
            <option value='B2'>  7
            <option value='CC'>  8
            <option value='E6'>  9
            <option value='FF'> 10</select>
        ���������[�h����
        <!-- ������ύX����ƃ����[�h���Ԃ��ύX�ł��܂��B
             �������Aconfig.inc �̃^�C���A�E�g�b����蒷���ƁA���������Ƀ^�C���A�E�g���Ă��܂��܂��B -->
        <select name='Reload'>
            <option value='20'>20�b
            <option value='30'>30�b
            <option value='60'>60�b
            <option value='90'>90�b
        </select>
        </td></tr>
        <tr><td align='right'>�\���s�� <select name = 'logview'><option value='10'  >10�s<option value='20' selected >20�s<option value='30'  >30�s<option value='40'  >40�s<option value='50'  >50�s</select>�@�@<input type='submit' value='��������'>�@<input type="button" value="�@�߂�@" onClick="history.back(1)"></td></tr>
</form>
        <tr><td valign='top' nowrap></td></tr> 
</table>
<br>
</BODY>
</HTML>
