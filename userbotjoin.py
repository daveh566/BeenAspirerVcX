from pyrogram import Client
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from decorators import authorized_users_only
from decorators import errors
from callsmusic import client as USER
from config import SUDO_USERS

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>ADD ME AS 🔥 ADMIN TO YOUR GROUP FIRST</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "IntimacyVcHelper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I JOINED HERE AS YOU REQUESTED")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>HELPER ALREADY IN YOUR CHAT</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 WAITING ERROR 🛑 \n User {user.first_name} COULDN'T JOIN YOUR GROUP! MAKE SURE USER IS NOT BANNED 😉 IN YOUR GROUP."
            "\n\nOr manually add @DaisyXhelper to your Group and try again</b>",
        )
        return
    await message.reply_text(
        "<b>HELPER USERBOT JOINED YOUR CHAT</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>User couldn't leave your group! May be floodwaits."
            "\n\nOr manually kick me from to your Group</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is chat even linked")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>ADD ME AS ADMIN OF TO YOUR CHANNELFIRST</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "IntimacyVcHelper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>HELPER ALREADY IN YOUR CHANNEL</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 WAITING ERROR 🛑 \n User {user.first_name} COULDN'T JOIN YOUR CHANNEL DUE TO HEAVY JOIN REQUESTS! MAKE SURE USER IS NOT BANNED IN CHANNEL 😉."
            "\n\nOr MANUALLY ADD @IntimacyVcHelper TO YOUR GROUP AND TRY AGAIN</b>",
        )
        return
    await message.reply_text(
        "<b>HELPER USERBOT JOINED YOUR CHANNEL</b>",
    )
    
