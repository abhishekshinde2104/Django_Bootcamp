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
import random

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
all_cards = []
card=''
comp = []
user = []

values = {'K':13,'Q':12,'J':11,'1':10,'9':9,'8':8,'7':7,'6':6,'5':5,"4":4,"3":3,"2":2,'A':99}

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """


    def __init__(self):
        pass
    def create_deck(self):
        for i in range(0,4):
            for j in range(0,13):
                card=SUITE[i]+RANKS[j]
                all_cards.append(card)
        #print(all_cards)
    def shuffle_deck(self):
        random.shuffle(all_cards)
        #print(all_cards)
    def divide_deck(self):
        comp = all_cards[::2]
        user = all_cards[1::2]
        return (comp,user)
        #print(comp)
        #print(user)
        #print(len(user))


class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self):
        #super().__init__()
        pass


    def game_logic(self,comp,user):
        print("This is inside Game Logic !!")
        #print(comp)
        #print(user)

        #for i in range(0,26):
        comp_choice=random.choice(comp)
        print("User has : ",len(user)," cards in your deck.")
        user_choice=input("Enter the number of card u want to put : ")
        user_choice = user[int(user_choice)-1]
        print(comp_choice)
        print(user_choice)


        if(values[comp_choice[1]] > values[user_choice[1]]):
            user_loss=user_choice
            comp_gain=comp_choice
            user.remove(user_loss)
            comp.remove(comp_gain)
            comp.append(user_loss)
            comp.append(comp_gain)
            print("Comp win this turn ..")
        elif(values[comp_choice[1]] == values[user_choice[1]]):
                #comp_cards_war = []
                #user_cards_war = []
                #for i in range(0,3):
                #    comp_cards_war.append(random.choice(comp))
                #    print("User has : ",len(user)," cards in your deck.")
               #      user_cards_war.append(user[int(input("Enter the card number to go to war : "))-1])
                #if(values[random.choice(comp_cards_war)[1]] > values)

            print("War Game")
        else:
            print("User Win")


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    pass


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
d=Deck()
d.create_deck()
d.shuffle_deck()
c,u=d.divide_deck()
h=Hand()
h.game_logic(c,u)

# Use the 3 classes along with some logic to play a game of war!
