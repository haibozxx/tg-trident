import logging
from fastapi import FastAPI
from api.api import api_router
from core.config import settings

import uvicorn


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

app = FastAPI(openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(api_router, prefix=settings.API_V1_STR)

    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, debug=True, workers=1)
