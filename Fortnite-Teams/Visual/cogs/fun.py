import discord
import random
import aiohttp
from colorama import Fore as Color
from discord.ext.commands import clean_content
from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bon(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.message.reply("Please specify who to ban!")
        else:
            print(
                f"{Color.WHITE} {ctx.author} just used the bon command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
            )
            await ctx.message.reply(f"`{member}` has been banned!")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unbon(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.message.reply("Please specify who to unban!")
        else:
            print(
                f"{Color.WHITE} {ctx.author} just used the unbon command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
            )
            await ctx.message.reply(f"`{member}` has been unbanned!")

    @commands.command(aliases=['pog'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poggify(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.message.reply("Please specify who to poggify!")
        else:
            print(
                f"{Color.WHITE} {ctx.author} just used the poggify command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
            )
            await ctx.message.reply(f"`{member}` has been poggified!")

    @commands.command(aliases=['unpog'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unpoggify(self, ctx, member: discord.Member = None):
        if member == None:
            await ctx.message.reply("Please specify who to unpoggify!")
        else:
            print(
                f"{Color.WHITE} {ctx.author} just used the unpoggify command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
            )
            await ctx.message.reply(
                f"`{member}` has been unpoggified... You are so uncool...")

    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx):
        embed = discord.Embed(title="Meme",
                              description="Here is your meme!",
                              color=0x33FFFF)

        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/dankmemes/new.json?sort=hot'
            ) as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(
                    0, 25)]['data']['url'])
                embed.set_author(name="#VisualOT")
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text=f"Requested By {ctx.author}")
                print(
                    f"{Color.WHITE} {ctx.author} just used the meme command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
                )
                await ctx.message.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rr(self, ctx):
        print(
            f"{Color.WHITE} {ctx.author} just used the rr command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.message.delete()
        await ctx.send(file=discord.File('cat_meow_compilation.mp3'))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def mayo(self, ctx):
        print(
            f"{Color.WHITE} {ctx.author} just used the mayo command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.message.delete()
        await ctx.send(file=discord.File('AC_DC.mp3'))

    @commands.command(aliases=['gay-scanner', 'gayscanner', 'gay', 'gayrate'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def howgay(self, ctx, *, user: clean_content = None):
        if not user:
            user = ctx.author.name
        gayness = random.randint(0, 100)
        if gayness <= 33:
            gayStatus = random.choice([
                "No homo", "Wearing socks", '"Only sometimes"', "Straight-ish",
                "No homo bro", "Girl-kisser", "Hella straight"
            ])
            gayColor = 0x33FFFF
        elif 33 < gayness < 66:
            gayStatus = random.choice([
                "Possible homo", "My gay-sensor is picking something up",
                "I can't tell if the socks are on or off", "Gay-ish",
                "Looking a bit homo", "lol half  g a y",
                "safely in between for now"
            ])
            gayColor = 0x33FFFF
        else:
            gayStatus = random.choice([
                "LOL YOU GAY XDDD FUNNY", "HOMO ALERT",
                "MY GAY-SENSOR IS OFF THE CHARTS", "STINKY GAY", "BIG GEAY",
                "THE SOCKS ARE OFF", "HELLA GAY"
            ])
            gayColor = 0x33FFFF
        emb = discord.Embed(description=f"Gayness for **{user}**",
                            color=gayColor)
        emb.add_field(name="Gayness:", value=f"`%{gayness} gay`")
        emb.add_field(name="Comment:", value=f"`{gayStatus}` :kiss_mm:")
        emb.set_author(
            name="Gay-Scanner™",
            icon_url=
            "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/ICA_flag.svg/2000px-ICA_flag.svg.png"
        )
        print(
            f"{Color.WHITE} {ctx.author} just used the howgay command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.send(embed=emb)

    @commands.command(aliases=['ppsize', 'sizepp'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pp(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author
            size = random.choice([
                "2cm", "`3ft`", "`a vagina`", "`too small to be measured`",
                "`-16in`", "`bigger than a whole airplane`",
                "`too small to be seen`", "`6cm`", "`9in`", "`1 ft`",
                "`bigger than your mom`"
            ])
            pp = discord.Embed(title='PP Size Dectector!',
                               description="Measuring your pp!",
                               color=0x33FFFF)
            pp.add_field(name='Your PP is: ', value=f"{size}")
            pp.set_author(name="#VisualOT")
            pp.set_thumbnail(url=ctx.author.avatar_url)
            pp.set_footer(text=f"Requested By {ctx.author}")
            print(
                f"{Color.WHITE} {ctx.author} just used the pp command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
            )
            await ctx.channel.send(embed=pp)


def setup(bot):
    bot.add_cog(fun(bot))
