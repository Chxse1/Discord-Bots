import discord
import sys
import os
from discord.ext import commands
from main import embed_color

def restart_bot():
  os.execv(sys.executable, ["python3"] + sys.argv)

class owner(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command(aliases=['res'])
  @commands.is_owner()
  async def restart(self, ctx):
    print(f"{ctx.author} used the restart command | {ctx.channel}")
    await ctx.message.reply("Restarting! Please Wait...")
    restart_bot()

  @commands.command(hidden=True, aliases=['rel'])
  @commands.is_owner()
  async def reload(self, ctx, cog):
    if cog == "all":
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    self.bot.unload_extension(f"cogs.{filename[:-3]}")
                    self.bot.load_extension(f"cogs.{filename[:-3]}")
                    print(f"{ctx.author} used the reload command | {ctx.channel}")
                    await ctx.message.reply(f"`{filename[:-3]}` was Successfully Reloaded!")
                except:
                    self.bot.load_extension(f"cogs.{filename[:-3]}")
                    self.bot.unload_extension(f"cogs.{filename[:-3]}")
                    self.bot.load_extension(f"cogs.{filename[:-3]}")
                    print(f"{ctx.author} used the reload command | {ctx.channel}")
                    await ctx.message.reply(f"`{filename[:-3]}` was Successfully Loaded and Reloaded!")
    else:
        try:
            self.bot.unload_extension(f"cogs.{cog}")
            self.bot.load_extension(f"cogs.{cog}")
            print(f"{ctx.author} used the reload command | {ctx.channel}")
            await ctx.message.reply(f"`{cog}` was Successfully Reloaded!")
        except:
            self.bot.load_extension(f"cogs.{cog}")
            self.bot.unload_extension(f"cogs.{cog}")
            self.bot.load_extension(f"cogs.{cog}")
            print(f"{ctx.author} used the reload command | {ctx.channel}")
            await ctx.message.reply(f"`{cog}` was Successfully Loaded and Reloaded")

  @commands.command(aliases=["cg"])
  @commands.is_owner()
  async def cogs(self, ctx):
    cogs = []
    for cog in self.bot.cogs:
        cogs.append(cog)
    embed = discord.Embed(
		title="**Cog Names**",
		description="*Here are the names of the current cogs.*",
		color=embed_color)
    embed.add_field(name="**My Cogs:**", value=f"`{'`, `'.join(cogs)}`")
    embed.set_footer(
		text="This is an Owner-Only Command, meaning you can't use it!")
    print(f"{ctx.author} used the cogs command | {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command(hidden=True)
  @commands.is_owner()
  async def unload(self, ctx, cog):
    if cog == "owner":
      await ctx.reply("NO")
    else:
      try:
          self.bot.unload_extension(f"cogs.{cog}")
          print(f"{ctx.author} used the unload command | {ctx.channel}")
          await ctx.message.reply(f"`{cog}` was Successfully Unloaded!")
      except:
          await ctx.message.reply(f"`{cog}` isn't Loaded or doesn't exist!")


  @commands.command(hidden=True)
  @commands.is_owner()
  async def load(self, ctx, cog):
    try:
        self.bot.load_extension(f"cogs.{cog}")
        print(f"{ctx.author} used the load command | {ctx.channel}")
        await ctx.message.reply(f"`{cog}` was Successfully Loaded!")
    except:
        await ctx.message.reply(f"`{cog}` isn't Unloaded or doesn't exist!") 

def setup(bot):
  bot.add_cog(owner(bot))
