import discord
import random
import aiohttp
import asyncio
from discord.commands import slash_command
import datetime
from discord.ext import commands
from main import embed_color, hashtag, afk

class slash(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @slash_command(guild_id=938228924796772425, name="gayrate", description="Show you how gay someone is!")
  async def gayrate(self, ctx, user:discord.Member=None):
    if user == None:
      percentage = random.randint(1,100)
      embed=discord.Embed(title="Gayrate", description=f"You are `{percentage}%` gay!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.respond(embed=embed)
    else:
      percentage = random.randint(1,100)
      embed=discord.Embed(title="Gayrate", description=f"{user.mention} is `{percentage}%` gay!", color=embed_color)
      embed.set_thumbnail(url=user.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.respond(embed=embed)

  @slash_command(guild_id=938228924796772425, name="simprate", description="Show you how much of a simp someone is!")
  async def simprate(self, ctx, user:discord.Member=None):
    if user == None:
      percentage = random.randint(1,100)
      embed=discord.Embed(title="Simprate", description=f"You are `{percentage}%` of a simp!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.respond(embed=embed)
    else:
      percentage = random.randint(1,100)
      embed=discord.Embed(title="Simprate", description=f"{user.mention} is `{percentage}%` of a simp!", color=embed_color)
      embed.set_thumbnail(url=user.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.respond(embed=embed)

  @slash_command(guild_id=938228924796772425, name="eightball", description="Gives you an answer to your question!")
  async def eightball(self, ctx, message=None):
    if message == None:
      embed=discord.Embed(title="Error", description="What is your question?", color=embed_color)
      await ctx.respond(embed=embed)
    else:
      list = ['Yes', 'No', 'Maybe', 'Ask Again', 'Hell Yeah', 'Hell No', 'Concentrate and Ask Again', 'Better Not Tell You Now', 'My Sources Say No']
      embed=discord.Embed(title="Eight-Ball", description="Here is my answer to my question!", color=embed_color)
      embed.add_field(name=f"Question: `{message}`", value=f"**Answer: `{random.choice(list)}`**")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.respond(embed=embed)

  @slash_command(guild_id=938228924796772425, name="meme", description="Show you a random meme!")
  async def meme(self, ctx):
    embed=discord.Embed(title="Meme", description="Here is a random meme for you!", color=embed_color)

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.set_footer(text=f"Requested by {ctx.author}")
            embed.set_author(name=hashtag)
            await ctx.respond(embed=embed)

  @slash_command(guild_id=938228924796772425, name="help", description="Show you my commands!")
  async def help(self, ctx, category=None):
    if category == None:
      embed=discord.Embed(title="Help", description="Here is a list of all of my help categories!", color=embed_color)
      embed.add_field(name="`s!help information`", value="This shows you the list of my information commands!", inline=False)
      embed.add_field(name="`s!help moderation`", value="This shows you the list of my moderation commands!", inline=False)
      embed.add_field(name="`s!help fun`", value="This shows you the list of my fun commands!", inline=False)
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.respond(embed=embed)
    elif category == 'moderation' or category == 'mod':
      embed=discord.Embed(title="Moderation", description="Here is a list of my moderation commands!", color=embed_color)
      embed.add_field(name="List of economy commands!", value="`Kick` | `Ban` | `Mute` | `Unmute` | `Purge`")
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.respond(embed=embed)
    elif category == 'info' or category == 'information':
      embed=discord.Embed(title="Information", description="Here is a list of my information commands!", color=embed_color)
      embed.add_field(name="List of economy commands!", value="`Serverinfo` | `Avatar` | `AFK` | `Membercount` | `Snipe` | `Ping`")
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.respond(embed=embed)
    elif category == 'fun':
      embed=discord.Embed(title="Fun", description='Here is a list of all my fun commands!', color=embed_color)
      embed.add_field(name="List of fun commands!", value="`Eightball` | `Simprate` | `Gayrate` | `Meme`")
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.respond(embed=embed)
    else:
      embed=discord.Embed(title="Error", description="This category was not found!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      await ctx.respond(embed=embed)

  @slash_command(guild_id=938228924796772425, name="avatar", description="Show you someones avatar!")
  async def avatar(self, ctx, user:discord.Member=None):
    if user == None:
      embed=discord.Embed(title="Avatar", description=f"Here is {ctx.author.mention}'s avatar!", color=embed_color)
      embed.set_image(url=ctx.author.avatar.url)
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      await ctx.respond(embed=embed)
    else:
      embed=discord.Embed(title="Avatar", description=f"Here is {user.mention}'s avatar!", color=embed_color)
      embed.set_image(url=user.avatar.url)
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      await ctx.respond(embed=embed)

  @slash_command(guild_id=938228924796772425, name="serverinfo", description="Show you information about this server!")
  async def serverinfo(self, ctx):
    embed = discord.Embed(title="Server Info", description=f"{ctx.guild.name}", color=embed_color)
    embed.add_field(name="Owner", value=f'`{ctx.guild.owner}`', inline=False)
    embed.add_field(name="Channels", value=f'`{len(ctx.guild.channels)}`', inline=False)
    embed.add_field(name="Roles", value=f'`{len(ctx.guild.roles)}`', inline=False)
    embed.add_field(name="Server Created", value=f'`{ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p")}`', inline=False)
    embed.add_field(name="Membercount", value=f'`{len(ctx.guild.members)}`', inline=False)
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
    embed.set_author(name=hashtag)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    print(f"{ctx.author} used the serverinfo command | {ctx.channel}")
    await ctx.respond(embed=embed)

  @slash_command(guild_id=938228924796772425, name="afk", description="Sets your AFK!")
  async def afk(self, ctx, *, reason="No Reason Provided"):
        member = ctx.author
        if member.id in afk.keys():
            afk.pop(member.id)
        else:
            try:
                await member.edit(nick=f"[AFK] {member.display_name}")
            except:
                pass
        afk[member.id] = reason
        embed=discord.Embed(title="AFK", description=f"{member.mention} has gone AFK!", color=embed_color)
        embed.add_field(name="Reason", value=f"`{reason}`")
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_author(name=hashtag)
        embed.set_thumbnail(url=ctx.author.avatar.url)
        print(f"{ctx.author} used the afk command | {ctx.channel}")
        await ctx.respond(embed=embed)

  @slash_command(guild_id=938228924796772425, name="membercount", description="Show you the membercount of this guild!")
  async def membercount(self, ctx):
    embed=discord.Embed(title="Membercount", description="Here is the amount of members in your server!", color=embed_color)
    embed.add_field(name="Members:", value=f"`{len(ctx.guild.members)}`")
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
    embed.set_author(name=hashtag)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)

  @slash_command(guild_id=938228924796772425, name="ping", description="Show you the bot latency!")
  async def ping(self, ctx):
    embed=discord.Embed(title="Ping", description="Here is my latency!", color=embed_color)
    embed.add_field(name="Latency:", value=f"`{round(self.bot.latency * 1000)}`ms")
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
    embed.set_author(name=hashtag)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)

  @slash_command(guild_id=938228924796772425, name="kick", description="Kick a specified user!")
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member = None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a user for me to kick!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.respond(embed=embed)
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
      await ctx.respond(embed=embed)
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
      await ctx.respond(embed=embed)
      await ctx.guild.kick(member, reason=reason)

  @slash_command(guild_id=938228924796772425, name="ban", description="Ban a specified user!")
  @commands.has_permissions(ban_members = True)
  async def ban(self, ctx, member:discord.Member=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error!", description="Please specify a user for me to ban!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.respond(embed=embed)
      return
    elif member.id == ctx.author.id:
      embed=discord.Embed(title="Error!", description="You can't ban yourself!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.respond(embed=embed)
      return
    elif member.top_role >= ctx.author.top_role:
      embed=discord.Embed(title="Error", description="You can't ban someone with a higher role than you!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.respond(embed=embed)         
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

      await ctx.respond(embed=embed)
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
      await ctx.respond(embed=embed)
      await member.send(embed=embed2)
      await ctx.guild.ban(member, reason = f"Ban Command Used By {ctx.author.name}#{ctx.author.discriminator} | Reason: {reason}")

  @slash_command(guild_id=938228924796772425, name="mute", description="Mute a specified user!")
  @commands.has_permissions(moderate_members=True)
  async def mute(self, ctx, member: discord.Member=None, minutes: int=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a member for me to mute!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.respond(embed=embed)
      return
    elif minutes == None:
      embed=discord.Embed(title="Error", description="Please specify how many minutes you want this user muted!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.respond(embed=embed)
    elif reason == None:
      duration = datetime.timedelta(minutes=minutes)
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been timed out for `{minutes}` minutes!", value=f"Reason: `No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.timeout_for(duration, reason="No Reason Provided")
      await ctx.respond(embed=embed)
    else:
      duration = datetime.timedelta(minutes=minutes)
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been timed out for `{minutes}` minutes!", value=f"Reason: `{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.timeout_for(duration, reason=reason)
      await ctx.respond(embed=embed)

  @slash_command(guild_id=938228924796772425, name="unmute", description="Mute a specified user!")
  async def unmute(self, ctx, member:discord.Member=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a member for me to mute!", color=embed_color)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.respond(embed=embed)
      return
    elif reason == None:
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been unmuted!", value=f"Reason: `No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.remove_timeout(reason="No Reason Provided")
      await ctx.respond(embed=embed)
    else:
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been unmuted!", value=f"Reason: `{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.remove_timeout(reason=reason)
      await ctx.respond(embed=embed)
      
  @slash_command(guild_id=938228924796772425, name="purge", description="Purge the specified amount of messages!")
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, limit:int=None):
    if limit == None:
      embed=discord.Embed(title="Error", description="Please specify how many messages to purge!", color=embed_color)
      await ctx.respond(embed=embed)
    elif limit > 100:
      embed=discord.Embed(title="Error", description="I can not purge this amount of messages!", color=embed_color)
      await ctx.respond(embed=embed)
    else:
      embed= discord.Embed(title="Purge", description=f"`{limit}` message(s) have been purged!")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await ctx.channel.purge(limit=limit + 1)
      await ctx.respond(embed=embed)

def setup(bot):
  bot.add_cog(slash(bot))