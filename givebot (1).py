#created by @Rexurection #Anti-Skid

from pyrogram import *
from pyrogram.types import *
import time

api_id = 7058291
api_hash = "5b9ea5b6baa2905c7ae2822a04b8e835"
bot_token = "2102291533:AAGZ8hmUfqPAF1TzZuiGQwzpEY3o1iN3y5w"
ADMINS = [2098361897,910209349] #metti id degli admin
CHAT_ID = -1001799909671 #chat id del canale

bot = Client('bot', api_id, api_hash, bot_token)

@bot.on_message(filters.private & filters.command('start'))
async def start(Client, msg):
    await msg.reply_text(f"Ciao, {msg.from_user.mention}!")

@bot.on_message(filters.command('give'))
async def give_cmd(Client, msg):
    if msg.from_user.id in ADMINS:
        try:
            give_cmd.preso = False
            ss = msg.text
            sss = ss.split()
            give_cmd.typeegive = sss[1]
            give_cmd.varr = sss[2]
            await bot.send_message(CHAT_ID, f"""**Give**
            Tipo account: {give_cmd.typeegive}
            Clicca il bottone Ottieni per vincere!""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🔐 Ottieni', 'get')]]))
        except Exception as e:
            await msg.reply_text(e)
            await msg.reply_text('Errore! ^')
    else:
        pass

@bot.on_callback_query()
async def callback_manager(Client, query):
    if query.data == "get":
        global preso
        is_preso = give_cmd.preso
        time.sleep(2)
        if is_preso == True:
                pass
        else:
                var = query.from_user.id
                varr = query.from_user.mention
                callback_manager.vincitore = query.from_user.mention
                await bot.send_message(var, f"Hai vinto! Ecco le credenziali: `{give_cmd.varr}`")
                preso = True
                time.sleep(2)
        try:
            
            await query.message.edit_text(f"""**Give**
            Tipo account: {give_cmd.typeegive}
            Vincitore: {callback_manager.vincitore}
            GG!""")           
            await query.answer('Hai vinto! Controlla il bot per le credenziali!', show_alert=True)
            
        except Exception as e:
            print(e)


bot.run()