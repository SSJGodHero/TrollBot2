#Lenny Bot Alpha

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
    print("Lenny Bot is online")

@client.event
async def on_message(message):

#Statements

    if message.content.upper() == "SMH":
        await client.send_message(message.channel, "How about you actually shake your head instead of texting it?")

    if message.content.upper() == "IS LENNY BOT HERE?":
        await client.send_message(message.channel, "No...kappa ( ͡° ͜ʖ ͡°)")

    if message.content.upper() == "IS LENNY BOT HERE":
        await client.send_message(message.channel, "Maybe I am, maybe I'm not...you'll never know (⌐▀͡ ̯ʖ▀)")

    if message.content.upper() == "TEST":
        await client.send_message(message.channel, "Passed")

    if message.content.upper() == "GAY":
        await client.send_message(message.channel, "No, you")

    if message.content.upper() == "HOMIE":
        await client.send_message(message.channel, "That's not a word")
        
    if message.content.upper() == "I H8 U":
        await client.edit_message(message.content, "i luf u", Embed)
        await client.send_message(message.channel, "There c:")
#Commands

    if message.content.startswith('/ping'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.startswith('/tr'):
        await client.send_message(message.channel, "https://youtu.be/gkTb9GP9lVI")

    if message.content.startswith('/say'):
        args = message.content.split(" ")
        #args[0] = /say
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

    if message.content.startswith('/rickroll'):
        await client.send_message(message.channel, "This isn't a joke, I'm not sure why you typed this. Many lives are at stake... https://youtu.be/xfr64zoBTAQ")

client.run("Mzk3OTAyMzc2MjkzNDk4ODkx.DS3YNw.0PsItuKDCAq1owKHIiFz4gJwFvs")
