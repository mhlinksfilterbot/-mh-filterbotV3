import asyncio 

from pyrogram import Client as lucifermoringstar_robot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserIsBlocked, PeerIdInvalid

from LuciferMoringstar_Robot.admins.index_files import index_files_to_db
from LuciferMoringstar_Robot.database.autofilter_db import get_file_details
from LuciferMoringstar_Robot.database._utils import get_size, is_subscribed
from LuciferMoringstar_Robot.database._utils import lucifer_temp

from translation import LuciferMoringstar
from config import BUTTONS, FORCES_SUB, CUSTOM_FILE_CAPTION, START_MSG, DEV_NAME, bot_info, ADMINS, team_name, team_link

from LuciferMoringstar_Robot.modules._text_ import module

lock = asyncio.Lock()

@lucifermoringstar_robot.on_callback_query()
async def cb_handler(client: lucifermoringstar_robot, query):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id

    if (clicked == typed):

# # ---------- ð [ | ðð¥ð¢ð¨ð£ ðððð§ðð¥ð¦ | ] ð ---------- # #

        if query.data.startswith("nextgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again ð",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("ð Êá´á´á´ á´á´É¢á´", callback_data=f"backgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"ð á´á´É¢á´s {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("á´Êá´sá´ ðï¸", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="ð¤ á´Êá´á´á´ á´Ê á´á´ ð¤", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("ð Êá´á´á´ á´á´É¢á´", callback_data=f"backgroup_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page â¡", callback_data=f"nextgroup_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"ð á´á´É¢á´s {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("á´Êá´sá´ ðï¸", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="ð¤ á´Êá´á´á´ á´Ê á´á´ ð¤", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backgroup"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again ð",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("É´á´xá´ á´á´É¢á´ â¡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"ð á´á´É¢á´s {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("á´Êá´sá´ ðï¸", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="ð¤ á´Êá´á´á´ á´Ê á´á´ ð¤", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )
                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("ð Êá´á´á´ á´á´É¢á´", callback_data=f"backgroup_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page â¡", callback_data=f"nextgroup_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"ð á´á´É¢á´s {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("á´Êá´sá´ ðï¸", callback_data="close")]
                )
                buttons.append(
                    [InlineKeyboardButton(text="ð¤ á´Êá´á´á´ á´Ê á´á´ ð¤", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# # ---------- ð [ | ðð¢ð§ ð£ð  ðððð§ðð¥ð¦ | ] ð ---------- # #


        elif query.data.startswith("nextbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again ð",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("ð Êá´á´á´ á´á´É¢á´", callback_data=f"backbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"ð á´á´É¢á´s {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("á´Êá´sá´ ðï¸", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("ð Êá´á´á´ á´á´É¢á´", callback_data=f"backbot_{int(index)+1}_{keyword}"),InlineKeyboardButton("Next Page â¡", callback_data=f"nextbot_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"ð á´á´É¢á´s {int(index)+2}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("á´Êá´sá´ ðï¸", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

        elif query.data.startswith("backbot"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("This Is My Old Message So Please Request Again ð",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("É´á´xá´ á´á´É¢á´ â¡", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"ð á´á´É¢á´á´ {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("á´Êá´sá´ ðï¸", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("ð Êá´á´á´ á´á´É¢á´s", callback_data=f"backbot_{int(index)-1}_{keyword}"),InlineKeyboardButton("Next Page â¡", callback_data=f"nextbot_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"ð á´á´É¢á´s {int(index)}/{data['total']}", callback_data="pages"),
                     InlineKeyboardButton("á´Êá´sá´ ðï¸", callback_data="close")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return

# ---------- ð [ | ððð§ ððððð¦ | ] ð ---------- #


        elif query.data.startswith("lucifermoringstar_robot"):
            ident, file_id = query.data.split("#")
            files_ = await get_file_details(file_id)
            if not files_:
                return await query.answer('No such file exist.')
            files = files_[0]
            title = files.file_name
            size=get_size(files.file_size)
            caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, title=title, size=size, caption=files.caption)

            try:
                if FORCES_SUB and not await is_subscribed(client, query):
                    await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
                    return
                else:
                    await client.send_cached_media(
                        chat_id=query.from_user.id,
                        file_id=file_id,
                        caption=caption
                        )
                    await query.answer('ð¤ á´Êá´á´á´ á´á´, Éª Êá´á´ á´ sá´É´á´ ÒÉªÊá´s ÉªÉ´ á´á´ ð¤',show_alert = True)
            except UserIsBlocked:
                await query.answer('Unblock the bot mahn !',show_alert = True)
            except PeerIdInvalid:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")
            except Exception as e:
                await query.answer(url=f"https://t.me/{bot_info.BOT_USERNAME}?start=subscribe")

# ---------- ð [ | ð£ð  ððððð¦ | ] ð ---------- #

        elif query.data.startswith("pmfile"):
            if FORCES_SUB and not await is_subscribed(client, query):
                await query.answer("I Like Your Smartness, But Don't Be Oversmart ð",show_alert=True)
                return
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=get_size(files.file_size)
                
                caption=CUSTOM_FILE_CAPTION.format(mention=query.from_user.mention, title=title, size=size, caption=files.caption)

                buttons = [[
                  InlineKeyboardButton('ð á´Ê ÊÉªÉ´á´s ð', url='https://t.me/+gyZFP-mFh7YyN2Q1')
                  ]]                 
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )


# ---------- ð [ | ð ð¢ðð¨ððð¦ | ] ð ---------- #


        elif query.data == "start":
            if query.from_user.id not in ADMINS: 
                buttons = [[
                 InlineKeyboardButton("âï¸ á´á´á´ á´á´ á´á´ Êá´á´Ê á´Êá´á´ âï¸", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
                 ],[
                 InlineKeyboardButton("Êá´Êá´", callback_data="help"),
                 InlineKeyboardButton("á´Êá´á´á´", callback_data="about") 
                 ],[
                 InlineKeyboardButton("á´á´Êá´ á´á´á´ Éªá´s", url="https://t.me/+gyZFP-mFh7YyN2Q1"),
                 InlineKeyboardButton("Êá´Ç« á´á´á´ Éªá´s", url="https://t.me/moviereqgroup_movieshub")
                 ]]
            else:
                buttons = [[
                 InlineKeyboardButton("âï¸ á´á´á´ á´á´ á´á´ Êá´á´Ê á´Êá´á´ âï¸", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
                 ],[
                 InlineKeyboardButton("Êá´Êá´", callback_data="bot_owner"),
                 InlineKeyboardButton(" á´Êá´á´á´", callback_data="about") 
                 ],[
                 InlineKeyboardButton("á´á´Êá´ á´á´á´ Éªá´s", url="https://t.me/+gyZFP-mFh7YyN2Q1"),
                 InlineKeyboardButton("á´á´á´ Éªá´ Êá´Ç«", url="https://t.me/moviereqgroup_movieshub")
                 ]]               
            await query.message.edit(text=START_MSG.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "help":
            buttons = [[
              InlineKeyboardButton("Êá´á´á´", callback_data="start"),
              InlineKeyboardButton("á´Êá´á´á´", callback_data="about")
              ]]               
            await query.message.edit(text=LuciferMoringstar.HELP_MSG.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "about":
            buttons = [[
             InlineKeyboardButton("Êá´á´á´", callback_data="start"),
             InlineKeyboardButton("á´Êá´sá´ ðï¸", callback_data="close")
             ]]               
            await query.message.edit(text=LuciferMoringstar.ABOUT_MSG.format(mention=query.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "close":
            await query.message.delete()

        elif query.data == "bot_owner":
            buttons = [[
             InlineKeyboardButton('Êá´á´á´', callback_data="start"),
             InlineKeyboardButton('á´Êá´á´á´', callback_data="about")
             ]]               
            await query.message.edit(text=LuciferMoringstar.PR0FESS0R_99.format(mention=query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)


        elif query.data == "autofilter":
            buttons = [[ InlineKeyboardButton('ð Êá´á´á´', callback_data="help") ]]          
            await query.message.edit(module.autofilter_text.format(team=team_name, team_link=team_link), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "ban":
            buttons = [[ InlineKeyboardButton('ð Êá´á´á´', callback_data="help") ]]          
            await query.message.edit(module.ban_text.format(team=team_name, team_link=team_link), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "mute":
            buttons = [[ InlineKeyboardButton('ð Êá´á´á´', callback_data="help") ]]          
            await query.message.edit(module.mute_text.format(team=team_name, team_link=team_link), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "pin":
            buttons = [[ InlineKeyboardButton('ð Êá´á´á´', callback_data="help") ]]          
            await query.message.edit(module.pin_message.format(team=team_name, team_link=team_link), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

        elif query.data == "close":
            await query.message.delete()

# ---------- â ï¸ [ | Other | ] â ï¸ ---------- #

        elif query.data.startswith("index"):
            bot = client 
            if query.data.startswith('index_cancel'):
                lucifer_temp.CANCEL = True
                return await query.answer("Cancelling Indexing")
            _, raju, chat, lst_msg_id, from_user = query.data.split("#")
            if raju == 'reject':
                await query.message.delete()
                await client.send_message(int(from_user),
                                       f'Your Submission for indexing {chat} has been decliened by our moderators.',
                                       reply_to_message_id=int(lst_msg_id))
                return

  
            if lock.locked():
                return await query.answer('Wait until previous process complete.', show_alert=True)
            msg = query.message
            await query.answer('Processing...â³', show_alert=True)
            if int(from_user) not in ADMINS:
                await bot.send_message(int(from_user),
                                       f'Your Submission for indexing {chat} has been accepted by our moderators and will be added soon.',
                                       reply_to_message_id=int(lst_msg_id))
            await msg.edit(
                "Starting Indexing",
                reply_markup=InlineKeyboardMarkup(
                  [[InlineKeyboardButton('Cancel', callback_data='index_cancel')]]
                  )
            )
            try:
                chat = int(chat)
            except:
                chat = chat
            await index_files_to_db(int(lst_msg_id), chat, msg, bot)




        elif query.data == "pages":
            await query.answer("@LuciferMoringstar_Robot")


    else:
        await query.answer("Please Request",show_alert=True)




