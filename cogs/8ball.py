import random
import discord
from discord.ext import commands


class Ball:
    """8 ball game"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True)
    async def eball(self, ctx, *, yourquestion):
        """Let the 8 ball decide your fate"""
        question = yourquestion
        answers = ['It is certain', 'Yes', 'I don\'t know, probably?', 'HELL YEAH!!!', 'Of course',
                   'It isn\'t too certain', 'Doubtful', 'My sources say no',
                   'Nope', 'No, so cya!', '**scoff** Are you kidding me?!', 'Impossible!',
                   'That is absurd!']
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color, title='Let the 8 ball decide',
                           description='Question: ' + question + '\n''Answer: ' + random.choice(answers))
        await self.Aya.say(embed=em)


def setup(Aya):
    Aya.add_cog(Ball(Aya))
