import typing

from telethon import TelegramClient
from db.session import SessionLocal, container
from core.config import settings

def get_db() -> typing.Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

        
async def get_tg_client(phone: str) -> TelegramClient:
    api_id=settings.API_ID
    api_hash=settings.API_HASH
    # phone = "+12269408818" # new account
    # phone = "+17165463277"
    # phone = "+15489656225"
    sess = container.new_session(phone)
    client = TelegramClient(sess, api_id, api_hash, proxy=("socks5", '127.0.0.1', 7890))
    await client.connect()
    return client
