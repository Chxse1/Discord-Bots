#
##
### Imports
##
#

# Discord Stuff

import discord 
import datetime 
import time
from discord.ext import commands, tasks

# Other Stuff

import os
import json
import urllib
import random
import asyncio
from colorama import Fore as Color

# Slash Commands

from discord_slash import SlashCommand

#
##
### Setup
##
#

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = commands.when_mentioned_or(","), case_insensitive=True, intents=intents, owner_ids=[392028323707879435, 758290177919156244, 526175895862640660, 852423298481651743])
bot.remove_command("help")

slash = SlashCommand(bot, sync_commands=True)

@bot.event  # Sets status when bot is online.
async def on_ready():
  channel = bot.get_channel(897410207779553300)
  print(f"{Color.LIGHTCYAN_EX} We have logged in as Helix!")
  print(f"{Color.GREEN} If you see this, then Helix is running!")
  print(f"{Color.MAGENTA} Type ,help for a list of commands.")
  await bot.change_presence(activity=discord.Game(
	    name=f",help | SLASH COMMANDS ARE HERE! | Watching over {len(bot.users)} users and {len(bot.guilds)} guilds! | Join support using the ,support command!"))

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
      embed=discord.Embed(title="Error",
                          description="Missing Arguments...")
      embed.add_field(name="You are missing required arguments!",
                      value="Use the required arguments to use this command.")
      await ctx.message.reply(embed=embed, mention_author=False)
    elif isinstance(error,commands.errors.CommandNotFound):
      embed=discord.Embed(title="Error",description="No Such Command Found")
      embed.add_field(name="This command was not found.",
                      value="Use the `,help` command to get help.")
      await ctx.message.reply(embed=embed, mention_author=False)
    elif isinstance(error,commands.errors.NotOwner):
      embed=discord.Embed(title="Error", description="Incorrect User!")
      embed.add_field(name="You are not the owner of the bot!",
                      value="You cannot use this command!")
      await ctx.message.reply(embed=embed, mention_author=False)
    elif isinstance(error,commands.errors.BadArgument):
        await ctx.message.reply(f"Data type passed is invalid\n`{str(error)}`", mention_author=False)
    else:
        raise error

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event 
async def on_guild_join(guild):
      server = bot.get_guild(guild.id)
      channel = guild.text_channels[0]
      channellol = bot.get_channel(897676676039860224)
      invlink = await channel.create_invite(unique=True)
      print(f"Helix has been added to a new server! Name: {Color.MAGENTA} {guild.name} {Color.WHITE} | ID: {Color.MAGENTA} {guild.id} {Color.WHITE} | Invite: {Color.MAGENTA} {invlink} {Color.WHITE} | Owner: {Color.MAGENTA} {guild.owner.name}#{guild.owner.discriminator} {Color.WHITE} | Helix is now watching over {Color.MAGENTA} {len(bot.users)} {Color.WHITE} users and {Color.MAGENTA} {len(bot.guilds)} {Color.WHITE} servers!")
      await channellol.send(f"Helix has been added to a new server! Name: `{guild.name}` | ID: `{guild.id}` | Invite: {invlink} | Owner: `{guild.owner.name}#{guild.owner.discriminator}` | Helix is now watching over `{len(bot.users)}` users and `{len(bot.guilds)}` servers!")
 
@bot.event
async def on_message_edit(before, after):
    try:
        await bot.process_commands(after)
    except:
        raise Exception

#
##
### Cog Commands Below 
##
#

