import discord
from discord.ext import commands
from main import embed_color, hashtag

class help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.cooldown(1,1.5, commands.BucketType.user)
  async def help(self, ctx, category=None):
    if category == None:
      embed=discord.Embed(title="Help", description="Here is a list of all of my help categories!", color=embed_color)
      embed.add_field(name="`s!help information`", value="This shows you the list of my information commands!", inline=False)
      embed.add_field(name="`s!help moderation`", value="This shows you the list of my moderation commands!", inline=False)
      embed.add_field(name="`s!help fun`", value="This shows you the list of my fun commands!", inline=False)
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
    elif category == 'moderation' or category == 'mod':
      embed=discord.Embed(title="Moderation", description="Here is a list of my moderation commands!", color=embed_color)
      embed.add_field(name="List of economy commands!", value="`Kick` | `Ban` | `Mute` | `Unmute` | `Purge`")
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
    elif category == 'info' or category == 'information':
      embed=discord.Embed(title="Information", description="Here is a list of my information commands!", color=embed_color)
      embed.add_field(name="List of economy commands!", value="`Serverinfo` | `Avatar` | `AFK` | `Membercount` | `Snipe` | `Ping`")
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
    elif category == 'fun':
      embed=discord.Embed(title="Fun", description='Here is a list of all my fun commands!', color=embed_color)
      embed.add_field(name="List of fun commands!", value="`8Ball` | `Simprate` | `Gayrate` | `Memes`")
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
    else:
      embed=discord.Embed(title="Error", description="This category was not found!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      await ctx.reply(embed=embed)

def setup(bot):
  bot.add_cog(help(bot))