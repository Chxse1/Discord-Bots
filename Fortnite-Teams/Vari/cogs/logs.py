

import discord

import datetime

from datetime import date

from main import embed_color, team_name, hashtag, welcome_channels, banner_url, logo_url

from discord.ext import commands



class logs(commands.Cog):

  def __init__(self, bot):

    self.bot = bot



  @commands.Cog.listener()

  async def on_ready(self):

    print("Ready!")


  @commands.Cog.listener()
  async def on_message_edit(self, ctx, after):
    try:
        await self.bot.process_commands(after)
    except:
        raise Exception
    if (ctx.author.bot):
      return
    else:
      log_channel = self.bot.get_channel(970217179066798131)

      embed=discord.Embed(title=f">>> Edited Message", description=f"[**__Jump to Message__**](https://discordapp.com/channels/{ctx.guild.id}/{ctx.channel.id}/{after.id})\nBefore:```{ctx.content}```After:```{after.content}```", color=0x071029)

      embed.add_field(name=f"Channel: ", value=f"<#{ctx.channel.id}> | `{ctx.channel.id}`")

      embed.set_author(name=f"{ctx.author} | {ctx.author.id}", icon_url=ctx.author.avatar.url)

      embed.set_footer(text=f"""• Today at {datetime.datetime.today().strftime("%I:%M %p")}""")

      await log_channel.send(embed=embed)



  @commands.Cog.listener()

  async def on_guild_channel_create(self, channel):

    log_channel = self.bot.get_channel(970217179066798131)

    embed=discord.Embed(title=f">>> Channel Created", description=f"[**__Jump to Channel__**](https://discordapp.com/channels/{channel.guild.id}/{channel.id})\nChannel Created: ```#{channel.name} | {channel.id}```", color=0x071029)

    embed.set_author(name=f"{channel.guild.name}", icon_url=channel.guild.icon.url)

    embed.set_footer(text=f"""• Today at {datetime.datetime.today().strftime("%I:%M %p")}""")

    await log_channel.send(embed=embed)



  @commands.Cog.listener()

  async def on_guild_channel_delete(self, channel):

    log_channel = self.bot.get_channel(970217179066798131)

    embed=discord.Embed(title=f">>> Channel Deleted", description=f"Channel Deleted: ```#{channel.name} | {channel.id}```", color=0x071029)

    embed.set_author(name=f"{channel.guild.name}", icon_url=channel.guild.icon.url)

    embed.set_footer(text=f"""• Today at {datetime.datetime.today().strftime("%I:%M %p")}""")

    await log_channel.send(embed=embed)



  @commands.Cog.listener()

  async def on_member_join(self, user):
  
    role = discord.utils.get(user.guild.roles, id=970215180027953162)
    await user.add_roles(role)
    channel = self.bot.get_channel(970215202094198865)
    embed=discord.Embed(title=f"__Welcome to {team_name}__", description=f"Everyone welcome {user.mention} ({user.name}#{user.discriminator})!", color=embed_color)
    embed.add_field(name=f"Welcome to {team_name}!", value="We hope you enjoy your stay!", inline=False)
    embed.add_field(name="Check out the following channels!", value=welcome_channels, inline=False)
    embed.add_field(name="Membercount", value=f"`{len(user.guild.members)}`")
    embed.set_author(name=team_name)
    embed.set_footer(text=hashtag)
    embed.set_thumbnail(url=logo_url)
    embed.set_image(url=banner_url)
    await channel.send(embed=embed)

    log_channel = self.bot.get_channel(970217179066798131)

    embed=discord.Embed(title=f">>> Member Joined", description=f"Member Joined: ```{user} | {user.id}```Created At: ```{user.created_at.strftime('%Y-%m-%d %H:%M:%S %p')}```", color=0x071029)

    embed.set_author(name=f"{user}", icon_url=user.avatar.url)

    embed.set_footer(text=f"""• Today at {datetime.datetime.today().strftime("%I:%M %p")}""")

    await log_channel.send(embed=embed)



  @commands.Cog.listener()

  async def on_member_remove(self, user):

    log_channel = self.bot.get_channel(970217179066798131)

    embed=discord.Embed(title=f">>> Member Left", description=f"Member Left: ```{user} | {user.id}```Left At: ```Today at {datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}```", color=0x071029)

    embed.set_author(name=f"{user}", icon_url=user.avatar.url)

    embed.set_footer(text=f"""• Today at {datetime.datetime.today().strftime("%I:%M %p")}""")

    await log_channel.send(embed=embed)



  @commands.Cog.listener()

  async def on_guild_role_create(self, role):

    log_channel = self.bot.get_channel(970217179066798131)

    embed=discord.Embed(title=f">>> Role Created", description=f"Role Created: ```{role.name} | {role.id}```", color=0x071029)

    embed.set_author(name=f"{role.guild.name}", icon_url=role.guild.icon.url)

    embed.set_footer(text=f"""• Today at {datetime.datetime.today().strftime("%I:%M %p")}""")

    await log_channel.send(embed=embed)



  @commands.Cog.listener()

  async def on_guild_role_update(self, role, after):

    log_channel = self.bot.get_channel(970217179066798131)

    embed=discord.Embed(title=f">>> Role Updated", description=f"ID: ```{role.id}``` Role Before: ```{role.name}```Role After:```{after.name}```", color=0x071029)

    embed.set_author(name=f"{role.guild.name}", icon_url=role.guild.icon.url)

    embed.set_footer(text=f"""• Today at {datetime.datetime.today().strftime("%I:%M %p")}""")

    await log_channel.send(embed=embed)



  @commands.Cog.listener()

  async def on_guild_role_delete(self, role):

    log_channel = self.bot.get_channel(970217179066798131)

    embed=discord.Embed(title=f">>> Role Deleted", description=f"Role Deleted: ```{role.name}```", color=0x071029)

    embed.set_author(name=f"{role.guild.name}", icon_url=role.guild.icon.url)

    embed.set_footer(text=f"""• Today at {datetime.datetime.today().strftime("%I:%M %p")}""")

    await log_channel.send(embed=embed)



def setup(bot):

  bot.add_cog(logs(bot))
