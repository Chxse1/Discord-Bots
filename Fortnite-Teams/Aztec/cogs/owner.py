import discord
import os
import sys
from discord.ext import commands
from colorama import Fore as Color

def restart_bot():
  os.execv(sys.executable, ["python"] + sys.argv)

class owner(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command(aliases=['res'])
  @commands.is_owner()
  async def restart(self, ctx):
    print(f"{Color.WHITE} {ctx.author} just used the restart command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")    
    await ctx.message.reply("Restarting! Please Wait...")
    restart_bot()

  @commands.command(aliases=['announce'])  # Say Command
  @commands.is_owner()
  async def say(self, ctx, *, message=None):
    if message == None:
      embed = discord.Embed(title="Error!", description="Missing Arguments!")
      embed.add_field(name="You are missing required arguments!", value="Specify what you want me to say...")
      await ctx.message.reply(embed=embed, delete_after = 2)
    else:
      await ctx.message.delete()
      print(f"{Color.WHITE} {ctx.author} just used the say command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.send(message)

  @commands.command(hidden=True, aliases=['rel'])
  @commands.is_owner()
  async def reload(self, ctx, cog):
    if cog == "all":
      for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
          try:
            self.bot.unload_extension(f"cogs.{filename[:-3]}")
            self.bot.load_extension(f"cogs.{filename[:-3]}")
            await ctx.message.reply(f"`{filename[:-3]}` was Successfully Reloaded!", mention_author=False)
          except:
            self.bot.load_extension(f"cogs.{filename[:-3]}")
            self.bot.unload_extension(f"cogs.{filename[:-3]}")
            self.bot.load_extension(f"cogs.{filename[:-3]}")
            await ctx.message.reply(f"`{filename[:-3]}` was Successfully Loaded and Reloaded!", mention_author=False)
    else:
      try:
        self.bot.unload_extension(f"cogs.{cog}")
        self.bot.load_extension(f"cogs.{cog}")
        await ctx.message.reply(f"`{cog}` was Successfully Reloaded!", mention_author=False)
      except:
        self.bot.load_extension(f"cogs.{cog}")
        self.bot.unload_extension(f"cogs.{cog}")
        self.bot.load_extension(f"cogs.{cog}")
        await ctx.message.reply(f"`{cog}` was Successfully Loaded and Reloaded", mention_author=False)

  @commands.command(aliases=["cg"])
  @commands.is_owner()
  async def cogs(self, ctx):
    cogs = []
    for cog in self.bot.cogs:
      cogs.append(cog)
    embed = discord.Embed(
	      title="**Cog Names**",
	      description="*Here are the names of the current cogs.*",
	      color=0x0000FF)
    embed.add_field(name="**My Cogs:**", value=f"`{'`, `'.join(cogs)}`")
    embed.set_footer(
	      text="This is an Owner-Only Command, meaning you can't use it!")
    await ctx.message.reply(embed=embed, mention_author=False)

  @commands.command(hidden=True)
  @commands.is_owner()
  async def unload(self, ctx, cog):
    if cog == "owner":
      await ctx.reply("This cog can not be unloaded. If this cog is unloaded, then some problems may occur.")
      return
    try:
      self.bot.unload_extension(f"cogs.{cog}")
      await ctx.message.reply(f"`{cog}` was Successfully Unloaded!", mention_author=False)
    except:
      await ctx.message.reply(f"`{cog}` isn't Loaded or doesn't exist!", mention_author=False)


  @commands.command(hidden=True)
  @commands.is_owner()
  async def load(self, ctx, cog):
    try:
      self.bot.load_extension(f"cogs.{cog}")
      await ctx.message.reply(f"`{cog}` was Successfully Loaded!", mention_author=False)
    except:
      await ctx.message.reply(f"`{cog}` isn't Unloaded or doesn't exist!", mention_author=False) 

  @commands.command()
  @commands.is_owner()
  async def configrole1(self, ctx, toggle, member:discord.Member=None, *, id1):
    if toggle == 'add':
      if member == None:
        role = discord.utils.get(ctx.guild.roles, id=id1)
        await ctx.message.delete()
        await ctx.author.add_roles(role)
        await ctx.send("This is not a command! Try again!")
      else:
        role = discord.utils.get(ctx.guild.roles, id=id1)
        await ctx.message.delete()
        await member.add_roles(role)
        await ctx.send("This is not a command! Try again!")
    elif toggle == 'remove':
      if member == None:
        role = discord.utils.get(ctx.guild.roles, id=id1)
        await ctx.message.delete()
        await ctx.author.remove_roles(role)
        await ctx.send("This is not a command! Try again!")
      else:
        role = discord.utils.get(ctx.guild.roles, id=id1)
        await ctx.message.delete()
        await member.remove_roles(role)
        await ctx.send("This is not a command! Try again!")

def setup(bot):
  bot.add_cog(owner(bot))
