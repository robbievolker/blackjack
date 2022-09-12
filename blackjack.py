
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
        deck = newDeck()

def wantToPlay():
    value = input("Do you want to play Blackjack? (Y/N)")
    if(value == "Y" or value == "y"):
        return True
    elif(value == "N" or value == "n"):
        return False
    else:
        print("You have entered an incorrect value.")
        return False

def newDeck():
    suits = ["hearts", "diamonds", "spades", "clubs"]
    deck = [Card(value, suit) for value in range(1, 14) for suit in suits]
    return deck


if __name__ == "__main__": main()
