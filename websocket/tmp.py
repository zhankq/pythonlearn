#!/usr/bin/env python3

# WS server example

import asyncio
import datetime
import random
import websockets
import redis
import json



r = redis.Redis(host='localhost', port=6379, db=0,password="foobared")   #如果设置了密码，就加上password=密码
pub = r.pubsub()
pub.subscribe('redisChat') # 调频道



async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")



async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

########################################################################

USERS = set()
STATE = {"value": 0}


async def register(websocket):
    USERS.add(websocket)
    await notify_users()

async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])

def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})

def state_event():
    return json.dumps({"type": "state", **STATE})

async def redis_demo(websocket, path):
   # name = await websocket.recv()
    #USERS.add(websocket)

    while True:
        data = pub.parse_response() # 准备接收
        await websocket.send(str(data))
     #   for user in USERS:
     #       user.send(str(data))






start_server = websockets.serve(redis_demo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



