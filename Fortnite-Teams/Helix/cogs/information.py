import discord, datetime, time
from discord.ext import commands
from colorama import Fore as Color

start_time = time.time()


class information(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()  # Help Command
	async def info(self, ctx):
		embed = discord.Embed(
		    title="___**Information Commands**___",
		    description="**These are Helix's Information Commands!**",
		    colour=discord.Colour.random())
		embed.add_field(
		    name="**___Available Commands___**",
		    value=
		    "`botinfo`, `userinfo`, `serverinfo`, `invite`, `support`, `ping`, `links`",
		    inline=False)
		embed.add_field(name="**___Botinfo___**",
		                value="Shows you info on Helix!",
		                inline=False)
		embed.add_field(name="**___Userinfo___**",
		                value="Shows you info on someone!",
		                inline=False)
		embed.add_field(name="**___Serverinfo___**",
		                value="Shows you info on this server!",
		                inline=False)
		embed.add_field(name="**___Invite___**",
		                value="Gives an invite link to invite Helix!",
		                inline=False)
		embed.add_field(name="**___Support___**",
		                value="Gives you Helix's Support Server!",
		                inline=False)
		embed.add_field(name="**___Ping___**",
		                value="Shows bot latency of Helix!",
		                inline=False)
		embed.add_field(name="**___Uptime___**",
		                value="Shows the Uptime of Helix!",
		                inline=False)
		embed.add_field(name="**___Links___**",
		                value="Shows all the links you might need for Helix!",
		                inline=False)
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Requested by {ctx.author}.")
		print(f"{Color.WHITE} {ctx.author} just used the info command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await ctx.message.reply(embed=embed, mention_author=False)    
        
	@commands.command(aliases=['link'])
	async def links(self, ctx):
		embed = discord.Embed(title="___**Links**___", description="**Here are all of the links you may need for Helix!**", colour=discord.Colour.random())
		embed.add_field(name="Invite Link!", value="[___Click Here!___](https://discord.com/api/oauth2/authorize?client_id=899887955211071498&permissions=268553335&scope=bot)", inline=False)    
		embed.add_field(name="Support Server!", value="[___Click Here!___](https://discord.gg/75e2uhvhdR)", inline=False)
		embed.add_field(name="Website!", value="[___Click Here!___](https://sites.google.com/view/helixdiscordbot/home)", inline=False)
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Requested by {ctx.author}.")
		print(f"{Color.WHITE} {ctx.author} just used the links command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await ctx.message.reply(embed=embed, mention_author=False)
        
	@commands.command(aliases=['inv'])
	async def invite(self, ctx):
		embed = discord.Embed(title="**___Invite___**",
		                      description="Invite Link for Helix!",
		                      colour=discord.Colour.random())
		embed.add_field(
		    name="**Helix's Invite Link**",
		    value=
		    "[___Click Here!___](https://discord.com/api/oauth2/authorize?client_id=899887955211071498&permissions=268553335&scope=bot)",
		    inline=False)
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Requested By {ctx.author}")
		print(f"{Color.WHITE} {ctx.author} just used the invite command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await ctx.message.reply(embed=embed, mention_author=False)

	@commands.command(aliases=['server', 's'])
	async def support(self, ctx):
		embed = discord.Embed(title="**___Support___**",
		                      description="Support Server for Helix!",
		                      colour=discord.Colour.random())
		embed.add_field(name="**Helix's Server**",
		                value="[___Click Here!___](https://discord.gg/75e2uhvhdR)",
		                inline=False)
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Requested By {ctx.author}")
		print(f"{Color.WHITE} {ctx.author} just used the support command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await ctx.message.reply(embed=embed, mention_author=False)

	@commands.command()
	async def ping(self, ctx: commands.Context):
		start_time = time.time()
		end_time = time.time()
		embed = discord.Embed(
		    title="**___Pong!___** :ping_pong:",
		    description="Hello there! Bot latency can be found below!",
		    colour=discord.Colour.random())
		embed.add_field(name="**Bot Latency**",
		                value=f"`{round(self.bot.latency * 1000)}`ms",
		                inline=False)
		embed.add_field(name="**API Latency**",
		                value=f"`{round((end_time - start_time) * 1000)}`ms",
		                inline=False)
		embed.set_author(name="Helix is Watching!")
		embed.set_thumbnail(url=ctx.author.avatar.url)
		embed.set_footer(text=f"Requested By {ctx.author}")
		print(f"{Color.WHITE} {ctx.author} just used the ping command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await ctx.message.reply(embed=embed, mention_author=False)

	@commands.command(aliases=['whois', 'ui'])
	async def userinfo(self, ctx, *, user: discord.Member = None):
		if user is None:
			user = ctx.author
		date_format = "%a, %d %b %Y %I:%M %p"
		embed = discord.Embed(description=user.mention)
		embed.set_author(name=str(user), icon_url=user.avatar.url)
		embed.set_thumbnail(url=user.avatar.url)
		embed.add_field(name="Joined",
		                value=user.joined_at.strftime(date_format))
		members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
		embed.add_field(name="User ID", value=f'{user.id}')
		embed.add_field(name="Registered",
		                value=user.created_at.strftime(date_format))
		if len(user.roles) > 1:
			role_string = ' '.join([r.mention for r in user.roles][1:])
			embed.add_field(name="Roles [{}]".format(len(user.roles) - 1),
			                value=role_string,
			                inline=False)
		perm_string = ', '.join([
		    str(p[0]).replace("_", " ").title() for p in user.guild_permissions
		    if p[1]
		])
		embed.add_field(name="Guild permissions",
		                value=perm_string,
		                inline=False)
		embed.set_footer(
		    text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}',
		    icon_url=ctx.author.avatar.url)
		print(f"{Color.WHITE} {ctx.author} just used the userinfo command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		return await ctx.message.reply(embed=embed, mention_author=False)

	@commands.command(aliases=["si"])
	async def serverinfo(self, ctx):
		embed = discord.Embed(title="Server Info", description="Here is the information to this server!")
		embed.add_field(name="Server Name", value=f'`{ctx.guild.name}`', inline=False)
		embed.add_field(name="Server ID", value=f'`{ctx.guild.id}`', inline=True)
		embed.add_field(name="Creation Date", value=f'`{ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p")}`', inline=False)
		embed.add_field(name="Server Owner", value=f'`{ctx.guild.owner}`', inline=False)
		embed.add_field(name="Role Amount", value=f'`{len(ctx.guild.roles)}`', inline=False)
		embed.add_field(name="Channel Amount", value=f'`{len(ctx.guild.channels)}`', inline=False)
		embed.add_field(name="Membercount", value=f'`{len(ctx.guild.members)}`', inline=False)
		embed.set_thumbnail(url=ctx.guild.icon_url)
		embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar.url)
		print(f"{Color.WHITE} {ctx.author} just used the serverinfo command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
		await ctx.message.reply(embed=embed, mention_author=False)


def setup(bot):
	bot.add_cog(information(bot))