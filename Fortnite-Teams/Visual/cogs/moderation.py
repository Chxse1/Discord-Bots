import discord
from discord.ext import commands
from colorama import Fore as Color


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(kick_members=True)
    async def kick(self,
                   ctx,
                   member: discord.Member = None,
                   *,
                   reason: str = None):
        if member == None:
            embed = discord.Embed(
                title="Error",
                description="Please specify a user for me to kick!",
                color=0xFF0000)
            await ctx.message.reply(embed=embed)
            return
        if reason == None:
            reason = "No Reason Provided"
        embed = discord.Embed(title="User Kicked",
                              description=f"{member.mention} has been kicked!",
                              color=0x33FFFF)
        embed.add_field(name="Reason:", value=f"`{reason}`")
        embed.set_author(name="#VisualOT")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Kicked by {ctx.author}.")
        await ctx.guild.kick(member)
        await ctx.message.reply(embed=embed)
        return
        embed = discord.Embed(title="User Kicked",
                              description=f"{member.mention} has been kicked!",
                              color=0x33FFFF)
        embed.add_field(name="Reason:", value=f"`{reason}`")
        embed.set_author(name="#VisualOT")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Kicked by {ctx.author}.")
        print(
            f"{Color.WHITE} {ctx.author} just used the kick command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.guild.kick(member)
        await ctx.message.reply(embed=embed)

    @commands.command(pass_context=True, hidden=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        embed = discord.Embed(title="Purged",
                              description=f"Purged `{limit}` messages")
        print(
            f"{Color.WHITE} {ctx.author} just used the purge command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.send(embed=embed, delete_after=5)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(ban_members=True)
    async def ban(self,
                  ctx,
                  member: discord.Member = None,
                  *,
                  reason: str = None):
        if member == None:
            embed = discord.Embed(
                title="Error",
                description="Please specify a user for me to ban!",
                color=0xFF0000)
            await ctx.message.reply(embed=embed)
            return
        if reason == None:
            reason = "No Reason Provided"
        embed = discord.Embed(title="User Banned",
                              description=f"{member.mention} has been banned!",
                              color=0x33FFFF)
        embed.add_field(name="Reason:", value=f"`{reason}`")
        embed.set_author(name="#VisualOT")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Banned by {ctx.author}.")
        print(
            f"{Color.WHITE} {ctx.author} just used the ban command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.message.reply(embed=embed)
        await ctx.guild.ban(member, reason=reason)
        return

        embed2 = discord.Embed(
            title="Banned",
            description=f"You have been banned from Team Vision!",
            color=0x33FFFF)
        embed.add_field(name="Reason:", value=f"`{reason}`")
        embed.set_author(name="#VisualOT")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Banned by {ctx.author}.")
        print(
            f"{Color.WHITE} {ctx.author} just used the ban command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.member.send(embed=embed2)

        embed = discord.Embed(title="User Banned",
                              description=f"{member.mention} has been banned!",
                              color=0x33FFFF)
        embed.add_field(name="Reason:", value=f"`{reason}`")
        embed.set_author(name="#VisualOT")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text=f"Banned by {ctx.author}.")
        print(
            f"{Color.WHITE} {ctx.author} just used the ban command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
        )
        await ctx.message.reply(embed=embed)
        await ctx.member.ban(reason=reason)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member: discord.Member = None):
        if member == None:
            embed = discord.Embed(
                title="Error",
                description="Please specify a user for me to unban!",
                color=0xFF0000)
            await ctx.message.reply(embed=embed)
            return
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split("#")

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name,
                                                       member_discriminator):
                    embed = discord.Embed(
                        title="User Unbanned",
                        description=f"`{member}` has been unbanned!",
                        color=0x33FFFF)
                    embed.set_author(name="#VisualOT")
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    embed.set_footer(text=f"Unbanned by {ctx.author}.")
                    print(
                        f"{Color.WHITE} {ctx.author} just used the unban command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}"
                    )
                    await ctx.guild.unban(user)
                    await ctx.send(embed=embed)
                    return


def setup(bot):
    bot.add_cog(moderation(bot))
