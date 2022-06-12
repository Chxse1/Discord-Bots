import discord
import os
from discord.ext import commands

embed_color = 0x00FFFF
team_name = "Varmony"
hashtag = "#VarmonyOT"
welcome_channels = "<#947221903393833012>, <#947223463930757140>, <#947223517974392903>, <#947226184125657109>, and <#947226415177302016>!"
prefix = ['v!', 'V!']
intents = discord.Intents.all()
owner_ids = [852423298481651743]
help_command = None

bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents, help_command=help_command, owner_ids=owner_ids)

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('OTM2OTk2ODc3MzQ0MzI5Nzc5.YfVUWA.RQc1vV09XZoS4DYQ2Id_moS0bu0')