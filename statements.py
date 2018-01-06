#Lenny Bot Statements

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "/")

@client.event
async def on_ready():
    print("Lenny Bot (Statements) is online")

@client.event
async def on_message(message):

    if message.content.upper().startswith('SMH') or message.content.upper().endswith('SMH'):
        await client.send_message(message.channel, "How about you actually shake your head instead of texting it?")

    if message.content.upper().startswith("IS LENNY BOT HERE?") or message.content.upper().endswith("IS LENNY BOT HERE?"):
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper().startswith("TEST") or message.content.upper().endswith("TEST"):
        pass_fail = ['Passed', 'Failed']
        await client.send_message(message.channel, random.choice(pass_fail))

    if message.content.upper().startswith("GAY") or message.content.upper().endswith("GAY"):
        await client.send_message(message.channel, "No, you")

    if message.content.upper().startswith("HOMIE") or message.content.upper().endswith("HOMIE"):
        await client.send_message(message.channel, "'Homie' isn't a word")

    if message.content.upper().startswith("LENNY BOT ARE YOU HERE?") or message.content.upper().endswith("LENNY BOT ARE YOU HERE?"):
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper().startswith("LENNY ARE YOU HERE") or message.content.upper().endswith("LENNY ARE YOU HERE"):
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper().startswith("IS LENNY HERE") or message.content.upper().endswith("IS LENNY HERE"):
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question']
        await client.send_message(message.channel, random.choice(reply))    

    if message.content.upper().startswith("KYS") or message.content.upper().endswith("KYS"):
        await client.send_message(message.channel, "That's rude, you're practically encouraging suicide")

    if message.content.upper().startswith("SMOKIN' THAT COOKIN' HOT POT") or message.content.upper().endswith("SMOKIN' THAT COOKIN' HOT POT"):
        words2 = ['Take the pot off the stove, you could start a fire noob', 'Smoking a hot pot will give you 3rd degree burns, are you ok?']
        await client.send_message(message.channel, random.choice(words2))

    if message.content.upper().startswith("STUPID LENNY BOT") or message.content.upper().endswith("STUPID LENNY BOT"):
        come_back = ['I know you are, but what am I?', 'Is that right? And what exactly have you accomplished in your lifetime that makes you Einstein?', 'Unless your name is Google, stop acting like you know everything']
        await client.send_message(message.channel, random.choice(come_back))

    if message.content.upper().startswith("STUPID LENNY") or message.content.upper().endswith("STUPID LENNY"):
        come_back = ['I know you are, but what am I?', 'Is that right? And what exactly have you accomplished in your lifetime that makes you Einstein?', 'Unless your name is Google, stop acting like you know everything']
        await client.send_message(message.channel, random.choice(come_back))

    if message.content.upper().startswith("I H8 U") or message.content.upper().endswith("I H8 U"):
        await client.delete_message(message)
        await client.send_message(message.channel, "He lufs u")

    if message.content.upper().startswith("I HATE U") or message.content.upper().endswith("I HATE U") or message.content.upper().startswith("I HATE YOU") or message.content.upper().endswith("I HATE YOU"):
        await client.delete_message(message)
        await client.send_message(message.channel, "He lufs u")

    if message.content.upper() == "THANKS LENNY BOT" or message.content.upper() == "THANKS LENNY" or message.content.upper() == "THANK YOU LENNY BOT" or message.content.upper() == "THANK YOU LENNY" or message.content.upper() == "TY LENNY" or message.content.upper() == "TY LENNY BOT":
        await client.send_message(message.channel, "You're welcome :3")
        


client.run("Mzk4NTUxOTUzNTEwMTA1MDg5.DTAOHA.c8W8ey-t8fZYlc7_AzgpGXl5uWM")
