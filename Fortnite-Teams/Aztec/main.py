#
##
### Imports
##
#

import discord
import os
import asyncio
from colorama import Fore as Color
from discord.ext import commands

#
##
### Setup
##
#

intents = discord.Intents.all()
intents.members = True

def prefix(bot, msg):
  return(['a!', 'A!'])

bot = commands.Bot(command_prefix = prefix, case_insensitive=True, intents=intents, owner_ids=[852423298481651743, 789681414064832532, 931886376750833674, 791941780554907658, 753706491965341748, 579009067733745664, 857606108462186526, 931270448111583352, 921744263795052585])
bot.remove_command('help')

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f'cogs.{filename[:-3]}')

#@bot.command()
#async def e(ctx, title, *, description):
#  embed=discord.Embed(title=title, description=description, color=0x0000FF)
#  await ctx.send(embed=embed)

#
##
### Snipe
##
#

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@bot.event
async def on_message_delete(message):

  global snipe_message_content
  global snipe_message_author
  global snipe_message_author_id
  global snipe_message_id

  snipe_message_content = message.content
  snipe_message_author = message.author.name
  snipe_message_author_id = message.author.discriminator
  snipe_message_id = message.id
  await asyncio.sleep(60)

  if message.id == snipe_message_id:
      snipe_message_author = None
      snipe_message_content = None
      snipe_message_id = None

@bot.command(aliases=['s'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def snipe(message):
  if snipe_message_content==None:
      await message.channel.send("Theres nothing to snipe.")
  else:
      embed = discord.Embed(title="Sniped!", description="Here is the message that was deleted!", color=0x0000FF)
      embed.add_field(name="Author", value=f"`{snipe_message_author}#{snipe_message_author_id}`", inline=False)
      embed.add_field(name="Content:", value=f"`{snipe_message_content}`", inline=False)
      embed.set_footer(text=f"#FearAztec", icon_url=message.author.avatar.url)
      embed.set_author(name= "#FearAztec")
      print(f"{Color.WHITE} {message.author} just used the snipe command. {Color.MAGENTA} Guild: {message.guild} {Color.CYAN} Channel: {message.channel}")
      await message.channel.send(embed=embed)
      return

@bot.command(pass_context=True)
@commands.is_owner()
async def embed(ctx, *, message):
  await ctx.message.delete()
  embed=discord.Embed(title=" ", description=f"{message}", color=0x0000FF)
  embed.set_author(name="#FearAztec")
  embed.set_thumbnail(url=ctx.author.avatar.url)
  embed.set_footer(text=f"By: {ctx.author}")
  await ctx.send(embed=embed)

#
##
### Starting Bot
##
#

bot.run('OTQ5MzQwMjU4Njc0Mjc4NDIx.YiI8Aw.kTUO2hb_k8M-Pks9gDoMREBojc0')