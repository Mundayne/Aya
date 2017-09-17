'''MIT License

Copyright (c) 2017 verixx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

import discord
from discord.ext import commands

class Utility:

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True)
    async def info(self, ctx):
        serv_owner = ctx.message.server.owner
        '''Info for the bot'''
        em = discord.Embed(title='Bot Info', color=0xE74C3C, description='Info about Aya:')
        em.add_field(name='Name', value='Aya#5745')
        em.add_field(name='Public Release Date', value='TBA')
        em.add_field(name='Developers', value='Oxilium#5477 and Jason#1510')
        em.add_field(name='Contributors', value='Drinka#2180')
        em.add_field(name='Discord Test and Support Server', value='[Support Server](https://discord.gg/PuScp9K)')
        em.add_field(name='Github', value='[/TheOxilium/Aya](https://github.com/TheOxilium/Aya)')
        em.set_footer(text='Aya')
        em.set_thumbnail(url='https://i.gyazo.com/49647cc71298498b2508721adbd2fccc.jpg')
        try:
            await self.Aya.say(embed=em)
        except discord.HTTPException:
            await self.Aya.say('{} I need the embed links permission to send this.'.format(serv_owner.mention))

    @commands.command(pass_context=True, aliases=['ui', 'user'])
    async def userinfo(self, ctx, user: discord.Member = None):
        user = user or ctx.message.author
        server = ctx.message.server
        serv_owner = server.owner
        avi = user.avatar_url or user.default_avatar_url
        roles = sorted(user.roles, key=lambda c: c.position)
        roles = roles[::1]

        rolenamelist = []
        for role in roles:
            if role.name != '@everyone':
                rolenamelist.append(role.name)
        rolenames = ', '.join(rolenamelist) or 'None'

        time = ctx.message.timestamp
        desc = '{0} is chilling in {1} mode.'.format(user.name, user.status)
        member_number = sorted(server.members, key=lambda m: m.joined_at).index(user) + 1
        em = discord.Embed(color=0x832EEA, description=desc, timestamp=time)
        em.add_field(name='Name', value=user.name, inline=True)
        em.add_field(name='Member No.',value=str(member_number),inline = True)
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y'))
        em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y'))
        em.add_field(name='Roles', value=rolenames, inline=True)
        em.set_footer(text='User ID: '+str(user.id))
        em.set_thumbnail(url=avi)
        try:
            await self.Aya.say(embed = em)
        except discord.HTTPException:
            await self.Aya.say('{} I need the embed links permission to send this.'.format(serv_owner.mention))


def setup(Aya):
    Aya.add_cog(Utility(Aya))