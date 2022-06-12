import discord
import os
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", intents=intents, case_sensitive=True, owner_id=['852423298481651743'])

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('OTUxMjY4Mzc3MzA4MDQ1NDA0.Yik_tg.86o0YIsRKaLQwW7Ko4hci1iaBGk')