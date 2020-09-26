<?php
	$key="qw8J";
	$defaultdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
	$json=json_encode($defaultdata);
	$text = $json;
   	$outText = '';

    	// Iterate through each character
	for($i=0;$i<strlen($text);$i++) {
		$outText .= $text[$i] ^ $key[$i % strlen($key)];
	}
	$cookie=base64_encode($outText);
	echo $cookie;
?>
