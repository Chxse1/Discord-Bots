import discord
from discord.ext import commands
from colorama import Fore as Color

class credits(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['creds', 'cred'])
    async def credits(self, ctx):
        embed = discord.Embed(title="**___Credits___**",
                              description="Credits of Helix!",
                              colour=discord.Colour.random())
        embed.add_field(name="**___Developers___**", value="`~Chase~#4471`, `||Dank Lord||#9919`, `darx#2424`", inline=False)
        embed.add_field(name="**___More Coming___**",
                        value="`Eventually more people are gonna come to Helix!`",
                        inline=False)
        embed.set_author(name="Helix is Watching!")
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.set_footer(text=f"Requested By {ctx.author}")
        print(f"{Color.WHITE} {ctx.author} just used the credits command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.message.reply(embed=embed, mention_author=False)

def setup(bot):
  bot.add_cog(credits(bot))