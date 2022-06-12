import discord
import os
import datetime
import json
import random
from discord.ext import commands

class economy(commands.Cog):
  def __init__(self,bot:commands.Bot):
      self.bot = bot

  @commands.command(aliases=['bal'])
  async def balance(self, ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    embed = discord.Embed(title="Balance", description=f"`{ctx.author}`'s balance!", color = discord.Color.red())
    embed.add_field(name="Wallet Balance", value=f"`{wallet_amt}`")
    embed.add_field(name='Bank Balance',value=f"`{bank_amt}`")
    await ctx.reply(embed=embed)

  @commands.command()
  async def beg(self, ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    embed=discord.Embed(title="Beg", description=f"{ctx.author} got `{earnings}` coins!", color=0xFFFFF)
    
    await ctx.reply(embed=embed)

    users[str(user.id)]["wallet"] += earnings

    with open("bank.json",'w') as f:
        json.dump(users,f)


  @commands.command(aliases=['with'])
  async def withdraw(self, ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        embed=discord.Embed(title="Error", description="No amount specified!", color=0xFFFFFF)
        await ctx.reply(embed=embed)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        embed=discord.Embed(title="Error", description="Insufficient balance!", color=0xFFFFFF)
        await ctx.reply(embed=embed)
        return
    if amount < 0:
        embed=discord.Embed(title="Error", description="This has to be a positive number!", color=0xFFFFFF)
        await ctx.reply(embed=embed)
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    embed=discord.Embed(title="Withdraw", description=f"{ctx.author.mention} has withdrew `{amount}` coins!", color=0xFFFFFF)
    await ctx.reply(embed=embed)


  @commands.command(aliases=['dep'])
  async def deposit(self, ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        embed=discord.Embed(title="Error", description="No amount specified!", color=0xFFFFFF)
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        embed=discord.Embed(title="Error", description="Insufficient balance!", color=0xFFFFFF)
        return
    if amount < 0:
        embed=discord.Embed(title="Error", description="This must be a positive number!", color=0xFFFFFF)
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    embed=discord.Embed(title="Deposit", description=f"{ctx.author.mention} has deposited `{amount}` coins!", color=0xFFFFFF)
    await ctx.reply(embed=embed)


  @commands.command()
  async def send(self, ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        embed=discord.Embed(title="Error", description="No amount specified!", color=0xFFFFFF)
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        embed=discord.Embed(title="Error", description="Unsufficient balance!", color=0xFFFFFF)
        return
    if amount < 0:
        embed=discord.Embed(title="Error", description="This must be a positive number!", color=0xFFFFFF)
        await ctx.reply(embed=embed)
        return

    await update_bank(ctx.author,-1*amount,'bank')
    await update_bank(member,amount,'bank')
    embed=discord.Embed(title="Send", description=f"{ctx.author.mention} has given {member.mention} `{amount}` coins!", color=0xFFFFFF)
    await ctx.reply(embed=embed)


  @commands.command(aliases=['rb'])
  async def rob(self, ctx, user:discord.Member):
    await open_account(ctx.author)
    await open_account(user)
    bal = await update_bank(user)

    if bal[0]<100:
        embed=discord.Embed(title="Error", description="This user has less than 100 coins, making it useless to rob them!", color=0xFFFFFF)
        await ctx.reply(embed=embed)
        return

    earning = random.randrange(0,bal[0])

    await update_bank(ctx.author,earning)
    await update_bank(user,-1*earning)
    embed=discord.Embed(title="Rob", description=f"{ctx.author.mention} robbed {user.mention} and got `{earning}` coins!", color=0xFFFFFF)
    await ctx.reply(embed=embed)

async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('bank.json','w') as f:
        json.dump(users,f)

    return True


async def get_bank_data():
    with open('bank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('bank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal

def setup(bot):
  bot.add_cog(economy(bot))