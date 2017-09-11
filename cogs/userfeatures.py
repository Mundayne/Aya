import discord
from discord.ext import commands
import datetime
import json


class UserFeatures:
    def __init__(self, Aya):
        self.Aya = Aya


    @commands.command()
    async def register(self, ctx):
        # read the data from the file and convert it to json
        with open('data/bankholders.json', 'r') as f:
            data = json.loads(f.read())
        # get the IDs
        user_id = str(ctx.message.author.id)
        guild_id = discord.Guild.id

        # if not in data, give money to start off
        if user_id not in data:
            user = {'user': user_id, 'guild': guild_id, 'money': 200}
            data[user_id] = user
            global pdcollect
            pdcollect = False
            await ctx.send('Registration complete. Balance: $200')
        else:
            await ctx.send('You already have an account.')

        # save that data back to the database
        with open('data/bankholders.json', 'w') as f:
            f.write(json.dumps(data, indent=4))

    @commands.command(aliases=['bal'])
    async def balance(self, ctx):
        user_id = str(ctx.message.author.id)
        with open('data/bankholders.json', 'r') as f:
            data = json.loads(f.read())
        em = discord.Embed(title='Balance', color=0x2ECC71)
        em.add_field(name='Account Holder', value=discord.Message.author)
        em.add_field(name='Account Balance', value=data[user_id]['money'])
        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            await ctx.send('{} I need the embed links permission to send this.'.format(serv_owner))

    @commands.command()
    async def payday(self, ctx):
        user_id = str(ctx.message.author.id)
        with open('data/bankholders.json', 'r') as f:
            data = json.loads(f.read())
        global pdcollect
        if pdcollect == False:
            pdcollect = True
        else:
            pass


def setup(Aya):
    Aya.add_cog(UserFeatures(Aya))
