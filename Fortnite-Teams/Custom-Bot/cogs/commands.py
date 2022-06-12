import discord
import datetime
from discord.ext import commands
from discord.utils import get
from afks import afks

class Commands(commands.Cog):
  def __init__(self,bot:commands.Bot):
      self.bot = bot

  @commands.command()
  @commands.cooldown(1,3, commands.BucketType.user)
  async def help(self, ctx):
    embed=discord.Embed(title="Help", description="Here is a list of all of my commands!", color=0xFFFFFF)
    embed.add_field(name="`Help`", value="Shows this message!")
    embed.add_field(name="`AFK`", value="Sets you as afk!")
    embed.add_field(name="`Ban`", value="Bans the specified user!")
    embed.add_field(name="`Kick`", value="Kicks the specified user!")
    embed.add_field(name="`Mute`", value="Mutes a specified user!")
    embed.add_field(name="`Unmute`", value="Unmutes a specified user!")
    embed.add_field(name="`Embed`", value="Puts your message in an embed!")
    embed.add_field(name="`Suggest`", value="Adds your suggestion!")
    embed.add_field(name="`Balance`", value="Shows your balance!")
    embed.add_field(name="`Beg`", value="Begs people for coins!")
    embed.add_field(name="`Withdraw`", value="Withdraws coins from the bank!")
    embed.add_field(name="`Send`", value="Sends coins to a user!")
    embed.add_field(name="`Deposit`", value="Deposits coins to the bank!")
    embed.add_field(name="`Rob`", value="Robs coins from a user!")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    await ctx.reply(embed=embed)

  @commands.command()
  @commands.cooldown(1,15, commands.BucketType.user)
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member = None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a user for me to kick!", color=0xFFFFFF)
      await ctx.reply(embed=embed)
      return
    if reason == None:
      embed = discord.Embed(title="User Kicked", description=f"{member.mention} has been kicked. ", color=0xFFFFFF)
      embed.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Kicked by {ctx.author}.")

      embed2 = discord.Embed(title="Kicked", description=f"You have been kicked from `{ctx.guild.name}` by `{ctx.author}`.", color=0xFFFFFF)
      embed2.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed2.set_footer(text=f"Kicked by {ctx.author}.")
      await member.send(embed=embed2)
      await ctx.reply(embed=embed)
      await ctx.guild.kick(member)
      return
    embed = discord.Embed(title="User Kicked", description=f"{member.mention} has been kicked. ", color=0xFFFFFF)
    embed.add_field(name="Reason:", value=f"`{reason}`")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Kicked by {ctx.author}.")

    embed2 = discord.Embed(title="Kicked", description=f"You have been kicked from `{ctx.guild.name}` by `{ctx.author}`.", color=0xFFFFFF)
    embed2.add_field(name="Reason:", value=f"`{reason}`")
    embed2.set_thumbnail(url=ctx.author.avatar.url)
    embed2.set_footer(text=f"Kicked by {ctx.author}.")
    await member.send(embed=embed2)
    await ctx.reply(embed=embed)
    await ctx.guild.kick(member)

  @commands.command()
  @commands.has_permissions(ban_members = True)
  @commands.cooldown(1,15, commands.BucketType.user)
  async def ban(self, ctx, member:discord.Member=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error!", description="Please specify a user for me to ban!", color=0xFFFFFF)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      return
    elif member.id == ctx.author.id:
      embed=discord.Embed(title="Error!", description="You can't ban yourself!", color=0xFFFFFF)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      return
    elif member.top_role >= ctx.author.top_role:
      embed=discord.Embed(title="Error", description="You can't ban someone with a higher role than you!", color=0xFFFFFF)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)         
      return
    elif reason == None:
      embed = discord.Embed(title="User Banned", description=f"{member.mention} has been banned. ", color=0xFFFFFF)
      embed.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Banned by {ctx.author}.")

      embed2 = discord.Embed(title="Banned", description=f"You have been banned from `{ctx.guild.name}` by `{ctx.author}`.", color=0xFFFFFF)
      embed2.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed2.set_footer(text=f"Kicked by {ctx.author}.")

      await ctx.reply(embed=embed)
      await member.ban(reason = f"Ban Command Used By {ctx.author.name}#{ctx.author.discriminator} | Reason: No Reason Provided")
    else: 
      embed = discord.Embed(title="User Banned", description=f"{member.mention} has been banned.", color=0xFFFFFF)
      embed.add_field(name="Reason:", value=f"`{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Banned by {ctx.author}.")

      embed2 = discord.Embed(title="Banned", description=f"You have been banned from `{ctx.guild.name}` by `{ctx.author}`.", color=0xFFFFFF)
      embed2.add_field(name="Reason:", value=f"`{reason}`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed2.set_footer(text=f"Banned by {ctx.author}.")
      await ctx.reply(embed=embed)
      await member.send(embed=embed2)
      await member.ban(reason = f"Ban Command Used By {ctx.author.name}#{ctx.author.discriminator} | Reason: {reason}")
      
  @commands.command(pass_context=True)
  @commands.cooldown(1,3, commands.BucketType.user)
  async def embed(self, ctx, *, message):
    embed=discord.Embed(title="Embed", description=f"{message}", color=0xFFFFFF)
    await ctx.reply(embed=embed)

  @commands.command(pass_context=True)
  @commands.cooldown(1,10, commands.BucketType.user)
  async def suggest(self, ctx, *, message=None):
    if message == None:
      await ctx.reply("Please give me a suggestiong that you want to suggest!")
      return
    channel = self.bot.get_channel(941061189524418570)
    # 933580415321669662
    embed=discord.Embed(title="Suggestion!", description=f"{message}", color=0xFFFFFF)
    message = await channel.send(embed=embed)
    await message.add_reaction('<:ZeonYes:936757832336945182>')
    await message.add_reaction('<:ZeonNo:936757847994286080>')

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
      embed=discord.Embed(title="AFK", description=f"{member.mention} has gone AFK!", color=0xFFFFFF)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.add_field(name="Reason", value=f"`{reason}`")
      print(f"{ctx.author} used the AFK command!")
      await ctx.send(embed=embed)

  @commands.command(aliases=['mute'])
  @commands.cooldown(1,10, commands.BucketType.user)
  @commands.has_permissions(moderate_members=True)
  async def timeout(self, ctx, member: discord.Member=None, minutes: int=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a member for me to mute!", color=0xFFFFFF)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      return
    elif minutes == None:
      embed=discord.Embed(title="Error", description="Please specify how many minutes you want this user muted!", color=0xFFFFFF)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
    elif reason == None:
      duration = datetime.timedelta(minutes=minutes)
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=0xFFFFFF)
      embed.add_field(name=f"{member} has been timed out for `{minutes}` minutes!", value=f"Reason: `No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      await member.timeout_for(duration, reason="No Reason Provided")
      await ctx.reply(embed=embed)
      return
    duration = datetime.timedelta(minutes=minutes)
    embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=0xFFFFFF)
    embed.add_field(name=f"{member} has been timed out for `{minutes}` minutes!", value=f"Reason: `{reason}`")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    await member.timeout_for(duration, reason=reason)
    await ctx.reply(embed=embed)

  @commands.command(aliases=['untimeout'])
  @commands.cooldown(1,10, commands.BucketType.user)
  async def unmute(self, ctx, member:discord.Member=None, *, reason=None):
    if member == None:
      embed=discord.Embed(title="Error", description="Please specify a member for me to mute!", color=0xFFFFFF)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      await ctx.reply(embed=embed)
      return
    elif reason == None:
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=0xFFFFFF)
      embed.add_field(name=f"{member} has been unmuted!", value=f"Reason: `No Reason Provided`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      await member.remove_timeout(reason="No Reason Provided")
      await ctx.reply(embed=embed)
      return
    embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=0xFFFFFF)
    embed.add_field(name=f"{member} has been unmuted!", value=f"Reason: `{reason}`")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    await member.remove_timeout(reason=reason)
    await ctx.reply(embed=embed)

def setup(bot):
  bot.add_cog(Commands(bot))