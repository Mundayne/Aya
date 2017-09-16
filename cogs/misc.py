import random
import discord
import safygiphy
from discord.ext import commands

class Misc:
    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True)
    async def gif(self, ctx, *, tag):
        ''' Get a random gif. Usage: gif <tag> '''
        serv_owner = ctx.message.server.owner
        g = safygiphy.Giphy()
        gif = g.random(tag=tag)
        color = ("#%06x" % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color)
        em.set_image(url=str(gif.get('data', {}).get('image_original_url')))
        try:
            await self.Aya.say(embed=em)
        except discord.HTTPException:
            await self.Aya.say('{} I need the embed links permission to send this.'.format(serv_owner.mention))

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

    @commands.command(pass_context=True, aliases=['rolldice', 'diceroll'])
    async def dice(self, ctx, number_of_dice=1):
        '''Rolls a certain number of dice'''
        serv_owner = ctx.message.server.owner
        fmt = ''
        for i in range(1, number_of_dice + 1):
            fmt += '`Dice {}: {}`\n'.format(i, random.randint(1, 6))
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color, title='Roll a certain number of dice', description=fmt)
        try:
            await self.Aya.say(embed=em)
        except discord.HTTPException:
            await self.Aya.say('{} I need the embed links permission to send this.'.format(serv_owner.mention))

    @commands.command(pass_context=True, aliases=['coinflip'])
    async def flipcoin(self, ctx):
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

    @commands.command(pass_context=True, aliases=['8ball', 'eball'])
    async def ball8(self, ctx, *, yourquestion):
        """Let the 8 ball decide your fate"""
        serv_owner = ctx.message.server.owner
        question = yourquestion
        answers = ['It is certain', 'Yes', 'I don\'t know, probably?', 'HELL YEAH!!!', 'Of course', 'Most likely',
                   'Yup',
                   'It isn\'t too certain', 'Maybe', 'I really don\'t know...',
                   'Doubtful', 'My sources say no',
                   'Nope', 'No, so cya!', '**scoff** Are you kidding me?!', 'Impossible!', 'That is absurd!']
        color = ('#%06x' % random.randint(8, 0xFFFFFF))
        color = int(color[1:], 16)
        color = discord.Color(value=color)
        em = discord.Embed(color=color, title='Let the 8 ball decide',
                           description='Question: ' + question + '\nAnswer: ' + random.choice(answers))
        try:
            await self.Aya.say(embed=em)
        except discord.HTTPException:
            await self.Aya.say('{} I need the embed links permission to send this.'.format(serv_owner.mention))


def setup(Aya):
    Aya.add_cog(Misc(Aya))