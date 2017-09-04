***REMOVED***


class Help:
    """Help Menu"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command()
    async def help(self):
        """Help Menu"""
        await self.Aya.say("""
         ```
         >> This is the Aya commands index.
         -----
         a.help: Help menu 
         ---- MODERATION ----
         a.kick <name>: Kick someone out of the server
         a.ban <name>: Ban someone from the server
         a.unban <name>: Unban someone
         
         ---- PLUGINS ----
         
         a.load: Load a plugin
         a.reload: Reload a plugin
         a.unload: Unload a plugin
         
         ---- ENTERTAINMENT ---
         
         a.gif <tag>: Get a random gif
         a.war: Play a game of war
         a.dice: Roll a certain number of dice
         a.coinflip: Flip a coin
         a.eball: Let the 8 ball decide your fate
         ```
        """)


def setup(Aya):
    Aya.add_cog(Help(Aya))
