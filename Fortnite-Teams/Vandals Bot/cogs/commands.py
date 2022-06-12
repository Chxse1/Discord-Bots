import discord
import datetime
import json
from colorama import Fore as Color
from discord.ext import commands
from discord.utils import get
from afks import afks

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

class commands(commands.Cog):
  def __init__(self,bot:commands.Bot):
      self.bot = bot

  @commands.command()
  @commands.cooldown(1,5, commands.BucketType.user)
  async def help(self, ctx):
    embed=discord.Embed(title="Help", description="Here is a list of my commands!", color=0x2140DA)
    embed.add_field(name="Moderation", value="`Kick` | `Ban` | `Mute` | `Warn`", inline=False)
    embed.add_field(name="Utility", value="`Lock` | `Unlock` | `Purge`", inline=False)
    embed.add_field(name="Economy", value="`Balance` | `Beg` | `Withdraw` | `Deposit` | `Send` | `Rob`", inline=False)
    embed.add_field(name="Fun", value="`Say` | `AFK`", inline=False)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Kicked by {ctx.author}.")
    embed.set_author(name="#VandalsOT")
    await ctx.message.reply(embed=embed)

  @commands.command(pass_context=True)
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, limit: int):
    embed = discord.Embed(title="Purged!", description=f"`{limit}` messages have been purged.", color=0x2140DA)
    embed.set_author(name="#VandalsOT")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Purged By {ctx.author}")
    await ctx.channel.purge(limit=limit)
    await ctx.send(embed=embed)

  @commands.cooldown(1,5, commands.BucketType.user)
  async def say(self, ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

  @commands.command(aliases=['ul'])
  @commands.has_permissions(manage_channels=True)
  async def unlock(self, ctx, channel: discord.TextChannel = None):
    role = discord.utils.get(ctx.author.guild.roles, id=812860928877264946)
    overwrite = ctx.channel.overwrites_for(role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(role, overwrite=overwrite)
    embed = discord.Embed(title='Unlock', description=f'Unlocked `{ctx.channel.name}`!')
    embed.set_author(name="#VandalsOT")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Unlocked by {ctx.author}.")
    await ctx.message.reply(embed=embed)

  @commands.command(aliases=['l'])
  @commands.has_permissions(manage_channels=True)
  async def lock(self, ctx, channel: discord.TextChannel = None):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(title='Lock', description=f'Locked `{ctx.channel.name}`!')
    embed.set_author(name="#VandalsOT")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Locked by {ctx.author}.")
    await ctx.message.reply(embed=embed)

  @commands.command(aliases=['mute'])
  @commands.cooldown(1,10, commands.BucketType.user)
  @commands.has_permissions(moderate_members=True)
  async def timeout(self, ctx, member: discord.Member=None, minutes: int=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a member for me to mute!", color=0x2140DA)
      await ctx.reply(embed=embed)
      return
    elif minutes == None:
      embed=discord.Embed(title="Error", description="Please specify how many minutes you want this user muted!", color=0x2140DA)
      await ctx.reply(embed=embed)
    elif reason == None:
      duration = datetime.timedelta(minutes=minutes)
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=0x2140DA)
      embed.add_field(name=f"{member} has been timed out for `{minutes}` minutes!", value=f"Reason: `No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name="#VandalsOT")
      await member.timeout_for(duration, reason="No Reason Provided")
      await ctx.reply(embed=embed)
      return
    duration = datetime.timedelta(minutes=minutes)
    embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=0x2140DA)
    embed.add_field(name=f"{member} has been timed out for `{minutes}` minutes!", value=f"Reason: `{reason}`")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_author(name="#VandalsOT")
    embed.set_footer(text=f"Requested by {ctx.author}")
    await member.timeout_for(duration, reason=reason)
    await ctx.reply(embed=embed)

  @commands.command(aliases=['untimeout'])
  @commands.cooldown(1,10, commands.BucketType.user)
  async def unmute(self, ctx, member:discord.Member=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a member for me to mute!", color=0x2140DA)
      await ctx.reply(embed=embed)
      return
    elif reason == None:
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=0x2140DA)
      embed.add_field(name=f"{member} has been unmuted!", value=f"Reason: `No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name="#VandalsOT")
      await member.remove_timeout(reason="No Reason Provided")
      await ctx.reply(embed=embed)
      return
    embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=0x2140DA)
    embed.add_field(name=f"{member} has been unmuted!", value=f"Reason: `{reason}`")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_author(name="#VandalsOT")
    embed.set_footer(text=f"Requested by {ctx.author}")
    await member.remove_timeout(reason=reason)
    await ctx.reply(embed=embed)

  @commands.command()
  @commands.cooldown(1,15, commands.BucketType.user)
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member = None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a user for me to kick!", color=0x2140DA)
      await ctx.reply(embed=embed)
      return
    if reason == None:
      embed = discord.Embed(title="User Kicked", description=f"{member.mention} has been kicked. ", color=0x2140DA)
      embed.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Kicked by {ctx.author}.")
      embed.set_author(name="#VandalsOT")

      embed2 = discord.Embed(title="Kicked", description=f"You have been kicked from `{ctx.guild.name}` by `{ctx.author}`.", color=0x2140DA)
      embed2.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed2.set_footer(text=f"Kicked by {ctx.author}.")
      embed.set_author(name="#VandalsOT")
      await member.send(embed=embed2)
      await ctx.reply(embed=embed)
      await ctx.guild.kick(member)
      return
    embed = discord.Embed(title="User Kicked", description=f"{member.mention} has been kicked. ", color=0x2140DA)
    embed.add_field(name="Reason:", value=f"`{reason}`")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Kicked by {ctx.author}.")
    embed.set_author(name="#VandalsOT")

    embed2 = discord.Embed(title="Kicked", description=f"You have been kicked from `{ctx.guild.name}` by `{ctx.author}`.", color=0x2140DA)
    embed2.add_field(name="Reason:", value=f"`{reason}`")
    embed2.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_author(name="#VandalsOT")
    embed2.set_footer(text=f"Kicked by {ctx.author}.")
    await member.send(embed=embed2)
    await ctx.reply(embed=embed)
    await ctx.guild.kick(member)

  @commands.command()
  @commands.has_permissions(ban_members = True)
  @commands.cooldown(1,15, commands.BucketType.user)
  async def ban(self, ctx, member:discord.Member=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error!", description="Please specify a user for me to ban!", color=0x2140DA)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      return
    elif member.id == ctx.author.id:
      embed=discord.Embed(title="Error!", description="You can't ban yourself!", color=0x2140DA)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      return
    elif member.top_role >= ctx.author.top_role:
      embed=discord.Embed(title="Error", description="You can't ban someone with a higher role than you!", color=0x2140DA)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)         
      return
    elif reason == None:
      embed = discord.Embed(title="User Banned", description=f"{member.mention} has been banned. ", color=0x2140DA)
      embed.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Banned by {ctx.author}.")
      embed.set_author(name="#VandalsOT")

      embed2 = discord.Embed(title="Banned", description=f"You have been banned from `{ctx.guild.name}` by `{ctx.author}`.", color=0x2140DA)
      embed2.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed2.set_footer(text=f"Kicked by {ctx.author}.")
      embed.set_author(name="#VandalsOT")

      await ctx.reply(embed=embed)
      await member.ban(reason = f"Ban Command Used By {ctx.author.name}#{ctx.author.discriminator} | Reason: No Reason Provided")
    else: 
      embed = discord.Embed(title="User Banned", description=f"{member.mention} has been banned.", color=0x2140DA)
      embed.add_field(name="Reason:", value=f"`{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Banned by {ctx.author}.")
      embed.set_author(name="#VandalsOT")

      embed2 = discord.Embed(title="Banned", description=f"You have been banned from `{ctx.guild.name}` by `{ctx.author}`.", color=0x2140DA)
      embed2.add_field(name="Reason:", value=f"`{reason}`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_author(name="#VandalsOT")
      embed2.set_footer(text=f"Banned by {ctx.author}.")
      await ctx.reply(embed=embed)
      await member.send(embed=embed2)
      await member.ban(reason = f"Ban Command Used By {ctx.author.name}#{ctx.author.discriminator} | Reason: {reason}")

  @commands.command()
  @commands.cooldown(1,10, commands.BucketType.user)
  async def afk(self, ctx, *, reason="No Reason Provided"):
      member = ctx.author
      if member.id in afks.keys():
          afks.pop(member.id)
      else:
          try:
              await member.edit(nick=f"[AFK] {member.display_name}")
          except:
              pass
      afks[member.id] = reason
      embed=discord.Embed(title="AFK", description=f"{member.mention} has gone AFK!", color=0x2140DA)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name="#VandalsOT")
      embed.add_field(name="Reason", value=f"`{reason}`")
      await ctx.send(embed=embed)

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.has_permissions(view_audit_log=True)
  async def warn(self,ctx,user:discord.User=None,*reason:str):
    if user == None:
      embed=discord.Embed(title="Error...", description="No User Specified...", color=0x2140DA)
      embed.add_field(name="Please specify the user being warned.", value="Ex: `v!warn <User> <Reason>`")
      embed.set_author(name="#VandalsOT")
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.set_footer(text=f"Requested By {ctx.author}")
      await ctx.message.reply(embed=embed)
      return
    if not reason:
      embed=discord.Embed(title="Error...", description="No Arguments Given...", color=0x2140DA)
      embed.add_field(name="Please specify what the reason is for.", value="Ex: `v!warn <User> <Reason>`")
      embed.set_author(name="#VandalsOT")
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
      json.dump(report,f, indent=4)
    embed1=discord.Embed(title="Warned", description=f"`{user.name}#{user.discriminator}` has been warned!", color=0x2140DA)
    embed1.add_field(name="Reason:", value=f"`{reason}`")
    embed1.set_author(name="#VandalsOT")
    embed1.set_thumbnail(url=ctx.author.avatar_url)
    embed1.set_footer(text=f"Warned by {ctx.author}")
    await ctx.message.reply(embed=embed1)

    embed2=discord.Embed(title="Warned", description="You have been warned.", color=0x2140DA)
    embed2.add_field(name=f"You have been warned in `{ctx.guild.name}` by `{ctx.author.name}#{ctx.author.discriminator}`.", value=f"Reason: `{reason}`")
    embed2.set_author(name="#VandalsOT")
    embed2.set_thumbnail(url=ctx.author.avatar_url)
    embed2.set_footer(text=f"Warned by {ctx.author}")
    await user.send(embed=embed2)

  @commands.command(aliases=['warnings'])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def warns(self,ctx,user:discord.User):
    for current_user in report['users']:
      if user.name == current_user['name']:
        embed = discord.Embed(title="Warnings", description=f"`{user.name}#{user.discriminator}` has `{len(current_user['reasons'])}` warning(s).", color=0x2140DA)
        embed.add_field(name="Warnings:", value=f"`{'`, `'.join(current_user['reasons'])}`")
        embed.set_author(name="#VandalsOT")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested By {ctx.author}")
        await ctx.message.reply(embed=embed)
        break
    else:
        embed = discord.Embed(title="Warnings", description=f"`{user.name}#{user.discriminator}` has `0` warnings.", color=0x2140DA)
        embed.add_field(name="Warnings:", value=f"`None`")
        embed.set_author(name="#VandalsOT")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested By {ctx.author}")
        await ctx.message.reply(embed=embed)

def setup(bot):
  bot.add_cog(commands(bot))