from discord.ext import commands

class customs(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command()
  @commands.cooldown(1,10,commands.BucketType.user)
  async def tinx(self, ctx):
    print(f"{ctx.author} used the tinx command | {ctx.channel}")
    await ctx.reply('<@831523224281939989> is cute :)')

  @commands.command()
  @commands.cooldown(1,10,commands.BucketType.user)
  async def daddy(self, ctx):
    print(f"{ctx.author} used the daddy command | {ctx.channel}")
    await ctx.reply('<@823255297723203625> is daddy')

def setup(bot):
  bot.add_cog(customs(bot))