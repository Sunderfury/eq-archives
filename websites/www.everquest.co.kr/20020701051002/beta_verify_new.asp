<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">

<html>
<head>
	<title>��������Ʈ�� ���� ���� ȯ���մϴ�.!</title>
<style>
td {font-size:9pt; color:#c8c8c8; line-height:1.5}
td.border_lb {border-left:1 solid #7e898f; border-bottom:1 solid #7e898f}
td.border_tlb {border-top:1 solid #7e898f; border-left:1 solid #7e898f; border-bottom:1 solid #7e898f; background-color:#3b556f; color:#dddddd}
td.border_lrb {border-right:1 solid #7e898f; border-left:1 solid #7e898f; border-bottom:1 solid #7e898f;color:#dddddd}
td.border_tlbr {border-top:1 solid #7e898f; border-left:1 solid #7e898f; border-bottom:1 solid #7e898f; border-right:1 solid #7e898f;background-color:#3b556f; color:#dddddd}
.inbox {background-color:#1a3547; border : 1 1 1 1 solid #656e72; color: #c8c8c8}
#menu1 {display:none; }
#menu2 {display:none; }
#menu3 {display:none;}
#menu4 {display:none;}
#menu5 {display:none;}


a.copy:link			{ text-decoration:none; color:#3a465c; font-size:9pt}
a.copy:visited		{ text-decoration:none; color:#3a465c; font-size:9pt}
a.copy:hover		    { text-decoration:underline; color:#3a465c; font-size:9pt}
a.copy:active		{ text-decoration:none; color:#3a465c; font-size:9pt}

a:link			{ text-decoration:underline; color:#dddddd; font-size:9pt}
a:visited		{ text-decoration:none; color:#7b90a7; font-size:9pt}
a:hover		    { text-decoration:underline; color:#ffffcc; font-size:9pt}
a:active		{ text-decoration:underline; color:#dddddd; font-size:9pt}

a.dx:visited		{ text-decoration:none; color:#f2bb37; font-size:9pt}
a.dx:link			{ text-decoration:none; color:#f2bb37; font-size:9pt}
a.dx:hover		    { text-decoration:none; color:#ffffcc; font-size:9pt}
a.dx:active		{ text-decoration:none; color:#f2bb37; font-size:9pt}
</style>
<script language="javascript">
	function imgChg(imgName,n,imgStatus){
		var vash = imgName + "_" + imgStatus +".gif";
		
		if ( n == 0 ){
			document.images[imgName].src = vash;
		} else {
			document.images[imgName + n].src = vash;
		}
	}
	
		function toggleMenu(currMenu, imgName, menuname) {
			if (document.all) {
				thisMenu = eval("document.all." + currMenu + ".style")
			
				if (thisMenu.display == "block") {
					thisMenu.display = "none"
								document.images[menuname].src = "live_main_img/live_" + imgName + "_off.gif"
					
				}
				else {
					thisMenu.display = "block"
					document.images[menuname].src = "live_main_img/live_" + imgName + "_on.gif"
			
				}
				return false
			}
			else {
				return true
			}
		}
	function open_win(num){
		fullname='sclass_pop'+num+'.html'
		window.open(fullname,'sclass','toolbar=no,directories=no, copyhistory=no, status=0,menubar=0,location=0,scrollbars=no,resizable=no,width=626,height=540');
	}
	function submit_form(count){
		var name = document.frm.your_name.value;
		var jumin1 = document.frm.jumin1.value;
		var jumin2 = document.frm.jumin2.value;
	
		switch (count){
			case 'submit' :
    			if (name.length == 0){
					alert("������ ������ �ֽñ� �ٶ��ϴ�.");
					document.frm.your_name.focus();
					}
				
				else if (jumin1.length == 0 || jumin2.length== 0){
					alert("�ֹε�Ϲ�ȣ�� �Է��� �ֽñ� �ٶ��ϴ�.");
					document.frm.jumin1.focus();
				}
				else {

					document.frm.submit();
				}
				break;
			case 'reset' :
				document.frm.reset();
				document.frm.jumin1.focus();				
				break;
		}
	}
</script>
</head>
<body style="margin:0 0 0 0" background="common_img/intro_rockbg.jpg" onload="return toggleMenu('menu4', 'mu24', 'menu44'); ">
<form name="frm" method="post" action="live_newaccount.asp">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
 <tr>
  <td align="center" valign="top">
<!--������ ��ü ���̺�-->
	<table cellpadding="0" cellspacing="0" border="0">
	 <tr>
	   <td><img src="live_main_img/live_mnlogo01.gif" width="179" height="84" alt="" border="0"></td>
	   <td><img src="live_main_img/live_mnbg02.jpg" width="470" height="84" alt="" border="0"></td>
	   <td><img src="live_main_img/live_mnbg03.jpg" width="131" height="84" alt="" border="0"></td>
	   </tr>
	  <tr>
	    <td valign="top" bgcolor="#071429">
		<!--������ �޴�-->
		   <table cellpadding="0" cellspacing="0" border="0">
	 <tr>
	   <td valign="top"><img src="live_main_img/live_mnlogo02.gif" width="179" height="28" alt="" border="0"></td>
	  </tr>
	  <tr>
	  <td valign="top">
	     <table cellpadding="0" cellspacing="0" border="0" height="410" width="179" style="background-image:url('live_main_img/live_mnbg01.jpg'); background-repeat:no-repeat; background-color:#071429">
	  <tr>
	   <td align="left" height="19" style="padding-left:30;" valign="top"><a href="live_main.asp" onfocus="blur()"><img src="live_main_img/live_mu01.gif" width="121" height="19" alt="" border="0"></a></td>
	  </tr>
	  <tr>
	   <td align="left"   height="19" style="padding-left:30;" valign="top"><a href="https://bbs.lineage.co.kr/lineage/bbs2002/list.asp?group=bbs1&bbs=notify" onfocus="blur()"><img src="live_main_img/live_mu02.gif" width="121" height="19" alt="" border="0"></a></td>
	  </tr>
	   <tr>
	   <td align="left"   height="19" style="padding-left:30;" valign="top"><A HREF="#" onClick="return toggleMenu('menu1', 'mu03', 'menu11');" onfocus="blur()"><img name="menu11" src="live_main_img/live_mu03_off.gif" width="121" height="19" alt="" border="0"></a><br>
<SPAN ID="menu1">
	<a href="live_install.asp" onMouseOver="imgChg('live_main_img/live_mu04','0','over');" onMouseOut="imgChg('live_main_img/live_mu04','0','out');" onfocus="blur()"><img name="live_main_img/live_mu04" src="live_main_img/live_mu04_out.gif" width="121" height="19" alt="" border="0"></a><br>
	<a href="live_interface.asp" onMouseOver="imgChg('live_main_img/live_mu05','0','over');" onMouseOut="imgChg('live_main_img/live_mu05','0','out');" onfocus="blur()"><img name="live_main_img/live_mu05" src="live_main_img/live_mu05_out.gif" width="121" height="19" alt="" border="0"></a><br>
	<a href="live_race.asp" onMouseOver="imgChg('live_main_img/live_mu06','0','over');" onMouseOut="imgChg('live_main_img/live_mu06','0','out');" onfocus="blur()"><img name="live_main_img/live_mu06" src="live_main_img/live_mu06_out.gif" width="121" height="19" alt="" border="0"></a><br>
	<a href="live_class.asp" onMouseOver="imgChg('live_main_img/live_mu07','0','over');" onMouseOut="imgChg('live_main_img/live_mu07','0','out');" onfocus="blur()"><img name="live_main_img/live_mu07" src="live_main_img/live_mu07_out.gif" width="121" height="19" alt="" border="0"></a><br>
	<a href="live_religion.asp" onMouseOver="imgChg('live_main_img/live_mu08','0','over');" onMouseOut="imgChg('live_main_img/live_mu08','0','out');" onfocus="blur()"><img name="live_main_img/live_mu08" src="live_main_img/live_mu08_out.gif" width="121" height="19" alt="" border="0"></a><br>
	<a href="live_magic.asp" onMouseOver="imgChg('live_main_img/live_mu09','0','over');" onMouseOut="imgChg('live_main_img/live_mu09','0','out');" onfocus="blur()"><img name="live_main_img/live_mu09" src="live_main_img/live_mu09_out.gif" width="121" height="19" alt="" border="0"></a><br>
	<a href="live_skill.asp" onMouseOver="imgChg('live_main_img/live_mu10','0','over');" onMouseOut="imgChg('live_main_img/live_mu10','0','out');" onfocus="blur()"><img name="live_main_img/live_mu10" src="live_main_img/live_mu10_out.gif" width="121" height="19" alt="" border="0"></a><br>
	<a href="live_quest.asp" onMouseOver="imgChg('live_main_img/live_mu11','0','over');" onMouseOut="imgChg('live_main_img/live_mu11','0','out');" onfocus="blur()"><img name="live_main_img/live_mu11" src="live_main_img/live_mu11_out.gif" width="121" height="19" alt="" border="0"></a><br>
	<a href="live_map.asp" onMouseOver="imgChg('live_main_img/live_mu12','0','over');" onMouseOut="imgChg('live_main_img/live_mu12','0','out');" onfocus="blur()"><img name="live_main_img/live_mu12" src="live_main_img/live_mu12_out.gif" width="121" height="19" alt="" border="0"></a><br>
	<a href="live_hunt.asp" onMouseOver="imgChg('live_main_img/live_mu13','0','over');" onMouseOut="imgChg('live_main_img/live_mu13','0','out');" onfocus="blur()"><img name="live_main_img/live_mu13" src="live_main_img/live_mu13_out.gif" width="121" height="19" alt="" border="0"></a><br>
	<a href="live_guild.asp" onMouseOver="imgChg('live_main_img/live_mu14','0','over');" onMouseOut="imgChg('live_main_img/live_mu14','0','out');" onfocus="blur()"><img name="live_main_img/live_mu14" src="live_main_img/live_mu14_out.gif" width="121" height="19" alt="" border="0"></a><br>
	</span>
</td>
	   </tr>
	   <tr>
	   <td align="left"   height="19" style="padding-left:30;" valign="top"><A HREF="#" onClick="return toggleMenu('menu2', 'mu15', 'menu22'); "  onfocus="blur()"><img name="menu22" src="live_main_img/live_mu15_off.gif" width="121" height="19" alt="" border="0"></a><br>
	   <SPAN ID="menu2">
	   <a href="live_client.asp" onMouseOver="imgChg('live_main_img/live_mu16','0','over');" onMouseOut="imgChg('live_main_img/live_mu16','0','out');" onfocus="blur()"><img name="live_main_img/live_mu16" src="live_main_img/live_mu16_out.gif" width="121" height="19" alt="" border="0"></a><br>
	   <a href="live_movie.asp" onMouseOver="imgChg('live_main_img/live_mu17','0','over');" onMouseOut="imgChg('live_main_img/live_mu17','0','out');" onfocus="blur()"><img name="live_main_img/live_mu17" src="live_main_img/live_mu17_out.gif" width="121" height="19" alt="" border="0"></a><br>
	   <a href="live_wallpaper.asp" onMouseOver="imgChg('live_main_img/live_mu18','0','over');" onMouseOut="imgChg('live_main_img/live_mu18','0','out');" onfocus="blur()"><img name="live_main_img/live_mu18" src="live_main_img/live_mu18_out.gif" width="121" height="19" alt="" border="0"></a><br>
	   <a href="live_screenshot.asp" onMouseOver="imgChg('live_main_img/live_mu19','0','over');" onMouseOut="imgChg('live_main_img/live_mu19','0','out');" onfocus="blur()"><img name="live_main_img/live_mu19" src="live_main_img/live_mu19_out.gif" width="121" height="19" alt="" border="0"></a><br>
	   </span>
	   </td>
	   </tr>
	   <tr>
	   <td align="left"   height="19" style="padding-left:30;" valign="top"><A HREF="#" onClick="return toggleMenu('menu3', 'mu20', 'menu33'); "  onfocus="blur()"><img name="menu33" src="live_main_img/live_mu20_off.gif" width="121" height="19" alt="" border="0"></a><br>
	   	   <SPAN ID="menu3">
<a href="https://bbs.lineage.co.kr/lineage/bbs2002/list.asp?group=bbs1&bbs=free" onMouseOver="imgChg('live_main_img/live_mu21','0','over');" onMouseOut="imgChg('live_main_img/live_mu21','0','out');" onfocus="blur()"><img name="live_main_img/live_mu21" src="live_main_img/live_mu21_out.gif" width="121" height="19" alt="" border="0"></a><br>
<a href="live_bugreport.asp" onMouseOver="imgChg('live_main_img/live_mu22','0','over');" onMouseOut="imgChg('live_main_img/live_mu22','0','out');" onfocus="blur()"><img name="live_main_img/live_mu22" src="live_main_img/live_mu22_out.gif" width="121" height="19" alt="" border="0"></a><br>
<a href="https://bbs.lineage.co.kr/lineage/bbs2002/list.asp?group=bbs1&bbs=guild" onMouseOver="imgChg('live_main_img/live_mu23','0','over');" onMouseOut="imgChg('live_main_img/live_mu23','0','out');" onfocus="blur()"><img name="live_main_img/live_mu23" src="live_main_img/live_mu23_out.gif" width="121" height="19" alt="" border="0"></a><br>		   
<a href="live_fansite.asp" onMouseOver="imgChg('live_main_img/live_mu232','0','over');" onMouseOut="imgChg('live_main_img/live_mu232','0','out');" onfocus="blur()"><img name="live_main_img/live_mu232" src="live_main_img/live_mu232_out.gif" width="121" height="19" alt="" border="0"></a><br>
	   </span>
	   </td>
	   </tr>
	   <tr>
	   <td align="left"   height="19" style="padding-left:30;" valign="top"><A HREF="#" onClick="return toggleMenu('menu4', 'mu24', 'menu44'); " onfocus="blur()"><img name="menu44" src="live_main_img/live_mu24_off.gif" width="121" height="19" alt="" border="0"></a><br>
	    <SPAN ID="menu4">
		<a href="beta_verify_new.asp" onMouseOver="imgChg('live_main_img/live_mu25','0','over');" onMouseOut="imgChg('live_main_img/live_mu25','0','out');" onfocus="blur()"><img name="live_main_img/live_mu25" src="live_main_img/live_mu25_out.gif" width="121" height="19" alt="" border="0"></a><br>
		<a href="live_lost_passwd.asp" onMouseOver="imgChg('live_main_img/live_mu26','0','over');" onMouseOut="imgChg('live_main_img/live_mu26','0','out');" onfocus="blur()"><img name="live_main_img/live_mu26" src="live_main_img/live_mu26_out.gif" width="121" height="19" alt="" border="0"></a><br>
	  </span>
	   </tr>
	   <tr>
	   <td align="left"   height="19" style="padding-left:30;" valign="top"><A HREF="#" onClick="return toggleMenu('menu5', 'mu27', 'menu55'); " onfocus="blur()"><img name="menu55" src="live_main_img/live_mu27_off.gif" width="121" height="19" alt="" border="0"></a><br>
	    <SPAN ID="menu5">
		<a href="live_agreement.asp" onMouseOver="imgChg('live_main_img/live_mu28','0','over');" onMouseOut="imgChg('live_main_img/live_mu28','0','out');" onfocus="blur()"><img name="live_main_img/live_mu28" src="live_main_img/live_mu28_out.gif" width="121" height="19" alt="" border="0"></a><br>
		<a href="live_manage.asp" onMouseOver="imgChg('live_main_img/live_mu29','0','over');" onMouseOut="imgChg('live_main_img/live_mu29','0','out');" onfocus="blur()"><img name="live_main_img/live_mu29" src="live_main_img/live_mu29_out.gif" width="121" height="19" alt="" border="0"></a><br>
		<a href="live_faq.asp" onMouseOver="imgChg('live_main_img/live_mu30','0','over');" onMouseOut="imgChg('live_main_img/live_mu30','0','out');" onfocus="blur()"><img name="live_main_img/live_mu30" src="live_main_img/live_mu30_out.gif" width="121" height="19" alt="" border="0"></a><br>
		<a href="live_support.asp" onMouseOver="imgChg('live_main_img/live_mu31','0','over');" onMouseOut="imgChg('live_main_img/live_mu31','0','out');" onfocus="blur()"><img name="live_main_img/live_mu31" src="live_main_img/live_mu31_out.gif" width="121" height="19" alt="" border="0"></a><br>
		</span>
	   </td>
	   </tr>
	    <tr>
	   <td align="left"  height="19"  style="padding-left:30;" valign="top"><a href="http://www.everquest.co.kr" onfocus="blur()"><img src="live_main_img/live_mu32.gif" width="121" height="19" alt="" border="0"></a></td>
	   </tr>
	   <tr>
	   <td align="left" style="padding-left:15;"  valign="top" height="30"><img src="live_main_img/live_mu33.gif" width="152" height="15" alt="" border="0"></td>
	   </tr>
	   <tr>
	    <td align="center" valign="top" height="75"><a href="live_norrath.asp"><img src="live_main_img/live_norrathbn.gif" width="146" height="63" alt="" border="0"></a></td>
	   </tr>
	   <tr>
	    <td align="center" valign="top" height="400"><img src="live_main_img/live_mnpro01.gif" width="111" height="40" alt="" border="0"></td>
	   </tr>
	 </table>
	 </td>
	 </tr>
	 <tr>
	  <td></td>
	 </tr>
	 </table>
		<!--������ �޴� ��-->
		</td>
		<td valign="top" colspan="2" bgcolor="#071429">
		<!--��� -->
			<table cellpadding="0" cellspacing="0" border="0">
				<tr>
					<td><img src="live_account_img/live_actitle.gif" width="587" height="28" alt="" border="0"></td>
					<td><img src="live_shot_img/live_scrbg03.jpg" width="14" height="28" alt="" border="0"></td>
				</tr>
				<tr>
					<td background="live_shot_img/live_scrinbg.gif" valign="top" >
						<!-- Contents : Class -->
						<table cellpadding="0" cellspacing="0" border="0" style="color:#dddddd">
							<tr>
								<td height="15" colspan="2"></td>
							</tr>
							<tr>
					<td width="30" >&nbsp;</td>
					<td style="padding-left:10px; padding-right:30px;">��û�� �Է��Ͻ� �ֹε�Ϲ�ȣ�� �̸��� �Է��Ͽ� ��������Ʈ Ŭ���� ��Ÿ�׽��ͷ� ������ <br>�Ǿ����� Ȯ���� �ֽñ� �ٶ��ϴ�.<br> ��Ÿ�׽�Ʈ�� ���� �ȳ��� Ȩ�������� ���������� ������ �ֽʽÿ�.<br><br><b><font color="#eba418">�� ��Ÿ�׽��ͷ� �����ǽ� �е��� �ٷ� ��������ȭ������ �̵��˴ϴ�.</font></b><br><br><br>
</td>
				</tr>
				<tr>
					<td colspan="2"  align="center"><img src="live_account_img/live_acbr.gif" width="582" height="6" alt="" border="0"></td>
				</tr>
								<td colspan="2" background="live_account_img/live_acbg.gif" width="587" align="center">
								<table cellpadding="0" cellspacing="0" border="0" width="500" style="color:#c8c8c8; vertical-align:top">
							<tr>
								<td  height="27"></td>
							</tr>
							<tr>
								<td height="20" align="center">�ֹε�Ϲ�ȣ</TD>
							</tr>
							<tr>
								<td height="20" align="center"><input name="jumin1" class="inbox" type="Text" size="16" maxlength="6"> - <input name="jumin2" class="inbox" type="Text" size="16" maxlength="7"><br><br></TD>
							</tr>
							<tr>
								<td height="20" align="center">�� ��</TD>
							</tr>
							<tr>
								<td height="20" align="center"><input name="your_name" type="Text" size="18" class="inbox" maxlength="12"><br><br></TD>
							</tr>
							<tr>
								<tD height="40" align="center"><a href="javascript:submit_form('submit');" onfocus="blur();"><img src="live_account_img/betatester_abu01_off.gif" width="83" height="21" alt="" border="0"  onmouseover="this.src='live_account_img/betatester_abu01_on.gif'" onmouseout="this.src='live_account_img/betatester_abu01_off.gif'"></a></td>
							</tr>
						</table>
								</td>
							</tr>
							
							
						</table>
						<!-- Contents : Class -->
					</td>
					<td bgcolor="#071429" valign="top"><img src="live_shot_img/live_scrbg04.jpg" width="14" height="308" alt="" border="0"></td>
				</tr>
				<tr>
					<td><img src="live_account_img/live_acbg2.gif" width="587" height="7" alt="" border="0"></td>
					<td bgcolor="#071429"></td>
				</tr>
				<tr>
			
	   <td  bgcolor="#071429" align="center"><br><br>
	   <!--copy right-->
	   <table cellpadding="0" cellspacing="0" border="0">
	   <tr>
		 <td align="center"  height="36"><img src="common_img/bar.gif" width="366" height="26" alt="" border="0"></td>
		</tr>
		<tr>
		 <td align="center" height="35" style="font-size:8pt"><font color="#364258" style="font-family: 'verdana'; font-size:7pt">EverQuest, The Ruins of Kunark, The Scars of Velious and The Shadows of Luclin are trademarks of<br>
Sony Computer Entertainment America Inc. SOE and SOE logo are trademarks of Sony Online Entertainment Inc. <br>
All other trademarks are properties of their respective owners. <br>��2002 Sony Computer Entertainment America Inc.  Used with permission.<br>
All rights reserved.<br></font></td>
		</tr>
		<tr>
			<td height="25"></td>
		</tr>
	   </table>
	   <!--copy right-->
	   </td>
				</tr>
			<td align="left" bgcolor="#071429">
	    <!--�ѱ��� copyright-->
		<table cellpadding="0" cellspacing="0" border="0">
	   <tr>
	   <td  align="center"><font color="#313e51" style="font-size:8pt; letter-spacing:0">����Ư���� �Ｚ�� 143-8 �±����� (��)135-090 �߿�������Ʈ / ��ǥ�̻�: ������  ��ǥ ��ȭ : 02-2186-3300</font></td>
       </tr>
	  <tr>
	   <td align="center"><font color="#313e51" style="font-size:8pt; letter-spacing:0">����ڵ�Ϲ�ȣ:220-81-43000 / ����Ǹž��Ű� �� 14381ȣ / �����: 1566-6600 (�������� ��������) </font></td>
       </tr>
	   <tr>
	   <td align="center"><font color="#313e51" style="font-size:8pt; letter-spacing:0">FAX:02-556-6206 / �������� ��ȣå����:�ּ���(<a class="copy" href="mailto:eqprivacy@everquest.co.kr">eqprivacy@everquest.co.kr</a>) / <a class="copy" href="mailto:webmaster@everquest.co.kr" style="font-size:8pt">�������� ����</a></font><br><br><br></td>
       </tr>
	  </table>
		<!--�ѱ��� copyright-->	<br><br><br><br>
	   </td>
			</table>
		<!--���-->
		</td>
	  </tr>
	   </table>
<!--������ ��ü ���̺�-->	   
	</td>
	</tr>
</table>	   


</form>
</body>
</html>
