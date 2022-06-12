import discord
import os
import random
from discord.ext import commands

afks = {}
embed_color = 0x001457
team_name = "Team Arial"
hashtag = "#WeAreArial"
welcome_channels = "<#831098624254541845>, <#876191291912888381>, <#876190757961216090>, <#876190259984076820>, <#876190326606417921>, <#904660682325241876>"
banner_url = "https://cdn-longterm.mee6.xyz/plugins/welcome/images/931616849928519720/3ebc4da446b64c3f31ca437c8d7b75ebcbcd1fff29d10c14f846c31295e5a335.png"
logo_url = "https://cdn.discordapp.com/icons/931616849928519720/666f9076319c866ec6a2a948e57d057c.png?size=1024"
prefix = 'a!'
intents = discord.Intents.all()
owner_ids = [852423298481651743, 927510522738397225]
help_command = None

bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents, help_command=help_command, owner_ids=owner_ids)

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		bot.load_extension(f"cogs.{filename[:-3]}")

bot.run('OTcwMzI5MjUyNzMxOTUzMjEz.Ym6XiQ.D6JIgOS56N1nfIdFAvqJXxgh6FE')
