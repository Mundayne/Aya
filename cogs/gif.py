import random
***REMOVED***
import safygiphy
***REMOVED***


class Gif:
    """Gets a random gif"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True)
    async def gif(self, ctx, *, tag):
        ''' Get a random gif. Usage: gif <tag> '''
        g = safygiphy.Giphy()
        gif = g.random(tag=tag)
        color = ("#%06x" % random.randint(8, 0xFFFFFF))
        color = int(color[1:***REMOVED***, 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color)
        em.set_image(url=str(gif.get('data', {}).get('image_original_url')))
        await self.Aya.say(embed=em)


def setup(Aya):
    Aya.add_cog(Gif(Aya))
