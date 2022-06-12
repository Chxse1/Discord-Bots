import discord
from pystyle import Colorate, Colors
from discord.ext import commands
from main import embed_color, hashtag

class events(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_connect(self):
    print(Colorate.Horizontal(Colors.rainbow, "Connecting to the Bot!"))
    await self.bot.change_presence(activity=discord.Game(name=f"Getting Ready! Give me a bit!"))

  @commands.Cog.listener()
  async def on_ready(self):
    print(Colorate.Horizontal(Colors.rainbow, "Ready!"))
    await self.bot.change_presence(activity=discord.Game(name=f"s!help | {hashtag} | Watching over {len(self.bot.users)}"))

  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    if after.author == self.bot.user:
      return
    else:
      try:
          await self.bot.process_commands(after)
      except:
          raise Exception

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error,commands.errors.CommandNotFound):
        embed=discord.Embed(title="Error", description="This is not a command! Try again!", color=embed_color)
        await ctx.message.reply(embed=embed)
    elif isinstance(error,commands.errors.NotOwner):
        embed=discord.Embed(title="Error", description="You are not an owner of the bot, you can't use this command!", color=embed_color)
        await ctx.message.reply(embed=embed)
    elif isinstance(error,commands.errors.MissingPermissions):
        embed=discord.Embed(title="Error", description="You are missing the required permissions!", color=embed_color)
        await ctx.message.reply(embed=embed)
    elif isinstance(error,commands.errors.CommandOnCooldown):
        embed=discord.Embed(title="Error", description="You are on cooldown for this command!", color=embed_color)
        await ctx.message.reply(embed=embed)
    else:
        raise error

  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = discord.utils.get(member.guild.channels, id=846262476756353027)
    embed=discord.Embed(title="Welcome!", description=f"Welcome {member.mention} ({member}) to Synchronize!", color=embed_color)
    embed.add_field(name=f"Hey, {member.name}! Welcome to Synchronize! We hope to see you active soon!", value="Make sure to check the following channels out!\n\n--------------------------------------------------\n\n<#726551142913278073>, <#870295540955512903>, <#879063238699016192>, <#962356762218995762>")
    embed.set_author(name=member.guild.name)
    embed.set_footer(text="Have a Nice Day!", icon_url="https://cdn.discordapp.com/attachments/963434810980827227/963549284760944650/F1927B84-C179-430A-8DFB-573D4AB44638.jpg")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/963434810980827227/963549284760944650/F1927B84-C179-430A-8DFB-573D4AB44638.jpg")
    await channel.send(embed=embed)

def setup(bot):
  bot.add_cog(events(bot))