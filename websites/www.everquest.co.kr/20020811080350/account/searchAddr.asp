
<html>
<head>
<title> �ּ�ã�� </title>
<meta http-equiv="Content-Type" content="text/html; charset=euc-kr">
<style>
.inputBox 
{
	color:#c8c8c8;
}
.button 
{
	BACKGROUND-COLOR:#E9EADF;
	BACKGROUND-REPEAT: no-repeat; 
	
	BORDER-BOTTOM-COLOR: white; 
	BORDER-BOTTOM-WIDTH: 1px; 
	BORDER-LEFT-COLOR: white; 
	BORDER-LEFT-WIDTH: 1px; 
	BORDER-RIGHT-COLOR: white; 
	BORDER-RIGHT-WIDTH: 1px; 
	BORDER-TOP-COLOR: white; 
	BORDER-TOP-WIDTH: 1px; 
	COLOR: rgb(65,49,49); 
	FONT-FAMILY: ����; 
	FONT-SIZE: 9pt;
	CURSOR:HAND;
}
.Cls_service
{
	FONT-FAMILY: "gulim";
	FONT-SIZE: 9pt;
	BACKGROUND-COLOR:#16173d;
	COLOR: #c8c8c8;
}
.bg-over
{
	FONT-FAMILY: "gulim";
	FONT-SIZE: 9pt;
	COLOR: #c8c8c8;
	BACKGROUND-COLOR:#373262;
}
</style>
<script LANGUAGE="javascript">
<!--
function searchAddr_click() {
	var addrToSearch;
	addrToSearch = document.searchAddr.addr.value;
	
	if (addrToSearch == ""){
		alert("�ּҸ� �Է��ϼ���");
		return false;
	}
	else if (addrToSearch.length < 2){
		alert("�ּҷδ� 2���̻����� ��Ȯ�ϰ� �Է��ϼ���.");
		return false;
	}
	ttt.src = "searchAddrproc.asp?addr=" + document.searchAddr.addr.value;
}

function window_onload() {
	document.searchAddr.addr.focus();
}


function set_addr(obj)
{
	var t = obj.getElementsByTagName("td");
	var	f = opener.document.forms[0];

	f.zipcode1.value= t(2).innerText;
	f.zipcode2.value=t(3).innerText;
	f.addr1.value=t(0).innerText;	
window.close();
//	f.addr2.value = t(1).innerText;
}

function document_onkeydown() {
	var oActive;
	
	if(event.keyCode == 13) {
		oActive = document.activeElement;
		if (oActive.id == "addr"){
			document.searchAddr.bt_addr.focus();
		}
	}
}

//-->

</script>
<script LANGUAGE="javascript" FOR="document" EVENT="onkeydown">
<!--
 document_onkeydown()
//-->
</script>

</head>

<body LANGUAGE="javascript" onload="return window_onload()" bgcolor="#16173d">
<form name="searchAddr" method="POST">
	<p> <b><font color="#c8c8c8" style="font-size:9pt">ã���� �ϴ� �ּ��� ��/��/���� �Է��ϼ���.</b> <br> &nbsp;&nbsp;&nbsp; (��:�Ｚ��, �Ÿ�1��)</font> <br>
	&nbsp;&nbsp;&nbsp; 
		<input type="text" id="addr" class="inputBox" style="width:150px; border-top:1 solid #606060;border-left:1 solid #606060; border-bottom:1 solid #606060;border-right:1 solid #606060;background-color:31335d"> 
		<input type="button" id="bt_addr" value="�ּҰ˻�" class="button" onclick="return searchAddr_click()" style="height:20; font-size:9pt">
</form>
<xml ID="ttt"> </xml>
	<table datasrc="#ttt">

		<tr width="380" class="cls_service" onclick="javascript:set_addr(this)" onmouseover="className='bg-over';this.style.cursor='hand'" onmouseout="className='cls_service'">
			
			<td width="230"> <span datafld="mainAddr"> </span> </td>
			<td width="90"> <span datafld="restAddr"> </span> </td>
			<td width="30"> <span datafld="forePostZip"> </span> </td>
			<td width="30"> <span datafld="backPostZip"> </span> </td>
		</tr>

	</table>

</body>
</html>