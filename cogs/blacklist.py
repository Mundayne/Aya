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
    @commands.has_permissions(manage_server=True)
    async def blacklist(self, ctx):
        """Blacklists a word from the server"""
        self.Aya.say('Available arguments: \n```a.blacklist add <word>: Adds a word to the blacklist'
                     '\na.blacklist remove <word>: Removes a word from the blacklist.'
                     '\na.blacklist list: Lists currently blacklisted words.')

    @blacklist.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def add(self, ctx, word: str):
        """Adds a word the blacklist"""
        word = word.lower()
        data.setdefault(ctx.message.server.id, {})
        if word not in data[ctx.message.server.id]:
            data[ctx.message.server.id].setdefault(word, ctx.message.author.id)
            with open('data/blacklist.json', 'w') as f:
                f.write(json.dumps(data, indent=4))
            await self.Aya.say(word + " has been blacklisted.")
        else:
            await self.Aya.say(word + " is already blacklisted.")

    @blacklist.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def remove(self, ctx, word: str):
        """Removes a word from the blacklist"""
        try:
            word = word.lower()
            if word in data[ctx.message.server.id]:
                del data[ctx.message.server.id][word]
                with open('data/blacklist.json', 'w') as f:
                    f.write(json.dumps(data, indent=4))
                await self.Aya.say(word + " has been successfully removed from the blacklist.")
            else:
                await self.Aya.say(word + " is not blacklisted.")
        except KeyError:
            await self.Aya.say("You must add a word to the blacklist before invoking this command.")

    @blacklist.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def list(self, ctx):
        """Lists current blacklisted words"""
        keylist = []
        try:
            for key in data[ctx.message.server.id].keys():
                keylist.append(key)
            keylist = ', '.join(keylist)
            await self.Aya.say('Blacklisted words: \n`' + keylist + '`')
        except KeyError:
            await self.Aya.say('You must add a word to the blacklist before invoking this command.')

    async def on_message(self, message):
        serv_owner = message.server.owner
        if message.author.id == self.Aya.user.id:
            return
        else:
            if not message.author.permissions_in(message.channel).manage_server:
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
                                await self.Aya.send_message(message.channel, "{} I tried to delete {}'s message,"
                                                                             " but I need permissions to delete messages.".format(serv_owner.mention, message.author.mention))
                                return
                        else:
                            pass
                else:
                    return
            else:
                return


def setup(Aya):
    Aya.add_cog(Blacklist(Aya))
