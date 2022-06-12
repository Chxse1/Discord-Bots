import discord
from discord.ext import commands
import inspect
import os
import sys
import datetime
from colorama import Fore as Color

def restart_bot():
    os.execv(sys.executable, ["python"] + sys.argv)

class owner(commands.Cog):
    def __init__(self, bot):
      self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def chelp(self, ctx):
      embed = discord.Embed(title="**___Cog Commands___**",
                            description="Here are some commands for cogs.",
                            colour=discord.Colour.random())
      embed.add_field(name="**___Available Commands___**",
                      value="`load`, `unload`, `reload`, `cogs`")
      embed.add_field(name="**___Load___**",
                      value="Loads a cog.",
                      inline=False)
      embed.add_field(name="**___Unload___**",
                      value="Unloads a cog.",
                      inline=False)
      embed.add_field(name="**___Reload___**",
                      value="Reloads a cog.",
                      inline=False)
      embed.add_field(name="**___Cogs___**",
                      value="Shows you available cogs.",
                      inline=False)
      embed.set_author(name="Helix is watching!")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text="This is an Owner-Only Command, meaning you can't use it!")
      print(f"{Color.WHITE} {ctx.author} just used the cog help command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(embed=embed, mention_author=False)

    @commands.command(aliases=['o', 'oc'])  # Owner Help Command
    @commands.is_owner()
    async def owner(self, ctx):
      embed = discord.Embed(title="___**Owner Commands**___",
		                        description="**These are Helix's Owner's Commands!**",
		                        colour=discord.Colour.random())
      embed.add_field(name="**___Available Commands___**",
		                  value="`say`, `eval`, `restart`, `servercount`, `membercount`, `servers`, `chelp`",
		                  inline=False)
      embed.add_field(name="**___Say___**",
		                  value="Says anything.",
		                  inline=False)
      embed.add_field(name="**___Eval___**",
		                  value="Evaluates Code/Math.",
		                  inline=False)
      embed.add_field(name="**___Restart___**",
		                  value="Restarts the bot!.",
		                  inline=False)
      embed.add_field(name="**___Servercount___**",
		                  value="Shows how many servers the bot is in.",
		                  inline=False)
      embed.add_field(name="**___Membercount___**",
		                  value="Shows how many members the bot is watching.",
		                  inline=False)
      embed.add_field(name="**___Servers___**",
                      value="Shows you what servers Helix is in.",
                      inline=False)
      embed.add_field(name="**___CHelp___**",
                      value="Shows you the Cog commands.",
                      inline=False)
      embed.set_author(name="Helix is wathcing!")
      embed.set_thumbnail(url=ctx.author.avatar.url)
      embed.set_footer(text="This is an Owner-Only Command, meaning you can't use it!")
      print(f"{Color.WHITE} {ctx.author} just used the owner command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(embed=embed, mention_author=False)

    @commands.command(aliases=['announce'])  # Say Command
    @commands.is_owner()
    async def say(self, ctx, *, message=None):
      if message == None:
        embed = discord.Embed(title="Error!", description="Missing Arguments!")
        embed.add_field(name="You are missing required arguments!", value="Specify what you want me to say...")
        await ctx.message.reply(embed=embed, delete_after = 2, mention_author=False)
      else:
        await ctx.message.delete()
        print(f"{Color.WHITE} {ctx.author} just used the say command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.send(message)

    
    @commands.command(aliases=['res'])
    @commands.is_owner()
    async def restart(self, ctx):
      embed=discord.Embed(title="Restarting....",
                          description="Helix is Restarting...")
      embed.set_author(name="Please wait just a second...")
      embed.set_footer(text="This is an Owner-Only Command, meaning you can't use it!")
      print(f"{Color.WHITE} {ctx.author} just used the restart command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(embed=embed, mention_author=False)
      restart_bot()

    @commands.command(aliases=['membercount', 'mc', 'uc'])
    @commands.is_owner()
    async def botmc(self, ctx):
      embed = discord.Embed(
		      title="**___Membercount___**",
		      description=f"Watching over `{len(self.bot.users)}` users.")
      embed.set_footer(text="This is an Owner-Only Command, meaning you can't use it!")
      print(f"{Color.WHITE} {ctx.author} just used the membercount command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(embed=embed, mention_author=False)
    
    @commands.command(aliases=['servercount', 'sc', 'gc'])
    @commands.is_owner()
    async def botsc(self, ctx):
      embed = discord.Embed(title="**___Servercount___**",
		                        description=f"Connected to `{len(self.bot.guilds)}` servers.")
      embed.set_footer(text="This is an Owner-Only Command, meaning you can't use it!")
      print(f"{Color.WHITE} {ctx.author} just used the servercount command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(embed=embed, mention_author=False)
    @commands.command(aliases=["guilds"])
    @commands.is_owner()
    async def servers(self, ctx):
      embed = discord.Embed(title="**Servers**",
                            description="*These are some servers that Helix is in!*",
                            colour=discord.Colour.random())
      embed.add_field(name=f"**Total Guilds**",
                      value=f"`{len(self.bot.guilds)}`",
                      inline=False)
      embed.add_field(name=f"**Servers:**",
                      value=f"`{'`, `'.join([guild.name for guild in self.bot.guilds])}`",
                      inline=False)
      embed.set_footer(text="This is an Owner-Only Command, meaning you can't use it!")
      print(f"{Color.WHITE} {ctx.author} just used the servers command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(embed=embed, mention_author=False)
        
    @commands.command(aliases=["leaveg", "leaves"])
    @commands.is_owner()
    async def leave(self, ctx, guild: discord.Guild = None):

      if guild is None:

        await ctx.message.reply("Please Specify a Server!", mention_author=False)

      else:

        print(f"{Color.WHITE} {ctx.author} just used the leave command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.message.reply(f"Success! I left `{guild}`! | ID: {guild.id}", mention_author=False)
        await ctx.guild.leave()

def setup(bot):
  bot.add_cog(owner(bot))