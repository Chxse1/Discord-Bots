import discord
from discord.ext import commands
from discord.utils import get
from afks import afks

def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

class Events(commands.Cog):
  def __init__(self,bot:commands.Bot):
      self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot.user:
      return

    elif message.author.id in afks.keys():
          afks.pop(message.author.id)
          try:
              await message.author.edit(nick = remove(message.author.display_name))
          except:
              pass
          embed=discord.Embed(title="AFK", description=f"Welcome back {message.author.mention}, I removed your AFK!", color=0x2140DA)
          embed.set_thumbnail(url=message.author.avatar.url)
          embed.set_footer(text=f"Requested by {message.author}")
          print(f"{message.author} has came back from AFK!")
          await message.channel.send(embed=embed, delete_after=5)

    for id, reason in afks.items():
        member = get(message.guild.members, id = id)
        if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or message.author.id in message.raw_mentions:
            embed=discord.Embed(title="AFK", description=f"{member.mention} is AFK! \nReason: `{reason}`", color=0x2140DA)
            embed.set_thumbnail(url=message.author.avatar.url)
            embed.set_author(name="#VandalsOT!")
            await message.channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_ready(self):
    print('We have logged into {0.user}!'.format(self.bot))
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"over {len(self.bot.users)} users! | v!help"))

  @commands.Cog.listener()
  async def on_member_join(self, ctx, member):
    role = discord.utils.get(member.guild.roles, id=938267173397352508)
    await member.add_roles(role)
    channel = self.bot.get_channel(942578519853137920)
    embed=discord.Embed(title="Welcome", description=f"Everyone welcome {member.mention}({member.name}#{member.discriminator}) to Team Vandals!", color=0x33FFFF)
    embed.add_field(name="We hope you enjoy your stay!", value="Make sure to read the <#940029507157512232>!", inline=False)
    embed.add_field(name="Have fun at Team Visual!", value="Visit <#940029526371614760> to see our qualifications and make sure to say hello in <#942578519853137920>!", inline=False)
    embed.set_author(name="#VandalsOT!")
    embed.set_footer(text=f"Welcome!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/942278525304578069/942609146941952080/logo_1_1.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/942278525304578069/942611790859210772/png.png")
    await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_command_error(self,ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
      embed=discord.Embed(title="Error", description=f"You did not provide the required arguments! | {error}")
      await ctx.message.reply(embed=embed)
    elif isinstance(error,commands.errors.CommandNotFound):
      embed=discord.Embed(title="Error",description=f"No Such Command Found! | {error}")
      await ctx.message.reply(embed=embed)
    elif isinstance(error,commands.errors.NotOwner):
      embed=discord.Embed(title="Error", description=f"You are not the owner of the bot! | {error}")
      await ctx.message.reply(embed=embed)
    else:
      embed=discord.Embed(title="Error", description=error)
      await ctx.message.reply(embed=embed)

def setup(bot):
  bot.add_cog(Events(bot))