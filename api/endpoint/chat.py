import logging
import traceback
from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
from api.depends import get_tg_client
from schemas.response import Response
from tg_api.chat import Chat
from telethon.errors.rpcerrorlist import UserDeactivatedBanError, FloodError

router = APIRouter()


class CreateChatReq(BaseModel):
    phone: str
    chat_link: str
    chat_name: str
    chat_type: int = 1#1:群 2:频道

#根据群链接创建群
@router.post("/create_chat")
async def create_chat(req: CreateChatReq):
    try:
        async with get_tg_client(req.phone) as client:
            chat = Chat(client)
            chat_entity = await chat.get_chat_by_link(req.chat_link)
            participants_iter = await chat.get_chat_participants(chat_entity)
            users = []
            async for participants in participants_iter:
                # logging.info(participants.stringify())
                users.append(participants)
            result = None
            if req.chat_type == 1:
                result = await chat.create_chat_add_user(users, title=req.chat_name)
            else:
                channel_updates = await chat.create_channel(req.chat_name)
                result = await chat.join_channel(channel_updates, users)
            if not result:
                return Response(code=-1)
            return Response()
    except UserDeactivatedBanError as e:
        logging.error(traceback.format_exc())
        return Response(code=-1, msg="User deactivated ban error")
    except FloodError as e:
        logging.error(traceback.format_exc())
        return Response(code=-1, msg="flood error")
    except Exception as e:
        logging.error(traceback.format_exc())
        return Response(code=-1, msg="server error")

class GetChatInfoReq(BaseModel):
    link: str
    phone: str

# 获取群成员数量和名称
@router.post("/get_chat_info")
async def get_chat_info(req: GetChatInfoReq):
    client = get_tg_client(req.phone)
    if not client.is_connected():
        await client.connect()
    chat = Chat(client)
    response = chat.get_chat_detail_by_link(req.link)
    participants_count = response.full_chat.participants_count
    title = response.chats[0].title
    data = {"participants_count": participants_count, "title": title}
    return Response(data=data)

class SendMessageReq(BaseModel):
    phone: str
    chat_id: str # or chat link, 群的唯一标识
    texts: List[str]
    
#发送群消息
@router.post("/send_message_to_chat")
async def send_message_to_chat(req: List[SendMessageReq]):
    client = get_tg_client(req.phone)
    if not client.is_connected():
        await client.connect()
    chat = Chat(client)
    try:
        chat_entity = await client.get_entity(req.chat_id)
        for text in req.texts:
            await chat.send_message(chat_entity, text)
    except Exception as e:
        logging.error(traceback.format_exc())
    return Response()

class AddAdminUserReq(BaseModel):
    phone: str
    chat_id: str
    user_ids: List[str]

#添加管理员
@router.post("/add_admin_user")
async def add_admin_user(req: AddAdminUserReq):
    client = get_tg_client(req.phone)
    if not client.is_connected():
        await client.connect()
    chat = Chat(client)
    chat_entity = await client.get_entity(req.chat_id)
    for user_id in req.user_ids:
        user_entity = await client.get_entity(user_id)
        chat.add_admin_user(chat_entity, user_entity)
    return Response()

class DeleteAdminUserReq(BaseModel):
    phone: str
    chat_id: str
    user_ids: List[str]

#删除管理员
@router.post("/delete_admin_user")
async def delete_admin_user(req: DeleteAdminUserReq):
    client = get_tg_client(req.phone)
    if not client.is_connected():
        await client.connect()
    chat = Chat(client)
    chat_entity = await client.get_entity(req.chat_id)
    for user_id in req.user_ids:
        user_entity = await client.get_entity(user_id)
        chat.delete_admin_user(chat_entity, user_entity)
    return Response()


class DeleteChatReq(BaseModel):
    phone: str
    chat_id: int

#删除群/解散群
@router.post("/delete_chat") 
async def delete_chat(req: DeleteChatReq):
    client = get_tg_client(req.phone)
    if not client.is_connected():
        await client.connect()
    chat = Chat(client)
    result = chat.delete_chat(req.chat_id)
    if result:
        return Response()
    else:
        return Response(code=-1, msg="Couldn't delete chat")
