#! ~/virtualenvs/Discord/bin/env python3
# -*- coding: utf-8 -*-

import discord
import logging
from discord.ext import commands

# Setting the logging module
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

Aya = commands.Bot('a.')
Aya.remove_command('help')

default_extensions = [
    'cogs.help',
    'cogs.invite',
    'cogs.moderator',
    'cogs.coinflip',
    'cogs.dice',
    'cogs.gif',
    'cogs.8ball',
    'cogs.userfeatures',
    'cogs.minigames',
]


@Aya.event
async def on_ready():
    print('Aya is ready! \n User : {} \n ID : {}'.format(Aya.user.name, Aya.user.id))

@Aya.command()
async def cogs(ctx):
    """A better way to show the names of the cogs"""
    await ctx.send('cogs : ')
    for cog in default_extensions:
        await ctx.send(cog)

@Aya.command()
async def load(ctx, *, cogname):
    """Load a cog"""
    if ctx.message.author == ctx.message.server.owner:
        try:
            Aya.load_extension('cogs.{}'.format(cogname))
            default_extensions.append('cogs.{}'.format(cogname))
            print('{} has been loaded.'.format(cogname))
        except Exception as e:
            await ctx.send('\N{PISTOL}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\N{OK HAND SIGN}')
    else:
        Aya.say('You don\'t have permission.')


@Aya.command()
async def unload(ctx, *, cogname):
    """Unload a cog"""
    if ctx.message.author == ctx.message.server.owner:
        try:
            Aya.unload_extension('cogs.{}'.format(cogname))
            default_extensions.remove('cogs.{}'.format(cogname))
            print('{} has been unloaded.'.format(cogname))
        except Exception as e:
            await ctx.send('\N{PISTOL}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\N{OK HAND SIGN}')
    else:
        ctx.send('You don\'t have permission.')


@Aya.command(pass_context=True)
async def reload(ctx, *, cogname):
    """Reload a cog"""
    if ctx.message.author == ctx.message.server.owner:
        try:
            Aya.unload_extension('cogs.{}'.format(cogname))
            default_extensions.remove('cogs.{}'.format(cogname))
            Aya.load_extension('cogs.{}'.format(cogname))
            default_extensions.append('cogs.{}'.format(cogname))
            print('{} has been reloaded.'.format(cogname))
        except Exception as e:
            await ctx.send('\N{PISTOL}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('\N{OK HAND SIGN}')
    else:
        ctx.send('You don\'t have permission.')


@Aya.command()
async def ping():
    """Ping Aya"""
    await ctx.send('Pong!')


if __name__ == "__main__":
    print('Loading extensions...')
    for ext in default_extensions:
        Aya.load_extension(ext)
    print('Good to go!')
    print('----------')

Aya.run('')
