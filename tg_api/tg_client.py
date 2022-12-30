
from telethon import TelegramClient


class TgClient:
    
    async def init_client(self, phone: str) -> TelegramClient:
        api_id=17349
        api_hash="344583e45741c457fe1862106095a5eb"
        session = phone
        client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 7890))
        await client.start()
        return client
        