import asyncio
import tornado.web

from handler.handler import Handler
from handler.account import ModifyFirstNameHandler, ModifyPhotoHandler


async def main():
    app = tornado.web.Application([
        (r"/", Handler),
        (r"/account/modify_photo", ModifyPhotoHandler),
        (r"/account/modify_name", ModifyFirstNameHandler),
    ])
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())