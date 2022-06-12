import discord
from discord.ext import commands
from main import embed_color

class customs(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command(aliases=['rape', 'efuck', 'bumfuck', 'erape', 'ebumfuck', 'assfuck', 'eassfuck', 'buttfuck', 'ebuttfuck', 'esex', 'sex', 'pussy', 'epussy', 'butttouch', 'ebutttouch', 'bang', 'ebang', 'e-fuck', 'e-rape', 'e-bumfuck', 'e-assfuck', 'e-buttfuck', 'e-sex', 'e-pussy', 'e-butttouch', 'e-bang'])
  async def fuck(self, ctx, fucked:discord.Member):
    await ctx.reply(f"{ctx.author.mention} fucked {fucked.mention} so hard, {fucked.mention}'s asshole started bleeding! LMAOO")

  @commands.command(aliases=['echo', 'announce'])
  async def say(self, ctx, channel=None, *, message=None):
    await ctx.message.delete()
    if channel == None:
      embed=discord.Embed(title="Error", description="Please specify the channel", embed=embed_color)
      await ctx.reply(embed=embed)
    elif message == None:
      embed=discord.Embed(title="Error", description="Please specify the message", embed=embed_color)
      await ctx.reply(embed=embed)
    else:
      sendchannel = self.bot.get_channel(channel)
      await sendchannel.send(message)

def setup(bot):
  bot.add_cog(customs(bot))
