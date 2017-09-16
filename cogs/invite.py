import random
import discord
from discord.ext import commands


class Invite:
    """Aya invite link"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True)
    async def invite(self, ctx):
        """ Use this link to add Aya to your server! """
        serv_owner = ctx.message.server.owner
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color,
                           title='Invite me to your server!',
                           footer='Aya',
                           description='[Click here](https://discordapp.com/api/oauth2/authorize?client_id={}&scope=bot&permissions=8)'
                           .format(self.Aya.user.id))
        try:
            await self.Aya.say(embed=em)
        except discord.HTTPException:
            await self.Aya.say('{} I need the embed links permission to send this.'.format(serv_owner.mention))


def setup(Aya):
    Aya.add_cog(Invite(Aya))
