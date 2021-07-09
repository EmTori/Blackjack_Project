import csv
from random import shuffle
import sys
import os

DECK_FILENAME = "Card_Deck.csv"

#Exits program if something fails
def exitProgram():
    print("Exiting program.")
    print()
    print("Bye!")
    sys.exit()

#Load the card deck file
def loadCardDeck():
    try:
        cardDeck = []
        with open(DECK_FILENAME, "r", newline = "") as file:
            reader = csv.reader(file)
            for row in reader:
                card = [row[0], row[1]]
                cardDeck.append(card)
        return cardDeck
    except FileNotFoundError as e:                            #If the program cant find the card deck file it will end the program
        print("Could not find file " +DECK_FILENAME+ "!")
        exitProgram()
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()

#Save the card deck file
def saveCardDeck(cardDeck):
    try:
        with open(DECK_FILENAME, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(cardDeck)
    except OSError as e:                                      #OS error will end the program
        print(type(e), e)
        exitProgram()
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()

#Assigning values to the cards in the deck
def score(cardDeck, hand):
    score = 0
    if cardDeck == ("10", "Jack", "Queen", "King"):        #Assigns a score of 10 to the 10, Jack, Queen, and King cards
        score += 10
    elif cardDeck == ("3", "4", "5", "6", "7", "8", "9"):  #Assigns a score of that matches to all the card numbers
        score += int(cardDeck)
    elif cardDeck == ("Ace"):                              #Assigns a score of 1 or 11 Ace cards
        while True:
            aceChoice = input("Do you want the Ace to be 1 or 11: ")
            if aceChoice == "1":                              #Player chooses 1
                score += 1                                     #Score is set to 1
                break
            elif aceChoice == "11":                           #Player chooses 11
                score += 11                                    #Score is set to 11
                break
            else:                                             #Player enters invalid choice
                print("Invalid choice. Please enter '1' or '11'.")
                continue
    return score

#Shuffles and deals the 2 first cards to both the player and dealer
def dealCards(cardDeck, playerHand, dealerHand):
    shuffle(cardDeck)                                         #Shuffles card deck
    
    for i in range(2):                                        #A for loop that adds 2 cards to the players hand
        playerHand.append(cardDeck.pop())
    dealerHand.append(cardDeck.pop())                         #Adds 1 card to the dealers hand

#Player chooses hit or stand   
def hitOrStand(cardDeck, playerHand, dealerHand, hit, stand):
    while True:                                               #
        playerChoice = input("Hit or stand? (hit/stand): ")
        print()
        
        if playerChoice.lower() == "hit":                     #Player chooses hit
            hit = True                                        #Hit set to true
            playerHand.append(cardDeck.pop())                 #Adds card to player hand
            displayCards(playerHand, dealerHand, hit, stand)
            continue
            
        elif playerChoice.lower() == "stand":                 #Player chooses stand
            stand = True                                      #stand set to true
            dealerHand.append(cardDeck.pop())
            displayCards(playerHand, dealerHand, hit, stand)
            break
            
        else:                                                 #Player enters invalid choice
            print("'" +playerChoice+ "'" +
                  " is not a proprer command." +
                  " Please enter hit or stand.")
            print()
            continue
        
def isGameOver(playerHand, dealerHand, score):
    pass    

#Show the dealers and players hand
def displayCards(playerHand, dealerHand, hit, stand):
    if hit == False and stand == False:                       #If hit and stand is false, print dealers and players hands
        print("DEALER'S SHOW CARD: ")
        for cards in dealerHand:                              #A for loop that shows all cards in dealers hand
            print(cards[0], cards[1])
        print("???")
        print()
        
        print("YOUR CARDS: ")
        for cards in playerHand:                              #A for loop that shows all cards in players hand
            print(cards[0], cards[1])
        print() 

    elif hit == True and stand == False:                      #If hit is true and stand is false, print only players hand
        print("YOUR CARDS: ")
        for cards in playerHand:                              #A for loop that shows all cards in players hand
            print(cards[0], cards[1])
        print()

    else:                                                     #Anything else, print only dealers hand
        print("DEALER'S SHOW CARD: ")
        for cards in dealerHand:                              #A for loop that shows all cards in dealers hand
            print(cards[0], cards[1])
        print()
        
#Blackjack intoduction        
def gameName():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

#Main function
def main():
    gameName()
    cardDeck = loadCardDeck()
    playerHand = []
    dealerHand = []

    hitting = False
    standing = False

    again = "y"
    while again.lower() == "y":                               #While loop for replaying game
        dealCards(cardDeck, playerHand, dealerHand)
        displayCards(playerHand, dealerHand, hitting, standing)
        hitOrStand(cardDeck, playerHand, dealerHand, hitting, standing)

        print("YOUR POINTS:     " +str(score(cardDeck, playerHand)))
        print("DEALER'S POINTS: " +str(score(cardDeck, dealerHand)))
        print()

        playerHand.clear()                                    #Clears players hand
        dealerHand.clear()                                    #Clears dealers hand
        
        again = input("Play again? (y/n): ")
        print()
        
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()
