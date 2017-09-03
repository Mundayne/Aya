import discord
from discord.ext import commands

Aya = commands.Bot('a.')
Aya.remove_command('help')

client = discord.Client()

default_extensions = [
    'plugins.moderator.moderator',
    'plugins.minigames.minigames',
    'plugins.coinflip.coinflip',
    'plugins.invite.invite',
    'plugins.dice.dice',
    'plugins.gif.gif',
    'plugins.8ball.8ball',
    'plugins.help.help',
]


@Aya.event
async def on_ready():
    print('Aya is ready! \n User : {} \n ID : {}'.format(Aya.user.name, Aya.user.id))


@Aya.command(pass_context=True)
async def load(ctx, *, plugin):
    """ loading a plugin """
    if ctx.message.author == ctx.message.server.owner:
        try:
            Aya.load_extension('plugins.{}.{}'.format(plugin, plugin))
            default_extensions.append('plugins.{}.{}'.format(plugin, plugin))
        except Exception as e:
            await Aya.say('\N{PISTOL}')
            await Aya.say('{}: {}'.format(type(e).__name__, e))
        else:
            await Aya.say('\N{OK HAND SIGN}')
    else:
        Aya.say('You don\'t have permission.')


@Aya.command(pass_context=True)
async def unload(ctx, *, plugin):
    """ unloading a plugin """
    if ctx.message.author == ctx.message.server.owner:
        try:
            Aya.unload_extension('plugins.{}.{}'.format(plugin, plugin))
            default_extensions.remove('plugins.{}.{}'.format(plugin, plugin))
        except Exception as e:
            await Aya.say('\N{PISTOL}')
            await Aya.say('{}: {}'.format(type(e).__name__, e))
        else:
            await Aya.say('\N{OK HAND SIGN}')
    else:
        Aya.say('You don\'t have permission.')


@Aya.command(pass_context=True)
async def reload(ctx, *, plugin):
    """ reloading a plugin """
    if ctx.message.author == ctx.message.server.owner:
        try:
            Aya.unload_extension('plugins.{}.{}'.format(plugin, plugin))
            default_extensions.remove('plugins.{}.{}'.format(plugin, plugin))
            Aya.load_extension('plugins.{}.{}'.format(plugin, plugin))
            default_extensions.append('plugins.{}.{}'.format(plugin, plugin))
        except Exception as e:
            await Aya.say('\N{PISTOL}')
            await Aya.say('{}: {}'.format(type(e).__name__, e))
        else:
            await Aya.say('\N{OK HAND SIGN}')
    else:
        Aya.say('You don\'t have permission.')


@Aya.command()
async def ping():
    """ Testing if the bot is up and working """
    await Aya.say('Pong!')


if __name__ == "__main__":
    for ext in default_extensions:
        Aya.load_extension(ext)
    print('Default plugins has been loaded.')
    print('----------')

Aya.run('')
