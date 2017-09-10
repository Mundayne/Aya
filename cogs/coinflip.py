import random
import discord
from discord.ext import commands


class Flip:
    """Flips a coin"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True, aliases=['flipcoin'])
    async def coinflip(self):
        """Flips a coin"""
        serv_owner = ctx.message.server.owner
        choices = ['You got Heads', 'You got Tails']
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color, title='Coinflip:', description=random.choice(choices))
        try:
            await self.Aya.say(embed=em)
        except discord.HTTPException:
            await self.Aya.say('{} I need the embed links permission to send this.'.format(serv_owner.mention))


def setup(Aya):
    Aya.add_cog(Flip(Aya))
