import discord
from discord.ext import commands
import random
import json
import urllib
import aiohttp
from colorama import Fore as Color

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() # Fun Help Command
    async def fun(self, ctx):
        embed = discord.Embed(title="___**Fun Commands**___",
                              description="**These are Helix's Fun Commands!**",
                              colour=discord.Colour.random())
        embed.add_field(name="**___Available Commands___**",
                        value="`coinflip`, `pp`, `randomnumber`, `meme`",
                        inline=False)
        embed.add_field(name="**___Coinflip___**",
                        value="Flips a coin that lands on heads or tails. ",
                        inline=False)
        embed.add_field(name="**___PP___**", 
                        value="Detects your PP size!", 
                        inline=False)
        embed.add_field(name="**___Randomnum___**", 
                        value="Picks a random number between 1-100!", 
                        inline=False)
        embed.add_field(name="**___Messageme___**", 
                        value="Messages you exactly what you said.",
                        inline=False)
        embed.add_field(name="**___Meme___**",
                        value="Shows a random meme!",
                        inline=False)
        embed.set_author(name="Helix is Watching!")
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}.")
        print(f"{Color.WHITE} {ctx.author} just used the fun command! {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.message.reply(embed=embed, mention_author=False)
    
    @commands.command(aliases=['cf'])
    async def coinflip(self, ctx, *guess:str):
        if not guess:
            embed=discord.Embed(title="Error...", description="No Arguments Given...", colour=discord.Colour.random())
            embed.add_field(name="Please specify either heads or tales!", value="Ex: `,coinflip Heads`")
            embed.set_author(name="Helix is Watching!")
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.set_footer(text=f"Requested By {ctx.author}")
            await ctx.message.reply(embed=embed, mention_author=False)
            return
        choices = ["Heads", "Tails"]
        answer = random.choice(choices)
        embed = discord.Embed(description="**Heads or Tails?**")
        embed.add_field(name=f"**Your Guess:** `{guess}`",
                        value=f"**Answer:** `{answer}`")
        print(f"{Color.WHITE} {ctx.author} just used the coinflip command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.message.reply(embed=embed, mention_author=False)
        
    @commands.command(pass_context=True)
    async def pp(self, ctx, *, user: discord.Member = None):
        if user == None:
            choices = [
            "8===D", "8=====D", "8=======D", "8==========D", "8================D", "This user is a female!"
        ]
            rancoin = random.choice(choices)
            embed = discord.Embed(title="PP Size Detector", description="Detects the size of your PP.", colour=discord.Colour.random())
            embed.add_field(name="Your PP Size:", value=f"`{rancoin}`", inline=False)
            embed.set_author(name="Helix is Watching!")
            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.set_footer(text=f"This is 100% real!")
            print(f"{Color.WHITE} {ctx.author} just used the pp command! {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
            await ctx.message.reply(embed=embed, mention_author=False)
            return
        choices = [
            "8===D", "8=====D", "8=======D", "8==========D", "8================D", "This user is a female!"
        ]
        rancoin = random.choice(choices)
        embed = discord.Embed(title="PP Size Detector", description="Detects the size of your PP.", colour=discord.Colour.random())
        embed.add_field(name="Your PP Size:", value=f"`{rancoin}`", inline=False)
        embed.set_author(name="Helix is Watching!")
        embed.set_thumbnail(url=user.avatar.url)
        embed.set_footer(text=f"This is 100% real!")
        print(f"{Color.WHITE} {ctx.author} just used the pp command! {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.message.reply(embed=embed, mention_author=False)

    @commands.command(pass_context = True, aliases=['rn', 'randomnum'])
    async def randomnumber(self, ctx):
        embed = discord.Embed(title="Random Number", description = "Picks a random number between 1-100.", color=discord.Color.random())
        embed.add_field(name="Number:", value=f"`{(random.randint(1, 101))}`")
        embed.set_author(name="Helix is Watching!")
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        print(f"{Color.WHITE} {ctx.author} just used the randomnumber command! {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.message.reply(embed=embed, mention_author=False)

    @commands.command(aliases=['dmme', 'pmme', 'messageme'])
    async def msgme(self, ctx, *, message:str):
        embed=discord.Embed(title="Message", description="Here is your message!", color=discord.Color.random())
        embed.add_field(name="Message:", value=f"`{message}`")
        embed.set_author(name="Helix is Watching!")
        embed.set_thumbnail(url=ctx.author.avatar.url)
        embed.set_footer(text=f"Message from {ctx.author}")
        await ctx.author.send(embed=embed)

        embed2=discord.Embed(title="Sent!", description="Your message has been sent!", color=discord.Color.random())
        embed2.add_field(name="Check your DM's!", value="If you didn't get the message, make sure that your DM's are enabled!", inline=False)
        embed2.set_author(name="Helix is Watching!")
        embed2.set_thumbnail(url=ctx.author.avatar.url)
        embed2.set_footer(text=f"Message sent to {ctx.author}")
        print(f"{Color.WHITE} {ctx.author} just used the msgme command! {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
        await ctx.message.reply(embed=embed2, mention_author=False)
        
    @commands.command(pass_context=True)
    async def meme(self, ctx):
      embed = discord.Embed(title="Meme", description="Here is your meme!")

      async with aiohttp.ClientSession() as cs:
         async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
              res = await r.json()
              embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
              embed.set_author(name="Helix is Watching!")
              embed.set_thumbnail(url=ctx.author.avatar.url)
              embed.set_footer(text=f"Requested By {ctx.author}")
              await ctx.message.reply(embed=embed)
        
def setup(bot):
  bot.add_cog(fun(bot))