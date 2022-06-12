import discord

import datetime

import asyncio

from discord.ext import commands

from main import hashtag, embed_color

from discord.commands import slash_command



snipe_message_content = None

snipe_message_author = None

snipe_message_id = None



class snipe(commands.Cog):

  def __init__(self, bot):

      self.bot = bot



  @commands.Cog.listener()

  async def on_message_delete(self, message):

    if (message.author.bot):
      return

    else:

      log_channel = self.bot.get_channel(967862848850132992)

      embed=discord.Embed(title=f">>> Deleted Message", description=f"```{message.content}```", color=0x071029)

      embed.add_field(name=f"Channel: ", value=f"<#{message.channel.id}> | `{message.channel.id}`")

      embed.set_author(name=f"{message.author} | {message.author.id}", icon_url=message.author.avatar.url)

      embed.set_footer(text=f"""• Today at {datetime.datetime.today().strftime("%I:%M %p")}""")

      await log_channel.send(embed=embed)



      global snipe_message_content

      global snipe_message_author

      global snipe_message_author_id

      global snipe_message_id



      snipe_message_content = message.content

      snipe_message_author = message.author.name

      snipe_message_author_id = message.author.discriminator

      snipe_message_id = message.id
 
      await asyncio.sleep(60)



      if message.id == snipe_message_id:

        snipe_message_author = None

        snipe_message_content = None

        snipe_message_id = None



  @commands.command(aliases=['s'])

  @commands.cooldown(1, 5, commands.BucketType.user)

  async def snipe(self, message):

    if snipe_message_content==None:

      await message.channel.send("Theres nothing to snipe.")

    else:

      embed = discord.Embed(title="Sniped!", description="Here is the message that was deleted!", color=embed_color)

      embed.add_field(name="Author", value=f"`{snipe_message_author}#{snipe_message_author_id}`", inline=False)

      embed.add_field(name="Content:", value=f"`{snipe_message_content}`", inline=False)

      embed.set_footer(text=f"Requested by {message.author}", icon_url=message.author.avatar.url)

      embed.set_author(name=hashtag)

      await message.channel.send(embed=embed)

      print(f"{message.author} used the snipe command | {message.channel}")



  @slash_command(name="snipe", description="Snipe the deleted message!")

  async def _snipe(self, message):

    if snipe_message_content==None:

      await message.respond("Theres nothing to snipe.")

    else:

      embed = discord.Embed(title="Sniped!", description="Here is the message that was deleted!", color=embed_color)

      embed.add_field(name="Author", value=f"`{snipe_message_author}#{snipe_message_author_id}`", inline=False)

      embed.add_field(name="Content:", value=f"`{snipe_message_content}`", inline=False)

      embed.set_footer(text=f"Requested by {message.author}", icon_url=message.author.avatar.url)

      embed.set_author(name=hashtag)

      await message.respond(embed=embed)

      print(f"{message.author} used the snipe command | {message.channel}")



def setup(bot):

  bot.add_cog(snipe(bot))
