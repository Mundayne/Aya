import random

***REMOVED***
***REMOVED***


class Mod:
    """ Moderation tools """

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True)
    async def kick(self, ctx, *, member):
        """ To kick someone out of the server """
        kickmsg = ['Poor %s is out!', 'These people don\'t understand!', 'Seeya %s!'***REMOVED***
***REMOVED***
            await self.Aya.kick(member)
            await self.Aya.say(random.choice(kickmsg) % member)
        except discord.Forbidden:
            await self.Aya.send_message(ctx.message.channel, '{}: Who do you think you are?'
                                        .format(ctx.message.author))

    @commands.command(pass_context=True)
    async def ban(self, ctx, *, member):
        banmsg = ['We won\'t see %s again!', 'These people really really don\'t understand', 'See you never %s!'***REMOVED***
***REMOVED***
            await self.Aya.ban(member, delete_message_days=1)
            await self.Aya.say(random.choice(banmsg) % member)
        except discord.Forbidden:
            await self.Aya.send_message(ctx.message.channel, '{}: Who do you really think you are ?'
                                        .format(ctx.message.author))

    @commands.command(pass_context=True)
    async def unban(self, ctx, *, member):
        unbanmsg = ['%s is back from hell!', 'Welcome back! %s'***REMOVED***
***REMOVED***
            await self.Aya.unban(discord.Server, member)
            await self.Aya.say(random.choice(unbanmsg) % member)
        except discord.Forbidden:
            await self.Aya.send_message(ctx.message.channel, '{} : You don\'t understand how this place work, do you ?'
                                        .format(ctx.message.author))


def setup(Aya):
    Aya.add_cog(Mod(Aya))
