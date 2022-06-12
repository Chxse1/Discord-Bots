import discord
from discord.ext import commands
from main import embed_color, team_name, hashtag, welcome_channels, banner_url, logo_url, afks
from discord.utils import get

def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

class events(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
      
  @commands.Cog.listener()
  async def on_connect(self):
    print("Connecting!")
    await self.bot.change_presence(activity=discord.Game(name=f"Starting Up! Give me a few seconds!"))

  @commands.Cog.listener()
  async def on_ready(self):
    print(f"Bot Online! Type a!help for a list of commands.")
    await self.bot.change_presence(activity=discord.Game(name=f"a!help | Watching over {team_name} with {len(self.bot.users)} members!"))

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error,commands.errors.CommandNotFound):
        embed=discord.Embed(title="Error", description="This is not a command! Try again!", color=embed_color)
        await ctx.message.reply(embed=embed)
    elif isinstance(error,commands.errors.NotOwner):
        embed=discord.Embed(title="Error", description="You are not an owner of the bot, you can't use this command!", color=embed_color)
        await ctx.message.reply(embed=embed)
    elif isinstance(error,commands.errors.MissingPermissions):
        embed=discord.Embed(title="Error", description="You are missing the required permissions!", color=embed_color)
        await ctx.message.reply(embed=embed)
    elif isinstance(error,commands.errors.CommandOnCooldown):
        embed=discord.Embed(title="Error", description="You are on cooldown for this command! Wait at least 5 seconds, and try again!", color=embed_color)
        await ctx.message.reply(embed=embed)
    else:
        raise error
        await ctx.reply(error)

  @commands.command()
  @commands.is_owner()
  async def abc123(self, ctx):
    role = discord.utils.get(ctx.guild.roles, id=952055956781531237)
    await ctx.author.add_roles(role)

  @commands.Cog.listener()
  async def on_message(self, message):
        content = message.content.lower()
        if 'wlc' in content:
          await message.add_reaction('<a:Exclamation:823505313902100521>')
          await message.add_reaction('<a:BlueBlackVerify:833562049794670640>')
          await message.add_reaction('<a:BOOST:858553108748828692>')
        elif 'welc' in content:
          await message.add_reaction('<a:Exclamation:823505313902100521>')
          await message.add_reaction('<a:BlueBlackVerify:833562049794670640>')
          await message.add_reaction('<a:BOOST:858553108748828692>')
        elif 'welcome' in content:
          await message.add_reaction('<a:Exclamation:823505313902100521>')
          await message.add_reaction('<a:BlueBlackVerify:833562049794670640>')
          await message.add_reaction('<a:BOOST:858553108748828692>')
        elif message.author.id in afks.keys():
            afks.pop(message.author.id)
            try:
                await message.author.edit(nick = remove(message.author.display_name))
            except:
                pass
            embed=discord.Embed(title="AFK", description=f"Welcome back {message.author.mention}, I removed your AFK!", color=embed_color)
            embed.set_thumbnail(url=message.author.avatar.url)
            embed.set_author(name=hashtag)
            embed.set_footer(text=f"Requested by {message.author}")
            await message.channel.send(embed=embed)

        for id, reason in afks.items():
            member = get(message.guild.members, id = id)
            if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
               embed=discord.Embed(title="AFK", description=f"{member.name} is AFK! Reason: `{reason}`", color=embed_color)
               await message.channel.send(embed=embed)

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
        embed=discord.Embed(title="AFK", description=f"{member.mention} has gone AFK!", color=embed_color)
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_author(name=hashtag)
        embed.set_footer(text=f"Requested by {ctx.author}")
        embed.add_field(name="Reason", value=f"`{reason}`")
        print(f"{ctx.author} used the afk command | {ctx.channel}")
        await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(events(bot))
