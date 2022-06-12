import discord
import random
import asyncio
from main import embed_color, hashtag
from discord.ext import commands

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

class fun(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def bon(self, ctx, member : discord.Member = None):
    if member == None:
      await ctx.message.reply("Please specify who to ban!")
    else:
      print(f"{ctx.author} used the bon command | {ctx.channel}")
      await ctx.message.reply(f"`{member}` has been banned!")

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def unbon(self, ctx, member : discord.Member = None):
    if member == None:
      await ctx.message.reply("Please specify who to unban!")
    else:
      print(f"{ctx.author} used the unbon command | {ctx.channel}")
      await ctx.message.reply(f"`{member}` has been unbanned!")

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def rr(self, ctx):
    await ctx.message.delete()
    print(f"{ctx.author} used the rr command | {ctx.channel}")
    await ctx.send(file=discord.File('Audio/cat_meow_compilation.mp3'))

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def mayo(self, ctx):
    await ctx.message.delete()
    print(f"{ctx.author} used the mayo command | {ctx.channel}")
    await ctx.send(file=discord.File('Audio/AC_DC.mp3'))

  @commands.command(aliases=['gay-scanner', 'gayscanner', 'gay', 'gayrate'])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def howgay(self, ctx, *, user: discord.Member=None):
    if user == None:
        user = ctx.author.name
        gayness = random.randint(0,100)
        gayStatus = random.choice(["No Homo", 
                                "Some Homo", 
                                "Only Sometimes", 
                                "Kinda Gay", 
                                "Gay as Hell", 
                                "Have you even seen a girl?", 
                                "Hella Gay"])
        gayColor = embed_color
        emb = discord.Embed(description=f"Gayness for **{user}**", color=gayColor)
        emb.add_field(name="Gayness:", value=f"`%{gayness}` gay")
        emb.add_field(name="Comment:", value=f"`{gayStatus}`")
        emb.set_author(name=hashtag, icon_url=ctx.author.avatar.url)
        print(f"{ctx.author} used the howgay command | {ctx.channel}")
        await ctx.send(embed=emb)
    else:
        gayness = random.randint(0,100)
        gayStatus = random.choice(["No Homo", 
                                "Some Homo", 
                                "Only Sometimes", 
                                "Kinda Gay", 
                                "Gay as Hell", 
                                "Have you even seen a girl?", 
                                "Hella Gay"])
        gayColor = embed_color
        emb = discord.Embed(description=f"Gayness for **{user}**", color=gayColor)
        emb.add_field(name="Gayness:", value=f"`%{gayness}` gay")
        emb.add_field(name="Comment:", value=f"`{gayStatus}`")
        emb.set_author(name=hashtag, icon_url=user.avatar.url)
        print(f"{ctx.author} used the howgay command | {ctx.channel}")
        await ctx.send(embed=emb)

def setup(bot):
  bot.add_cog(fun(bot))