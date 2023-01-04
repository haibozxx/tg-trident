import asyncio
# import tornado.web

# from handler.handler import Handler
# from handler.account import ModifyFirstNameHandler, ModifyPhotoHandler


# async def main():
#     app = tornado.web.Application([
#         (r"/", Handler),
#         (r"/account/modify_photo", ModifyPhotoHandler),
#         (r"/account/modify_name", ModifyFirstNameHandler),
#     ])
#     app.listen(8888)
#     await asyncio.Event().wait()

# if __name__ == "__main__":
#     asyncio.run(main())

from fastapi import FastAPI
from api.api import api_router
from core.config import settings

import uvicorn

app = FastAPI(openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(api_router, prefix=settings.API_V1_STR)

    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888)
