import asyncio
from telethon import TelegramClient
import logging
import traceback

from tg_api.chat import Chat
from tg_api.account import Account


# logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    # level=logging.WARNING)


# async def main():

    # api_id=17349
    # api_hash="344583e45741c457fe1862106095a5eb"
    # session = "186"

    # client = TelegramClient(session, api_id, api_hash, proxy=("socks5", '127.0.0.1', 7890))
    # try:
    #     # await client.connect()
    #     await client.start()

    #     # todo
    #     chat = Chat(client)
        # link = "https://t.me/pionexcn"
        # link = "https://t.me/oke_test"
        # chat_entity = await chat.get_chat_by_link(link)
        # participants = await chat.get_chat_participants(chat_entity)
        # participants_list = []
        # async for participant in participants:
            # print(participant)
            # participants_list.append(participant)
        # print("len:", len(participants_list))
        # chatUpdate = await chat.create_chat_add_user(participants_list, "1230")
        # print("type:", chatUpdate.stringify())
        # chatObj = chatUpdate.chats[0]
        # input_text = "https://img.freepik.com/free-vector/cute-woman-teacher-thailand-uniform-character-education-back-school-logo-cartoon-art-illustration_56104-1541.jpg?w=1380&t=st=1672367801~exp=1672368401~hmac=d9ee36d612da83a97b3a73c6b9a5646e7567f4364183762f560cbb1bbdde80ca"
        # input_text = "'<a href=\"tg://user?id=me\">Mentions</a>'"
        # message = await client.send_message(chatObj, input_text, file="/Users/haiboz/Downloads/girl.webp")
        # await client.send_file(chatObj, input_text, caption="[links](https://example.com) and [mentions](@username) (or using IDs like in the Bot API: [mention](tg://user?id=123456789)")
        # res = await client.pin_message(chatObj, message, notify=True)
        # print(message.stringify())
        # print("res:", res)

        
        # async for dialogs in client.iter_dialogs():
        #     if dialogs.title == "test_123321":
        #         print(dialogs.entity.stringify())
            # print(dialogs.id, dialogs.title)
            # if dialogs.title.startswith("1229"):
            #     await client.delete_dialog(dialogs)


        # await chat.create_channel(title="title_fadfaduisdfjads", about="adfadf")

        # u = Account(client)
        # await u.modify_user_photo(input_text)
        # await u.modify_user_name("first_name", "last_name")

        

    # except Exception as e:
    #     # logging.error(traceback.format_exc())
    #     traceback.print_exc()
    # finally:
    #     client.disconnect()

# if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(main())
    # except Exception as e:
    #     traceback.print_exc()
    #     # logging.error(traceback.format_exc())
    # finally:
    #     pass
    #     # if not loop.is_closed():
    #     #     loop.close()
