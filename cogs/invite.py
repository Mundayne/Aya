import random
***REMOVED***
***REMOVED***


class Invite:
    """Aya invite link"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command()
    async def invite(self):
        """ Use this link to add Aya to your server! """
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:***REMOVED***, 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color,
                           title='Invite me to your server!',
                           footer='Aya',
                           description='[Click here***REMOVED***(https://discordapp.com/api/oauth2/authorize?client_id={}&scope=bot&permissions=8)'
                           .format(self.Aya.user.id))
        await self.Aya.say(embed=em)


def setup(Aya):
    Aya.add_cog(Invite(Aya))
