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
          embed=discord.Embed(title="AFK", description=f"Welcome back {message.author.mention}, I removed your AFK!", color=0x1EEED2)
          embed.set_thumbnail(url=message.author.avatar.url)
          embed.set_footer(text=f"Requested by {message.author}")
          print(f"{message.author} has came back from AFK!")
          await message.channel.send(embed=embed, delete_after=5)

    for id, reason in afks.items():
        member = get(message.guild.members, id = id)
        if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or message.author.id in message.raw_mentions:
            embed=discord.Embed(title="AFK", description=f"{member.mention} is AFK! \nReason: `{reason}`", color=0x1EEED2)
            embed.set_thumbnail(url=message.author.avatar.url)
            await message.channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_ready(self):
    print('We have logged into {0.user}!'.format(self.bot))
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"https://www.zeonbot.com/ | z!help"))

def setup(bot):
  bot.add_cog(Events(bot))