# Telegram Link : https://telegram.dog/CyberWallNetwork
# Repo Link : https://github.com/PR0FESS0R-99/Auto-Approved-Bot
# License Link : https://github.com/PR0FESS0R-99/Auto-Approved-Bot/blob/Auto-Approved-Bot/LICENSE

from os import environ
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    User,
    ChatJoinRequest,
)

cyberwallnetwork = Client(
    "Auto Approval Bot",
    bot_token=environ["5678143706:AAH48xfDfWs8xHrym9yRMJ95QuXQK4BU56A"],
    api_id=int(environ["2308238"]),
    api_hash=environ["5439c9950ef07b4f7b433f5a37de5abd"],
)

CHAT_ID = [int(cyberwallnetwork) for cyberwallnetwork in environ.get("CHAT_ID", None).split()]
TEXT = environ.get(
    "APPROVED_WELCOME_TEXT", "🙋‍♀️ Hey!! __{mention}__\n🙌 Welcome To __{title}__\n\n**✅ Your Auto Approved**"
)
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()


@cyberwallnetwork.on_message(filters.private & filters.command(["start"]))
async def start(client: cyberwallnetwork, message: Message):
    approvedbot = await client.get_me()
    start_button = [
        [
            InlineKeyboardButton(
                "😸 Github",
                url=f"https://www.viz.com/home.html",
            ),
            InlineKeyboardButton(
                "🔊 Channel", 
                url="t.me/cyberwallnetwork"
            ),
        ],
        [
            InlineKeyboardButton(
                "➕️ Add me in your Chat/Group", 
                url="http://t.me/{approvedbot.username}?startgroup=botstart"
            )
        ],
    ]
    await client.send_message(
        chat_id=message.chat.id,
        text=f"🙋‍♀️ Hey __{message.from_user.mention}__,\nℹ I am Auto Approval Bot!! Just [➕ Add me in your Group/Channel](http://t.me/{approvedbot.username}?startgroup=botstart) As a Admin and click /help to check required Permission me as a Admin",
        reply_markup=InlineKeyboardMarkup(start_button),
        disable_web_page_preview=True,
    )

@cyberwallnetwork.on_message(filters.private & filters.command(["help"]))
async def start(client: cyberwallnetwork, message: Message):
    approvedbot = await client.get_me()
    help_button = [
        [
            InlineKeyboardButton(
                "➕️ Add me in your Chat/Group", 
                url="http://t.me/{approvedbot.username}?startgroup=botstart"
            )
        ],
    ]
    await client.send_message(
        chat_id=message.chat.id,
        text=f"**Make sure you give me That following Permission As a Admin**",
        reply_markup=InlineKeyboardMarkup(help_button),
        disable_web_page_preview=True,
    )

@cyberwallnetwork.on_chat_join_request(
    (filters.group | filters.channel) & filters.chat(CHAT_ID)
    if CHAT_ID
    else (filters.group | filters.channel)
)
async def autoapprove(client: cyberwallnetwork, message: ChatJoinRequest):
    chat = message.chat
    user = message.from_user
    print(f"{user.first_name} New Member here...!!")
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(
            chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title)
        )

print("Auto Approved Bot")
cyberwallnetwork.run()
