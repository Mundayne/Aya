***REMOVED***
import random
***REMOVED***
import asyncio

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

    @commands.command(pass_context=True)
    async def war(self, ctx):
        '''Play a game of war'''
        cards = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Jack', 12: 'Queen',
                 13: 'King', 14: 'Ace'}
        member = ctx.message.author
        player = random.randint(2, 14)
        dealer = random.randint(2, 14)
        msg = await self.Aya.say('Shuffling the cards...')
        asyncio.sleep(1)
        await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                    'Dealing...')
        asyncio.sleep(1)
        await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                    'Dealing...\n'
                                    '------{}------'.format(member.name))
        if int(player) > int(dealer):
            asyncio.sleep(1)
            await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                        'Dealing...\n'
                                        '------{}------\n'.format(member.name) +
                                   '`Player: ' + cards[player***REMOVED*** + '`\n'
                                                                 '`Dealer: ' + cards[dealer***REMOVED*** + '`\n'
                                                                                               'You won!')
        elif int(player) < int(dealer):
            asyncio.sleep(1)
            await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                        'Dealing...\n'
                                        '------{}------\n'.format(member.name) +
                                   '`Player: ' + cards[player***REMOVED*** + '`\n'
                                                                 '`Dealer: ' + cards[dealer***REMOVED*** + '`\n'
                                                                                               'You lost...')
***REMOVED***
            asyncio.sleep(1)
            await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                        'Dealing...\n'
                                        '------{}------\n'.format(member.name) +
                                   'Both you and the dealer drawed a ' + cards[
                                       player***REMOVED*** + '. War function coming soon...')
            player2 = random.randint(2, 14)
            player3 = random.randint(2, 14)
            player4 = random.randint(2, 14)
            dealer2 = random.randint(2, 14)
            dealer3 = random.randint(2, 14)
            dealer4 = random.randint(2, 14)
            if int(player4) > int(dealer4):
                asyncio.sleep(1)
                await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                            'Dealing...\n'
                                            '------{}------\n'.format(member.name) +
                                       '`Player: ' + cards[player***REMOVED*** + '`, ' + cards[player2***REMOVED*** + ', ' + cards[
                                           player3***REMOVED*** + ', `Deciding Card: ' + cards[player4***REMOVED*** + '`\n'
                                                                                              '`Dealer: ' + cards[
                                           dealer***REMOVED*** + '`, ' + cards[dealer2***REMOVED*** + ', ' + cards[
                                           dealer3***REMOVED*** + ', `Deciding Card: ' + cards[dealer4***REMOVED*** + '`\n'
                                                                                              'You won!')
            elif int(player4) < int(dealer4):
                asyncio.sleep(1)
                await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                            'Dealing...\n'
                                            '------{}------\n'.format(member.name) +
                                       '`Player: ' + cards[player***REMOVED*** + '`, ' + cards[player2***REMOVED*** + ', ' + cards[
                                           player3***REMOVED*** + ', `Deciding Card: ' + cards[player4***REMOVED*** + '`\n'
                                                                                              '`Dealer: ' + cards[
                                           dealer***REMOVED*** + '`, ' + cards[dealer2***REMOVED*** + ', ' + cards[
                                           dealer3***REMOVED*** + ', `Deciding Card: ' + cards[dealer4***REMOVED*** + '`\n'
                                                                                              'You lost...')
    ***REMOVED***
                asyncio.sleep(1)
                await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                            'Dealing...\n'
                                            '------{}------\n'.format(member.name) +
                                       '`Player: ' + cards[player***REMOVED*** + '`, ' + cards[player2***REMOVED*** + ', ' + cards[
                                           player3***REMOVED*** + ', `Deciding Card: ' + cards[player4***REMOVED*** + '`\n'
                                                                                              '`Dealer: ' + cards[
                                           dealer***REMOVED*** + '`, ' + cards[dealer2***REMOVED*** + ', ' + cards[
                                           dealer3***REMOVED*** + ', `Deciding Card: ' + cards[dealer4***REMOVED*** + '`\n'
                                                                                              'It\'s a tie.')

def setup(Aya):
    Aya.add_cog(Minigames(Aya))