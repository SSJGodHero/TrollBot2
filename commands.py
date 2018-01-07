#Lenny Bot Commands

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
    print("Lenny Bot (Commands) is online")

@client.event
async def on_message(message):

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

    if message.content.startswith('/kick'):
        response = ['The person has been kicked...( ͡° ͜ʖ ͡°)', 'HHHHHHHHH no', 'Kappa']
        await client.send_message(message.channel, random.choice(response))

    if message.content.startswith('/jihad'):
        jihad = ['I love anime so much.', 'I luf u', 'Do you guys watch Grimgar?', 'I am a Saiyan', '#TeamAlex', 'Hassan. I luf u.', 'I love DBZ so much.']
        await client.send_message(message.channel, random.choice(jihad))

    if message.content.startswith('/num1'):
        robbie = ['https://i.ytimg.com/vi/P3to8euoDQQ/maxresdefault.jpg', 'https://pbs.twimg.com/profile_images/688918577496231936/72BRi7c1.jpg', 'https://www.youtube.com/watch?v=PfYnvDL0Qcw', 'https://vignette.wikia.nocookie.net/abandoned-discovery-island-rp/images/7/71/Robbieroten-mainimage.jpg/revision/latest?cb=20161112204148']
        await client.send_message(message.channel, random.choice(robbie))

    if message.content.startswith('/dewit'):
        await client.send_message(message.channel, "https://pbs.twimg.com/profile_images/575699272303140864/tuvCN6-E.jpeg")

#Help Command *****DO NOT TOUCH***** -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    if message.content.startswith('/help'):
        emb = (discord.Embed(description='''Lenny Bot was coded for the intention of trolling, having fun, and offering commands to users. How Lenny Bot will troll won't be specified, you'll have to find out on your own.
\nCommands:\n
/help -- Displays the list of commands for Lenny Bot.
/ping -- Has Lenny Bot mention you and say "Pong!".
/wow -- A video for your troubles.
/lol -- Lenny Bot picks 1 out of the 3 random videos to display (with more to be added soon).
/say <text> -- Type the command followed by anything you want Lenny Bot to say.
/rr -- You're very welcome.
/coin -- Lenny Bot flips a coin.
/reem -- Just for you Reem.
/jawad -- Just for you Jawad.
/hassan -- Just for you Hassan.
/jihad -- Just for you Jihad
/dice -- Lenny Bot rolls a dice.
/num1 -- Who's number one?
/dewit -- Do it.
/kick -- A command so you can kick someone out of the group.\n
**NOTE: Lenny Bot is still in the beta stage, and is being worked on.**''', colour=0x3DF270))
        emb.set_author(name="Help", icon_url='https://www.lennyfaces.net/public/og-image.png')
        await client.send_message(message.channel, embed = emb)


client.run("Mzk4NTUxOTUzNTEwMTA1MDg5.DTAOHA.c8W8ey-t8fZYlc7_AzgpGXl5uWM")
