#Lenny Bot Images

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import json
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
    print("Lenny Bot (Images) is online")

@client.command
async def num2(ctx):
    with open('C:/Users/Administrator/Pictures/72BRi7c1.png', 'r') as robbie:
        await client.send_file(channel, robbie)



client.run("Mzk4NTUxOTUzNTEwMTA1MDg5.DTAOHA.c8W8ey-t8fZYlc7_AzgpGXl5uWM")
