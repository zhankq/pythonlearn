<?php

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->auth('foobared');


$redis->subscribe(array('test'), 'callback');

// 回调函数,这里写处理逻辑
function callback($instance, $channelName, $message) {
 $str = $channelName."==>".$message.PHP_EOL;
 echo $str;
 file_put_contents("write.txt", $str, FILE_APPEND);;
}
