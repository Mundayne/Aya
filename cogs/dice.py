import random
import discord
from discord.ext import commands


class Dice:
    '''Roll a certain number of dice'''

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True)
    async def dice(self, ctx, number_of_dice=1):
        '''Rolls a certain number of dice'''
        fmt = ''
        for i in range(1, number_of_dice + 1):
            fmt += '`Dice {}: {}`\n'.format(i, random.randint(1, 6))
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color, title='Roll a certain number of dice', description=fmt)
        await self.Aya.say(embed=em)


def setup(Aya):
    Aya.add_cog(Dice(Aya))
