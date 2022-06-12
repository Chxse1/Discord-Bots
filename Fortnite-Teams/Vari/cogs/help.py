import discord
from main import embed_color, hashtag
from discord.ext import commands

class help(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def help(self, ctx):
    embed = discord.Embed(title="Help!", description="Here is a list of help menus you can use!", color=embed_color)
    embed.add_field(name="`a!Help`", value="Shows this message!", inline=True)
    embed.add_field(name="`a!Moderation`", value="Shows moderation commands!", inline=True)
    embed.add_field(name="`a!Fun`", value="Shows fun commands!", inline=True)
    embed.add_field(name="`a!Utility`", value="Shows utility commands!", inline=True)
    embed.add_field(name="`a!Customs`", value="Shows the custom commads!", inline=True)
    embed.add_field(name="`a!Owner`", value="Shows owner commands!", inline=True)
    embed.set_author(name=hashtag)
    embed.set_footer(text=f"Requested by {ctx.author}!")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    print(f"{ctx.author} used the help command | {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command(aliases=['customs'])
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def custom(self, ctx):
    embed = discord.Embed(title="Help!", description="Here is a list of custom commands!", color=embed_color)
    embed.add_field(name="`Fuck`", value="Fuck a specified user!", inline=True)
    embed.set_author(name=hashtag)
    embed.set_footer(text=f"Requested by {ctx.author}!")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    print(f"{ctx.author} used the custom command | {ctx.channel}")
    await ctx.message.reply(embed=embed)


  @commands.command(aliases=['mod'])
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def moderation(self, ctx):
    embed=discord.Embed(title="Moderation Help", description="This is a list of moderation commands you can use!", color=embed_color)
    embed.add_field(name="`Kick`", value="Kicks a specified user!", inline=True)
    embed.add_field(name="`Ban`", value="Bans a specified user!", inline=True)
    embed.add_field(name="`Purge`", value="Purges a certain amount of messages!", inline=True)
    embed.add_field(name="`Mute`", value="Mutes the specified user!", inline=True)
    embed.add_field(name="`Unmute`", value="Unmutes the specified user!", inline=True)
    embed.set_author(name=hashtag)
    embed.set_footer(text=f"Requested by {ctx.author}!")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    print(f"{ctx.author} used the moderation command | {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command(aliases=['o'])
  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.is_owner()
  async def owner(self, ctx):
    embed = discord.Embed(title="Owner Help", description="This is the owner help command! Try out some commands!", color=embed_color)
    embed.add_field(name="`Reload`", value="Reloads a cog!", inline=True)
    embed.add_field(name="`Load`", value="Loads a cog!", inline=True)
    embed.add_field(name="`Unload`", value="Unloads a cog!", inline=True)
    embed.add_field(name="`Cogs`", value="Shows you all the cogs!", inline=True)
    embed.set_author(name=hashtag)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    print(f"{ctx.author} used the owner command | {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def fun(self, ctx):
    embed=discord.Embed(title="Fun Commands", description="Here is a list of fun commands!", color=embed_color)
    embed.add_field(name="`Bon`", value="This is a fun command that sends a message showing that a user is banned!", inline=True)
    embed.add_field(name="`Unbon`", value="This is a fun command that sends a message showing that a user is unbanned!", inline=True)
    embed.add_field(name="`Snipe`", value="Snipes a deleted message!", inline=True)
    embed.add_field(name="`RR`", value="Sends an audio file of a rick roll!", inline=True)
    embed.add_field(name="`Mayo`", value="Sends an audio file of mayonnaise on an escalator!", inline=True)
    embed.add_field(name="`Say`", value="Says a specified message!", inline=True)
    embed.set_author(name=hashtag)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    print(f"{ctx.author} used the fun command | {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command(aliases=['util'])
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def utility(self, ctx):
    embed=discord.Embed(title="Utility Commands", description="Here is a list of utility commands!", color=embed_color)
    embed.add_field(name="`Ping`", value="Shows you the bot latency!", inline=True)
    embed.add_field(name="`Serverinfo`", value="Shows you info on this server!", inline=True)
    embed.add_field(name="`Userinfo`", value="Shows you info on the specified user!", inline=True)
    embed.add_field(name="`Membercount`", value="Shows you amount of members in this guild!", inline=True)
    embed.add_field(name="`Bug`", value="Sends a bug you found to the bot dea!", inline=True)
    embed.add_field(name="`Suggest`", value="Sends a suggestion you suggest to the bot dea!", inline=True)
    embed.add_field(name="`Avatar`", value="Shows you the avatar and banner of a specified user!", inline=True)
    embed.add_field(name="`Banner`", value="Shows you the avatar and banner of a specified user!", inline=True)
    embed.add_field(name="`Join`", value="Shows you the how to join message!", inline=True)
    embed.add_field(name="`AFK`", value="Sets you as afk!", inline=True)
    embed.set_author(name=hashtag)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    print(f"{ctx.author} used the utility command | {ctx.channel}")
    await ctx.message.reply(embed=embed)

def setup(bot):
  bot.add_cog(help(bot))
