import discord
import random
import aiohttp
import datetime
from colorama import Fore as Color
from discord.ext.commands import clean_content
from discord.ext import commands
from discord.utils import get
from afks import afks

class commands(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def help(self, ctx, command=None):
    if command == None:
      embed = discord.Embed(title="Help", description="This is the help command! Try out some commands!", color=0x0000FF)
      embed.add_field(name="`a!help`", value="Shows this message!", inline=False)
      embed.add_field(name="`a!moderation`", value="Shows moderation commands!", inline=False)
      embed.add_field(name="`a!fun`", value="Shows fun commands!", inline=False)
      embed.add_field(name="`a!other`", value="Shows other commands!", inline=False)
      embed.add_field(name="`a!owner`", value="Developer Only Commands!")
      embed.add_field(name="More Coming Soon!", value="More Coming Soon!", inline=False)
      embed.set_author(name="#FearAztec")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested By {ctx.author}")
      print(f"{Color.WHITE} {ctx.author} just used the help command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(embed=embed)

  @commands.command(aliases=['mod'])
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def moderation(self, ctx):
    embed=discord.Embed(title="Moderation Commands", description="Here is a list of moderation commands!", color=0x0000FF)
    embed.add_field(name="`Purge`", value="Purges an amount of commands!", inline=False)
    embed.add_field(name="`Kick`", value="Kicks the specified user!", inline=False)
    embed.add_field(name="`Ban`", value="Bans the specified user!", inline=False)
    embed.add_field(name="`Unban`", value="Unbans the specified user!", inline=False)
    embed.add_field(name="`Mute`", value="Mutes the specified user!", inline=False)
    embed.add_field(name="`Unmute`", value="Unmutes the specified user!", inline=False)
    embed.add_field(name="`Lock`", value="Locks this channel!", inline=False)
    embed.add_field(name="`Unlock`", value="Unlocks this channel!", inline=False)
    embed.set_author(name="#FearAztec")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    print(f"{Color.WHITE} {ctx.author} just used the moderation command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def fun(self, ctx):
    embed=discord.Embed(title="Fun Commands", description="Here is a list of fun commands!", color=0x0000FF)
    embed.add_field(name="`Bon`", value="This is a fun command that sends a message showing that a user is banned!", inline=False)
    embed.add_field(name="`Unbon`", value="This is a fun command that sends a message showing that a user is unbanned!", inline=False)
    embed.add_field(name="`Poggify`", value="Poggifies a specified user!", inline=False)
    embed.add_field(name="`Unpoggify`", value="Unpoggifies a specified user!", inline=False)
    embed.add_field(name="`Meme`", value="Shows you a meme!", inline=False)
    embed.add_field(name="`Snipe`", value="Snipes a deleted message!", inline=False)
    embed.add_field(name="`PP`", value="Shows you how big your pp is!", inline=False)
    embed.set_author(name="#FearAztec")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    print(f"{Color.WHITE} {ctx.author} just used the fun command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command(aliases=['others'])
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def other(self, ctx):
    embed=discord.Embed(title="Other Commands", description="Here is a list of other commands!", color=0x0000FF)
    embed.add_field(name="`Ping`", value="Shows you the bot latency!", inline=False)
    embed.add_field(name="`Serverinfo`", value="Shows you info on this server!", inline=False)
    embed.add_field(name="`Userinfo`", value="Shows you info on the specified user!", inline=False)
    embed.add_field(name="`Membercount`", value="Shows you amount of members in this guild!", inline=False)
    embed.add_field(name="`Credits`", value="Shows you credits of this bot!", inline=False)
    embed.add_field(name="`Bug`", value="Sends a bug you found to the bot dev!", inline=False)
    embed.add_field(name="`Suggest`", value="Sends a suggestion you suggest to the bot dev!", inline=False)
    embed.add_field(name="More Coming Soon!", value="More Coming Soon!", inline=False)
    embed.set_author(name="#FearAztec")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    print(f"{Color.WHITE} {ctx.author} just used the other command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command(aliases=['o'])
  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.is_owner()
  async def owner(self, ctx):
    embed = discord.Embed(title="Owner Help", description="This is the owner help command! Try out some commands!", color=0x0000FF)
    embed.add_field(name="`Say`", value="Says what you want it to!", inline=False)
    embed.add_field(name="`Reload`", value="Reloads a cog!", inline=False)
    embed.add_field(name="`Load`", value="Loads a cog!", inline=False)
    embed.add_field(name="`Unload`", value="Unloads a cog!", inline=False)
    embed.add_field(name="`Cogs`", value="Shows you all the cogs!", inline=False)
    embed.set_author(name="#FearAztec")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    print(f"{Color.WHITE} {ctx.author} just used the owner command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def bon(self, ctx, member : discord.Member = None):
    if member == None:
      await ctx.message.reply("Please specify who to ban!")
    else:
      print(f"{Color.WHITE} {ctx.author} just used the bon command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(f"`{member}` has been banned!")

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def unbon(self, ctx, member : discord.Member = None):
    if member == None:
      await ctx.message.reply("Please specify who to unban!")
    else:
      print(f"{Color.WHITE} {ctx.author} just used the unbon command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(f"`{member}` has been unbanned!")

  @commands.command(aliases=['pog'])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def poggify(self, ctx, member : discord.Member = None):
    if member == None:
      await ctx.message.reply("Please specify who to poggify!")
    else:
      print(f"{Color.WHITE} {ctx.author} just used the poggify command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(f"`{member}` has been poggified!") 

  @commands.command(aliases=['unpog'])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def unpoggify(self, ctx, member : discord.Member = None):
    if member == None:
      await ctx.message.reply("Please specify who to unpoggify!")
    else:
      print(f"{Color.WHITE} {ctx.author} just used the unpoggify command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(f"`{member}` has been unpoggified... You are so uncool...") 

  @commands.command(pass_context=True)
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def meme(self, ctx):
      embed = discord.Embed(title="Meme", description="Here is your meme!", color=0x0000FF)

      async with aiohttp.ClientSession() as cs:
          async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
              res = await r.json()
              embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
              embed.set_author(name="#FearAztec")
              embed.set_thumbnail(url=ctx.author.avatar.url)
              embed.set_footer(text=f"Requested By {ctx.author}")
              print(f"{Color.WHITE} {ctx.author} just used the meme command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
              await ctx.message.reply(embed=embed)

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def rr(self, ctx):
    print(f"{Color.WHITE} {ctx.author} just used the rr command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.delete()
    await ctx.send(file=discord.File('cat_meow_compilation.mp3'))

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def mayo(self, ctx):
    print(f"{Color.WHITE} {ctx.author} just used the mayo command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.delete()
    await ctx.send(file=discord.File('AC_DC.mp3'))

  @commands.command(aliases=['gay-scanner', 'gayscanner', 'gay', 'gayrate'])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def howgay(self, ctx,* ,user: clean_content=None):
        if not user:
            user = ctx.author.name
        gayness = random.randint(0,100)
        if gayness <= 33:
            gayStatus = random.choice(["No homo", 
                                       "Wearing socks", 
                                       '"Only sometimes"', 
                                       "Straight-ish", 
                                       "No homo bro", 
                                       "Girl-kisser", 
                                       "Hella straight"])
            gayColor = 0x0000FF
        elif 33 < gayness < 66:
            gayStatus = random.choice(["Possible homo", 
                                       "My gay-sensor is picking something up", 
                                       "I can't tell if the socks are on or off", 
                                       "Gay-ish", 
                                       "Looking a bit homo", 
                                       "lol half  g a y", 
                                       "safely in between for now"])
            gayColor = 0x0000FF
        else:
            gayStatus = random.choice(["LOL YOU GAY XDDD FUNNY", 
                                       "HOMO ALERT", 
                                       "MY GAY-SENSOR IS OFF THE CHARTS", 
                                       "STINKY GAY", 
                                       "BIG GEAY", 
                                       "THE SOCKS ARE OFF", 
                                       "HELLA GAY"])
            gayColor = 0x0000FF
        emb = discord.Embed(description=f"Gayness for **{user}**", color=gayColor)
        emb.add_field(name="Gayness:", value=f"`%{gayness} gay`")
        emb.add_field(name="Comment:", value=f"`{gayStatus}` :kiss_mm:")
        emb.set_author(name="Gay-Scanner™", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/ICA_flag.svg/2000px-ICA_flag.svg.png")
        print(f"{Color.WHITE} {ctx.author} just used the howgay command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.send(embed=emb)
        
  @commands.command(aliases=['ppsize', 'sizepp'])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def pp(self, ctx):
        size = random.choice(["2cm", 
                                   "`3ft`", 
                                   "`a vagina`", 
                                   "`too small to be measured`", 
                                   "`-16in`", 
                                   "`bigger than a whole airplane`", 
                                   "`too small to be seen`", 
                                   "`6cm`", 
                                   "`9in`", 
                                   "`1 ft`", 
                                   "`bigger than your mom`"])
        pp = discord.Embed(title='PP Size Dectector!', description="Measuring your pp!", color=0x0000FF)
        pp.add_field(name='Your PP is: ', value=f"{size}") 
        pp.set_author(name="#FearAztec")
        pp.set_thumbnail(url=ctx.author.avatar.url)
        pp.set_footer(text=f"Requested By {ctx.author}")
        print(f"{Color.WHITE} {ctx.author} just used the pp command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.channel.send(embed=pp)

  @commands.command(pass_context=True, hidden=True)
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, limit: int):
      await ctx.channel.purge(limit=limit)
      print(f"{Color.WHITE} {ctx.author} just used the purge command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.send(f"Purged `{limit}` messages!", delete_after = 5)

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
      embed.set_author(name="#FearAztec")

      embed2 = discord.Embed(title="Kicked", description=f"You have been kicked from `{ctx.guild.name}` by `{ctx.author}`.", color=0x2140DA)
      embed2.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed2.set_footer(text=f"Kicked by {ctx.author}.")
      embed.set_author(name="#FearAztec")
      await member.send(embed=embed2)
      await ctx.reply(embed=embed)
      await ctx.guild.kick(member)
      return
    embed = discord.Embed(title="User Kicked", description=f"{member.mention} has been kicked. ", color=0x2140DA)
    embed.add_field(name="Reason:", value=f"`{reason}`")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Kicked by {ctx.author}.")
    embed.set_author(name="#FearAztec")

    embed2 = discord.Embed(title="Kicked", description=f"You have been kicked from `{ctx.guild.name}` by `{ctx.author}`.", color=0x2140DA)
    embed2.add_field(name="Reason:", value=f"`{reason}`")
    embed2.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_author(name="#FearAztec")
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
      embed.set_author(name="#FearAztec")

      embed2 = discord.Embed(title="Banned", description=f"You have been banned from `{ctx.guild.name}` by `{ctx.author}`.", color=0x2140DA)
      embed2.add_field(name="Reason:", value=f"`No Reason Provided`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed2.set_footer(text=f"Kicked by {ctx.author}.")
      embed.set_author(name="#FearAztec")

      await ctx.reply(embed=embed)
      await member.ban(reason = f"Ban Command Used By {ctx.author.name}#{ctx.author.discriminator} | Reason: No Reason Provided")
    else: 
      embed = discord.Embed(title="User Banned", description=f"{member.mention} has been banned.", color=0x2140DA)
      embed.add_field(name="Reason:", value=f"`{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Banned by {ctx.author}.")
      embed.set_author(name="#FearAztec")

      embed2 = discord.Embed(title="Banned", description=f"You have been banned from `{ctx.guild.name}` by `{ctx.author}`.", color=0x2140DA)
      embed2.add_field(name="Reason:", value=f"`{reason}`")
      embed2.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_author(name="#FearAztec")
      embed2.set_footer(text=f"Banned by {ctx.author}.")
      await ctx.reply(embed=embed)
      await member.send(embed=embed2)
      await member.ban(reason = f"Ban Command Used By {ctx.author.name}#{ctx.author.discriminator} | Reason: {reason}")

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member: discord.Member = None):
    if member == None:
      await ctx.message.reply("Please specify a user for me to Unban.", mention_author=False)
      return
    banned_users = await ctx.guild.bans()

    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
      user = ban_entry.user

      if (user.name, user.discriminator) == (member_name,
			                                       member_discriminator):
        embed = discord.Embed(title="User Unbanned",description=f"{user.mention} has been Unbanned. ",colour=discord.Colour.random())
        print(f"{Color.WHITE} {ctx.author} just used the unban command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.guild.unban(user)
        await ctx.message.reply(embed=embed, mention_author=False)
              
  @commands.command(aliases=['lock'])
  @commands.has_permissions(manage_channels=True)
  async def lockdown(self, ctx):
    role = discord.utils.get(ctx.guild.roles, id=907371853545349184)
    await ctx.channel.set_permissions(role, send_messages=False)
    print(f"{Color.WHITE} {ctx.author} just used the lock command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.reply("Channel Locked!")

  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def unlock(self, ctx):
    role = discord.utils.get(ctx.guild.roles, id=907371853545349184)
    await ctx.channel.set_permissions(role, send_messages=True)
    print(f"{Color.WHITE} {ctx.author} just used the unlock command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.reply("Channel Unlocked!")

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

  @commands.command(aliases=['creds'], help="Shows you the bot credits!", description="Use this command to see the credits of the bot!")
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def credits(self, ctx):
    embed=discord.Embed(title="Credits", description="Here are the credits of the developing of this bot!", color=0x0000FF)
    embed.add_field(name="Developer:", value="`! Chase#0001`")
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.set_author(name="#FearAztec")
    print(f"{Color.WHITE} {ctx.author} just used the credits command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command(help="Shows you the bot latency!", description="Use this to see the bot latency!")
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def ping(self, ctx):
    embed=discord.Embed(title="Pong!", description="Here is the bot latency!", color=0x0000FF)
    embed.add_field(name="Bot Latency:", value=f"`{round(self.bot.latency * 1000)}ms`")
    embed.set_footer(text=f"Requested by {ctx.author}") 
    embed.set_author(name="#FearAztec") 
    print(f"{Color.WHITE} {ctx.author} just used the ping command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command(aliases=["si"])
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def serverinfo(self, ctx):
    embed = discord.Embed(title="Server Info", description=f"{ctx.guild.name}", color=0x0000FF)
    embed.add_field(name="Owner", value=f'`{ctx.guild.owner}`', inline=False)
    embed.add_field(name="Channels", value=f'`{len(ctx.guild.channels)}`', inline=False)
    embed.add_field(name="Roles", value=f'`{len(ctx.guild.roles)}`', inline=False)
    embed.add_field(name="Server Created", value=f'`{ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p")}`', inline=False)
    embed.add_field(name="Membercount", value=f'`{len(ctx.guild.members)}`', inline=False)
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=f"#FearAztec")
    print(f"{Color.WHITE} {ctx.author} just used the serverinfo command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command(aliases=['mc'])
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def membercount(self, ctx):
    embed=discord.Embed(title="Membercount", description="Here is the amount of members in this server!", color=0x0000FF)
    embed.add_field(name="Count:", value=f"`{len(ctx.guild.members)}`")
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=f"#FearAztec")
    print(f"{Color.WHITE} {ctx.author} just used the membercount command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    await ctx.message.reply(embed=embed)


  @commands.command(aliases=['whois', 'ui'])
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def userinfo(self, ctx, *, user: discord.Member = None):
    if user is None:
      user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(description=f"Here is information on `{user.name}#{user.discriminator}`!", color=0x0000FF)
    embed.set_author(name=str(user), icon_url=user.avatar.url)
    embed.set_thumbnail(url=user.avatar.url)
    embed.add_field(name="Joined:", value=user.joined_at.strftime(date_format))
    embed.add_field(name="User ID:", value=f'{user.id}')
    embed.add_field(name="Registered:", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
      role_string = ' '.join([r.mention for r in user.roles][1:])
      embed.add_field(name="Roles [{}]".format(len(user.roles) - 1),
			              value=role_string,
			              inline=False)
    perm_string = ', '.join([
		    str(p[0]).replace("_", " ").title() for p in user.guild_permissions
		    if p[1]
	  ])
    embed.add_field(name="Guild Permissions:", value=perm_string, inline=False)
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar.url)
    print(f"{Color.WHITE} {ctx.author} just used the userinfo command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
    return await ctx.message.reply(embed=embed)

  @commands.command()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def bug(self, ctx, *, message=None):
    if message == None:
            await ctx.message.reply("Missing Required Arguments!\nUse this command like this, `a!bug (Bug)`!")
    else:
      await ctx.message.reply("Bug Sent! Please wait for this to be reviewed!")

      channel = self.bot.get_channel(927102800738005002)
      embed2 = discord.Embed(title=f"Bug reported!", description=f"Bug = `{message}`\n User: `{ctx.author.name}#{ctx.author.discriminator}`\n User ID: `{ctx.author.id}`", color=0x0000FF)
      embed2.set_author(name="New Bug!")
      print(f"{Color.WHITE} {ctx.author} just used the bug command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await channel.send(embed=embed2)

  @commands.command()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def suggest(self, ctx, *, message=None):
    if message == None:
          await ctx.message.reply("Missing Required Arguments!\nUse this command like this, `a!suggest (Suggestion)`!")
    else:
      await ctx.message.reply("Suggestion Sent! Please wait for this to be reviewed!")

      channel = self.bot.get_channel(927102848175587328)
      embed2 = discord.Embed(title=f"Suggestion Suggested!",description=f"Suggestion = `{message}`\n User: `{ctx.author.name}#{ctx.author.discriminator}`\n User ID: `{ctx.author.id}`", color=0x0000FF)
      embed2.set_author(name="New Suggestion!")
      print(f"{Color.WHITE} {ctx.author} just used the suggest command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await channel.send(embed=embed2)

  @commands.command(aliases=['av'])
  async def avatar(self, ctx, *,  avamember : discord.Member=None):
    if avamember == None:
      userAvatarUrl = ctx.author.avatar.url
      await ctx.message.reply(userAvatarUrl)
      return
    userAvatarUrl = avamember.avatar.url
    await ctx.message.reply(userAvatarUrl)

  @commands.command()
  @commands.cooldown(1,5, commands.BucketType.user)
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
      embed=discord.Embed(title="AFK", description=f"{member.mention} has gone AFK!", color=0x0000FF)
      embed.set_thumbnail(url=member.avatar.url)
      embed.set_author(name="#FearAztec")
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.add_field(name="Reason", value=f"`{reason}`")
      print(f"{ctx.author} used the AFK command!")
      await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(commands(bot))