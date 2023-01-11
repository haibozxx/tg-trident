from fastapi import APIRouter
from pydantic import BaseModel
from api import depends
from tg_api import account
from schemas.response import Response


router = APIRouter()


class ModifyPhotoReq(BaseModel):
    phone: str
    photo_url: str

#修改头像
@router.post("/modify_photo")
async def modify_photo(req: ModifyPhotoReq):
    phone = req.phone
    async with depends.get_tg_client(phone) as client:
        account_obj = account.Account(client)
        res = await account_obj.modify_user_photo(req.photo_url)
        if res:
            return Response()
        else:
            return Response(code=-1)


class ModifyNameReq(BaseModel):
    phone: str
    first_name: str
    last_name: str

#修改昵称
@router.post("/modify_name")
async def modify_name(req: ModifyNameReq):
    phone = req.phone
    async with depends.get_tg_client(phone) as client:
        account_obj = account.Account(client)
        res = await account_obj.modify_user_name(req.first_name, req.last_name)
        if res:
            return Response()
        else:
            return Response(code=-1)
