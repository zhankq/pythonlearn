import redis
r = redis.Redis(host='localhost', port=6379, db=0,password="foobared")   #如果设置了密码，就加上password=密码

pub = r.pubsub()
pub.subscribe('redisChat') # 调频道

while True:
    msg = pub.parse_response() # 准备接收
    #print(msg[2].decode('utf8'))
    print(str(msg[2]))


