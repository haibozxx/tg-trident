import typing
from telethon import TelegramClient, hints,types, client as tclient
from telethon.tl.functions.messages import AddChatUserRequest, CreateChatRequest,EditChatTitleRequest,DeleteChatRequest
from telethon.tl.functions.channels import CreateChannelRequest,InviteToChannelRequest,GetFullChannelRequest

class Chat:
    def __init__(self, client: TelegramClient) -> None:
        self.client = client

    async def get_chat_by_link(self, link: str) -> hints.Entity:
        entity = await self.client.get_entity(link)
        return entity

    async def get_chat_detail_by_link(self, link: str) -> types.messages.ChatFull:
        entity = await self.client.get_entity(link)
        result = await self.client(GetFullChannelRequest(entity))
        return result

    async def get_chat_participants(self, chat_entity: hints.EntityLike) -> tclient.chats._ParticipantsIter:
        return self.client.iter_participants(chat_entity)

    async def create_chat_add_user(self, users, title) -> typing.Any:
        res = await self.client(CreateChatRequest(users, title))
        return res

    async def create_channel(self,title:str, about: str = "") -> typing.Any:
        return await self.client(CreateChannelRequest(title=title, about=about, broadcast=True, megagroup=False))

    async def join_channel(self, channel, users) -> typing.Any:
        result = await self.client(InviteToChannelRequest(channel=channel,users=users))
        return result

    async def add_user_to_chat(self, chat_id: int, users: typing.Union[tclient.chats._ParticipantsIter, types.TypeInputUser]):
        if isinstance(users, tclient.chats._ParticipantsIter):
            for participant in users:
                res = await self.client(AddChatUserRequest(chat_id, participant))
                # print(res)
    
    async def send_message(self, entity: hints.EntityLike, msg: hints.MessageLike) -> typing.Any:
        return self.client.send_message(entity, msg)

    async def rename_chat_name(self, chat_id: int, title: str) -> typing.Any:
        return await self.client(EditChatTitleRequest(chat_id, title))

    async def add_admin_user(self, chat: hints.EntityLike, user: hints.EntityLike) -> types.Updates:
        return await self.client.edit_admin(chat, user, is_admin=True, add_admins=True, pin_messages=True, invite_users=True, add_admins=True)

    async def delete_admin_user(self, chat: hints.EntityLike, user: hints.EntityLike) -> types.Updates:
        return await self.client.edit_admin(chat, user, is_admin=False)

    async def delete_chat(self, chat_id: int):
        return await self.client(DeleteChatRequest(chat_id=chat_id))
