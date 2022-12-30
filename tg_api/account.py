import typing
import requests
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

class Account:

    def __init__(self, client: TelegramClient) -> None:
        self.client = client

    async def modify_user_photo(self, photo_url: str) -> typing.Any:
        resp = requests.get(photo_url)
        if resp.status_code != 200:
            raise Exception("read photo error")
        photo_byte = resp.content
        upload_file = await self.client.upload_file(photo_byte) 
        res = await self.client(UploadProfilePhotoRequest(upload_file))
        return res

    async def modify_user_name(self, first_name: str, last_name:str) -> typing.Any:
        return await self.client(UpdateProfileRequest(first_name, last_name))