@bot.command(hidden=True, aliases=['rel'])
@commands.is_owner()
async def reload(ctx, cog):
	if cog == "all":
		for filename in os.listdir("./cogs"):
			if filename.endswith(".py"):
				try:
					bot.unload_extension(f"cogs.{filename[:-3]}")
					bot.load_extension(f"cogs.{filename[:-3]}")
					await ctx.message.reply(f"{filename[:-3]} was Successfully Reloaded!", mention_author=False)
				except:
					bot.load_extension(f"cogs.{filename[:-3]}")
					bot.unload_extension(f"cogs.{filename[:-3]}")
					bot.load_extension(f"cogs.{filename[:-3]}")
					await ctx.message.reply(f"{filename[:-3]} was Successfully Loaded and Reloaded!", mention_author=False)
	else:
		try:
			bot.unload_extension(f"cogs.{cog}")
			bot.load_extension(f"cogs.{cog}")
			await ctx.message.reply(f"{cog} was Successfully Reloaded!", mention_author=False)
		except:
			bot.load_extension(f"cogs.{cog}")
			bot.unload_extension(f"cogs.{cog}")
			bot.load_extension(f"cogs.{cog}")
			await ctx.message.reply(f"{cog} was Successfully Loaded and Reloaded", mention_author=False)


@bot.command(hidden=True, aliases=["cg"])
@commands.is_owner()
async def cogs(ctx):
	cogs = []
	for cog in bot.cogs:
		cogs.append(cog)
	embed = discord.Embed(
	    title="**Cog Names**",
	    description="*Here are the names of the current cogs.*",
	    colour=discord.Colour.random())
	embed.add_field(name="**My Cogs:**", value=f"`{'`, `'.join(cogs)}`")
	embed.set_footer(
	    text="This is an Owner-Only Command, meaning you can't use it!")
	await ctx.message.reply(embed=embed, mention_author=False)

@bot.command()
@commands.is_owner()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for x in range(amount):
        await ctx.send(message)

@bot.command(hidden=True)
@commands.is_owner()
async def unload(ctx, cog):
	try:
		bot.unload_extension(f"cogs.{cog}")
		await ctx.message.reply(f"{cog} was Successfully Unloaded!", mention_author=False)
	except:
		await ctx.message.reply(f"{cog} isn't Loaded or doesn't exist!", mention_author=False)


@bot.command(hidden=True)
@commands.is_owner()
async def load(ctx, cog):
	try:
		bot.load_extension(f"cogs.{cog}")
		await ctx.message.reply(f"{cog} was Successfully Loaded!", mention_author=False)
	except:
		await ctx.message.reply(f"{cog} isn't Unloaded or doesn't exist!", mention_author=False)
    
#
##
### Uptime ---------------------------------------------------
##
#

start_time = time.time()

@commands.command(name="Uptime", description="See how long the bot has been online!")
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(title="Uptime", description="This is the amount of time Helix has been online!", colour=discord.Color.random())
    embed.add_field(name="**Helix Uptime!**", value=f"`{text}`\nH/M/S")
    embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")
    print(f"{Color.WHITE} {ctx.author} just used the uptime command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.send(embed=embed)
    
@bot.command(aliases=['bi']) # Bot Info
async def botinfo(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(title="My Information",
                          description="Bot Information on Helix",
                          colour=discord.Colour.random())
    embed.add_field(name="___**Developer**___",
                    value="`~Chase~#4471`, `||Dank Lord||#9919`, `darx#2424`",
                    inline=False)
    embed.add_field(name="___**Members**___",
                    value=f"`{len(bot.users)}`",
                    inline=False)
    embed.add_field(name="___**Guilds**___",
                    value=f"`{len(bot.guilds)}`",
                    inline=False)
    embed.add_field(name="___**Library**___",
                    value="`discord.py`",
                    inline=False)
    embed.add_field(name="**___Uptime___**",
                    value=f"`{text}`\nH/M/S",
                    inline=False)
    embed.set_author(name="Helix is Watching!")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    print(f"{Color.WHITE} {ctx.author} just used the botinfo command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.send(embed=embed)

#
##
### Running bot below
##
#

token = ('ODk5ODg3OTU1MjExMDcxNDk4.YW5T9w.04QtQuqU2D5wgrKM1diTpv9LaMc')
bot.run(token)