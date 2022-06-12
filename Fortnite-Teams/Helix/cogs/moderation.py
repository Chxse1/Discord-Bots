import discord
from discord.ext import commands
import json
from colorama import Fore as Color

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or(","),
                   intents=intents)
bot.warnings = {}  # guild_id : {member_id: [count, [(admin_id, reason)]]}


class moderation(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(case_insensitive=True,
	                  aliases=['mod'])  # Moderation Help Command
	async def moderation(self, ctx):
		embed = discord.Embed(
		    title="___**Moderation Commands**___",
		    description="**These are Helix's Moderation Commands!**",
		    colour=discord.Colour.random())
		embed.add_field(
		    name="**___Available Commands___**",
		    value="`kick`, `ban`, `unban`, `unlock`, `lock`, `mute`, `unmute`, `warn`, `warnings`",
		    inline=False)
		embed.add_field(name="**___Kick___**",
		                value="Kick a User from the Guild!",
		                inline=False)
		embed.add_field(name="**___Ban___**",
		                value="Bans a User from the Guild!",
		                inline=False)
		embed.add_field(name="**___Unban___**",
		                value="Unbans a User from the Guild!",
		                inline=False)
		embed.add_field(name="**___Unlock___**",
		                value="Unlocks a channel!",
		                inline=False)
		embed.add_field(name="**___Lock___**",
		                value="Locks a channel!",
		                inline=False)
		embed.add_field(name="**___Mute___**",
		                value="Mutes a user!",
		                inline=False)
		embed.add_field(name="**___Unmute___**",
		                value="Unmutes a user!",
		                inline=False)
		embed.add_field(name="**___Warn___**",
		                value="Warns a user!",
		                inline=False)
		embed.add_field(name="**___Warnings___**",
		                value="Shows what warnings a user has!",
		                inline=False)
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Requested by {ctx.author}.")
		print(f"{Color.WHITE} {ctx.author} just used the mod command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await ctx.message.reply(embed=embed, mention_author=False)
        
	@commands.command(aliases=['ub'])  # Unban Command
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, *, member: discord.Member = None):
		if member == None:
			await ctx.message.reply("Please specify a user for me to Unban.", mention_author=False)
			return
		banned_users = await ctx.guild.bans()

		member_name, member_discriminator = member.split('#')
		for ban_entry in banned_users:
			user = ban_entry.user

			if (user.name, user.discriminator) == (member_name,
			                                       member_discriminator):
				await ctx.guild.unban(user)
				embed = discord.Embed(
				    title="User Unbanned",
				    description=f"{user.mention} has been Unbanned. ",
				    colour=discord.Colour.random())
			print(f"{Color.WHITE} {ctx.author} just used the unban command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
			await ctx.message.reply(embed=embed, mention_author=False)

	@commands.command(aliases=['k'])  #Kick Command
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member = None, *, reason=None):
		if member == None:
			await ctx.message.reply("Please specify a user for me to Kick.", mention_author=False)
			return
		if reason == None:
			reason = " No Reason Provided"
		await ctx.guild.kick(member)
		embed = discord.Embed(title="User Kicked",
		                      description=f"{member.mention} has been kicked. ",
		                      colour=discord.Colour.random())
		embed.add_field(name="Reason:", value=f"`{reason}`")
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Kicked by {ctx.author}.")

		embed2 = discord.Embed(title="Kicked", description=f"You have been kicked from `{ctx.guild.name}` by `{ctx.author}`.", colour=discord.Colour.random())
		embed2.add_field(name="Reason:", value=f"{reason}")
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Kicked by {ctx.author}.")
		print(f"{Color.WHITE} {ctx.author} just used the kick command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await ctx.message.reply(embed=embed, mention_author=False)

	@commands.command(aliases=['ul'])
	@commands.has_permissions(manage_channels=True)
	async def unlock(self, ctx, channel: discord.TextChannel = None):
		overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
		overwrite.send_messages = True
		await ctx.channel.set_permissions(ctx.guild.default_role,
		                                  overwrite=overwrite)
		embed = discord.Embed(title='Helix',
		                      description=f'Unlocked `{ctx.channel.name}`')
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Unlocked by {ctx.author}.")
		print(f"{Color.WHITE} {ctx.author} just used the unlock command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await ctx.message.reply(embed=embed, mention_author=False)

	@commands.command(aliases=['l'])
	@commands.has_permissions(manage_channels=True)
	async def lock(self, ctx, channel: discord.TextChannel = None):
		overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
		overwrite.send_messages = False
		await ctx.channel.set_permissions(ctx.guild.default_role,
		                                  overwrite=overwrite)
		embed = discord.Embed(title='Helix',
		                      description=f'Locked `{ctx.channel.name}`')
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Locked by {ctx.author}.")
		print(f"{Color.WHITE} {ctx.author} just used the lock command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await ctx.message.reply(embed=embed, mention_author=False)

	@commands.has_permissions(manage_messages=True)
	@commands.command(aliases=['m'])
	async def mute(self, ctx, member: discord.Member = None, *, reason=None):
		guild = ctx.guild
		mutedRole = discord.utils.get(guild.roles, name="Muted")
		if member == None:
			await ctx.message.reply("Please specify a user for me to mute.", mention_author=False)
			return
		if not mutedRole:
			mutedRole = await guild.create_role(name="Muted")

			for channel in ctx.guild.channels:
				await channel.set_permissions(mutedRole,
				                              speak=False,
				                              send_messages=False,
				                              read_message_history=True,
				                              read_messages=True)
		await member.edit(roles=[mutedRole])
		embed = discord.Embed(title=f"Muted:",
		                      description=f"`{member}` was Muted.")
		embed.add_field(name="Reason:", value=f"`{reason}`")
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Muted by {ctx.author}.")
		await ctx.message.reply(embed=embed, mention_author=False)

		embed2 = discord.Embed(title="Muted", description=f"You have been muted in `{ctx.guild.name}`.", colour=discord.Colour.random())
		embed2.add_field(name=f"You were muted by `{ctx.author}`", value=f"Reason: `{reason}`")
		embed2.set_author(name="Helix is Watching!")
		embed2.set_thumbnail(url=ctx.author.avatar.url)
		embed2.set_footer(text=f"Muted by {ctx.author}.")
		print(f"{Color.WHITE} {ctx.author} just used the mute command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await member.send(embed=embed2)

	@commands.command(aliases=['um'])
	@commands.has_permissions(manage_messages=True)
	async def unmute(self, ctx, member: discord.Member = None):
		mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
		if member == None:
			await ctx.message.reply("Please specify a user for me to Unmute.", mention_author=False)
			return
		await member.remove_roles(mutedRole)
		embed = discord.Embed(title=f"Unmuted:",
		                      description=f"`{member}` has been Unmuted.")
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Unmuted by {ctx.author}.")
		await ctx.message.reply(embed=embed, mention_author=False)

		embed2 = discord.Embed(title="Unmuted", description=f"You have been Unmuted in `{ctx.guild.name}`.", colour=discord.Colour.random())
		embed2.add_field(name=f"You were Unmuted by:", value=f"`{ctx.author}`")
		embed2.set_author(name="Helix is Watching!")
		embed2.set_thumbnail(url=ctx.author.avatar.url)
		embed2.set_footer(text=f"Unmuted by {ctx.author}.")
		print(f"{Color.WHITE} {ctx.author} just used the unmute command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await member.send(embed=embed2)

	@commands.command(aliases=['b'])
	@commands.has_permissions(ban_members = True)
	async def ban(ctx, member:discord.Member=None, *, reason="Unspecified Reason."):
		if member == None:
			embed=discord.Embed(title="Error!", description="Unspecified User!", color=discord.Color.random())
			embed.add_field(name="Please specify a user!", value="Without a user specified, I can't ban anybody!")
			await ctx.message.reply(embed=embed, mention_author=False)
			return
		if member.id == ctx.author.id:
			embed=discord.Embed(title="Error!", description="")
			await ctx.send("You cannot ban yourself!")
			return
    
		if member.top_role >= ctx.author.top_role:
			await ctx.send(f"You can not ban a user with a higher role than you!")         
			return
		else: 
			await member.ban(reason = f"\nBan Command Used By {ctx.author.name}#{ctx.author.discriminator}")
			reasonEmbed = discord.Embed(description = f'Succesfully banned {member.mention} for {reason}\n \n ',color = discord.Color.random)
			reasonEmbed.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url='{}'.format(member.avatar.url))
			reasonEmbed.set_footer(text=f"Banned by {ctx.author.name}", icon_url = '{}'.format(ctx.author.avatar.url))
			await ctx.message.reply(embed=reasonEmbed, mention_author=False)

def setup(bot):
	bot.add_cog(moderation(bot))