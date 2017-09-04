import random
import discord
from discord.ext import commands
from datetime import datetime
import time

default_settings = {'PAYDAY_TIME': 86400, 'PAYDAY_AMOUNT': 1000, 'REGISTER_AMOUNT': 500}
account = [False, False, False]

class UserFeatures:

    def __init__(self, Aya):
        self.Aya = Aya


    @commands.command(pass_context=True)
    async def register(self, ctx):
        author = ctx.message.author
        '''Register a bank account'''
        if account == False:
            balance = 0
            account = True
            await self.Aya.say('Registration complete')
        else:
            await self.Aya.say('{}You already have an account.'.format(author.mention))
    async def payday(self, ctx):
        '''Gives you money every 24 hours'''
        author = ctx.message.author
        if account == True:
            balance += 1000
            await self.Aya.say('{} You earned ${}. Wait 24 hours for your next payday.'.format(author.mention, default_settings['PAYDAY_AMOUNT']))
        else:
            await self.Aya.say('{} You don\'t have an account yet. Type `sa.register` to create an account.'.format(author.mention))

    @commands.command(pass_context=True)
    async def balance(self, ctx):
        author = ctx.message.author
        if account == True:
            await self.Aya.say('{} Your balance is ' + balance + '.'.format(author.mention))
        else:
            await self.Aya.say('{} You don\'t have an account yet. Type `sa.register` to create an account.'.format(author.mention))


def setup(Aya):
    Aya.add_cog(UserFeatures(Aya))