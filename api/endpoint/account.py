from fastapi import APIRouter
from pydantic import BaseModel
from api import depends
from tg_api import account
from schemas.response import Response


router = APIRouter()


class ModifyPhotoReq(BaseModel):
    phone: str
    photo_url: str

@router.post("/modify_photo")
async def modify_photo(req: ModifyPhotoReq):
    phone = req.phone
    client = await depends.get_tg_client(phone)
    account_obj = account.Account(client)
    res = await account_obj.modify_user_photo(req.photo_url)
    if res:
        return Response()
    else:
        return Response(code=-1)
