import discord
import asyncio
from discord.ext import commands
from colorama import Fore as Color


class other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=['creds'],
        help="Shows you the bot credits!",
        description="Use this command to see the credits of the bot!")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def credits(self, ctx):
        print(
            f"{Color.WHITE} {ctx.author} just used the credits command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        embed = discord.Embed(title="Credits",
                              description="Here are the credits of the bot!")
        embed.add_field(name="Credits:", value="Bot Developer: `~Chase~#8243`")
        await ctx.message.reply(embed=embed)

    @commands.command(help="Shows you the bot latency!",
                      description="Use this to see the bot latency!")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ping(self, ctx):
        embed = discord.Embed(title="Pong!",
                              description="Here is the bot latency!",
                              color=0x33FFFF)
        embed.add_field(name="Bot Latency:",
                        value=f"`{round(self.bot.latency * 1000)}ms`")
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.set_author(name="#VisualOT")
        print(
            f"{Color.WHITE} {ctx.author} just used the ping command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.message.reply(embed=embed)

    @commands.command(aliases=["si"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def serverinfo(self, ctx):
        embed = discord.Embed(title="Server Info",
                              description=f"{ctx.guild.name}",
                              color=0x33FFFF)
        embed.add_field(name="Owner",
                        value=f'`{ctx.guild.owner}`',
                        inline=False)
        embed.add_field(name="Channels",
                        value=f'`{len(ctx.guild.channels)}`',
                        inline=False)
        embed.add_field(name="Roles",
                        value=f'`{len(ctx.guild.roles)}`',
                        inline=False)
        embed.add_field(
            name="Server Created",
            value=
            f'`{ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p")}`',
            inline=False)
        embed.add_field(name="Membercount",
                        value=f'`{len(ctx.guild.members)}`',
                        inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f"#VisualOT")
        print(
            f"{Color.WHITE} {ctx.author} just used the serverinfo command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.message.reply(embed=embed)

    @commands.command(aliases=['mc'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def membercount(self, ctx):
        embed = discord.Embed(
            title="Membercount",
            descrition="Here is the amount of members in this server!",
            color=0x33FFFF)
        embed.add_field(name="Count:", value=f"`{len(ctx.guild.members)}`")
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text=f"#VisualOT")
        print(
            f"{Color.WHITE} {ctx.author} just used the membercount command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.message.reply(embed=embed)

    @commands.command(aliases=['whois', 'ui'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def userinfo(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(
            description=
            f"Here is information on `{user.name}#{user.discriminator}`!",
            color=0x33FFFF)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined:",
                        value=user.joined_at.strftime(date_format))
        embed.add_field(name="User ID:", value=f'{user.id}')
        embed.add_field(name="Registered:",
                        value=user.created_at.strftime(date_format))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles) - 1),
                            value=role_string,
                            inline=False)
        perm_string = ', '.join([
            str(p[0]).replace("_", " ").title() for p in user.guild_permissions
            if p[1]
        ])
        embed.add_field(name="Guild Permissions:",
                        value=perm_string,
                        inline=False)
        embed.set_footer(
            text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}',
            icon_url=ctx.author.avatar_url)
        print(
            f"{Color.WHITE} {ctx.author} just used the userinfo command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        return await ctx.message.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def bug(self, ctx, *, message=None):
        if message == None:
            await ctx.message.reply(
                "Missing Required Arguments!\nUse this command like this, `v!bug (Bug)`!"
            )
        else:
            await ctx.message.reply(
                "Bug Sent! Please wait for this to be reviewed!")

            channel = self.bot.get_channel(936840088820776980)
            embed2 = discord.Embed(
                title=f"Bug reported!",
                description=
                f"Bug = `{message}`\n User: `{ctx.author.name}#{ctx.author.discriminator}`\n User ID: `{ctx.author.id}`",
                color=0x33FFFF)
            embed2.set_author(name="New Bug!")
            print(
                f"{Color.WHITE} {ctx.author} just used the bug command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
            )
            await channel.send(embed=embed2)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def suggest(self, ctx, *, message=None):
        if message == None:
            await ctx.message.reply(
                "Missing Required Arguments!\nUse this command like this, `v!suggest (Suggestion)`!"
            )
        else:
            await ctx.message.reply(
                "Suggestion Sent! Please wait for this to be reviewed!")

            channel = self.bot.get_channel(936840102523584593)
            embed2 = discord.Embed(
                title=f"Suggestion Suggested!",
                description=
                f"Suggestion = `{message}`\n User: `{ctx.author.name}#{ctx.author.discriminator}`\n User ID: `{ctx.author.id}`",
                color=0x33FFFF)
            embed2.set_author(name="New Suggestion!")
            print(
                f"{Color.WHITE} {ctx.author} just used the suggest command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
            )
            await channel.send(embed=embed2)

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *, avamember: discord.Member = None):
        if avamember == None:
            userAvatarUrl = ctx.author.avatar_url
            await ctx.message.reply(userAvatarUrl)
            return
        userAvatarUrl = avamember.avatar_url
        await ctx.message.reply(userAvatarUrl)


def setup(bot):
    bot.add_cog(other(bot))
