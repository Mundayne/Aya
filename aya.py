import discord
from discord.ext import commands

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
    'cogs.blacklist',
]


@Aya.event
async def on_ready():
    print('Aya is ready! \n User : {} \n ID : {}'.format(Aya.user.name, Aya.user.id))

@Aya.command(pass_context=True)
async def cogs(ctx):
    """A better way to show the names of the cogs"""
    await Aya.say('cogs : ')
    for cog in default_extensions:
        await Aya.say(cog)

@Aya.command(pass_context=True)
async def load(ctx, *, cogname):
    """Load a cog"""
    if ctx.message.author == ctx.message.server.owner:
        try:
            Aya.load_extension('cogs.{}'.format(cogname))
            default_extensions.append('cogs.{}'.format(cogname))
            print('{} has been loaded.'.format(cogname))
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
            print('{} has been unloaded.'.format(cogname))
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
            print('{} has been reloaded.'.format(cogname))
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

@Aya.command()
async def info():
    '''Info for the bot'''
    em = discord.Embed(title='Bot Info', color=0xE74C3C,description='Info about Aya:')
    em.add_field(name='Name', value='Aya#5745')
    em.add_field(name='Public Release Date', value='TBA')
    em.add_field(name='Developers', value='Oxilium#5477 and Jason#1510')
    em.add_field(name='Contributors', value='Drinka#2180')
    em.add_field(name='Discord Test and Support Server', value='[Support Server](https://discord.gg/PuScp9K)')
    em.add_field(name='Github', value='[/TheOxilium/Aya](https://github.com/TheOxilium/Aya)')
    em.set_footer(text='Aya')
    em.set_thumbnail(url='https://i.gyazo.com/49647cc71298498b2508721adbd2fccc.jpg')
    await Aya.say(embed=em)


if __name__ == "__main__":
    for ext in default_extensions:
        Aya.load_extension(ext)
    print('Good to go!')
    print('----------')

Aya.run('')
