#!/usr/bin/env python3

#Imported modules
import csv
from random import shuffle
import sys
import time

import db

#Card deck file name
DECK_FILENAME = "Card_Deck.csv"

#Exits program if something fails
def exitProgram():
    print("Exiting program.")
    print()
    print("Bye!")
    sys.exit()

def betMoney():
    pass
    

#Load the card deck file
def loadCardDeck():
    try:
        cardDeck = []
        with open(DECK_FILENAME, "r", newline = "") as file:
            reader = csv.reader(file)
            for row in reader:
                card = [row[0], row[1], row[2]]
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
def getScore(hand):
    total = 0                                                 #Total score in hand
    numberOfAces = 0                                          #Number of aces in a hand

    for card in hand:
        score = int(card[2])
        if score == 11:                                       #If the card is an Ace
            numberOfAces += 1                                 #Add 1 to number of aces
        total += score
        if numberOfAces >= 1:                                 #If number of aces is more than 1
            if total > 21:                                    #And total score is more than 21
                total -= 10                                   #Subtract 10 off of score
    return total

#Shuffles and deals the 2 first cards to both the player and dealer
def dealCards(cardDeck, playerHand, dealerHand):
    shuffle(cardDeck)                                         #Shuffles card deck
    
    for i in range(2):                                        #A for loop that adds 2 cards to the players hand
        playerHand.append(cardDeck.pop())
        dealerHand.append(cardDeck.pop())                     #Adds 1 card to the dealers hand

#Player chooses hit or stand   
def hitOrStand(cardDeck, playerHand, dealerHand, hit, stand, hand):
    while True:
        playerChoice = input("Hit or stand? (hit/stand): ")   #Player chooses hit or stand
        print()
        
        if playerChoice.lower() == "hit":                     #Player chooses hit
            hit = True                                        #Hit is set to true
            hand = False                                      #First hand is set to false
            playerHand.append(cardDeck.pop())                 #Adds card to player hand
            displayCards(playerHand, dealerHand, hit, stand)
            continue
            
        elif playerChoice.lower() == "stand":                 #Player chooses stand
            stand = True                                      #Stand is set to true
            while getScore(dealerHand) < 17:                  #If dealers score is below 17, they draw another card
                print("The dealer is drawing another card")
                print()
                time.sleep(1)                                 #1 second wait to give the illusion of dealer drawing another card
                dealerHand.append(cardDeck.pop())             #Adds card to dealer hand
                continue
            break
            
        else:                                                 #Player enters invalid choice
            print("'" +playerChoice+ "'" +
                  " is not a proprer command." +
                  " Please enter hit or stand.")
            print()
            continue

#Shows the games results depending on what score the player and dealer have       
def gameResults(playerHand, dealerHand, stand, hand):
    if getScore(playerHand) == 21 and hand == True:           #If the player gets 21, they win and get blackjack
        print("Blackjack!")
        print("You win! Congratulations!")
        print()
        
    elif getScore(playerHand) > 21:                           #If the player gets greater than 21, they bust and lose
        print("You busted and lose, Sorry.")
        print()

    elif getScore(dealerHand) > 21:                           #If the dealer gets greater than 21, they bust and the player wins
        print("The dealer busted and lost.")
        print("You win, Congratulations!")
        print()

    elif getScore(playerHand) > getScore(dealerHand):         #If the players score is greater than the dealers, the player wins
        print("You win.")
        print("Congratulations!")
        print()
            
    elif getScore(dealerHand) > getScore(playerHand):         #If the dealers score is greater than the players, the dealer wins
        print("The dealer won.")
        print("You lose, Sorry.")
        print()

    elif getScore(dealerHand) == getScore(playerHand):        #If the dealers score is the same as the players, there is a tie        
        print("There was a tie.")
        print("No one wins.")
        print()       
        
#Show the dealers and players hand
def displayCards(playerHand, dealerHand, hit, stand):
    if hit == False and stand == False:                       #If hit and stand is false, print dealers and players hands
        print("DEALER'S SHOW CARD: ")
        for card in dealerHand[:1]:                           #A for loop that shows all cards in dealers hand
            print(card[0],card[1])
            print("???")
        print()
        
        print("YOUR CARDS: (" +str(getScore(playerHand))+ " Points)")
        for cards in playerHand:                              #A for loop that shows all cards in players hand
            print(cards[0], cards[1])
        print()

    elif hit == True:                                         #If hit is true and stand is false, print only players hand
        print("YOUR CARDS: (" +str(getScore(playerHand))+ " Points)")
        for cards in playerHand:                              #A for loop that shows all cards in players hand
            print(cards[0], cards[1])
        print()

    elif stand == True:                                       #If hit is true and stand is false, print only players hand
        print("DEALER'S SHOW CARD: ")
        for cards in dealerHand:                              #A for loop that shows all cards in dealers hand
            print(cards[0], cards[1])
        print()

#Show the score for player and dealer
def showScores(playerHand, dealerHand):
    print("YOUR POINTS:     " +str(getScore(playerHand)))
    print("DEALER'S POINTS: " +str(getScore(dealerHand)))
    print()
        
#Blackjack intoduction        
def gameName():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

#Main function
def main():
    cardDeck = loadCardDeck()
    playerHand = []
    dealerHand = []

    hitting = False
    standing = False
    firstHand = True

    again = "y"
    while again.lower() == "y":                               #While loop for replaying game
        gameName()

        dealCards(cardDeck, playerHand, dealerHand)
        displayCards(playerHand, dealerHand, hitting, standing)
        hitOrStand(cardDeck, playerHand, dealerHand, hitting, standing, firstHand)

        showScores(playerHand, dealerHand)
        gameResults(playerHand, dealerHand, standing, firstHand)


        playerHand.clear()                                    #Clears players hand
        dealerHand.clear()                                    #Clears dealers hand
        
        again = input("Play again? (y/n): ")
        print()
        
    print("Come back soon!") 
    print("Bye!")

if __name__ == "__main__":
    main()