import discord
from discord.ext import commands
from colorama import Fore as Color


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help!",
                              description="Here is the help categories!",
                              color=0x33FFFF)
        embed.add_field(name="`Help`",
                        value="Shows the help categories!",
                        inline=True)
        embed.add_field(name="`Moderation`",
                        value="Shows the moderation commands!",
                        inline=True)
        embed.add_field(name="`Fun`",
                        value="Shows the fun commands!",
                        inline=True)
        embed.add_field(name="`Owner`",
                        value="Shows the owner commands!",
                        inline=True)
        embed.set_author(name="#VisualOT")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.message.reply(embed=embed)

    @commands.command(aliases=['mod'])
    async def moderation(self, ctx):
        embed = discord.Embed(
            title="Help!",
            description="Here is all of the moderation commands!",
            color=0x33FFFF)
        embed.add_field(name="`Purge`",
                        value="Purges a specified amount of messages!",
                        inline=True)
        embed.add_field(name="`Kick`",
                        value="Kicks a specified user!",
                        inline=True)
        embed.add_field(name="`Warns`",
                        value="Warns a user!",
                        inline=True)
        embed.add_field(name="`Warns`",
                        value="Shows you a user's warns!",
                        inline=True)
        embed.add_field(name="`Unban`",
                        value="Unbans a specified user!",
                        inline=True)
        embed.set_author(name="#VisualOT")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.message.reply(embed=embed)

    @commands.command(aliases=['o'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.is_owner()
    async def owner(self, ctx):
        embed = discord.Embed(
            title="Owner Help",
            description=
            "This is the owner help command! Try out some commands!",
            color=0x33FFFF)
        embed.add_field(name="`Restart`",
                        value="Restarts the bot!",
                        inline=True)
        embed.add_field(name="`Reload`", value="Reloads a cog!", inline=True)
        embed.add_field(name="`Load`", value="Loads a cog!", inline=True)
        embed.add_field(name="`Unload`", value="Unloads a cog!", inline=True)
        embed.add_field(name="`Cogs`",
                        value="Shows you all the cogs!",
                        inline=True)
        embed.set_author(name="#VisualOT")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested By {ctx.author}")
        print(
            f"{Color.WHITE} {ctx.author} just used the owner command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.message.reply(embed=embed)

    @commands.command(aliases=['others', 'misc', 'miscellaneous'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def other(self, ctx):
        embed = discord.Embed(title="Other Commands",
                              description="Here is a list of other commands!",
                              color=0x33FFFF)
        embed.add_field(name="`Ping`",
                        value="Shows you the bot latency!",
                        inline=True)
        embed.add_field(name="`Serverinfo`",
                        value="Shows you info on this server!",
                        inline=True)
        embed.add_field(name="`Userinfo`",
                        value="Shows you info on the specified user!",
                        inline=True)
        embed.add_field(name="`Membercount`",
                        value="Shows you amount of members in this guild!",
                        inline=True)
        embed.add_field(name="`Credits`",
                        value="Shows you credits of this bot!",
                        inline=True)
        embed.add_field(name="`Bug`",
                        value="Sends a bug you found to the bot dev!",
                        inline=True)
        embed.add_field(name="`Suggest`",
                        value="Sends a suggestion you suggest to the bot dev!",
                        inline=True)
        embed.add_field(name="More Coming Soon!",
                        value="More Coming Soon!",
                        inline=True)
        embed.set_author(name="#VisualOT")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Requested By {ctx.author}")
        print(
            f"{Color.WHITE} {ctx.author} just used the other command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.message.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def fun(self, ctx):
      embed=discord.Embed(title="Fun Commands", description="Here is a list of fun commands!", color=0x7316F4)
      embed.add_field(name="`Bon`", value="This is a fun command that sends a message showing that a user is banned!", inline=True)
      embed.add_field(name="`Unbon`", value="This is a fun command that sends a message showing that a user is unbanned!", inline=True)
      embed.add_field(name="`Poggify`", value="Poggifies a specified user!", inline=True)
      embed.add_field(name="`Unpoggify`", value="Unpoggifies a specified user!", inline=True)
      embed.add_field(name="`Meme`", value="Shows you a meme!", inline=True)
      embed.add_field(name="`Snipe`", value="Snipes a deleted message!", inline=True)
      embed.add_field(name="`RR`", value="Sends an audio file of a rick roll!", inline=True)
      embed.add_field(name="`Mayo`", value="Ssends an audio file of mayonnaise on an escalator!", inline=True)
      embed.add_field(name="`PP`", value="Shows you how big your pp is!", inline=True)
      embed.set_author(name="#VisualOT")
      embed.set_thumbnail(url=ctx.author.avatar_url)
      embed.set_footer(text=f"Requested By {ctx.author}")
      print(f"{Color.WHITE} {ctx.author} just used the fun command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
      await ctx.message.reply(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
