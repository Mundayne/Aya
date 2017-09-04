import discord
from discord.ext import commands

Aya = commands.Bot('a.')
Aya.remove_command('help')

client = discord.Client()

default_extensions = [
    'cogs.help',
    'cogs.invite',
    'cogs.moderator',
    'cogs.coinflip',
    'cogs.dice',
    'cogs.gif',
    'cogs.8ball',
]


@Aya.event
async def on_ready():
    print('Aya is ready! \n User : {} \n ID : {}'.format(Aya.user.name, Aya.user.id))


@Aya.command(pass_context=True)
async def load(ctx, *, cogname):
    """Load a cog"""
    if ctx.message.author == ctx.message.server.owner:
        try:
            Aya.load_extension('cogs.{}'.format(cogname))
            default_extensions.append('cogs.{}'.format(cogname))
            print('{cogname} has been loaded.')
        except Exception as e:
            await Aya.say('\N{PISTOL}')
            await Aya.say('{}: {}'.format(type(e).__name__, e))
        else:
            await Aya.say('\N{OK HAND SIGN}')
    else:
        Aya.say('You don\'t have permission.')


@Aya.command(pass_context=True)
async def unload(ctx, *, cogname):
    """Unload a cog"""
    if ctx.message.author == ctx.message.server.owner:
        try:
            Aya.unload_extension('cogs.{}'.format(cogname))
            default_extensions.remove('cogs.{}'.format(cogname))
            print('{cogname} has been unloaded.')
        except Exception as e:
            await Aya.say('\N{PISTOL}')
            await Aya.say('{}: {}'.format(type(e).__name__, e))
        else:
            await Aya.say('\N{OK HAND SIGN}')
    else:
        Aya.say('You don\'t have permission.')


@Aya.command(pass_context=True)
async def reload(ctx, *, cogname):
    """Reload a cog"""
    if ctx.message.author == ctx.message.server.owner:
        try:
            Aya.unload_extension('cogs.{}'.format(cogname))
            default_extensions.remove('cogs.{}'.format(cogname))
            Aya.load_extension('cogs.{}'.format(cogname))
            default_extensions.append('cogs.{}'.format(cogname))
            print('{cogname} has been reloaded.')
        except Exception as e:
            await Aya.say('\N{PISTOL}')
            await Aya.say('{}: {}'.format(type(e).__name__, e))
        else:
            await Aya.say('\N{OK HAND SIGN}')
    else:
        Aya.say('You don\'t have permission.')


@Aya.command()
async def ping():
    """Check if Aya is up and running"""
    await Aya.say('Pong!')


if __name__ == "__main__":
    for ext in default_extensions:
        Aya.load_extension(ext)
    print('Good to go!')
    print('----------')

Aya.run('')
