""" * * * * * * * * * * * *
*         IMPORTS         *
* * * * * * * * * * * * """

import discord
import os
import sys
import asyncio
import json
from colorama import Fore as Color
from discord.ext import commands
""" * * * * * * * * * * * *
*         SETUP           *
* * * * * * * * * * * * """

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".",
                   case_insensitive=True,
                   intents=intents,
                   owner_ids=[852423298481651743, 540951106847637514])

bot.remove_command('help')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f'cogs.{filename[:-3]}')

def restart_bot():
  os.execv(sys.executable, ["python"] + sys.argv)

""" * * * * * * * * * * * *
*         EVENTS          *
* * * * * * * * * * * * """


@bot.event
async def on_ready():
  print(f"Bot is ready!")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f" over Team Visual with {len(bot.users)} members!"))

@bot.event
async def on_member_join(member):
  role = discord.utils.get(member.guild.roles, id=812860928877264946)
  await member.add_roles(role)
  channel = bot.get_channel(812860999882768384)
  embed=discord.Embed(title="Welcome", description=f"Everyone welcome {member.mention}({member.name}#{member.discriminator}) to Team Visual!", color=0x33FFFF)
  embed.add_field(name="We hope you enjoy your stay!", value="Make sure to read the <#812860984011390996>!", inline=False)
  embed.add_field(name="Have fun at Team Visual!", value="Visit <#812861005158940732> to see our qualifications and make sure to say hello in <#812860999882768384>!", inline=False)
  embed.set_author(name="#VisualOT!")
  embed.set_footer(text=f"#VisualOT")
  embed.set_thumbnail(url="https://lh3.googleusercontent.com/PVhUg4sG2KsCzYQNUnEqAwdoJyXEb5-FSR7AyK5mlf7DlMDFU-KWFEZM4I-gLKsKLK4=w1200-h630-p")
  embed.set_image(url="https://lh3.googleusercontent.com/PVhUg4sG2KsCzYQNUnEqAwdoJyXEb5-FSR7AyK5mlf7DlMDFU-KWFEZM4I-gLKsKLK4=w1200-h630-p")
  await channel.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,commands.errors.CommandNotFound):
    # await ctx.message.reply(f"{error}")
      return
    if isinstance(error, commands.errors.NotOwner):
        embed = discord.Embed(title="Error",
                              description="You are not an owner of the bot!",
                              color=0xFF0000)
        await ctx.message.reply(embed=embed)
    elif isinstance(error, commands.errors.MissingPermissions):
        embed = discord.Embed(
            title="Error",
            description="You are missing permissions to do this!",
            color=0xFF0000)
        await ctx.message.reply(embed=embed)
    elif isinstance(error, commands.errors.CommandOnCooldown):
        embed = discord.Embed(
            title="Error",
            description="You are on cooldown for this command!",
            color=0xFF0000)
        await ctx.message.reply(embed=embed)
    elif isinstance(error, commands.errors.CommandInvokeError):
        embed = discord.Embed(title="Error",
                              description=f"{error}",
                              color=0xFF0000)
    elif isinstance(error, commands.errors.MemberNotFound):
        embed = discord.Embed(title="Error",
                              description="Member was not found.",
                              color=0xFF0000)
        await ctx.message.reply(embed=embed)
    else:
        raise error


""" * * * * * * * * * * * *
*         TESTING         *
* * * * * * * * * * * * """



""" * * * * * * * * * * * *
*         COG STUFF       *
* * * * * * * * * * * * """

@bot.command(aliases=['res'])
@commands.is_owner()
async def restart(ctx):
  embed=discord.Embed(title="Restarting", description="Restarting! Please wait!", color=0x33FFFF)
  print(f"{Color.WHITE} {ctx.author} just used the restart command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")    
  await ctx.message.reply(embed=embed)
  restart_bot()

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

@bot.command(aliases=["cg"])
@commands.is_owner()
async def cogs(ctx):
    cogs = []
    for cog in bot.cogs:
        cogs.append(cog)
    embed = discord.Embed(
	      title="**Cog Names**",
	      description="*Here are the names of the current cogs.*",
	      color=0x33FFFF)
    embed.add_field(name="**My Cogs:**", value=f"`{'`, `'.join(cogs)}`")
    embed.set_footer(
	      text="This is an Owner-Only Command, meaning you can't use it!")
    await ctx.message.reply(embed=embed, mention_author=False)

@bot.command(hidden=True)
@commands.is_owner()
async def unload(ctx, cog):
    try:
        bot.unload_extension(f"cogs.{cog}")
        await ctx.message.reply(f"`{cog}` was Successfully Unloaded!", mention_author=False)
    except:
        await ctx.message.reply(f"`{cog}` isn't Loaded or doesn't exist!", mention_author=False)


