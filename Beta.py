#Lenny Bot Beta

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import pickle

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
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper() == "IS LENNY BOT HERE":
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper() == "TEST":
        await client.send_message(message.channel, "Passed")

    if message.content.upper() == "GAY":
        await client.send_message(message.channel, "No, you")

    if message.content.upper() == "HOMIE":
        await client.send_message(message.channel, "That's not a word")

    if message.content.upper() == "LENNY BOT ARE YOU HERE?":
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper() == "LENNY BOT ARE YOU HERE":
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper() == "KYS":
        await client.send_message(message.channel, "That's rude, many people commit suicide everyday and you're practically encouraging it")

    if message.content.upper() == "SMOKIN' THAT COOKIN' HOT POT":
        words2 = ['Take the pot off the stove, you could start a fire noob', 'Smoking a hot pot will give you 3rd degree burns, are you ok?']
        await client.send_message(message.channel, random.choice(words2))

#Commands

    if message.content.startswith('/ping'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.startswith('/wow'):
        await client.send_message(message.channel, "https://youtu.be/sCR9f6QhSjY")

    if message.content.startswith('/lol'):
        await client.send_message(message.channel, "https://youtu.be/-B9fOFxlfnw")

    if message.content.startswith('/say'):
        args = message.content.split(" ")
        #args[0] = /say
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

    if message.content.startswith('/rr'):
        await client.send_message(message.channel, "This isn't a joke, I'm not sure why you typed this. Many lives are at stake... https://youtu.be/xfr64zoBTAQ")

    if message.content.startswith('/coin'):
        flip = ['Heads', 'Tails']
        await client.send_message(message.channel, random.choice(flip))

#Help Command *****DO NOT TOUCH*****

    if message.content.startswith('/help'):
        await client.send_message(message.channel, "Lenny Bot was coded for the intention to troll and offer commands for users. Specifications on how Lenny Bot will troll will not be said...get ready to be surprised c:.\n\nCommands:\n/say <text> -- Lenny Bot repeats what you say.\n/ping -- Lenny Bot mentions you and says 'Pong!'.\n/coin -- Lenny bot flips a coin.\n/wow -- gives you a youtube link c:\n/rr -- Surprise!\n/lol -- here's a video for your troubles.\n\nNOTE: This is the beta version of Lenny Bot, more commands to come.")



client.run("Mzk4NTUxOTUzNTEwMTA1MDg5.DTAOHA.c8W8ey-t8fZYlc7_AzgpGXl5uWM")
