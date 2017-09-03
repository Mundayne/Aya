import random

import discord
from discord.ext import commands


class Flip:
    """ Flips a coin"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command()
    async def coinflip(self):
        """Flips a coin"""
        choices = ['You got Heads', 'You got Tails']
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color, title='Coinflip:', description=random.choice(choices))
        await self.Aya.say(embed=em)


def setup(Aya):
    Aya.add_cog(Flip(Aya))
