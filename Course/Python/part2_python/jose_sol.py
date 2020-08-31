from random import shuffle
import random

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#mycards=[(s,r) for s in SUITE for r in RANKS ]
mycards=[]
for r in RANKS:
    for s in SUITE:
        mycards.append((s,r))

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """


    def __init__(self):
        print("Creating new orderded Deck!!")
        self.allcards = [(s,r) for s in SUITE for r in RANKS ]
        #list of all the cards

    def shuffle_deck(self):
        print("Shuffling Deck")
        shuffle(self.allcards)
        #shuffling the deck

    def split_in_half(self):
        return(self.allcards[:26],self.allcards[26:])
        #dividing the deck in half



class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards=cards

    def __str__(self):
        return "Contains {} cards ".format(len(self.cards))
        #how many cards i have

    def add(self,added_cards):
        self.cards.extend(added_cards)
        #adding cards

    def remove_cards(self):
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand

    def play_card(self):
        drawn_card = self.hand.remove_cards()
        print("{} has placed : {} ".format(self.name,drawn_card))
        print("\n")
        return drawn_card
        #removes the players card from his deck and places it down

    def remove_war_cards(self):
        war_cards =[]
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
        Return true if player has cards left
        """
        return len(self.hand.cards)!=0

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")


#Create a new deck and split it split_in_half
d=Deck()
d.shuffle_deck()
half1,half2=d.split_in_half()

#create both players
comp=Player("Computer",Hand(half1))

name=input("What is your name : ")
user=Player(name,Hand(half2))

total_rounds=0
war_counts=0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds+=1
    print("Time for a new round")
    print("Here are the current standings")
    print(user.name+" has the count : "+str(len(user.hand.cards)))
    print(comp.name+" has the count : "+str(len(comp.hand.cards)))
    print("Play a card")
    print("\n")

    table_cards = []

    c_card =comp.play_card()
    p_card =user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if(c_card[1]==p_card[1]):
        war_counts+=1
        print("WAR!!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("Game Over")
print("No of rounds "+str(total_rounds))
print("War countss "+str(war_counts))
