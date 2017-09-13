import asyncio

import discord
from discord.ext import commands
import json

global data
with open('data/blacklist.json', 'r') as f:
    data = json.loads(f.read())


class Blacklist:
    def __init__(self, Aya):
        self.Aya = Aya

    @commands.group(pass_context=True, invoke_without_command=True)
    async def blacklist(self, ctx):
        """Blacklists a word from the server"""
        self.Aya.say('Available arguments: \n```')

    @blacklist.command(pass_context=True)
    async def add(self, ctx, word: str):
        """Adds a word the blacklist"""
        # with open('data/blacklist.json', 'r') as f:
        #     data = json.loads(f.read())
        word = word.lower()
        data.setdefault(ctx.message.server.id, {})
        if word not in data[ctx.message.server.id]:
            data[ctx.message.server.id].setdefault(word, ctx.message.author.id)
            self.Aya.say(data)
            with open('data/blacklist.json', 'w') as f:
                f.write(json.dumps(data, indent=4))
            await self.Aya.say(word + " has been blacklisted.")
        else:
            await self.Aya.say(word + " is already blacklisted.")

    @blacklist.command(pass_context=True)
    async def remove(self, ctx, word: str):
        """Removes a word from the blacklist"""
        # with open('data/blacklist.json', 'r') as f:
        #     data = json.loads(f.read())
        word = word.lower()
        if word in data[ctx.message.server.id]:
            del data[ctx.message.server.id][word]
            with open('data/blacklist.json', 'w') as f:
                f.write(json.dumps(data, indent=4))
            await self.Aya.say(word + " has been successfully removed from the blacklist.")
        else:
            await self.Aya.say(word + " is not blacklisted.")

    @blacklist.command(pass_context=True)
    async def list(self, ctx):
        """Lists current blacklisted words"""
        # with open('data/blacklist.json', 'r') as f:
        #     data = json.loads(f.read())
        keylist = []
        for key in data[ctx.message.server.id].keys():
            keylist.append(key)
        keylist = ', '.join(keylist)
        await self.Aya.say('Blacklisted words: \n`' + keylist + '`')

    async def on_message(self, message):
        if message.author.id == self.Aya.user.id:
            return
        else:
            if message.server.id in data:
                words = list(map(lambda z: z.lower(), message.content.split()))
                for word in data[message.server.id]:
                    if word in words:
                        try:
                            await self.Aya.delete_message(message)
                            msg = await self.Aya.send_message(message.channel,
                                                              "Watch your language {}! ".format(message.author.mention))
                            await asyncio.sleep(3)
                            await self.Aya.delete_message(msg)
                            return
                        except discord.Forbidden:
                            await self.Aya.send_message(message.channel, "I tried to delete {}'s message,"
                                                                         " but I need permissions to delete messages.".format(message.author.mention))
                            return
                    else:
                        pass
            else:
                return


def setup(Aya):
    Aya.add_cog(Blacklist(Aya))
