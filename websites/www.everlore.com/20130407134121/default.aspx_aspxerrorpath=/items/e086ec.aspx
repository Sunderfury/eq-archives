
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title></title>
<script src="http://ak2.imgaft.com/script/jquery-1.3.1.min.js" type="text/javascript"></script>
<script type="text/javascript" language="javascript">
	$(document).ready(function () {
		jQuery.ajax({ url: 'https://mcc.godaddy.com/parked/park.aspx/?q=pFHmpKWcpzI5LzIlYaOvrvHlAzM2pFHmpGR2ZwR1BGp2WGV2L3MkWGAkYGD5ZwtlZQp2AGpmBGt5AGR5ZmLyZwMyMlHmpGVjZGZjAQN3ZQL0ZGVkWGV2L3xyZ3Rk-1', dataType: 'jsonp', type: 'GET', jsonpCallback: 'parkcallback',
			success: function (data) { if (data["returnval"] != null) { window.location.href = 'http://everlore.com?nr=' + data["returnval"]; } else { window.location.href = 'http://everlore.com?hg=0' } }
		});
	});
</script></head><body></body></html>