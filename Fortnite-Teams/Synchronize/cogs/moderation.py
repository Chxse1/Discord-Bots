import discord
import datetime
from discord.ext import commands
from main import embed_color, hashtag

class moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.cooldown(1,15, commands.BucketType.user)
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member = None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a user for me to kick!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      return
    if reason == None:
      embed = discord.Embed(title="User Kicked", description=f"{member.mention} has been kicked. ", color=embed_color)
      embed.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_footer(text=f"Kicked by {ctx.author}.")

      embed2 = discord.Embed(title="Kicked", description=f"You have been kicked from `{ctx.guild.name}` by `{ctx.author}`.", color=embed_color)
      embed2.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed2.set_author(name=hashtag)
      embed2.set_footer(text=f"Kicked by {ctx.author}.")
      await member.send(embed=embed2)
      await ctx.reply(embed=embed)
      await ctx.guild.kick(member,reason="No Reason Provided")
    else:
      embed = discord.Embed(title="User Kicked", description=f"{member.mention} has been kicked. ", color=embed_color)
      embed.add_field(name="Reason:", value=f"`{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_footer(text=f"Kicked by {ctx.author}.")

      embed2 = discord.Embed(title="Kicked", description=f"You have been kicked from `{ctx.guild.name}` by `{ctx.author}`.", color=embed_color)
      embed2.add_field(name="Reason:", value=f"`{reason}`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed2.set_author(name=hashtag)
      embed2.set_footer(text=f"Kicked by {ctx.author}.")
      await member.send(embed=embed2)
      await ctx.reply(embed=embed)
      await ctx.guild.kick(member, reason=reason)

  @commands.command()
  @commands.has_permissions(ban_members = True)
  @commands.cooldown(1,15, commands.BucketType.user)
  async def ban(self, ctx, member:discord.Member=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error!", description="Please specify a user for me to ban!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      return
    elif member.id == ctx.author.id:
      embed=discord.Embed(title="Error!", description="You can't ban yourself!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      return
    elif member.top_role >= ctx.author.top_role:
      embed=discord.Embed(title="Error", description="You can't ban someone with a higher role than you!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)         
      return
    elif reason == None:
      embed = discord.Embed(title="User Banned", description=f"{member.mention} has been banned. ", color=embed_color)
      embed.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_footer(text=f"Banned by {ctx.author}.")

      embed2 = discord.Embed(title="Banned", description=f"You have been banned from `{ctx.guild.name}` by `{ctx.author}`.", color=embed_color)
      embed2.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed2.set_author(name=hashtag)
      embed2.set_footer(text=f"Kicked by {ctx.author}.")

      await ctx.reply(embed=embed)
      await ctx.guild.ban(member, reason = f"Ban Command Used By {ctx.author.name}#{ctx.author.discriminator} | Reason: No Reason Provided")
    else: 
      embed = discord.Embed(title="User Banned", description=f"{member.mention} has been banned.", color=embed_color)
      embed.add_field(name="Reason:", value=f"`{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_footer(text=f"Banned by {ctx.author}.")

      embed2 = discord.Embed(title="Banned", description=f"You have been banned from `{ctx.guild.name}` by `{ctx.author}`.", color=embed_color)
      embed2.add_field(name="Reason:", value=f"`{reason}`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed2.set_footer(text=f"Banned by {ctx.author}.")
      await ctx.reply(embed=embed)
      await member.send(embed=embed2)
      await ctx.guild.ban(member, reason = f"Ban Command Used By {ctx.author.name}#{ctx.author.discriminator} | Reason: {reason}")

  @commands.command(aliases=['timeout'])
  @commands.cooldown(1,5, commands.BucketType.user)
  @commands.has_permissions(moderate_members=True)
  async def mute(self, ctx, member: discord.Member=None, minutes: int=None, *, reason=None):
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
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.timeout_for(duration, reason="No Reason Provided")
      await ctx.reply(embed=embed)
    else:
      duration = datetime.timedelta(minutes=minutes)
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been timed out for `{minutes}` minutes!", value=f"Reason: `{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.timeout_for(duration, reason=reason)
      await ctx.reply(embed=embed)

  @commands.command(aliases=['untimeout'])
  @commands.cooldown(1,5, commands.BucketType.user)
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
      await ctx.reply(embed=embed)
    else:
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been unmuted!", value=f"Reason: `{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.remove_timeout(reason=reason)
      await ctx.reply(embed=embed)
      
  @commands.command(aliases=['clear'])
  @commands.cooldown(1,5, commands.BucketType.user)
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, limit:int=None):
    if limit == None:
      embed=discord.Embed(title="Error", description="Please specify how many messages to purge!", color=embed_color)
      await ctx.send(embed=embed)
    elif limit > 100:
      embed=discord.Embed(title="Error", description="I can not purge this amount of messages!", color=embed_color)
      await ctx.send(embed=embed)
    else:
      embed= discord.Embed(title="Purge", description=f"`{limit}` message(s) have been purged!")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.channel.purge(limit=limit + 1)
      await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(moderation(bot))