from discord.ext import commands


class Help:
    """Help Menu"""

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True)
    async def help(self, ctx):
        """Help Menu"""
        await self.Aya.say("""
         ```
         >> This is the Aya commands index.
         -----
         a.help: Help menu
         
         ---- UTILITY ----
         
         a.info: Shows important info about Aya
         a.userinfo <user>: Gets the user info of someone
         a.serverinfo: See some info about the server
         
         ---- MODERATION ----
         
         a.kick <name>: Kick someone out of the server
         a.ban <name>: Ban someone from the server
         a.unban <name>: Unban someone
         a.bans: Get a list of banned people in the server
         a.filter <add|remove|list> <word>: Bans a word from the server
         a.clean <number>: Deletes a certain number of your messages
         a.purge <number>: Deletes a certain number of anyone's messages
         
         ---- PLUGINS ----
         
         a.coglist: Shows the list of cogs that you can load and unload
         a.load: Load a plugin
         a.reload: Reload a plugin
         a.unload: Unload a plugin
         
         ---- ENTERTAINMENT ----
         
         a.gif <tag>: Get a random gif
         a.war: Play a game of war
         a.dice <number of dice>: Roll a certain number of dice
         a.flipcoin: Flip a coin
         a.8ball <question>: Let the 8 ball decide your fate
         a.lottery: Enter in the lottery
         
         ---- ECONOMY ----
         
         a.register: Register an account in the bank
         a.balance: Check your account balance
         ```
        """)


def setup(Aya):
    Aya.add_cog(Help(Aya))
