import asyncio
from teleredis import RedisSession
from telethon import TelegramClient
import logging
import traceback

from tg_api.chat import Chat
from tg_api.account import Account
from db import session
from db.cache import redis_connector


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARN)



async def main():

    api_id=17349
    api_hash="344583e45741c457fe1862106095a5eb"
    # phone = "12269408818" # session = db.container.new_session("+15489656225")
    phone = "14387710232"
    sess = session.container.new_session(phone)
    logger = logging.getLogger()
    # sess = RedisSession(phone, redis_connector)
    client = TelegramClient(sess, api_id, api_hash, proxy=("socks5", '127.0.0.1', 7890), base_logger=logger)
    await client.start("+"+phone)

    # if not client.is_connected():
    # await client.connect()

    # user = await client.get_me()
    # print(user.stringify())

    # if not await client.is_user_authorized():
    #     phone = '+16136550780' 
    #     await client.send_code_request(phone) 
    #     code = input('enter code: ') 
    #     await client.sign_up(code, first_name='Anna', last_name='Banana') 
    try:
        # await client.connect()
        # await client.start()

        # Allowing `user` to pin messages in `chat`
        # await client.edit_admin(chat, user, pin_messages=True)

#             # # todo
        chat = Chat(client)
#             # # link = "https://t.me/pionexcn"
        # link = "https://t.me/oke_test"
        # link = "https://t.me/Javaer"
        # link = "https://t.me/ctest1234"
        # chat_entity = await chat.get_chat_by_link(link)
        # chat_entity = await client.get_entity(link)
        # print(chat_entity.stringify())
        # print(chat_entity.title)
        # chat_id = chat_entity.id
        # print("Chat id:", chat_id)
        # from telethon.tl.functions.messages import GetFullChatRequest, GetChatsRequest
        # from telethon.tl.functions.channels import GetChannelsRequest
        # from telethon.tl.functions.channels import GetFullChannelRequest
        # resp = await client(GetFullChannelRequest(chat_entity))
        # print(resp.stringify())
        # count = resp.full_chat.participants_count
        # print("count:", count)
        # participants = await chat.get_chat_participants(chat_entity)
        # participants_list = []
        # async for participant in participants:
        #     print(participant)
        #     participants_list.append(participant)
        # print("len:", len(participants_list))
        # chatUpdate = await chat.create_chat_add_user(participants_list, "1230")
        # print("type:", chatUpdate.stringify())
#             # chatObj = chatUpdate.chats[0]
#             # input_text = "https://img.freepik.com/free-vector/cute-woman-teacher-thailand-uniform-character-education-back-school-logo-cartoon-art-illustration_56104-1541.jpg?w=1380&t=st=1672367801~exp=1672368401~hmac=d9ee36d612da83a97b3a73c6b9a5646e7567f4364183762f560cbb1bbdde80ca"
#             # input_text = "'<a href=\"tg://user?id=me\">Mentions</a>'"
#             # message = await client.send_message(chatObj, input_text, file="/Users/haiboz/Downloads/girl.webp")
#             # await client.send_file(chatObj, input_text, caption="[links](https://example.com) and [mentions](@username) (or using IDs like in the Bot API: [mention](tg://user?id=123456789)")
#             # res = await client.pin_message(chatObj, message, notify=True)
#             # print(message.stringify())
#             # print("res:", res)

        
        async for dialogs in client.iter_dialogs():
            # print(dialogs.id, dialogs.title)
            # print(dialogs.stringify())
            async for message in client.iter_messages(dialogs):
                print(message.id, message.text)
                print("============")
                
        # await chat.create_channel(title="title_fadfaduisdfjads", about="adfadf")

#             # u = Account(client)
#             # await u.modify_user_photo(input_text)
#             # await u.modify_user_name("first_name", "last_name")

        

    except Exception as e:
        # logging.error(traceback.format_exc())
        traceback.print_exc()
    finally:
        client.disconnect()

if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    try:
        # loop.run_until_complete(main())
        asyncio.run(main())
    except Exception as e:
        traceback.print_exc()
        # logging.error(traceback.format_exc())
    finally:
        pass
        # if not loop.is_closed():
        #     loop.close()
