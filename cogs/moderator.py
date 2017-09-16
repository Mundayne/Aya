import random
import discord
from discord.ext import commands
import json
import asyncio

global data
with open('data/blacklist.json', 'r') as f:
    data = json.loads(f.read())

class Mod:
    """Moderation tools"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True)
    async def kick(self, ctx, *, member):
        """Kicks someone out of the server"""
        kickmsg = ['Poor %s is out!', 'These people don\'t understand!', 'Cya %s!']
        try:
            await self.Aya.kick(member)
            await self.Aya.say(random.choice(kickmsg) % member)
        except discord.Forbidden:
            await self.Aya.send_message(ctx.message.channel, '{}: Who do you think you are?'
                                        .format(ctx.message.author))

    @commands.command(pass_context=True)
    async def ban(self, ctx, member: discord.Member):
        '''Ban someone from the server.'''
        try:
            await self.Aya.ban(member)
            await self.Aya.say('Banned {} from the server.'.format(member))
        except:
            await self.Aya.say('You don\'t have the permission to ban members.')


    def find_user(self, bans, member):
        return [user for user in bans if user.id == member or user.name.lower() == member.lower()]

    async def _unban(self, ctx, server, user):
        try:
            await self.Aya.unban(server, user)
            await self.Aya.say('Unbanned {} from the server.'.format(user))
        except:
            await self.Aya.say('You don\'t have the permission to unban members.')

    @commands.command(pass_context=True)
    async def unban(self, ctx, member: str):
        '''Unban someone using their user ID or name.'''
        server = ctx.message.server
        try:
            bans = await self.Aya.get_bans(server)
        except:
            await self.Aya.say('You don\'t have the permission to see the bans.')
            return

        users = self.find_user(bans, member)
        print(users)
        print([user.name for user in bans])

        if len(users) > 1:
            return await self.Aya.say('Multiple users found.')
        if len(users) < 1:
            return await self.Aya.say('User not found.')

        await self._unban(ctx, server, users[0])

    @commands.command(pass_context=True)
    async def bans(self, ctx):
        '''See a list of banned users.'''
        server = ctx.message.server
        try:
            bans = await self.Aya.get_bans(server)
        except:
            await self.Aya.say('You don\'t have the permission to see the bans.')
        else:
            await self.Aya.say('**List of banned users:**```bf\n{}\n```'.format(
                ', '.join([str(u) for u in bans])))

    @commands.group(pass_context=True, invoke_without_command=True)
    @commands.has_permissions(manage_server=True)
    async def filter(self, ctx):
        """Filters a word from the server"""
        self.Aya.say('Available arguments: \n```a.blacklist add <word>: Adds a word to the filter list'
                     '\na.blacklist remove <word>: Removes a word from the filter list.'
                     '\na.blacklist list: Lists current filtered words.')

    @filter.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def add(self, ctx, word: str):
        """Adds a word the filter list"""
        word = word.lower()
        data.setdefault(ctx.message.server.id, {})
        if word not in data[ctx.message.server.id]:
            data[ctx.message.server.id].setdefault(word, ctx.message.author.id)
            with open('data/blacklist.json', 'w') as f:
                f.write(json.dumps(data, indent=4))
            await self.Aya.say(word + " has been filtered.")
        else:
            await self.Aya.say(word + " is already filtered.")

    @filter.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def remove(self, ctx, word: str):
        """Removes a word from the filter list"""
        try:
            word = word.lower()
            if word in data[ctx.message.server.id]:
                del data[ctx.message.server.id][word]
                with open('data/blacklist.json', 'w') as f:
                    f.write(json.dumps(data, indent=4))
                await self.Aya.say(word + " has been successfully removed from the filter list.")
            else:
                await self.Aya.say(word + " is not filtered.")
        except KeyError:
            await self.Aya.say("You must add a word to the filter list before invoking this command.")

    @filter.command(pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def list(self, ctx):
        """Lists current filtered words"""
        keylist = []
        try:
            for key in data[ctx.message.server.id].keys():
                keylist.append(key)
            keylist = ', '.join(keylist)
            await self.Aya.say('Filtered words: \n`' + keylist + '`')
        except KeyError:
            await self.Aya.say('You must add a word to the filter list before invoking this command.')

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
                                                                  "Watch your language {}! ".format(
                                                                      message.author.mention))
                                await asyncio.sleep(3)
                                await self.Aya.delete_message(msg)
                                return
                            except discord.Forbidden:
                                await self.Aya.send_message(message.channel, "{} I tried to delete {}'s message,"
                                                                             " but I need permissions to delete messages.".format(
                                    serv_owner.mention, message.author.mention))
                                return
                        else:
                            pass
                else:
                    return
            else:
                return

    @commands.command(aliases=['p'], pass_context=True)
    @commands.has_permissions(manage_server=True)
    async def purge(self, ctx, msgs: int = 100):
        '''Shortcut to clean all your messages.'''
        await self.Aya.delete_message(ctx.message)
        if msgs < 10000:
            async for message in self.Aya.logs_from(ctx.message.channel, limit=msgs):
                try:
                    await self.Aya.delete_message(message)
                    msg = await self.Aya.say('**'+str(msgs)+' messages** were successfully deleted.')
                    asyncio.sleep(3)
                    await self.Aya.delete_message(msg)
                except:
                    pass
        else:
            await self.Aya.send_message(ctx.message.channel, 'Too many messages to delete. Enter a number < 10000')

    @commands.command(aliases=['c'], pass_context=True)
    async def clean(self, ctx, msgs: int):
        '''Shortcut to clean all your messages.'''
        await self.Aya.delete_message(ctx.message)
        if msgs < 10000:
            async for message in self.Aya.logs_from(ctx.message.channel, limit=msgs):
                try:
                    if message.author == self.Aya.user:
                        await self.Aya.delete_message(message)
                except:
                    pass
        else:
            await self.Aya.send_message(ctx.message.channel, 'Too many messages to delete. Enter a number < 10000')


def setup(Aya):
    Aya.add_cog(Mod(Aya))
