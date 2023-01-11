from telethon import TelegramClient
from teleredis import RedisSession
import redis

redis_connector = redis.Redis(host='192.168.5.17', port=10002, db=0, decode_responses=False)