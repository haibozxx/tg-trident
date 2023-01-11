from fastapi import APIRouter
from api.endpoint import account, chat

api_router = APIRouter()

api_router.include_router(account.router, prefix="/account")
api_router.include_router(chat.router, prefix="/chat")
