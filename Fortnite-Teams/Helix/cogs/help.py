import discord
from discord.ext import commands
from colorama import Fore as Color

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['h'])    # Help Command
    async def help(self, ctx):
        embed = discord.Embed(title="___**Helix's Help Guide!**___",
                              description="**This is Helix's Help Guide!**",
                              colour=discord.Colour.random())
        embed.add_field(
                name="**___Available Categories___**",
                value="`Help` | `Moderation` | `Utility` | `Fun` | `Info` | `Music` | `Credits`",
                inline=False)
        embed.add_field(name="**___Help___**",
                        value="Shows this command.",
                        inline=False)
        embed.add_field(name="**___Moderation___**",
                        value="Shows Moderation Commands.",
                        inline=False)
        embed.add_field(name="**___Utility___**",
                        value="Shows Utility Commands.",
                        inline=False)
        embed.add_field(name="**___Fun___**",
                        value="Shows Fun Commands.",
                        inline=False)
        embed.add_field(name="**___Info___**",
                        value="Shows Information Commands.",
                        inline=False)
        embed.add_field(name="**___Owner___**",
                        value="These are commands made for the owners only.",
                        inline=False)
        embed.add_field(name="**___Credits___**",
                        value="Shows credits of the Bot.",
                        inline=False)
        embed.add_field(name="**___Invite Helix___**",
                        value="[Invite](https://discord.com/api/oauth2/authorize?client_id=899887955211071498&permissions=268553335&scope=bot)",
                        inline=False)
        embed.add_field(name="**___Helix's Server___**",
                        value="[Support](https://discord.gg/75e2uhvhdR)",
                        inline=False)
        embed.set_author(name="Helix is Watching!")
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.set_footer(text=f"Requested By {ctx.author}")
        print(f"{Color.WHITE} {ctx.author} just used the help command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.message.reply(embed=embed, mention_author=False)

def setup(bot):
  bot.add_cog(help(bot))