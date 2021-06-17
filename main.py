# ==== Bot Connextion ==== #

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
@client.event
async def on_ready():
    print("Conexiune stabilita !")

# ==== Bot Commands ==== #


# ==== Bot Client Key ==== #
client.run("ODU0MzA1Nzc2NjUwNDIwMjI0.YMiAQQ.Wef2LP-tMqyds7tAuafaTIHcdvo")
