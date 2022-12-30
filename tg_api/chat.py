import typing
from telethon import TelegramClient, hints,types, client as tclient
from telethon.tl.functions.messages import AddChatUserRequest, CreateChatRequest,EditChatTitleRequest
from telethon.tl.functions.channels import CreateChannelRequest

class Chat:
    def __init__(self, client: TelegramClient) -> None:
        self.client = client

    async def get_chat_by_link(self, link: str) -> hints.Entity:
        entity = await self.client.get_entity(link)
        return entity

    async def get_chat_participants(self, chat_entity: hints.EntityLike) -> tclient.chats._ParticipantsIter:
        return self.client.iter_participants(chat_entity)

    async def create_chat_add_user(self, users, title="") -> typing.Any:
        res = await self.client(CreateChatRequest(users, title))
        # print("create_chat_add_user:", res)
        return res

    async def create_channel(self,title:str, about: str) -> typing.Any:
        return await self.client(CreateChannelRequest(title=title, about=about, broadcast=True, megagroup=False))

    async def add_user_to_chat(self, chat_id: int, users: typing.Union[tclient.chats._ParticipantsIter, types.TypeInputUser]):
        if isinstance(users, tclient.chats._ParticipantsIter):
            for participant in users:
                res = await self.client(AddChatUserRequest(chat_id, participant))
                # print(res)
    
    async def send_message(self, entity: hints.EntityLike, msg: hints.MessageLike) -> typing.Any:
        return self.client.send_message(entity, msg)

    async def rename_chat_name(self, chat_id: int, title: str) -> typing.Any:
        return await self.client(EditChatTitleRequest(chat_id, title))
