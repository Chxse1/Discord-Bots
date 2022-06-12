import discord
from discord.ext import commands
import inspect
import asyncio
import random
from colorama import Fore as Color

class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['util', 'u']) # Utility Help Command
    async def utility(self, ctx):
        embed = discord.Embed(title="___**Utility Commands**___",
                              description="**These are Helix's Utility Commands!**",
                              colour=discord.Colour.random())
        embed.add_field(name="**___Available Commands___**",
                        value="`giveaway`, `bug`, `suggest`, `slowmode`, `clear`",
                        inline=False)
        embed.add_field(name="**___Giveaway___**",
                        value="Starts a giveaway!",
                        inline=False)
        embed.add_field(name="**___Bug___**",
                        value="Report a Bug!",
                        inline=False)
        embed.add_field(name="**___Suggest___**",
                        value="Suggest something to the bot!",
                        inline=False)
        embed.add_field(name="**___Slowmode___**",
                        value="Sets slowmode to a certain amount of seconds!",
                        inline=False)
        embed.add_field(name="**___Purge___**",
                        value="Purges the amount of messages you want!",
                        inline=False)
        embed.add_field(name="**___Clear___**",
                        value="Clears the channel of all messages!",
                        inline=False)
        embed.set_author(name="Helix is Watching!")
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}.")
        print(f"{Color.WHITE} {ctx.author} just used the utility command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.message.reply(embed=embed, mention_author=False)

    @commands.command(aliases=['gaw'])
    async def giveaway(self, ctx, time=None, *, prize=None):
        if time == None:
            return await ctx.message.reply('Please include a time! s | m | h | d', mention_author=False)
        elif prize == None:
            return await ctx.message.reply('Please include a prize! (,giveaway "Time" "Prize")', mention_author=False)
        embed = discord.Embed(title="Giveaway!", description=f"{ctx.author.mention} is giving away **{prize}**!")
        time_convert = {"s":1, "m":60, "h":3600, "d":86400}
        gawtime = int(time[0:-1]) * time_convert[time[-1]]
        embed.set_footer(text=f"Giveaway ends in {time}")
        print(f"{Color.WHITE} {ctx.author} just used the giveaway command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        gaw_msg = await ctx.message.reply(embed=embed, mention_author=False)

        await gaw_msg.add_reaction("🎉")
        await asyncio.sleep(gawtime)

        new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)

        users = await new_gaw_msg.reactions[0].users().flatten()

        users.pop(users.index(self.bot.user))

        winner = random.choice(users)

        await ctx.send(f"Congratulations! {winner.mention} has won the giveaway for **{prize}**")

    @commands.command()
    async def bug(self, ctx, *, message=None):
        if message == None:
          embed = discord.Embed(title="Error!",description="Missing Arguments!")
          embed.add_field(name="You are missing required arguments!", value="You need to specify what bug you want to report.")
          await ctx.message.reply(embed=embed, mention_author=False)
        else:
          embed = discord.Embed(title="Bug Sent",description="Thank you for reporting this bug, my developers will do something about this!") 
          embed.set_author(name="Helix is Watching!")
          embed.set_thumbnail(url=ctx.author.avatar.url)
          embed.set_footer(text=f"Requested By {ctx.author}")
          await ctx.message.reply(embed=embed, mention_author=False)

          channel = self.bot.get_channel(901343125082103809)
          embed2 = discord.Embed(title=f"Bug reported!",description=f"Bug = `{message}`\n Server = `{ctx.guild.name}`\n User: `{ctx.author.name}{ctx.author.discriminator}`\n User ID: `{ctx.author.id}`")
          print(f"{Color.WHITE} {ctx.author} just used the bug command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
          await channel.send(embed=embed2)

    @commands.command()
    async def suggest(self, ctx, *, message=None):
        if message == None:
          embed = discord.Embed(title="Error!",description="Missing Arguments!")
          embed.add_field(name="You are missing required arguments!", value="You need to specify what you want to suggest.")
          await ctx.message.reply(embed=embed, mention_author=False)
        else:
          embed = discord.Embed(title="Suggestion Sent",description="Thank you for suggesting this suggestion, my developers will think about this suggestion!") 
          embed.set_author(name="Helix is Watching!")
          embed.set_footer(text=f"Requested By {ctx.author}")
          await ctx.message.reply(embed=embed, mention_author=False)

          channel = self.bot.get_channel(901525351388303451)
          embed2 = discord.Embed(title=f"Suggestion Suggested!",description=f"Suggestion = `{message}`\n Server = `{ctx.guild.name}`\n User: `{ctx.author.name}{ctx.author.discriminator}`\n User ID: `{ctx.author.id}`")
          embed.set_author(name="New Suggestion!")
          print(f"{Color.WHITE} {ctx.author} just used the suggest command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
          await channel.send(embed=embed2)

    @commands.command(aliases=['sm'])
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds):
          await ctx.channel.edit(slowmode_delay=seconds)
          embed = discord.Embed(title='Helix',description=f"Set Slowmode To {seconds}s")
          embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}',icon_url=ctx.author.avatar.url)
          print(f"{Color.WHITE} {ctx.author} just used the slowmode command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
          await ctx.message.reply(embed = embed, mention_author=False) 

    @commands.command(aliases=['clearchannel', 'clr'])
    @commands.has_permissions(manage_channels=True)
    async def clear(self, ctx):
        channelthings = [ctx.channel.category, ctx.channel.position]
        await ctx.channel.clone()
        await ctx.channel.delete()
        embed=discord.Embed(title=f'Cleared Channel!', description=f'**Channel was cleared by {ctx.author.name}#{ctx.author.discriminator}**',timestamp=ctx.message.created_at)
        embed.set_image(url="https://media2.giphy.com/media/jmSImqrm28Vdm/200.gif")
        clearedchannel = channelthings[0].text_channels[-1]
        await clearedchannel.edit(position=channelthings[1])
        print(f"{Color.WHITE} {ctx.author} just used the clear command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await clearedchannel.send(embed=embed, mention_author=False)

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        embed = discord.Embed(title="Purged!", description=f"`{limit}` messages have been purged.")
        embed.set_author(name="Helix is Watching!")
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.set_footer(text=f"Purged By {ctx.author}")
        await ctx.channel.purge(limit=limit)
        print(f"{Color.WHITE} {ctx.author} just used the purge command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(utility(bot))