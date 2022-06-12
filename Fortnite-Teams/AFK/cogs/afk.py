import discord
from discord.ext import commands, tasks
from discord.utils import get
from afks import afks

def remove(afk):
    if "(AFK)" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

class AFK(commands.Cog):
    def __init__(self,bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def afk(self, ctx, *, reason="No Reason Provided"):
        member = ctx.author
        if member.id in afks.keys():
            afks.pop(member.id)
        else:
            try:
                await member.edit(nick=f"[AFK] {member.display_name}")
            except:
                pass
        afks[member.id] = reason
        embed=discord.Embed(title="AFK", description=f"{member.mention} has gone AFK!", color=0x7316F4)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name="#VariOT")
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.add_field(name="Reason", value=f"`{reason}`")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in afks.keys():
            afks.pop(message.author.id)
            try:
                await message.author.edit(nick = remove(message.author.display_name))
            except:
                pass
            embed=discord.Embed(title="AFK", description=f"Welcome back {message.author.mention}, I removed your AFK!", color=0x7316F4)
            embed.set_thumbnail(url=message.author.avatar_url)
            embed.set_author(name="#VariOT")
            embed.set_footer(text=f"Requested by {message.author}")
            await message.channel.send(embed=embed)

        for id, reason in afks.items():
            member = get(message.guild.members, id = id)
            if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
               embed=discord.Embed(title="AFK", description=f"{member.name} is AFK! Reason: `{reason}`", color=0x7316F4)
               await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(AFK(bot))