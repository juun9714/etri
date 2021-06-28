########################
# Server

import asyncio              
import websockets          
import json
import time
from datetime import datetime

dt = datetime.now()
dt.microsecond

async def accept(websocket, path):
    print("client connected")
    while True:
        data = await websocket.recv();#wait for client
        print("receive : " + data)
        x=json.loads(data)
        dt = datetime.now()
        s=str(dt.microsecond)
        #s=str(time.time())
        id=x["requestId"]
        response_json = '{"action":"get","requestId":"'+id+'","value":"2372", "timestamp":'+s+'}'
        await websocket.send(response_json);# send response
        
start_server = websockets.serve(accept, "127.0.0.1", 3001)

# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
########################