import discord
import asyncio
from discord.ext import commands
from discord.utils import get
from main import embed_color, hashtag, afk

def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

class information(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['av'])
  @commands.cooldown(1,3, commands.BucketType.user)
  async def avatar(self, ctx, user:discord.Member=None):
    if user == None:
      embed=discord.Embed(title="Avatar", description=f"Here is {ctx.author.mention}'s avatar!", color=embed_color)
      embed.set_image(url=ctx.author.avatar.url)
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      await ctx.reply(embed=embed)
    else:
      embed=discord.Embed(title="Avatar", description=f"Here is {user.mention}'s avatar!", color=embed_color)
      embed.set_image(url=user.avatar.url)
      embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
      embed.set_author(name=hashtag)
      await ctx.reply(embed=embed)

  @commands.command(aliases=["si"])
  @commands.cooldown(1, 3, commands.BucketType.user)
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
    await ctx.message.reply(embed=embed)

  @commands.Cog.listener()
  async def on_message(self, message):
        if message.author.id in afk.keys():
            afk.pop(message.author.id)
            try:
                await message.author.edit(nick = remove(message.author.display_name))
            except:
                pass
            embed=discord.Embed(title="AFK", description=f"Welcome back {message.author.mention}, I removed your AFK!", color=embed_color)
            embed.set_footer(text=message.author.name, icon_url=message.author.avatar.url)
            embed.set_author(name=hashtag)
            embed.set_thumbnail(url=message.author.avatar.url)
            await message.channel.send(embed=embed)

        for id, reason in afk.items():
            member = get(message.guild.members, id = id)
            if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
               embed=discord.Embed(title="AFK", description=f"{member.name} is AFK! Reason: `{reason}`", color=embed_color)
               await message.channel.send(embed=embed)

  @commands.command()
  @commands.cooldown(1,5, commands.BucketType.user)
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
        await ctx.send(embed=embed)

  @commands.command(aliases=['mc'])
  @commands.cooldown(1,3, commands.BucketType.user)
  async def membercount(self, ctx):
    embed=discord.Embed(title="Membercount", description="Here is the amount of members in your server!", color=embed_color)
    embed.add_field(name="Members:", value=f"`{len(ctx.guild.members)}`")
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
    embed.set_author(name=hashtag)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.reply(embed=embed)

  @commands.command()
  @commands.cooldown(1,3, commands.BucketType.user)
  async def ping(self, ctx):
    embed=discord.Embed(title="Ping", description="Here is my latency!", color=embed_color)
    embed.add_field(name="Latency:", value=f"`{round(self.bot.latency * 1000)}`ms")
    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar.url)
    embed.set_author(name=hashtag)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.reply(embed=embed)

def setup(bot):
  bot.add_cog(information(bot))