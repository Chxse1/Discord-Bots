import discord
from discord.ext import commands
from main import embed_color, hashtag

blacklisted = [852717613187465237]

class utility(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command(help="Shows you the bot latency!", description="Use this to see the bot latency!")
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def ping(self, ctx):
    embed=discord.Embed(title="Pong!", description="Here is the bot latency!", color=embed_color)
    embed.add_field(name="Bot Latency:", value=f"`{round(self.bot.latency * 1000)}ms`")
    embed.set_footer(text=f"Requested by {ctx.author}") 
    embed.set_author(name=hashtag)
    print(f"{ctx.author} used the ping command | {ctx.channel}")
    await ctx.message.reply(embed=embed)

  @commands.command(aliases=["si"])
  @commands.cooldown(1, 3, commands.BucketType.user)
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
    await ctx.message.reply(embed=embed)

  @commands.command(aliases=['mc'])
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def membercount(self, ctx):
    embed=discord.Embed(title="Membercount", description="Here is the amount of members in this server!", color=embed_color)
    embed.add_field(name="Count:", value=f"`{len(ctx.guild.members)}`")
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_footer(text=hashtag)
    print(f"{ctx.author} used the membercount command | {ctx.channel}")
    await ctx.message.reply(embed=embed)


  @commands.command(aliases=['whois', 'ui'])
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def userinfo(self, ctx, *, user: discord.Member = None):
    if user is None:
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
      await ctx.message.reply(embed=embed)
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
      await ctx.message.reply(embed=embed)

  @commands.command()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def bug(self, ctx, *, message=None):
    if ctx.author.id in blacklisted:
      embed=discord.Embed(title="Error", description="You are blacklisted from using this command!")
      await ctx.reply(embed=embed)
      return
    elif message == None:
      embed=discord.Embed(title="Error", description="Missing Required Args.\nUse this command as such, `a!bug <Bug>`")
      await ctx.reply(embed=embed)
    else:
      embed=discord.Embed(title="Success!", description="Bug Sent! Please wait for this to be reviewed!")
      await ctx.message.reply(embed=embed)
      user = await self.bot.fetch_user("852423298481651743")
      embed2 = discord.Embed(title=f"Bug reported!", description=f"Bug = `{message}`\n User: `{ctx.author.name}#{ctx.author.discriminator}`\n User ID: `{ctx.author.id}`", color=embed_color)
      embed2.set_author(name="New Bug!")
      print(f"{ctx.author} used the bug command | {ctx.channel}")
      await user.send(embed=embed2)

  @commands.command()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def suggest(self, ctx, *, message=None):
    if ctx.author.id in blacklisted:
      embed=discord.Embed(title="Error", description="You are blacklisted from using this command!")
      await ctx.reply(embed=embed)
    elif message == None:
      embed=discord.Embed(title="Error", description="Missing Required Args.\nUse this command as such, `a!suggest <Suggestion>`")
      await ctx.reply(embed=embed)
    else:
      await ctx.message.reply("Suggestion Sent! Please wait for this to be reviewed!")
      user = await self.bot.fetch_user("852423298481651743")
      embed2 = discord.Embed(title=f"Suggestion Suggested!",description=f"Suggestion = `{message}`\n User: `{ctx.author.name}#{ctx.author.discriminator}`\n User ID: `{ctx.author.id}`", color=embed_color)
      embed2.set_author(name="New Suggestion!")
      print(f"{ctx.author} used the suggest command | {ctx.channel}")
      await user.send(embed=embed2)

  @commands.command(aliases=['banner', 'av'])
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

  @commands.command(aliases=['howtojoin', 'how-tojoin', 'howto-join', 'how-to-join'])
  async def join(self, ctx):
    embed=discord.Embed(title="How To Join Vertigo Unit", description="""Run `/join` to see this command!""", color=embed_color)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_author(name=hashtag)
    embed.set_footer(text=f"Requested by {ctx.author}!")
    await ctx.reply(embed=embed)

  @commands.command(aliases=['socials'])
  async def social(self, ctx):
    embed=discord.Embed(title="Socials", description="https://solo.to/vertigoggs", color=embed_color)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    embed.set_author(name=hashtag)
    embed.set_footer(text=f"Requested by {ctx.author}!")
    await ctx.reply(embed=embed)

def setup(bot):
  bot.add_cog(utility(bot))
