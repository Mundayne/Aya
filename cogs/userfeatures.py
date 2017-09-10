import random
***REMOVED***
***REMOVED***
from datetime import datetime
import time
import os
import json

default_settings = {'PAYDAY_TIME': 86400, 'PAYDAY_AMOUNT': 1000, 'REGISTER_AMOUNT': 500}
account = [False, False***REMOVED***
class UserFeatures:

    def __init__(self, Aya):
        self.Aya = Aya

    def register(self, ctx):
        #read the data from the file and convert it to json
        with open('bankholders.json', 'r') as f:
            data = json.loads(f.read())

        user_id = ctx.message.author.id
        guild_id = ctx.message.server.id

        #if not in data, give money to start off
        if user_id not in data:
            user = {'guild': guild_id, 'money': 100}
            data[user_id***REMOVED*** #add that data to the database

        #save that data back to the database
        with open('bankholders.json', 'w') as f:
            f.write(json.dumps(data))


    @commands.command(pass_context=True)
    async def register(self, ctx):
        # read the data from the file and convert it to json
        with open('data/bankholders.json', 'r') as f:
            data = json.loads(f.read())

        user_id = ctx.message.author.id
        guild_id = ctx.message.server.id

        # if not in data, give money to start off
        if user_id not in data:
            user_account = {'user': user_id, 'guild': guild_id, 'money': 1000}
            await self.Aya.say('Registration complete. Balance: $1000')
***REMOVED***
            await self.Aya.say('You already have an account.')

        # save that data back to the database
        with open('bankholders.json', 'w') as f:
            f.write(json.dumps(data))




def setup(Aya):
    Aya.add_cog(UserFeatures(Aya))