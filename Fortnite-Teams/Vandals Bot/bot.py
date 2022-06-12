import discord
import os
from discord.ext import commands

def prefix(bot, msg):
    return['v!', 'V!']

intents = discord.Intents.all()

bot=commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)
bot.remove_command('help')

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('OTQ5MzQwMjU4Njc0Mjc4NDIx.YiI8Aw.kTUO2hb_k8M-Pks9gDoMREBojc0')