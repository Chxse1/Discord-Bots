import discord
import datetime
from main import embed_color, hashtag
from discord.ext import commands

class moderation(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member = None, *, reason:str=None):
    if member == None:
      await ctx.message.reply("Please specify a user for me to kick!")
      return
    elif reason == None:
      reason = "No Reason Provided"
      embed = discord.Embed(title="User Kicked",
		                    description=f"{member.mention} has been kicked!",
		                    color=embed_color)
      embed.add_field(name="Reason:", value=f"`{reason}`")
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Kicked by {ctx.author}.")
      await ctx.guild.kick(member)
      print(f"{ctx.author} used the kick command | {ctx.channel}")
      await ctx.message.reply(embed=embed)
      return
    else:
      embed=discord.Embed(title="User Kicked", description=f"{member.mention} has been kicked!", color=embed_color)
      embed.add_field(name="Reason:", value=f"`{reason}`")
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Kicked by {ctx.author}.")
      await ctx.guild.kick(member)
      print(f"{ctx.author} used the kick command | {ctx.channel}")
      await ctx.message.reply(embed=embed)

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member = None, *, reason:str=None):
    if member == None:
      await ctx.message.reply("Please specify a user for me to ban!")
      return
    if reason == None:
      reason = "No Reason Provided"
      embed = discord.Embed(title="User Banned",
		                    description=f"{member.mention} has been banned!",
		                    color=embed_color)
      embed.add_field(name="Reason:", value=f"`{reason}`")
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Banned by {ctx.author}.")
      await ctx.message.reply(embed=embed)
      print(f"{ctx.author} used the ban command | {ctx.channel}")
      await ctx.guild.ban(member, reason=reason)
    else:
      embed=discord.Embed(title="User Banned", description=f"{member.mention} has been banned!", color=embed_color)
      embed.add_field(name="Reason:", value=f"`{reason}`")
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Banned by {ctx.author}.")
      await ctx.message.reply(embed=embed)
      print(f"{ctx.author} used the ban command | {ctx.channel}")
      await ctx.member.ban(reason=reason)

  @commands.command(pass_context=True, hidden=True)
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, limit: int):
      embed=discord.Embed(title="Success", description=f"Purged `{limit}` messages!", color=embed_color)
      await ctx.channel.purge(limit=limit + 1)
      print(f"{ctx.author} used the purge command | {ctx.channel}")
      await ctx.send(embed=embed)

  @commands.command(aliases=['mute'])
  @commands.cooldown(1,10, commands.BucketType.user)
  @commands.has_permissions(moderate_members=True)
  async def timeout(self, ctx, member: discord.Member=None, minutes: int=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a member for me to mute!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      return
    elif minutes == None:
      embed=discord.Embed(title="Error", description="Please specify how many minutes you want this user muted!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
    elif reason == None:
      duration = datetime.timedelta(minutes=minutes)
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been timed out for `{minutes}` minutes!", value=f"Reason: `No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_footer(text=f"Requested by {ctx.author}")
      await member.timeout_for(duration, reason="No Reason Provided")
      print(f"{ctx.author} used the mute command | {ctx.channel}")
      await ctx.reply(embed=embed)
    else:
      duration = datetime.timedelta(minutes=minutes)
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been timed out for `{minutes}` minutes!", value=f"Reason: `{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.timeout_for(duration, reason=reason)
      print(f"{ctx.author} used the mute command | {ctx.channel}")
      await ctx.reply(embed=embed)

  @commands.command(aliases=['untimeout'])
  @commands.cooldown(1,10, commands.BucketType.user)
  async def unmute(self, ctx, member:discord.Member=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a member for me to mute!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      return
    elif reason == None:
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been unmuted!", value=f"Reason: `No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.remove_timeout(reason="No Reason Provided")
      print(f"{ctx.author} used the unmute command | {ctx.channel}")
      await ctx.reply(embed=embed)
    else:
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been unmuted!", value=f"Reason: `{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.remove_timeout(reason=reason)
      print(f"{ctx.author} used the unmute command | {ctx.channel}")
      await ctx.reply(embed=embed)

def setup(bot):
  bot.add_cog(moderation(bot))
