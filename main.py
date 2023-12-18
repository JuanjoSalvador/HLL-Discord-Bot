import os
import discord
import datetime
import requests
import logging

from random import randrange

from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure

from dotenv import load_dotenv

''' 
TO-DO

* Añadir soporte para Redis
* Configurar un segundo worker que se ejecute cada minuto y guarde métricas en Redis si se cumplen las condiciones (al menos 1 player)
* Todas las peticiones que se ejecutan aquí, deben ser consultas a los registros de Redis, 
'''

logging.basicConfig(level=logging.INFO)

load_dotenv()
# Esta información tiene que escribirse en el .env una vez se escriba
config = {
    'token': os.environ['DISCORD_TOKEN'],
    'server_id': os.environ['SERVER_ID'],
    'channel_id': os.environ['CHANNEL_ID']
}

#GUILD_ID = ''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    #data = requests.get(SERVER_METRICS).json()
    date = datetime.datetime.now()
    if config['channel_id']:
        get_data.start()
    print(f'[{date}] Bot activado correctamente.')
    # Guarda los datos en REDIS

@bot.event
async def on_disconnect():
    date = datetime.datetime.now()
    print(f'[{date}] Señal de desconexión recibida. Desconectando...')

@bot.event
async def on_resumed():
    date = datetime.datetime.now()
    print(f'[{date}] Reconectado.')

@bot.event
async def on_command_error(ctx, error):
    pass

# CONFIG COMMANDS
@bot.command(name='start', pass_context=True)
@has_permissions(administrator=True)
async def start_bot(ctx):
    guild_id = ctx.message.guild.id
    # Aquí lo ideal sería guardar esto en una base de datos persistente o escribirla en el .env del bot
    try:
        get_data.start()
        await ctx.send('Inicializado correctamente. Utiliza el comando !setchannel \
<channel_id> para cambiar el canal de voz donde se mostrarán los datos del servidor.')
    except Exception as ex:
        print(f'¡Ocurrió un error durante el arranque del bot! {ex}')
        await ctx.send('Ocurrió un error. Revisa los logs del servidor para \
más información.')

@tasks.loop(minutes=5.0)
async def get_data():
    try:
        channel_players = bot.get_channel(int(config['channel_id']))
        server_id = config['server_id']

        data = requests.get(f'https://api.battlemetrics.com/servers/{server_id}').json()
        current_map = data['data']['attributes']['details']['map']
        players = data['data']['attributes']['players']
        await channel_players.edit(name=f'📱 {players}/100 - {current_map}')
        date = datetime.datetime.now()
        bm_data = data['data']['attributes']['updatedAt']
        print(f'Actualizado: [{date}] {current_map} {players}/100')
        print(f'BattleMetrics: {bm_data}')
    except Exception as ex:
        print(f'¡Error! {ex}')

try:
    bot.run(config['token'], reconnect=True)

except Exception as ex:
    print(f'Ocurrió un error! {ex}')
