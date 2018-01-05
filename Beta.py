#Lenny Bot Beta

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
    print("Lenny Bot is online")

@client.event
async def on_message(message):

#Statements --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if message.content.upper() == "SMH":
        await client.send_message(message.channel, "How about you actually shake your head instead of texting it?")

    if message.content.upper() == "IS LENNY BOT HERE?":
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question', 'I am here, now leave me alone']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper() == "IS LENNY BOT HERE":
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question', 'I am here, now leave me alone']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper() == "TEST":
        await client.send_message(message.channel, "Passed")

    if message.content.upper() == "GAY" or message.content.upper() == "YOU ARE MAD GAY" or message.content.upper() == "YOU'RE MAD GAY" or message.content.upper() == "UR MAD GAY":
        await client.send_message(message.channel, "No, you")

    if message.content.upper() == "HOMIE":
        await client.send_message(message.channel, "That's not a word")

    if message.content.upper() == "LENNY BOT ARE YOU HERE?":
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question', 'I am here, now leave me alone']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper() == "LENNY BOT ARE YOU HERE":
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question', 'I am here, now leave me alone']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper() == "LENNY ARE YOU HERE":
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question', 'I am here, now leave me alone']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper() == "IS LENNY HERE?":
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question', 'I am here, now leave me alone']
        await client.send_message(message.channel, random.choice(reply))

    if message.content.upper() == "IS LENNY HERE":
        reply = ['No...kappa ( ͡° ͜ʖ ͡°)', 'Good question', 'I am here, now leave me alone']
        await client.send_message(message.channel, random.choice(reply))    

    if message.content.upper() == "KYS":
        await client.send_message(message.channel, "That's rude, many people commit suicide everyday and you're practically encouraging it")

    if message.content.upper() == "SMOKIN' THAT COOKIN' HOT POT":
        words2 = ['Take the pot off the stove, you could start a fire noob', 'Smoking a hot pot will give you 3rd degree burns, are you ok?']
        await client.send_message(message.channel, random.choice(words2))

    if message.content.upper() == "STUPID LENNY BOT":
        come_back = ['I know you are, but what am I?', 'Is that right? And what exactly have you accomplished in your lifetime that makes you Einstein?', 'Unless your name is Google, stop acting like you know everything']
        await client.send_message(message.channel, random.choice(come_back))

    if message.content.upper() == "STUPID LENNY":
        come_back = ['I know you are, but what am I?', 'Is that right? And what exactly have you accomplished in your lifetime that makes you Einstein?', 'Unless your name is Google, stop acting like you know everything']
        await client.send_message(message.channel, random.choice(come_back))

    if message.content.upper() == "KYS LENNY BOT":
        come_back2 = ["I would if I could but I can't", "If I were to kill myself then you will find that I will haunt your dreams"]
        await client.send_message(message.channel, random.choice(come_back2))

    if message.content.upper() == "I H8 U":
        await client.delete_message(message)
        await client.send_message(message.channel, "He lufs u")

    if message.content.upper() == "I HATE U" or message.content.upper() == "I HATE YOU":
        await client.delete_message(message)
        await client.send_message(message.channel, "He lufs u")

    if message.content.upper() == "THANKS LENNY BOT" or message.content.upper() == "THANKS LENNY" or message.content.upper() == "THANK YOU LENNY BOT" or message.content.upper() == "THANK YOU LENNY" or message.content.upper() == "TY LENNY" or message.content.upper() == "TY LENNY BOT":
        await client.send_message(message.channel, "You're welcome :3")

#Commands ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if message.content.startswith('/ping'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.startswith('/wow'):
        await client.send_message(message.channel, "https://youtu.be/hU7EHKFNMQg")

    if message.content.startswith('/lol'):
        links = ['https://youtu.be/nQB4nAjZIdE', 'https://youtu.be/sCR9f6QhSjY', 'https://youtu.be/-B9fOFxlfnw']
        await client.send_message(message.channel, random.choice(links))

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

    if message.content.startswith('/reem'):
        reem = ['Go home walking, Reem :^)', 'Reem, I will give you $100 if you go home walking', 'Reem, you should be respectful to your elders you nib']
        await client.send_message(message.channel, random.choice(reem))

    if message.content.startswith('/jawad'):
        jawad = ['I luf u', 'I disluf u', 'Do u luf me?', 'Nib', 'I hate anime', 'Anime is trash', 'Get rekt', 'Do you need an icepack for that burn?']
        await client.send_message(message.channel, random.choice(jawad))

    if message.content.startswith('/dice'):
        dice = ['1', '2', '3', '4', '5', '6']
        await client.send_message(message.channel, random.choice(dice))

    if message.content.startswith('/hassan'):
        hassan = ["Smokin' that cookin' hot pot", "You want some beef?", "Ofc Ofc"]
        await client.send_message(message.channel, random.choice(hassan))

#Help Command *****DO NOT TOUCH***** 

    if message.content.startswith('/help'):
        await client.send_message(message.channel, '''Lenny Bot was coded for the intention of trolling, having fun, and offering commands to users. How Lenny Bot will troll won't be specified, youll have to find out on your own.
\nCommands:\n
/help -- Displays the list of commands for Lenny Bot.
/ping -- Has Lenny Bot mention you and say "Pong!".
/wow -- A video for your troubles.
/lol -- Lenny Bot picks 1 out of the 3 random videos to display (with more to be added soon).
/say <text> -- Type the command followed by anything you want Lenny Bot to say.
/rr -- You're very welcome.
/coin -- Lenny Bot flips a coin.
/reem -- Just for you Reem.
/jawad -- Just for your Jawad.
/hassan -- Just for you Hassan.
/dice -- Lenny Bot rolls a dice.\n
**NOTE: Lenny Bot is still in the Beta stage, and is being worked on.**''')


client.run("Mzk4NTUxOTUzNTEwMTA1MDg5.DTAOHA.c8W8ey-t8fZYlc7_AzgpGXl5uWM")
