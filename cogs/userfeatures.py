import discord
from discord.ext import commands
import datetime
import json


class UserFeatures:
    USER_FILE = "data/bankholders.json"
    DEFAULT_BALANCE = 200
    DEFAULT_PAYDAY = 100
    
    def __init__(self, Aya):
        self.Aya = Aya
        with open(self.USER_FILE, 'r') as f:
            self.data = json.loads(f.read())
            
    def save(self):
        with open(self.USER_FILE, 'w') as f:
            f.write(json.dumps(self.data, indent=4))

    @commands.command(pass_context=True)
    async def register(self, ctx):
        # get the IDs
        user_id = str(ctx.message.author.id)
        guild_id = str(ctx.message.server.id)

        # if user not registered, create an account
        if user_id not in self.data:
            current_time = datetime.datetime.utcnow()
            account = {
                'guild': guild_id,
                'payday': current_time,
                'money': self.DEFAULT_BALANCE
            }
            
            # update the database
            self.data[user_id] = account
            self.save()
                
            await self.Aya.say('Registration complete. Balance: $%d' % account['money'])
            
        # do nothing if they already have an account
        else:
            await self.Aya.say('You already have an account.')

    @commands.command(pass_context=True, aliases=['bal'])
    async def balance(self, ctx):
        # get account info
        user_id = str(ctx.message.author.id)
        serv_owner = ctx.message.server.owner
        if user_id not in self.data:
            return await self.Aya.say('You don\'t have an account, please register using `a.register`')
        account = self.data[user_id]
        
        # create embed
        em = discord.Embed(title='Balance', color=0x2ECC71)
        em.add_field(name='Account Holder', value=ctx.message.author)
        em.add_field(name='Account Balance', value=account['money'])
        
        try:
            await self.Aya.say(embed=em)
        except discord.HTTPException:
            await self.Aya.say('{} I need the embed links permission to send this.'.format(serv_owner.mention))

    @commands.command(pass_context=True)
    async def payday(self, ctx):
        # get account details
        user_id = str(ctx.message.author.id)
        if user_id not in self.data:
            return await self.Aya.say('You don\'t have an account, please register using `a.register`.')
        account = self.data[user_id]
        
        # check if its payday for the user
        now = datetime.datetime.utcnow()
        if (now - account['payday']) > datetime.timedelta(1):
            await self.Aya.say('Its payday! You received %d' % self.DEFAULT_PAYDAY)
            account['payday'] = now
            account['money'] += self.DEFAULT_PAYDAY
            self.save()
        else:
            time_left = now - account['payday']
            await self.Aya.say('You still have ' + time_left + ' until your next payday.')

def setup(Aya):
    Aya.add_cog(UserFeatures(Aya))
