from discord.ext import commands
import discord
import C_F
import json
import IFN
from datetime import datetime
import getpass
import hashlib
import mysql.connector

C_F.log()
C_F.on_start()
IFN.on_start_IFN()

with open ("status/config.json" , 'r') as json_file_token :
    data = json.load(json_file_token)

bot = commands.Bot(command_prefix="!" , intents=discord.Intents.all())

if data['Public_key'] == 'NOTSET' :
    TAB = getpass.getpass(prompt="Active token bot > ")
    SETDEF = str(input("set this token as default (n,y) > "))

    if SETDEF == "Y" or SETDEF == "y" :
        data['Public_key'] = TAB
        C_F.log_logger('debug' , f"set {TAB} as default token key")
        print(f"set {TAB} as default token key")
        with open ("status/config.json" , 'w') as json_token_set_default :
            json.dump(data, json_token_set_default)

if data['Public_key'] != "NOTSET" :
    with open ("status/config.json" , 'r') as json_file :
        data = json.load(json_file)
    TAB = data['Public_key']

with open ("status/config.json" , 'r' ) as json_data :
    json_data1 = json.load(json_data)

GUIV = None

@bot.event
async def on_ready():
    print("hello, world")

    CHANNEL_KEY = int(data["room_key"])
    channel = bot.get_channel(CHANNEL_KEY)
    await channel.send("@everyone >>>> discord bot is ON <<<<")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    global GUIV
    GUIV = str(message.author.id)

    await bot.process_commands(message)

@commands.command()
async def event(ctx, arg='null',arg1='null',arg2='null',arg3='null',arg4="null",arg5="null",arg6="null") :
    if arg == 'add' :
        if GUIV == "870114551595683871":
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y %H:%M:%S") 

            event_name = str(arg1)
            event_description = str(arg2)
            event_date = str(arg3)
            event_image = str(arg4)
            event_game_type = str(arg5)

            m = hashlib.md5(event_game_type.encode('UTF-8'))
            r = hashlib.md5(event_date.encode('UTF-8'))
            print(m.hexdigest()+r.hexdigest())
            t = m.hexdigest()+r.hexdigest()

            event_room = str(arg6)

            if event_name == 'null' and event_date == 'null' :
                await ctx.send("""event name or event date is empty
    !add event [event name] [event description] [event date]
                            """)
            
            with open('status/event.json', 'r') as file:
                data = json.load(file)

            new_data = {
                "event_name":event_name,
                "event_discription":event_description,
                "event_date":event_date,
                "event_image":event_image,
                "event_game_type":event_game_type,
                "event_room":event_room,
                "event_code":t
            }
            data['event'].append(new_data)
            updated_json_data = json.dumps(data, indent=2)

            print(f'{dt_string} [discord session] calling command {arg} success')
            C_F.log_logger('debug' , f'{dt_string} [discord session] calling command {arg} success')

            with open('status/event.json', 'w') as file:
                file.write(updated_json_data)

    if arg == '-all-event' :
        if GUIV == "870114551595683871":
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y %H:%M:%S")

            file = open('status/event.json')
            data = json.load(file)

            channel = bot.get_channel(1192359523864805456)

            for i in data['event']:
                await channel.send(f"""
-----------------------[event detail]-----------------------

event name            >  {i['event_name']}
event description     >  {i['event_discription']}
event date            >  {i['event_date']}
event image           >  {i['event_image']}
event game type       >  {i['event_game_type']}
event code            >  {i['event_code']}
event room            >  {i['event_room']}

------------------------------------------------------------
            """)
            print(f'{dt_string} [discord session] calling command {arg} success')
            C_F.log_logger('debug' , f'{dt_string} [discord session] calling command {arg} success')
            file.close()

    if arg == 'announce' :
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S") 

        file = open('status/event.json')
        data = json.load(file)
            
        if arg1 == "honkai-starrail" :
            channel = bot.get_channel(1191273134792384593)
        if arg1 == "genshin-impact" :
            channel = bot.get_channel(1191273052038762576)
        if arg1 == "minecraft" :
            channel = bot.get_channel(1191272953350995998)
        if arg1 == "honkai-impact" :
            channel = bot.get_channel(1193117202463862866)

        for i in data['event']:
            if i['event_code'] == arg2 :
                await channel.send(f"""
@everyone
the content {i['event_name']} will be start soon({i['event_date']})
event description :
{i['event_discription']}

game/class - {i['event_game_type']}
meet at - {i["event_room"]}
    """)
                print(f'{dt_string} [discord session] calling command {arg} success')
                C_F.log_logger('debug' , f'{dt_string} [discord session] calling command {arg} success')

        
@commands.command()
async def server(ctx,arg='null',arg1='null',arg2='null'):

    C_F.log_logger('debug', f'[discord_session] call commamd {arg} ')
    if arg == "-tester-id-admin" and arg1 == 'null' and arg2 == 'null':
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")    
        if GUIV == "870114551595683871" :
            C_F.log_logger('debug', f'[discord_session] call commamd {arg} Success send answer to {GUIV}')
            await ctx.send("True")
            print(f'{dt_string}[discord_session] call commamd {arg} Success send answer to {GUIV}')     
        else :
            C_F.log_logger('debug', f'[discord_session] call commamd {arg} Success send answer to {GUIV}')
            await ctx.send("error")
            print(f'{dt_string}[discord_session] call commamd {arg} Success send answer to {GUIV}')     
        
    if arg == "-managment" and arg1 == "-get-software-info" and arg2 == "-get-version-info" :
        if GUIV == "870114551595683871" :
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
            with open ("status/software_info.json" , 'r') as soft_info :
                data = json.load(soft_info)

            await ctx.send(f"current discord bot version is {data['bot_version']} code name is {data['code_name']}")
            C_F.log_logger('debug', f'[discord_session] call commamd {arg} Success send answer to {GUIV}')     
            print(f'{dt_string}[discord_session] call commamd {arg} Success send answer to {GUIV}')  
        else :
            await ctx.send(f"Cannot bring data(you are not admin) [error][NA9930]")
            C_F.log_logger('debug', f'[discord_session][error][NA9930] call commamd {arg} Success send answer to {GUIV}')
            print(f'[discord_session][error][NA9930] call commamd {arg} Success send answer to {GUIV}')     

        
            
bot.add_command(server)
bot.add_command(event)

bot.run(TAB)
