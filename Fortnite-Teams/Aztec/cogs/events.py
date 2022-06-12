import discord
from colorama import Fore as Color
from discord.ext.commands import clean_content
from discord.ext import commands
from discord.utils import get
from afks import afks

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
      print(f"Bot Online! Type a!help for a list of commands.")
      await self.bot.change_presence(activity=discord.Game(name=f"a!help | Watching over Aztec with {len(self.bot.users)} members!"))

  @commands.Cog.listener()
  async def on_member_join(self, member):
    role = discord.utils.get(member.guild.roles, id=907371853545349184)
    await member.add_roles(role)
    channel = self.bot.get_channel(907371854182875266)
    embed=discord.Embed(title=f"__Welcome to Team Aztec!__", description=f"Everyone welcome {member.mention} ({member.name}#{member.discriminator})!", color=0x0000FF)
    embed.add_field(name="We hope you enjoy your stay!", value="Make sure to read the <#907371853662806065>!", inline=False)
    embed.add_field(name="Have fun at Team Aztec!", value="Visit <#907371854182875270> to see our qualifications and make sure to say hello in <#907371854182875266>!", inline=False)
    embed.add_field(name="Visit our Socials here!", value="[___Click Here!___](https://linktr.ee/Team_Aztec)", inline=False)
    embed.set_author(name="#FearAztec!")
    embed.set_footer(text=f"#FearAztec")
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/Cu-6Vr075y-YWB5TtHneN6nrycnA-HwsSZ_h1w_i9eE/https/cdn-longterm.mee6.xyz/plugins/welcome/images/907371853172072500/13e8d3223dabcba7a04b74c930ac6ec0796f9e1936dceec23d09d030f6ae5180.png?width=80&height=80")
    embed.set_image(url="https://images-ext-1.discordapp.net/external/cEnRyq2LdxsoWeTp9R6GxqoQwWh-zqOM66Y-w-B8c98/https/cdn-longterm.mee6.xyz/plugins/welcome/images/907371853172072500/4e9945181599074f03a67a2122b05362a3732fd631e9580db2d4d38b31dc0542.png?width=400&height=225")
    await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_message_edit(self, before, after):
    try:
        await self.bot.process_commands(after)
    except:
        raise Exception

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    embed=discord.Embed(title="Error", description=f"{error}", color=0x000FF)
    await ctx.reply(embed=embed)
    raise error

  @commands.Cog.listener()
  async def on_message(self, message):
        content = message.content.lower()
        if content == "welcome":
            await message.channel.send('Welcome!')
        elif content == "wlc":
            await message.channel.send('Welcome!')
        elif content == "welc":
            await message.channel.send('Welcome!')
        elif content == "Chase":
            await message.channel.send('Ik, Chase is the best developer ever :)')
            print(f"{message.author} said Chase!")

        if message.author.id in afks.keys():
            afks.pop(message.author.id)
            try:
                await message.author.edit(nick = remove(message.author.display_name))
            except:
                pass
            embed=discord.Embed(title="AFK", description=f"Welcome back {message.author.mention}, I removed your AFK!", color=0x0000FF)
            embed.set_thumbnail(url=message.author.avatar.url)
            embed.set_author(name="#FearAztec")
            embed.set_footer(text=f"Requested by {message.author}")
            print(f"{message.author} has came back from AFK!")
            await message.channel.send(embed=embed)

        for id, reason in afks.items():
            member = get(message.guild.members, id = id)
            if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
               embed=discord.Embed(title="AFK", description=f"{member.mention} is AFK! \nReason: `{reason}`", color=0x0000FF)
               embed.set_thumbnail(url=member.avatar.url)
               embed.set_author(name="#FearAztec")
               embed.set_footer(text=f"#FearAztec")
               await message.channel.send(embed=embed)

def setup(bot):
  bot.add_cog(events(bot))