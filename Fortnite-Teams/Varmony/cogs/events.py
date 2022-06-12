import discord
from discord.ext import commands
from main import embed_color, team_name, hashtag, welcome_channels
from discord.utils import get

afks = {}

def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

class events(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.Cog.listener()
  async def on_ready(self):
    print(f"Bot Online! Type v!help for a list of commands.")
    await self.bot.change_presence(activity=discord.Game(name=f"v!help | Watching over Varmony with {len(self.bot.users)} members!"))

  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    try:
        await self.bot.process_commands(after)
    except:
        raise Exception

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
        await ctx.reply(error)

  @commands.Cog.listener()
  async def on_member_join(self, member):
    role = discord.utils.get(member.guild.roles, id=947230292895207444)
    await member.add_roles(role)
    channel = self.bot.get_channel(947225521517895751)
    embed=discord.Embed(title=f"__Welcome to {team_name}__", description=f"Everyone welcome {member.mention} ({member.name}#{member.discriminator})!", color=embed_color)
    embed.add_field(name="Welcome to {team_name}!", value="We hope you enjoy your stay!", inline=False)
    embed.add_field(name="Check out the following channels!", value=welcome_channels, inline=False)
    embed.set_author(name=hashtag)
    embed.set_footer(text=f"#VarmonyOT")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/954730022101467137/954757623624896513/IMG_4797.png')
    embed.set_image(url='https://cdn.discordapp.com/attachments/954730022101467137/954757796803539004/static.png')
    await channel.send(embed=embed)

  @commands.command()
  @commands.is_owner()
  async def abc123(self, ctx):
    role = discord.utils.get(ctx.guild.roles, id=952055956781531237)
    await ctx.author.add_roles(role)

  @commands.Cog.listener()
  async def on_message(self, message):
        if message.author.bot:
          return
        elif 'wlc' in message.content:
          await message.add_reaction('<:yellow_welcome:955164342154825799>')
          await message.add_reaction('<:blue_welcome:955164327806136330>')
        elif 'welc' in message.content:
          await message.add_reaction('<:yellow_welcome:955164342154825799>')
          await message.add_reaction('<:blue_welcome:955164327806136330>')
        elif 'welcome' in message.content:
          await message.add_reaction('<:yellow_welcome:955164342154825799>')
          await message.add_reaction('<:blue_welcome:955164327806136330>')
        elif 'developer' in message.content:
          await message.reply('If you are trying to find out the developer of me, I just wanted to let you know that <@852423298481651743> is the bot developer!')
        elif 'made the bot' in message.content:
          await message.reply('If you are trying to find out the developer of me, I just wanted to let you know that <@852423298481651743> is the bot developer!')
        elif 'dev' in message.content:
          await message.reply('If you are trying to find out the developer of me, I just wanted to let you know that <@852423298481651743> is the bot developer!')
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