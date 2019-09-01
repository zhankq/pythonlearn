<?php

/**
 * redis sub(消息订阅端)
 * @ blog: phping.sinaapp.com
 * @date 2016-04-24 15:00
 */
$redis = new Redis();
// 第一个参数为redis服务器的ip,第二个为端口
$res = $redis->connect('127.0.0.1', 6379);
$redis->auth('foobared');

// test为发布的频道名称,hello,world为发布的消息
$res = $redis->publish('test','hello,world');
