import random
import sys


class Blackjack:

    HEARTS = chr(9829)  
    DIAMONDS = chr(9830)  
    SPADES = chr(9824)  
    CLUBS = chr(9827)  
   
    BACKSIDE = 'backside'

    Money = 5000

    def __init__(self):
        self.money = self.Money

    def main(self):
        print('''Blackjack, by Al Sweigart al@inventwithpython.com
         Rules:
           Try to get as close to 21 without going over.
           Kings, Queens, and Jacks are worth 10 points.
           Aces are worth 1 or 11 points.
           Cards 2 through 10 are worth their face value.
           (H)it to take another card.
           (S)tand to stop taking cards.
           On your first play, you can (D)ouble down to increase your bet
           but must hit exactly one more time before standing.
           In case of a tie, the bet is returned to the player.
           The dealer stops hitting at 17.''')

        while True:  
            
            if self.money <= 0:
                print("You're broke!")
                print("Good thing you weren't playing with real money.")
                print('Thanks for playing!')
                sys.exit()
            print('Money:', self.money)
            bet = self.getBet(self.money)
            deck = self.getDeck()
            dealerHand = [deck.pop(), deck.pop()]
            playerHand = [deck.pop(), deck.pop()]
            print('Bet:', bet)
            while True:  
                self.displayHands(playerHand, dealerHand, False)
                print()
                if self.getHandValue(playerHand) > 21:
                    break

                move = self.getMove(playerHand, self.money - bet)
                if move == 'D':
                    additionalBet = self.getBet(min(bet, (self.money - bet)))
                    bet += additionalBet
                    print('Bet increased to {}.'.format(bet))
                    print('Bet:', bet)
                if move in ('H', 'D'):
                    newCard = deck.pop()
                    rank, suit = newCard
                    print('You drew a {} of {}.'.format(rank, suit))
                    playerHand.append(newCard)
                    if self.getHandValue(playerHand) > 21:
                        continue
                if move in ('S', 'D'):
                    break
                
            if self.getHandValue(playerHand) <= 21:
                while self.getHandValue(dealerHand) < 17:
                    print('Dealer hits...')
                    dealerHand.append(deck.pop())
                    self.displayHands(playerHand, dealerHand, False)
                    if self.getHandValue(dealerHand) > 21:
                        break 
                    
                    input('Press Enter to continue...')
                    print('\n\n')
            self.displayHands(playerHand, dealerHand, True)
            playerValue = self.getHandValue(playerHand)
            dealerValue = self.getHandValue(dealerHand)
            if dealerValue > 21:
                print('Dealer busts! You win ${}!'.format(bet))
                self.money += bet
            elif (playerValue > 21) or (playerValue < dealerValue):
                print('You lost!')
                self.money -= bet
            elif playerValue > dealerValue:
                print('You won ${}!'.format(bet))
                self.money += bet
            elif playerValue == dealerValue:
                print('It\'s a tie, the bet is returned to you.')
            input('Press Enter to continue...')
            print('\n\n')

    def getBet(self, maxBet):
        """Спрашиваем у игрока, сколько он ставит на этот раунд."""
        while True:  
            print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
            bet = input('> ').upper().strip()
            if bet == 'QUIT':
                print('Thanks for playing!')
                sys.exit()
            if not bet.isdecimal():
                continue  
            bet = int(bet)
            if 1 <= bet <= maxBet:
                return bet  

    def getDeck(self):
        deck = []
        for suit in (self.HEARTS, self.DIAMONDS, self.SPADES, self.CLUBS):
            for rank in range(2, 11):
                deck.append((str(rank), suit))  
            for rank in ('J', 'Q', 'K', 'A'):
                deck.append((rank, suit))  
        random.shuffle(deck)
        return deck

    def displayHands(self, playerHand, dealerHand, showDealerHand):
        print()
        if showDealerHand:
            print('DEALER:', self.getHandValue(dealerHand))
            self.displayCards(dealerHand)
        else:
            print('DEALER: ???')
            self.displayCards([self.BACKSIDE] + dealerHand[1:])
        print('PLAYER:', self.getHandValue(playerHand))
        self.displayCards(playerHand)

    def getHandValue(self, cards):
        """ Возвращаем стоимость карт. Фигурные карты стоят 10, тузы — 11
        или 1 очко (эта функция выбирает подходящую стоимость карты)."""
        value = 0
        numberOfAces = 0
        for card in cards:
            rank = card[0]  
            if rank == 'A':
                numberOfAces += 1
            elif rank in ('K', 'Q', 'J'):  
                value += 10
            else:
                value += int(rank)
        value += numberOfAces  
        for i in range(numberOfAces):
            if value + 10 <= 21:
                value += 10
        return value

    def displayCards(self, cards):
        rows = ['', '', '', '', '']  
        for i, card in enumerate(cards):
            rows[0] += ' ___  '  
            if card == self.BACKSIDE:
                rows[1] += '|## | '
                rows[2] += '|###| '
                rows[3] += '|_##| '
            else:
                rank, suit = card  
                rows[1] += '|{} | '.format(rank.ljust(2))
                rows[2] += '| {} | '.format(suit)
                rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
        for row in rows:
            print(row)

    def getMove(self, playerHand, money):
        while True:
            moves = ['(H)it', '(S)tand']
            if len(playerHand) == 2 and money > 0:
                moves.append('(D)ouble down')
            movePrompt = ', '.join(moves) + '> '
            move = input(movePrompt).upper()
            if move in ('H', 'S'):
                return move  
            if move == 'D' and '(D)ouble down' in moves:
                return move  
