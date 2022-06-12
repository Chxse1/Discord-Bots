import discord
from colorama import Fore as Color
from discord.ext import commands
from discord.utils import get

guild_id = '935552988917936188'
embedcolor = '0xFFFF00'

class events(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
      print(f"Bot Online! Type .help for a list of commands.")
      await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Over {len(self.bot.users)} users! | .help"))

  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    try:
        await self.bot.process_commands(after)
    except:
        raise Exception

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    embed=discord.Embed(title="Error", description=f"{error}", color=0x000FF)
    await ctx.reply(embed=embed)
    raise error

def setup(bot):
  bot.add_cog(events(bot))