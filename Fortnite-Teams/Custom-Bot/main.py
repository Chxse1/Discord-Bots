import discord
import os
import datetime
import json
import random
from discord.ext import commands

def prefix(bot, msg):
    return(['z!', 'Z!'])

bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('OTQ5MzQwMjU4Njc0Mjc4NDIx.YiI8Aw.kTUO2hb_k8M-Pks9gDoMREBojc0')