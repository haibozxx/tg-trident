from fastapi import APIRouter
from api.endpoint import account

api_router = APIRouter()

api_router.include_router(account.router, prefix="/account")
