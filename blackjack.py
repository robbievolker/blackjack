import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

def main():
    play = wantToPlay()
    while(play == True):
        printIntro()

        deck = newDeck()

        playerHand = []
        playerCount = 0
        dealerHand = []
        dealerCount = 0
        while(len(playerHand) < 2):
            playerHand.append(deck.pop())
        while(len(dealerHand) < 2):
            dealerHand.append(deck.pop())

        playerTurn(playerHand)



        print("")
        print("Now it's the dealer's turn!")

        dealerCount = dealerTurn(dealerHand)
        print(dealerCount)
        play = wantToPlay()



def wantToPlay():
    value = input("Do you want to play Blackjack? (Y/N)")
    if(value == "Y" or value == "y"):
        return True
    elif(value == "N" or value == "n"):
        return False
    else:
        print("Please restart the game and enter either y or n")
        return False

def printIntro():
        print("Welcome to Blackjack!")
        print("This is a popular casino game where the objective is to get as close to the number 21 as possible with the value of your cards. If you go over 21, you're bust!")
        print("You will go first and then the dealer will go second.")
        print("An Ace is worth either 1 or 11. Picture cards are worth 10 each.")
        print("Good luck, and have fun!")
        print("")
        print("")

def hitOrStick():
    value = input("Do you want to hit or stick? (Y/N)")
    if(value == "Y" or value == "y"):
        return True
    elif(value == "N" or value == "n"):
        return False
    else:
        print("Please input Y or N.")

def newDeck():
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    #deck = [Card(value, suit) for value in range(1, 14) for suit in suits]
    deck = []

    for i in suits:
        for j in values:
            deck.append(Card(j, i))
    random.shuffle(deck)
    return deck

def playerTurn(hand):

    print("Your hand is:")
    playerCount = 0
    for card in hand:
        if(card.value == "King" or card.value == "Jack" or card.value == "Queen"):
            playerCount += 10
        elif(card.value == "Ace"):
            if(playerCount + 11 > 21):
                playerCount += 1
            else:
                playerCount += 11
        else:
            playerCount += card.value
        print(str(card.value)  + " of " + str(card.suit))
    print("")
    print("The total value is: " + str(playerCount))
    print("")

    if(playerCount > 21):
        print("Bust! You lose!")
        quit()

def dealerTurn(hand):
    dealerCount = 0
    while(dealerCount < 17):
        for card in hand:
            if(card.value == "King" or card.value == "Jack" or card.value == "Queen"):
                dealerCount += 10
            elif(card.value == "Ace"):
                if(dealerCount + 11 > 21):
                    dealerCount += 1
                else:
                    dealerCount += 11
            else:
                dealerCount += card.value
            print(str(card.value)  + " of " + str(card.suit))
        print("")
        print("The total value is: " + str(dealerCount))
        print("")
    return dealerCount

if __name__ == "__main__": main()
