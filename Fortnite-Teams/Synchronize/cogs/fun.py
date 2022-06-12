import discord
import random
import aiohttp
from discord.ext import commands
from main import embed_color, hashtag

class fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['gay-rate', 'how-gay', 'howgay', 'gay'])
  @commands.cooldown(1,3, commands.BucketType.user)
  async def gayrate(self, ctx, user:discord.Member=None):
    if user == None:
      percentage = random.randint(1,100)
      embed=discord.Embed(title="Gayrate", description=f"You are `{percentage}%` gay!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.reply(embed=embed)
    else:
      percentage = random.randint(1,100)
      embed=discord.Embed(title="Gayrate", description=f"{user.mention} is `{percentage}%` gay!", color=embed_color)
      embed.set_thumbnail(url=user.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.reply(embed=embed)

  @commands.command(aliases=['simp-rate', 'how-simp', 'howsimp', 'simp'])
  @commands.cooldown(1,3,commands.BucketType.user)
  async def simprate(self, ctx, user:discord.Member=None):
    if user == None:
      percentage = random.randint(1,100)
      embed=discord.Embed(title="Simprate", description=f"You are `{percentage}%` of a simp!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.reply(embed=embed)
    else:
      percentage = random.randint(1,100)
      embed=discord.Embed(title="Simprate", description=f"{user.mention} is `{percentage}%` of a simp!", color=embed_color)
      embed.set_thumbnail(url=user.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.reply(embed=embed)

  @commands.command(aliases=['8ball', '8-ball', 'eight-ball'])
  @commands.cooldown(1,3, commands.BucketType.user)
  async def eightball(self, ctx, message=None):
    if message == None:
      embed=discord.Embed(title="Error", description="What is your question?", color=embed_color)
      await ctx.reply(embed=embed)
    else:
      list = ['Yes', 'No', 'Maybe', 'Ask Again', 'Hell Yeah', 'Hell No', 'Concentrate and Ask Again', 'Better Not Tell You Now', 'My Sources Say No']
      embed=discord.Embed(title="8Ball", description="Here is my answer to my question!", color=embed_color)
      embed.add_field(name=f"Question: `{message}`", value=f"**Answer: `{random.choice(list)}`**")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.reply(embed=embed)

  @commands.command(aliases=['memes'])
  @commands.cooldown(1,3,commands.BucketType.user)
  async def meme(self, ctx):
    embed=discord.Embed(title="Meme", description="Here is a random meme for you!", color=embed_color)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.set_footer(text=f"Requested by {ctx.author}")
            embed.set_author(name=hashtag)
            await ctx.reply(embed=embed)

def setup(bot):
  bot.add_cog(fun(bot))