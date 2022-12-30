import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

STRING = os.environ.get("STRING", "1BVtsOKkBuyu3NlXKI8vQUpHBZpepFMyjvQsHxpetHKvCfxDXn5ntUhXH8GL-sv5-scpu6rYk4dCG8rbyZ5U3CGD_7akNEjFUX6f4KTt9gndjSP6pQIMqc4pAQO_OtaXyR7bsp0DLSKdHVlNWeGgL57QvhZPPDOXpiScXNSHT0fNdAhz5V7dZzsULYkiyjGE2EHgees4DJHnRl7WmOSjgOf-D9FMVjXT4nHzjyEWimDbTlsT1O37mihovo3YnqoL9BRsvP_lE5vY-JvCZ5f6S9dAh_gqwfx7v5rrV8bc-u4sb_AuD__nZoYx-Oh8rOuoUzjV-o15JwPchZ1yHIH961KS2nNah7us=")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
