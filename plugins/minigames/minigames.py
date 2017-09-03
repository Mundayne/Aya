import asyncio
import random

from discord.ext import commands


class Minigames:
    '''Play minigames such as war and battleship'''

    def __init__(self, Aya):
        self.Aya = Aya

    @commands.command(pass_context=True)
    async def war(self, ctx):

        '''Play a game of war with the bot'''

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
                                        '`Player: ' + cards[player] + '`\n'
                                                                      '`Dealer: ' + cards[dealer] + '`\n'
                                                                                                    'You won!')
        elif int(player) < int(dealer):
            asyncio.sleep(1)
            await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                             'Dealing...\n'
                                             '------{}------\n'.format(member.name) +
                                        '`Player: ' + cards[player] + '`\n'
                                                                      '`Dealer: ' + cards[dealer] + '`\n'
                                                                                                    'You lost...')
        else:
            asyncio.sleep(1)
            await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                             'Dealing...\n'
                                             '------{}------\n'.format(member.name) +
                                        'Both you and the dealer drawed a ' + cards[
                                            player] + '. War function coming soon...')
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
                                            '`Player: ' + cards[player] + '`, ' + cards[player2] + ', ' + cards[
                                                player3] + ', `Deciding Card: ' + cards[player4] + '`\n'
                                                                                                   '`Dealer: ' + cards[
                                                dealer] + '`, ' + cards[dealer2] + ', ' + cards[
                                                dealer3] + ', `Deciding Card: ' + cards[dealer4] + '`\n'
                                                                                                   'You won!')
            elif int(player4) < int(dealer4):
                asyncio.sleep(1)
                await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                                 'Dealing...\n'
                                                 '------{}------\n'.format(member.name) +
                                            '`Player: ' + cards[player] + '`, ' + cards[player2] + ', ' + cards[
                                                player3] + ', `Deciding Card: ' + cards[player4] + '`\n'
                                                                                                   '`Dealer: ' + cards[
                                                dealer] + '`, ' + cards[dealer2] + ', ' + cards[
                                                dealer3] + ', `Deciding Card: ' + cards[dealer4] + '`\n'
                                                                                                   'You lost...')
            else:
                asyncio.sleep(1)
                await self.Aya.edit_message(msg, 'Shuffling the cards...\n'
                                                 'Dealing...\n'
                                                 '------{}------\n'.format(member.name) +
                                            '`Player: ' + cards[player] + '`, ' + cards[player2] + ', ' + cards[
                                                player3] + ', `Deciding Card: ' + cards[player4] + '`\n'
                                                                                                   '`Dealer: ' + cards[
                                                dealer] + '`, ' + cards[dealer2] + ', ' + cards[
                                                dealer3] + ', `Deciding Card: ' + cards[dealer4] + '`\n'
                                                                                                   'It\'s a tie.')


def setup(Aya):
    Aya.add_cog(Minigames(Aya))
