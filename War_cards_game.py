#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.cards = [s+r for s in SUITE for r in RANKS]
    
    def __str__(self):
        return str(self.cards)
    def __len__(self):
        return len(self.cards)

    def shuffle_deck(self):
        shuffle(self.cards)

    def split_deck(self):
        return self.cards[:int(len(self.cards)/2)], self.cards[int(len(self.cards)/2):]
    
class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards: list):
        self.cards = list(cards)
    def __str__(self):
        return str(self.cards)
    def __len__(self):
        return len(self.cards)
    
    
    
    def add_cards(self, cards: list):
            self.cards.extend(cards)

    def draw_card(self):
        '''Removes "1" card from top.'''
        if(len(self.cards) <= 0):
            return -1
        return self.cards.pop(0)
    def get_hand(self):
        return self.cards
    

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, cards):
        self.player_name = name
        self.player_hand = Hand(cards)
    def __str__(self):
        return "Player: {}, Hand: {}".format(self.player_name, self.player_hand)

    def is_hand_empty(self) -> bool:
        return (len(self.player_hand) == 0)
    
    def draw_card(self):
        return self.player_hand.draw_card()
    def add_cards(self, cards):
        self.player_hand.add_cards(cards)

    def get_player_name(self):
        return self.player_name



class War:

    def __init__(self, p1: Player, p2: Player):
        self.player_one = p1
        self.player_two = p2
        self.table = []
        self.is_war = False
        self.game_over = False
        self.round_num = 1
    
    def get_card_heirarchy(card):
        card_str = card[1:]
        if(card_str == 'J'):
            return 11
        elif(card_str == 'Q'):
            return 12
        elif(card_str == 'K'):
            return 13
        elif(card_str == 'A'):
            return 14
        else:
            return int(card_str)
        

    def Gameplay(self):

        while(not self.player_one.is_hand_empty() or not self.player_two.is_hand_empty()):
            print(".: ~~> Round Number : {} <~~ :.".format(self.round_num))
            
            #IF is war, draw 4 and compare last 2 drawn
            #If not, draw 1 and compare
            for i in range(1+ int(self.is_war)*3):
                self.table.append(self.player_one.draw_card())
                self.table.append(self.player_two.draw_card())
                if(self.player_one.is_hand_empty() or self.player_two.is_hand_empty()):
                    self.game_over = True
                    break
            
            if(self.game_over):
                break
            print('#'*len(self.player_one.player_hand), " Player 1 {one} vs {two} Player 2 ".format(one = self.table[-2], two = self.table[-1]), '#'*len(self.player_two.player_hand))
            
            if(War.get_card_heirarchy(self.table[-2]) > War.get_card_heirarchy(self.table[-1])):
                self.player_one.add_cards(self.table)
                self.table = []
                self.is_war = False
                print("Player 1 Wins!")
            elif(War.get_card_heirarchy(self.table[-2]) < War.get_card_heirarchy(self.table[-1])):
                self.player_two.add_cards(self.table)
                self.table = []
                self.is_war = False
                print("Player 2 Wins!")
            else:
                self.is_war = True
                print("!!! WAR !!!")

            # print(self.player_one.player_name, self.player_one.player_hand)
            # print(self.player_two.player_name, self.player_two.player_hand)

            self.round_num += 1

        print("Game Over!")
        if(self.player_one.is_hand_empty()):
            print("{} Is the Winner!".format(self.player_two.get_player_name()))
        else:
            print("{} Is the Winner!".format(self.player_one.get_player_name()))

    

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

#Initializing The Deck
gameDeck = Deck()
#Shuffling The Deck
gameDeck.shuffle_deck()
#Splitting The Deck
d1, d2 = gameDeck.split_deck()


# Use the 3 classes along with some logic to play a game of war!
player_name = input("Enter Your Name: ")
me = Player(player_name, d1)
print(me)

comp = Player("Computar", d2)
print(comp)

game = War(me, comp)
game.Gameplay()