@bot.command(hidden=True)
@commands.is_owner()
async def load(ctx, cog):
    try:
        bot.load_extension(f"cogs.{cog}")
        await ctx.message.reply(f"`{cog}` was Successfully Loaded!", mention_author=False)
    except:
        await ctx.message.reply(f"`{cog}` isn't Unloaded or doesn't exist!", mention_author=False) 

""" * * * * * * * * * * * *
*         SNIPE           *
* * * * * * * * * * * * """

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
      embed = discord.Embed(title="Sniped!", description="Here is the message that was deleted!", color=0x33FFFF)
      embed.add_field(name="Author", value=f"`{snipe_message_author}#{snipe_message_author_id}`", inline=False)
      embed.add_field(name="Content:", value=f"`{snipe_message_content}`", inline=False)
      embed.set_footer(text=f"#VisualOT", icon_url=message.author.avatar_url)
      embed.set_author(name= "#VisualOT")
      print(f"{Color.WHITE} {message.author} just used the ping command. {Color.MAGENTA} Guild: {message.guild} {Color.CYAN} Channel: {message.channel}")
      await message.channel.send(embed=embed)
      return

""" * * * * * * * * * * * *
*         WARN            *
* * * * * * * * * * * * """

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(view_audit_log=True)
async def warn(ctx,user:discord.User=None,*reason:str):
  if user == None:
    embed=discord.Embed(title="Error...", description="No User Specified...", color=0x33FFFF)
    embed.add_field(name="Please specify the user being warned.", value="Ex: `v!warn <User> <Reason>`")
    embed.set_author(name="#VisualOT")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    await ctx.message.reply(embed=embed)
    return
  if not reason:
    embed=discord.Embed(title="Error...", description="No Arguments Given...", color=0x33FFFF)
    embed.add_field(name="Please specify what the reason is for.", value="Ex: `v!warn <User> <Reason>`")
    embed.set_author(name="#VisualOT")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    await ctx.message.reply(embed=embed)
    return
  reason = ' '.join(reason)
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)
      break
  else:
    report['users'].append({
      'name':user.name,
      'reasons': [reason,]
    })
  with open('reports.json','w+') as f:
    json.dump(report,f)
  embed1=discord.Embed(title="Warned", description=f"`{user.name}#{user.discriminator}` has been warned!", color=0x33FFFF)
  embed1.add_field(name="Reason:", value=f"`{reason}`")
  embed1.set_author(name="#VisualOT")
  embed1.set_thumbnail(url=ctx.author.avatar_url)
  embed1.set_footer(text=f"Warned by {ctx.author}")
  print(f"{ctx.author} has used the warn command...")
  await ctx.message.reply(embed=embed1)

  embed2=discord.Embed(title="Warned", description="You have been warned.", color=0x33FFFF)
  embed2.add_field(name=f"You have been warned in `{ctx.guild.name}` by `{ctx.author.name}#{ctx.author.discriminator}`.", value=f"Reason: `{reason}`")
  embed2.set_author(name="#VisualOT")
  embed2.set_thumbnail(url=ctx.author.avatar_url)
  embed2.set_footer(text=f"Warned by {ctx.author}")
  await user.send(embed=embed2)

@bot.command(aliases=['warnings'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def warns(ctx,user:discord.User):
  for current_user in report['users']:
    if user.name == current_user['name']:
      embed = discord.Embed(title="Warnings", description=f"`{user.name}#{user.discriminator}` has `{len(current_user['reasons'])}` warning(s).", color=0x33FFFF)
      embed.add_field(name="Warnings:", value=f"`{'`, `'.join(current_user['reasons'])}`")
      embed.set_author(name="#VisualOT")
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.set_footer(text=f"Requested By {ctx.author}")
      await ctx.message.reply(embed=embed)
      break
  else:
      embed = discord.Embed(title="Warnings", description=f"`{user.name}#{user.discriminator}` has `0` warnings.", color=0x33FFFF)
      embed.add_field(name="Warnings:", value=f"`None`")
      embed.set_author(name="#VisualOT")
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.set_footer(text=f"Requested By {ctx.author}")
      await ctx.message.reply(embed=embed)

@warn.error
async def kick_error(error, ctx):
  if isinstance(error,commands.errors.CommandInvokeError):
      embed=discord.Embed(title="Error",
                          description="Missing Arguments...")
      embed.add_field(name="You are missing required arguments!",
                      value="You are either missing arguments, or are using invalid, or incorrect arguments.")
      await ctx.message.reply(embed=embed)

""" * * * * * * * * * * * *
*         RUN BOT         *
* * * * * * * * * * * * """

bot.run('OTQ5MzQwMjU4Njc0Mjc4NDIx.YiI8Aw.kTUO2hb_k8M-Pks9gDoMREBojc0')