# ==== Bot Connextion ==== #

import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions

client = commands.Bot(command_prefix = '!')
@client.event
async def on_ready():
    print("Conexiune stabilita !")

# ==== Bot Commands ==== #

@client.command() #=== !hellobot ===
async def hellobot(ctx): #ctx = context parameter
     await ctx.send("Howdy, userino ! I'm TheWølfy bot and right now i'm online ! If you want help please type '!helpme'. Thanks ^_^")

@client.command() #=== !helpme ===
async def helpme(ctx):
    await ctx.send("""Glad to help you, userino ! The following are the commands and what can i do !: 
    !helpme - You already typed the command, lul. That's a command listing all the commands :>
    !hellobot - A hello message just to check if i'm on duty xd""")

@client.command() #=== !clear ===
@commands.has_role("Moderator")  # check the user role
async def clear(ctx, amount = 0):
    await ctx.channel.purge(limit=amount+1)  #ctx.channel = channel where is executed calling the purge
    await ctx.send("Deleted. Oopsie....i've typed in :\ might delete later")

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
        await ctx.send("Oopsie... You don't have admin permissions. You need 'Moderator' role to clear all the sh%t :)")

# ==== Bot Client Key ==== #
client.run("ODU0MzA1Nzc2NjUwNDIwMjI0.YMiAQQ.Wef2LP-tMqyds7tAuafaTIHcdvo")
