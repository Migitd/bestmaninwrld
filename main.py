# import all objectives
import discord
from discord.ext import commands, tasks
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('TOKEN')

# discord handling
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
activity = discord.Activity(type=discord.ActivityType.playing, name="Lunar Devs")
bot = commands.Bot(command_prefix=".", intents=intents, activity=activity, status=discord.Status.online)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print(bot.guilds)

bot.run(DISCORD_TOKEN)
