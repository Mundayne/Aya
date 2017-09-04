***REMOVED***
import random
***REMOVED***

class Minigames:
    def __init__(self, Aya):
        self.Aya = Aya
    @commands.command(pass_context=True)
    async def lottery(self, ctx):
        '''Enter the lottery and see if you win'''
        author = ctx.message.author
        numbers = [***REMOVED***
        for x in range(3):
            numbers.append(random.randint(1, 5))
        print (numbers)
        await self.Aya.say('Choose 3 numbers between 1 and 5 and separate each number with a space.')
        msg = await self.Aya.wait_for_message(timeout=30, author=ctx.message.author, channel=ctx.message.channel)
        if (msg.content[0***REMOVED*** == numbers[0***REMOVED***) and (msg.content[2***REMOVED*** == numbers[1***REMOVED***) and (msg.content[4***REMOVED*** == numbers[2***REMOVED***):
            await self.Aya.say('{} You won! Congratulations on winning the lottery!'.format(author.mention))
***REMOVED***
            await self.Aya.say('{} Too bad... You were the 124/125 who lost the lottery...'.format(author.mention))

def setup(Aya):
    Aya.add_cog(Minigames(Aya))