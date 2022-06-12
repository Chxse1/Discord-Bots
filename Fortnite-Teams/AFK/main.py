""" * * * * * * * * * * * *
*         IMPORTS         *
* * * * * * * * * * * * """

import discord
import os
import sys
import collection
import asyncio
import find
import json
from colorama import Fore as Color
from discord.ext import commands
""" * * * * * * * * * * * *
*         SETUP           *
* * * * * * * * * * * * """

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?",
                   case_insensitive=True,
                   intents=intents,
                   owner_ids=[852423298481651743])


""" * * * * * * * * * * * *
*         STUFF           *
* * * * * * * * * * * * """

def restart_bot():
  os.execv(sys.executable, ["python"] + sys.argv)

@bot.event
async def on_ready():
  print(f"Bot is ready!")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f" over Team Visual with {len(bot.users)} members!"))

@bot.event
async def on_command_error(ctx, error):
    await ctx.message.reply(f"{error}")

@bot.command(aliases=['res'])
@commands.is_owner()
async def restart(ctx):
  embed=discord.Embed(title="Restarting", description="Restarting! Please wait!", color=0x33FFFF)
  print(f"{Color.WHITE} {ctx.author} just used the restart command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")    
  await ctx.message.reply(embed=embed)
  restart_bot()
        
""" * * * * * * * * * * * *
*         COGS            *
* * * * * * * * * * * * """

@bot.command(hidden=True, aliases=['rel'])
@commands.is_owner()
async def reload(ctx, cog):
    if cog == "all":
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    bot.unload_extension(f"cogs.{filename[:-3]}")
                    bot.load_extension(f"cogs.{filename[:-3]}")
                    await ctx.message.reply(f"`{filename[:-3]}` was Successfully Reloaded!", mention_author=False)
                except:
                    bot.load_extension(f"cogs.{filename[:-3]}")
                    bot.unload_extension(f"cogs.{filename[:-3]}")
                    bot.load_extension(f"cogs.{filename[:-3]}")
                    await ctx.message.reply(f"`{filename[:-3]}` was Successfully Loaded and Reloaded!", mention_author=False)
    else:
        try:
            bot.unload_extension(f"cogs.{cog}")
            bot.load_extension(f"cogs.{cog}")
            await ctx.message.reply(f"`{cog}` was Successfully Reloaded!", mention_author=False)
        except:
            bot.load_extension(f"cogs.{cog}")
            bot.unload_extension(f"cogs.{cog}")
            bot.load_extension(f"cogs.{cog}")
            await ctx.message.reply(f"`{cog}` was Successfully Loaded and Reloaded", mention_author=False)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')

""" * * * * * * * * * * * *
*         RUN BOT         *
* * * * * * * * * * * * """

bot.run('ODk5MDM0NzMzNjIxNjk4NjIz.YWs5Vw.kRD0ZH8rCHCmrJBV0X-mMqYmgJg')