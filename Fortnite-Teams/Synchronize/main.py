# Imports

import discord
import os
from pystyle import Colorate, Colors
from discord.ext import commands

# Definitions for other files

afk = {}
prefix = ['s!', 'S!']
token = "OTY0NTEzNDQ1NzIwNTEwNTE1.YllvJQ.w1X9QX8Ga7U6PBv-Dk0UPlBt7s0"
embed_color = 0x000000
hashtag = "#2InSync"

# Bot Definition

bot = commands.Bot(command_prefix=prefix, case_insensitive=True, help_command=None, intents=discord.Intents.all())

# Cog Setup

for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(Colorate.Horizontal(Colors.rainbow, f"Loaded {filename}"))

# Bot Start

bot.run(token)