import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def main():
    play = wantToPlay()
    if(play == True):
        print("Welcome to Blackjack!")
        print("This is a popular casino game where the objective is to get as close to the number 21 as possible with the value of your cards. If you go over 21, you're bust!")
        print("You will go first and then the dealer will go second.")
        print("An Ace is worth either 1 or 11. Picture cards are worth 10 each.")
        print("Good luck, and have fun!")
        print("")
        print("")
        deck = newDeck()

        playerHand = []
        playerCount = 0
        dealerHand = []
        dealerCount = 0

        while(len(playerHand) < 2):
            playerHand.append(deck.pop())
        while(len(dealerHand) < 2):
            dealerHand.append(deck.pop())


        print("Your hand is:")
        for card in playerHand:
            playerCount += card.value
            print(str(card.value)  + " of " + str(card.suit))
        print("")
        print("The total value is: " + str(playerCount))
        print("")

def wantToPlay():
    value = input("Do you want to play Blackjack? (Y/N)")
    if(value == "Y" or value == "y"):
        return True
    elif(value == "N" or value == "n"):
        return False
    else:
        print("Please restart the game and enter either y or n")
        return False

def newDeck():
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    #deck = [Card(value, suit) for value in range(1, 14) for suit in suits]
    deck = []

    for i in suits:
        for j in values:
            deck.append(Card(i, j))
    random.shuffle(deck)
    return deck

if __name__ == "__main__": main()
