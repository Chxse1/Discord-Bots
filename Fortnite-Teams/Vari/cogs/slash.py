from pydoc import describe
import discord
import random
import datetime
from discord.ext import commands
from discord.utils import get
from main import hashtag, embed_color, afks
from discord.commands import slash_command

blacklisted = []

def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

class slash(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @slash_command(guild_ids=[820627674937688074], name="help", description="Shows you my help command!")
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
    await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="custom", description="Shows all of the custom commands!")
  async def custom(self, ctx):
    embed = discord.Embed(title="Help!", description="Here is a list of custom commands!", color=embed_color)
    embed.add_field(name="**__None!__**", value="Ask Chase for a custom command if you want one!", inline=True)
    embed.set_author(name=hashtag)
    embed.set_footer(text=f"Requested by {ctx.author}!")
    embed.set_thumbnail(url=ctx.author.avatar.url)
    print(f"{ctx.author} used the custom command | {ctx.channel}")
    await ctx.respond(embed=embed)


  @slash_command(guild_ids=[820627674937688074], name="moderation", description="Shows all of the moderation commands!")
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
    await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="fun", description="Shows all of the fun commands!")
  async def fun(self, ctx):
    embed=discord.Embed(title="Fun Commands", description="Here is a list of fun commands!", color=embed_color)
    embed.add_field(name="`Bon`", value="This is a fun command that sends a message showing that a user is banned!", inline=True)
    embed.add_field(name="`Unbon`", value="This is a fun command that sends a message showing that a user is unbanned!", inline=True)
    embed.add_field(name="`Snipe`", value="Snipes a deleted message!", inline=True)
    embed.add_field(name="`RR`", value="Sends an audio file of a rick roll!", inline=True)
    embed.add_field(name="`Mayo`", value="Ssends an audio file of mayonnaise on an escalator!", inline=True)
    embed.set_author(name=hashtag)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    print(f"{ctx.author} used the fun command | {ctx.channel}")
    await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="utility", description="Shows all of the utility commands!")
  async def utility(self, ctx):
    embed=discord.Embed(title="Utility Commands", description="Here is a list of utility commands!", color=embed_color)
    embed.add_field(name="`Ping`", value="Shows you the bot latency!", inline=True)
    embed.add_field(name="`Serverinfo`", value="Shows you info on this server!", inline=True)
    embed.add_field(name="`Userinfo`", value="Shows you info on the specified user!", inline=True)
    embed.add_field(name="`Membercount`", value="Shows you amount of members in this guild!", inline=True)
    embed.add_field(name="`Bug`", value="Sends a bug you found to the bot dea!", inline=True)
    embed.add_field(name="`Suggest`", value="Sends a suggestion you suggest to the bot dea!", inline=True)
    embed.add_field(name="`Avatar`", value="Shows you the avatar of a specified user!", inline=True)
    embed.add_field(name="`Banner`", value="Shows you the avatar and banner of a specified user!", inline=True)
    embed.add_field(name="`Join`", value="Shows you the how to join message!", inline=True)
    embed.add_field(name="`AFK`", value="Sets you as afk!", inline=True)
    embed.add_field(name="`Say`", value="Says a specified message!", inline=True)
    embed.set_author(name=hashtag)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_footer(text=f"Requested By {ctx.author}")
    print(f"{ctx.author} used the utility command | {ctx.channel}")
    await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="fuck", description="Fuck the specified user!")
  async def fuck(self, ctx, fucked:discord.Member):
    await ctx.respond(f"{ctx.author.mention} fucked {fucked.mention} so hard, {fucked.mention}'s asshole started bleeding! LMAOO")

  @slash_command(guild_ids=[820627674937688074], name="afk", description="Sets your AFK!")
  async def afk(self, ctx, *, reason):
        member = ctx.author
        if member.id in afks.keys():
            afks.pop(member.id)
        else:
            try:
                await member.edit(nick=f"[AFK] {member.display_name}")
            except:
                pass
        afks[member.id] = reason
        embed=discord.Embed(title="AFK", description=f"{member.mention} has gone AFK!", color=embed_color)
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_author(name=hashtag)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.add_field(name="Reason", value=f"`{reason}`")
        print(f"{ctx.author} used the afk command | {ctx.channel}")
        await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="bon", description='"Ban" the specified user!')
  async def bon(self, ctx, member : discord.Member):
      print(f"{ctx.author} used the bon command | {ctx.channel}")
      await ctx.respond(f"`{member}` has been banned!")

  @slash_command(guild_ids=[820627674937688074], name="unbon", description='"Unban" the specified user!')
  async def unbon(self, ctx, member : discord.Member):
      print(f"{ctx.author} used the unbon command | {ctx.channel}")
      await ctx.respond(f"`{member}` has been unbanned!")

  @slash_command(guild_ids=[820627674937688074], name="rr", description="Send an audio file!")
  async def rr(self, ctx):
    await ctx.message.delete()
    print(f"{ctx.author} used the rr command | {ctx.channel}")
    await ctx.respond(file=discord.File('Audio/cat_meow_compilation.mp3'))

  @slash_command(guild_ids=[820627674937688074], name="mayo", description="Send an audio file!")
  async def mayo(self, ctx):
    await ctx.message.delete()
    print(f"{ctx.author} used the mayo command | {ctx.channel}")
    await ctx.respond(file=discord.File('Audio/AC_DC.mp3'))

  @slash_command(guild_ids=[820627674937688074], name="howgay", description="Shows you how gay someone is!")
  async def howgay(self, ctx, *, user: discord.Member=None):
    if user == None:
        user = ctx.author.name
        gayness = random.randint(0,100)
        gayStatus = random.choice(["No Homo", 
                                "Some Homo", 
                                "Only Sometimes", 
                                "Kinda Gay", 
                                "Gay as Hell", 
                                "Have you even seen a girl?", 
                                "Hella Gay"])
        gayColor = embed_color
        emb = discord.Embed(description=f"Gayness for **{user}**", color=gayColor)
        emb.add_field(name="Gayness:", value=f"`%{gayness}` gay")
        emb.add_field(name="Comment:", value=f"`{gayStatus}`")
        emb.set_author(name=hashtag, icon_url=ctx.author.avatar.url)
        print(f"{ctx.author} used the howgay command | {ctx.channel}")
        await ctx.respond(embed=emb)
    else:
        gayness = random.randint(0,100)
        gayStatus = random.choice(["No Homo", 
                                "Some Homo", 
                                "Only Sometimes", 
                                "Kinda Gay", 
                                "Gay as Hell", 
                                "Have you even seen a girl?", 
                                "Hella Gay"])
        gayColor = embed_color
        emb = discord.Embed(description=f"Gayness for **{user}**", color=gayColor)
        emb.add_field(name="Gayness:", value=f"`%{gayness}` gay")
        emb.add_field(name="Comment:", value=f"`{gayStatus}`")
        emb.set_author(name=hashtag, icon_url=user.avatar.url)
        print(f"{ctx.author} used the howgay command | {ctx.channel}")
        await ctx.respond(embed=emb)

  @slash_command(guild_ids=[820627674937688074], name="kick", description="Kick the specified user!")
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason:str):
      embed=discord.Embed(title="User Kicked", description=f"{member.mention} has been kicked!", color=embed_color)
      embed.add_field(name="Reason:", value=f"`{reason}`")
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Kicked by {ctx.author}.")
      await ctx.respond(embed=embed)
      print(f"{ctx.author} used the kick command | {ctx.channel}")
      await ctx.guild.kick(member, reason=reason)

  @slash_command(guild_ids=[820627674937688074], name="ban", description="Ban the specified user!")
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason:str):
      embed=discord.Embed(title="User Banned", description=f"{member.mention} has been banned!", color=embed_color)
      embed.add_field(name="Reason:", value=f"`{reason}`")
      embed.set_author(name=hashtag)
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Banned by {ctx.author}.")
      await ctx.respond(embed=embed)
      print(f"{ctx.author} used the ban command | {ctx.channel}")
      await ctx.guild.ban(member, reason=reason)

  @slash_command(guild_ids=[820627674937688074], name="purge", description="Purge the specified amount of messages!")
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, limit:int):
        embed=discord.Embed(title="Success", description=f"Purged `{limit}` messages!", color=embed_color)
        await ctx.channel.purge(limit=limit + 1)
        print(f"{ctx.author} used the purge command | {ctx.channel}")
        await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="mute", description="Mute the specified user!")
  @commands.has_permissions(moderate_members=True)
  async def mute(self, ctx, member: discord.Member, minutes: int, *, reason):
      duration = datetime.timedelta(minutes=minutes)
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been timed out for `{minutes}` minutes!", value=f"Reason: `{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.timeout_for(duration, reason=reason)
      print(f"{ctx.author} used the mute command | {ctx.channel}")
      await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="unmute", description="Unmute the specified user!")
  @commands.has_permissions(moderate_members=True)
  async def unmute(self, ctx, member:discord.Member, *, reason):
      embed=discord.Embed(title="Muted", description=f"{member.mention} has been muted!", color=embed_color)
      embed.add_field(name=f"{member} has been unmuted!", value=f"Reason: `{reason}`")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_author(name=hashtag)
      await member.remove_timeout(reason=reason)
      print(f"{ctx.author} used the unmute command | {ctx.channel}")
      await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="ping", description="Shows you the latency of the bot!")
  async def ping(self, ctx):
    embed=discord.Embed(title="Pong!", description="Here is the bot latency!", color=embed_color)
    embed.add_field(name="Bot Latency:", value=f"`{round(self.bot.latency * 1000)}ms`")
    embed.set_footer(text=f"Requested by {ctx.author}") 
    embed.set_author(name=hashtag)
    print(f"{ctx.author} used the ping command | {ctx.channel}")
    await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="serverinfo", description="Shows you information on the server!")
  async def serverinfo(self, ctx):
    embed = discord.Embed(title="Server Info", description=f"{ctx.guild.name}", color=embed_color)
    embed.add_field(name="Owner", value=f'`{ctx.guild.owner}`', inline=False)
    embed.add_field(name="Channels", value=f'`{len(ctx.guild.channels)}`', inline=False)
    embed.add_field(name="Roles", value=f'`{len(ctx.guild.roles)}`', inline=False)
    embed.add_field(name="Server Created", value=f'`{ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p")}`', inline=False)
    embed.add_field(name="Membercount", value=f'`{len(ctx.guild.members)}`', inline=False)
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=hashtag)
    print(f"{ctx.author} used the serverinfo command | {ctx.channel}")
    await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="membercount", description="Shows you the amount of users in this server!")
  async def membercount(self, ctx):
    embed=discord.Embed(title="Membercount", description="Here is the amount of members in this server!", color=embed_color)
    embed.add_field(name="Count:", value=f"`{len(ctx.guild.members)}`")
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=hashtag)
    print(f"{ctx.author} used the membercount command | {ctx.channel}")
    await ctx.respond(embed=embed)


  @slash_command(guild_ids=[820627674937688074], name="userinfo", description="Shows you information on a user")
  async def userinfo(self, ctx, *, user: discord.Member = None):
    if user == None:
      user = ctx.author
      date_format = "%a, %d %b %Y %I:%M %p"
      embed = discord.Embed(description=f"Here is information on `{user.name}#{user.discriminator}`!", color=embed_color)
      embed.add_field(name="User:", value=ctx.author)
      embed.add_field(name="Joined:", value=user.joined_at.strftime(date_format))
      embed.add_field(name="User ID:", value=f'{user.id}')
      embed.add_field(name="Registered:", value=user.created_at.strftime(date_format))
      embed.set_author(name=hashtag)
      embed.set_footer(text=f"Requested by {ctx.author}")
      embed.set_thumbnail(url=user.avatar.url)

      if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
      embed.add_field(name="Roles [{}]".format(len(user.roles) - 1),
			              value=role_string,
			              inline=False)
      perm_string = ', '.join([
		    str(p[0]).replace("_", " ").title() for p in user.guild_permissions
		    if p[1]])
      embed.add_field(name="Guild Permissions:", value=perm_string, inline=False)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}')
      print(f"{ctx.author} used the userinfo command | {ctx.channel}")
      await ctx.respond(embed=embed)
    else:
      date_format = "%a, %d %b %Y %I:%M %p"
      embed = discord.Embed(description=f"Here is information on `{user.name}#{user.discriminator}`!", color=embed_color)
      embed.set_author(name=hashtag)
      embed.set_footer(text=f"Requested by {ctx.author}")
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
		    if p[1]])
      embed.add_field(name="Guild Permissions:", value=perm_string, inline=False)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}')
      print(f"{ctx.author} used the userinfo command | {ctx.channel}")
      await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="bug", description="Reports a bug to the bot dea!")
  async def bug(self, ctx, *, message):
    if ctx.author.id in blacklisted:
      embed=discord.Embed(title="Error", description="You are blacklisted from using this command!")
      await ctx.respond(embed=embed)
    else:
      embed=discord.Embed(title="Success!", description="Bug Sent! Please wait for this to be reviewed!")
      await ctx.respond(embed=embed)
      user = await self.bot.fetch_user("852423298481651743")
      embed2 = discord.Embed(title=f"Bug reported!", description=f"Bug = `{message}`\n User: `{ctx.author.name}#{ctx.author.discriminator}`\n User ID: `{ctx.author.id}`", color=embed_color)
      embed2.set_author(name="New Bug!")
      print(f"{ctx.author} used the bug command | {ctx.channel}")
      await user.send(embed=embed2)

  @slash_command(guild_ids=[820627674937688074], name="suggest", description="Suggests a suggestion to the bot dea!")
  async def suggest(self, ctx, *, message):
    if ctx.author.id in blacklisted:
      embed=discord.Embed(title="Error", description="You are blacklisted from using this command!")
      await ctx.respond(embed=embed)
    else:
      await ctx.respond(embed=embed2)
      user = await self.bot.fetch_user("852423298481651743")
      embed2 = discord.Embed(title=f"Suggestion Suggested!",description=f"Suggestion = `{message}`\n User: `{ctx.author.name}#{ctx.author.discriminator}`\n User ID: `{ctx.author.id}`", color=embed_color)
      embed2.set_author(name="New Suggestion!")
      print(f"{ctx.author} used the suggest command | {ctx.channel}")
      await user.send(embed=embed2)

  @slash_command(guild_ids=[820627674937688074], name="banner", description="Shows you someones avatar an banner!")
  async def avatar(self, ctx, user:discord.Member=None):
    if user == None:
      user=ctx.author
      req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
      banner_id = req["banner"]
      banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
      embed=discord.Embed(title="Avatar/Banner", description=f"Here is {user.mention}'s avatar and banner!")
      embed.set_image(url=banner_url)
      embed.set_thumbnail(url=user.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_footer(text=f"Requested by {ctx.author}!")
      await ctx.send(embed=embed)
    else:
      req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
      banner_id = req["banner"]
      banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
      embed=discord.Embed(title="Avatar/Banner", description=f"Here is {user.mention}'s avatar and banner!")
      embed.set_image(url=banner_url)
      embed.set_thumbnail(url=user.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_footer(text=f"Requested by {ctx.author}!")
      await ctx.send(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="avatar", description="Shows you someones avatar an banner!")
  async def avatar(self, ctx, user:discord.Member=None):
    if user == None:
      user=ctx.author
      req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
      banner_id = req["banner"]
      banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
      embed=discord.Embed(title="Avatar/Banner", description=f"Here is {user.mention}'s avatar and banner!")
      embed.set_image(url=banner_url)
      embed.set_thumbnail(url=user.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_footer(text=f"Requested by {ctx.author}!")
      await ctx.send(embed=embed)
    else:
      req = await self.bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
      banner_id = req["banner"]
      banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
      embed=discord.Embed(title="Avatar/Banner", description=f"Here is {user.mention}'s avatar and banner!")
      embed.set_image(url=banner_url)
      embed.set_thumbnail(url=user.avatar.url)
      embed.set_author(name=hashtag)
      embed.set_footer(text=f"Requested by {ctx.author}!")
      await ctx.send(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="say", description="Says the specified message!")
  @commands.has_permissions(administrator=True)
  async def say(self, ctx, *, message):
      await ctx.message.delete()
      print(f"{ctx.author} used the say command | {ctx.channel}")
      await ctx.respond(message)

  @slash_command(guild_ids=[820627674937688074], name="join", description="Shows you the how to join message!")
  async def join(self, ctx):
    embed=discord.Embed(title="How To Join Vertigo Unit", description="""
**Competitive Roster
- Must have multiple top 500 placements.
- Must have 5k+ points & 750+ pr
- Must have $10+ in earnings.
- Must have 5 clips to provide weekly.
- Any faked clips or placements will result in a drop/decline.

Creative Roster
- Must have unique building and impressive mechanics & retakes.
- Must have experience in boxfights.
- Must have experience in PGs.
- Any fake clips are an instant drop/decline

Streamer
- Must have at least 200 followers.
- Must have at least 15 viewers.
- Must have a funny or professional feel.

Content Creator
- Must have at least 100 followers/subscribers.
- Must have an average of 50+ views.
- Must have a funny or professional

GFX
- Must have prior experience.
- Must have a portfolio or work to show.
- Must have a professional software to work with (photoshop, blender etc.)

VFX
- Must have prior experience.
- Must have a video or work to show.
- Must have a actual software to work with (After Effects, Premiere Pro, Sony Vegas)

Moderator
- Must be active daily on discord
- Must have prior experience
- Must be respectful, and welcoming to new members

Management
- Must have prior experience
- Must have resume (or can fill out staff application below)
- The Management spots we offer are “Content Manager”, “Roster Manager”, “Event Manager” and “Community Manager”
- https://docs.google.com/forms/u/1/d/1eLZufC6MwE_rlFgRtNT-PEJAw4opcti6-0hShlCAgcA/edit
**""", color=embed_color)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_author(name=hashtag)
    embed.set_footer(text=f"Requested by {ctx.author}!")
    await ctx.respond(embed=embed, ephemeral=True)

  @slash_command(guild_ids=[820627674937688074], name="socials", description="Shows you our socials!")
  async def socials(self, ctx):
    embed=discord.Embed(title="Socials", description="https://solo.to/vertigoggs", color=embed_color)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_author(name=hashtag)
    embed.set_footer(text=f"Requested by {ctx.author}!")
    await ctx.respond(embed=embed)

  @slash_command(guild_ids=[820627674937688074], name="say", description="Says a specified message!")
  async def say(self, ctx, channel, *, message):
    sendchannel = self.bot.get_channel(channel)
    await sendchannel.send(message)


def setup(bot):
  bot.add_cog(slash(bot))
