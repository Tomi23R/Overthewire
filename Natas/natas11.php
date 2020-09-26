<?php
	$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
	$cookie='ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=';
	$json=json_encode($defaultdata);
	$cookie_decoded=base64_decode($cookie);

	$text = $cookie_decoded;
	$outText = '';
	$key = $json;

	// Iterate through each character
	for($i=0;$i<strlen($text);$i++) {
		$outText .= $text[$i] ^ $key[$i % strlen($key)];
	}
	echo $outText;
?>
