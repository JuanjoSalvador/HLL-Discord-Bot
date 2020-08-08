import os
import json
import random
import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')

bot = commands.Bot(command_prefix='!')

@bot.command(name='players')
async def player_count(ctx):
    r = requests.get(f'https://api.battlemetrics.com/servers/{SERVER_ID}')
    data = r.json()
    players = data['data']['attributes']['players']
    current_map = data['data']['attributes']['details']['map']
    response = f'Ahora mismo hay **{players} jugadores**, en el mapa **{current_map}**'
    await ctx.send(response)

bot.run(TOKEN)