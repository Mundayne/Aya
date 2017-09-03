***REMOVED***


class Help:
    """ Help Menu """

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command()
    async def help(self):
        """ help menu """
        await self.Aya.say("""
         ```
         >> This is the Aya commands index.
         -----
         
         a.help : Help menu 
         
         ---- MODERATION ----
         
         a.kick <name> : Kick <name> out
         a.ban <name> : Ban <name> out
         a.unban <name> : Get <name> back
         
         ---- PLUGINS ----
         
         a.load : load a plugin
         a.reload : reload a plugin
         a.unload : unload a plugin
         
         ---- ENTERTAINMENT ---
         
         a.gif <tag> : Obtain a gif
         a.war : play a little game
         a.dice : play a dice
         a.coinflip : flip a coin 
         a.eball : play 8 ball
         
         ```
        """)


def setup(Aya):
    Aya.add_cog(Help(Aya))
