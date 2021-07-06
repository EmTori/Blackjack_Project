#!/usr/bin/env python3

import csv
import random
import sys

import db

#File names in the current directory
DECK_FILENAME = "Card_Deck.csv"
DEALERS_HAND_FILENAME = "Dealers_Hand.csv"
PLAYERS_HAND_FILENAME = "Players_Hand.csv"

#Game score
DEALERS_SCORE = 0
PLAYERS_SCORE = 0

#Exits program if something fails
def exitProgram():
    print("Exiting program.")
    print()
    print("Bye!")
    sys.exit()

#Loads the dealers hand file
def loadDealersHand():
    try:
        dealersHand = []
        with open(DEALERS_HAND_FILENAME, "r", newline = "") as file:
            reader = csv.reader(file)
            for row in reader:
                card = [row[0], row[1]]
                dealersHand.append(card)
        return dealersHand
    except FileNotFoundError as e:                            #If the program cant find the dealers hand file it will creat a new one
        print("Could not find file: " +DEALERS_HAND_FILENAME+ "!")
        print("Starting a new empty file...")
        print()
        return dealersHand
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()

#Saves the dealers hand file
def saveDealersHand(dealersHand):
    try:
        with open(DEALERS_HAND_FILENAME, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(dealersHand)
    except OSError as e:                                      #OS error will end the program
        print(type(e), e)
        exitProgram()
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()

#Loads the Player hand file
def loadPlayersHand():
    try:
        playersHand = []
        with open(PLAYERS_HAND_FILENAME, "r", newline = "") as file:
            reader = csv.reader(file)
            for row in reader:
                card = [row[0], row[1]]
                playersHand.append(card)
        return playersHand
    except FileNotFoundError as e:                            #If the program cant find the players hand file it will creat a new one
        print("Could not find file: " +PLAYERS_HAND_FILENAME+ "!")
        print("Starting a new empty file...")
        print()
        return playersHand
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()

#Saves the Player hand file
def savePlayersHand(playersHand):
    try:
        with open(PLAYERS_HAND_FILENAME, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(playersHand)
    except OSError as e:                                      #OS error will end the program
        print(type(e), e)
        exitProgram()
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()

#Loads the deck of cards file
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
        print("Could not find file: " +DECK_FILENAME+ "!")
        exitProgram()
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()

#Saves the deck of cards file
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

#Adds a new card to the dealers hand
def dealersCards(cardDeck, dealersHand, DEALERS_SCORE):
    randomCard = random.randint(0, len(cardDeck)-1)           #Gets a random card from the card deck
    card = cardDeck[randomCard]
    dealersHand.append(card)                                  #Adds the random card to the dealers hand
    cardDeck.remove(card)                                     #Removes the random card from the card deck
    saveDealersHand(dealersHand)
    saveCardDeck(cardDeck)

#Adds a new card to the players hand
def playersCards(cardDeck, playersHand, PLAYERS_SCORE):
    randomCard = random.randint(0, len(cardDeck)-1)           #Gets a random card from the card deck
    card = cardDeck[randomCard]
    playersHand.append(card)                                  #Adds the random card to the players hand
    cardDeck.remove(card)                                     #Removes the random card from the card deck
    savePlayersHand(playersHand)
    saveCardDeck(cardDeck)

#Shows the players hand
def showPlayersHand(playersHand):
    print("YOUR CARDS: ")
    for cards in playersHand:
        print(cards[0], cards[1])
    print()

#Shows the dealers hand
def showDealersHand(dealersHand):
    print("DEALER'S SHOW CARD: ")
    for cards in dealersHand:
        print(cards[0], cards[1])
    print()

#---------------------------------------------------------------------------------------------------------------------------------------------#
##def playerBet(playersMoney):
##     money = float(playersMoney[0][0])
##     print("Money: " + str(money))
##     while True:
##         betAmount = int(input("Bet amount: "))
##
##         if betAmount < 5 and betAmount > 1000:
##             print("Bet amount cannot be less than 5 and greater than 1000.")
##             continue
##
##         elif betAmount > money:
##             print("You cannot bet more money than you have available.")
##             continue
##        
##         else:
##             money -= betAmount
##             playersMoney.append(money)
##             saveMoney(playersMoney)
##             print("Money: " + str(money))
##             break

#Loads the deck of cards file
def loadMoney():
    try:
        playersMoney = []
        with open("money.txt", "r", newline = "") as file:
            reader = csv.reader(file)
            for row in reader:
                money = [row[0]]
                playersMoney.append(money)
        return playersMoney
    except FileNotFoundError as e:                            #If the program cant find the card deck file it will end the program
        print("Could not find file: money.txt!")
        exitProgram()
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()

#Saves the deck of cards file
def saveMoney(playersMoney):
    try:
        with open("money.txt", "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(playersMoney)
    except OSError as e:                                      #OS error will end the program
        print(type(e), e)
        exitProgram()
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()

def betMoney(playersMoney):
    print("Money: ", playersMoney[0][0])
    while True:
        playerBet = int(input("Bet amount: "))
        if playerBet < 5 and playerBet > 1000:
            print("Player bet must be between 5 and 1000.")
            continue
        elif playerBet > int(playersMoney[0][0]):
            print("You cannot bet more money than you have.")
            continue
        elif playerBet <= int(playersMoney[0][0]):
            money = int(playersMoney[0][0])
            money -= playerBet
            playersMoney.append(money)
            saveMoney(playersMoney)
            break
#---------------------------------------------------------------------------------------------------------------------------------------------#   

#The game name and introduction
def gameName():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

#Main function
def main():
    gameName()

    cardDeck = loadCardDeck()
    dealersHand = loadDealersHand()
    playersHand = loadPlayersHand()

#---------------------------------------------------------------------------------------------------------------------------------------------#
    #playersMoney = db.loadMoney()
    playersMoney = loadMoney()
#---------------------------------------------------------------------------------------------------------------------------------------------#

    again = "y"
    while again == "y":

#---------------------------------------------------------------------------------------------------------------------------------------------#
        #playerBet(playersMoney)
        betMoney(playersMoney)
#---------------------------------------------------------------------------------------------------------------------------------------------#

        dealersCards(cardDeck, dealersHand, DEALERS_SCORE)
        
        playersCards(cardDeck, playersHand, PLAYERS_SCORE)
        playersCards(cardDeck, playersHand, PLAYERS_SCORE)

        showDealersHand(dealersHand)
        showPlayersHand(playersHand)

        while True:
            playerChoice = input("Hit or stand? (hit/stand): ")
            print()
            if playerChoice == "hit":
                playersCards(cardDeck, playersHand, PLAYERS_SCORE)
                showPlayersHand(playersHand)
                continue

            elif playerChoice == "stand":
                dealersCards(cardDeck, dealersHand, DEALERS_SCORE)
                showDealersHand(dealersHand)
                break

            else:
                print("'" +playerChoice+ "'" + " is not a proprer command." + " Please enter hit or stand.")
                print()
                continue
            
        print("YOUR POINTS:     " + str(PLAYERS_SCORE))
        print("DEALER'S POINTS: " + str(DEALERS_SCORE))
        print()

        again = input("Play again? (y/n): ")

    print()
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()
