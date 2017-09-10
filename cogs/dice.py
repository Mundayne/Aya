import random
***REMOVED***
***REMOVED***


class Dice:
    '''Roll a certain number of dice'''

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True, aliases=['rolldice', 'diceroll'***REMOVED***)
    async def dice(self, ctx, number_of_dice=1):
        '''Rolls a certain number of dice'''
        serv_owner = ctx.message.server.owner
        fmt = ''
        for i in range(1, number_of_dice + 1):
            fmt += '`Dice {}: {}`\n'.format(i, random.randint(1, 6))
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:***REMOVED***, 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color, title='Roll a certain number of dice', description=fmt)
***REMOVED***
            await self.Aya.say(embed=em)
        except discord.HTTPException:
            await self.Aya.say('{} I need the embed links permission to send this.'.format(serv_owner.mention))



def setup(Aya):
    Aya.add_cog(Dice(Aya))
