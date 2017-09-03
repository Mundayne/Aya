***REMOVED***
***REMOVED***

***REMOVED***
***REMOVED***

***REMOVED***

***REMOVED***
    'plugins.moderator.moderator',
    'plugins.minigames.minigames',
    'plugins.coinflip.coinflip',
    'plugins.invite.invite',
    'plugins.dice.dice',
    'plugins.gif.gif',
    'plugins.8ball.8ball',
***REMOVED***


***REMOVED***
***REMOVED***
***REMOVED***


***REMOVED***
async def load(ctx, *, plugin):
    """ loading a plugin """
***REMOVED***
***REMOVED***
            Aya.load_extension('plugins.{}.{}'.format(plugin, plugin))
            default_extensions.append('plugins.{}.{}'.format(plugin, plugin))
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***


***REMOVED***
async def unload(ctx, *, plugin):
    """ unloading a plugin """
***REMOVED***
***REMOVED***
            Aya.unload_extension('plugins.{}.{}'.format(plugin, plugin))
            default_extensions.remove('plugins.{}.{}'.format(plugin, plugin))
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***


***REMOVED***
async def reload(ctx, *, plugin):
    """ reloading a plugin """
***REMOVED***
***REMOVED***
            Aya.unload_extension('plugins.{}.{}'.format(plugin, plugin))
            default_extensions.remove('plugins.{}.{}'.format(plugin, plugin))
            Aya.load_extension('plugins.{}.{}'.format(plugin, plugin))
            default_extensions.append('plugins.{}.{}'.format(plugin, plugin))
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***


***REMOVED***
***REMOVED***
    """ Testing if the bot is up and working """
***REMOVED***


***REMOVED***
***REMOVED***
***REMOVED***
    print('Default plugins has been loaded.')
***REMOVED***

***REMOVED***
