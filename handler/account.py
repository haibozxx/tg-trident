import asyncio
import time
import tornado.web
from tornado import gen

class ModifyPhotoHandler(tornado.web.RequestHandler):

    def post(self):
        pass

    async def get(self):
        for i in range(5):
            print(i)
            # time.sleep(1)
            # await asyncio.sleep(1)
            await gen.sleep(1)

    
class ModifyFirstNameHandler(tornado.web.RequestHandler):
    
    def post(self):
        pass