# ==== Bot Connextion ==== #

import discord
from discord import user
from discord.ext import commands
from discord.ext.commands.core import has_permissions
from discord.ext.commands.errors import MissingPermissions
from discord.member import Member
from discord.user import User
from discord.ext.commands.cooldowns import BucketType
import youtube_dl
import os
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system

client = commands.Bot(command_prefix = '.')
@client.event
async def on_ready():
    print("Conexiune stabilita !")
    activity = discord.Game(name=".helpme")
    await client.change_presence(status=discord.Status.idle, activity=activity)

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Whoaa ! Teleporting was fun, hello dummies ! I'm TheWolfy bot. Type .helpme 👀")
        break

# ==== Bot Commands ==== #

@client.command() #=== !hellobot ===
async def hellobot(ctx): #ctx = context parameter
     await ctx.send("Howdy, userino ! I'm TheWølfy bot and right now i'm online ! If you want help please type '.helpme'. Thanks ^_^")

@client.command() #=== !helpme ===
async def helpme(ctx):
    await ctx.send("""Glad to help you, userino ! The following are the commands and what can i do !: 
    .helpme - You already typed the command, lul. That's a command listing all the commands :>
    .hellobot - A hello message just to check if i'm on duty xd
    .clear* [lines] - Clear how many lines you want.
    .kick* [@user] [reason] - If someone was a bad boi, you can kick him for a good reason
    .ban* [@user] [reason] - Same with kick, but the ban is permanently and can be undone by the administrator 
    .about - All the things about me
    .onlinecheck - See if i'm online
    .play [youtube link] - TheWolfy is also a DJ ! Play what you want
    .leave - Kick him out from the voice channel
    * = Administrative commands (acces gained for moderators / administrators)
    """)

@client.command()
async def onlinecheck(ctx):
    await ctx.send("""Status: Online
    
    Yes ! I'm online, but only when my master is online too. If you want to manage this server 24/7, pay fucking 4 dollars for a hosting service. xoxo""")

@client.command() #=== !clear ===
@commands.has_role("tot eu dar cu rosu ca-mi plc")
async def clear(ctx, amount = 0):
    await ctx.channel.purge(limit=amount+1)  #ctx.channel = channel where is executed calling the purge
    await ctx.send("Deleted. Oopsie....i've typed in :\ might delete later")


@client.command() #=== !kick ===
@commands.has_role("Chad aimer")
async def kick(ctx, member : discord.Member, *, reason=None): #saying member to read discord's member function
                                                              # * = Offer space after every argument written by the moderator / administrator
        
    if ctx.author.top_role <= member.top_role:
        await ctx.send("The person you tried to kick has equal or higher role than you")
        return
    await member.kick(reason=reason)
    await ctx.send(f"{member} has been kicked :^ (Reason: {reason})")
        
@client.command() #=== !ban ===
@commands.has_role("Chad aimer")
async def ban(ctx, member : discord.Member, *, reason=None): #saying member to read discord's member function
    if ctx.author.top_role <= member.top_role:
        await ctx.send("The person you tried to ban has equal or higher role than you")
        return
    await member.ban(reason=reason)
    await ctx.send(f"{member} has been banned :o (Reason: {reason})")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
        await ctx.send("Ugh, you don't have admin permissions for banning users")

@kick.error
async def kick_error(ctx,error):
    if isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
        await ctx.send("OOF, you don't have moderator permissions for kicking users, homie :v")

@clear.error
async def clear_error(ctx,error):
    if isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
        await ctx.send("You have to own a role upper than 'Unicorn Intergalactic' to perform a clear chat :>")

@client.command() #=== !about ===
async def about(ctx):
    await ctx.send(f"""Hi {ctx.author.mention} ! I'm TheWølfy bot, the same nickname as my creator's one. 
    I am here to help communities develop their own administration stuff and also maybe have fun together! 
    I'm designed in PYTHON3 programming language, in beta from June 2021. I have no feeling 'cause i'm a bot, duuuh
    so if you don't like me, i don't care :) 
    
    Creator & Owner: TheWølfy#2483
    Created: June 2021
    Version: 1.1T (R - Official Release | T - Beta version test)""")

@client.command()
async def ruja(ctx):
    for _ in range(2000):
        myid = '<@769510862192508928>'
        await ctx.send(f"<@769510862192508928> <@769510862192508928> <@769510862192508928> <@769510862192508928> <@769510862192508928> <@769510862192508928> <@769510862192508928> <@769510862192508928> <@769510862192508928> <@769510862192508928> <@769510862192508928> <@769510862192508928> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@769510862192508928> <@312568518568574976> <@312568518568574976> <@769510862192508928> <@312568518568574976><@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@769510862192508928> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976> <@312568518568574976>")

@client.command()
async def sexruja(context, user: discord.User):
    for _ in range(1000):
        await user.send("ce faci frumosule ma mai iubesti? :hot_face: :hot_face:")

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end then try again")
        

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    activity = discord.Game(name=f'"{url}"')
    await client.change_presence(status=discord.Status.idle, activity=activity)
    await ctx.send(f' Now playing: {url}')

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send("""Disconnected uWu
    
    *May except a little delay because of a bug""")
    activity = discord.Game(name=".helpme")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.'):
        await message.channel.send("""I'm under maintenance mode. Please come back later, seems that i have a lot of bugs needing fix -_-
        Reason of maintenance: Bugs (permissions f#cked up for the .clear command)
        ```css\nI'm coming back later, see ya !```""")

# ==== Bot Client Key ==== #
client.run("ODU0MzA1Nzc2NjUwNDIwMjI0.YMiAQQ.Wef2LP-tMqyds7tAuafaTIHcdvo")
