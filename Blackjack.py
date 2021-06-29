#!/usr/bin/env python3

import csv
import random
import sys

#File names in the current directory
DECK_FILENAME = "Card_Deck.csv"
DEALERS_HAND_FILENAME = "Dealers_Hand.csv"
PLAYERS_HAND_FILENAME = "Players_Hand.csv"

#Exits program if something fails
def exit_program():
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
    except FileNotFoundError as e:            #If the program cant find the dealers hand file it will creat a new, empty, file
        print("Could not find file: " +DEALERS_HAND_FILENAME+ "!")
        print("Starting new file...")
        print()
        return dealersHand
    except Exception as e:
        print(type(e), e)
        exit_program()

#Saves the dealers hand file
def saveDealersHand(dealersHand):
    with open(DEALERS_HAND_FILENAME, "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(dealersHand)

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
    except FileNotFoundError as e:            #If the program cant find the players hand file it will creat a new, empty, file
        print("Could not find file: " +PLAYERS_HAND_FILENAME+ "!")
        print("Starting new file...")
        print()
        return playersHand
    except Exception as e:
        print(type(e), e)
        exit_program()

#Saves the Player hand file
def savePlayersHand(playersHand):
    with open(PLAYERS_HAND_FILENAME, "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(playersHand)

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
    except FileNotFoundError as e:            #If the program cant find the card deck file it will end the program
        print("Could not find file: " +DECK_FILENAME+ "!")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

#Saves the deck of cards file
def saveCardDeck(cardDeck):
    with open(DECK_FILENAME, "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(cardDeck)

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

    cardDeck = loadCardDeck()
    dealersHand = loadDealersHand()
    playersHand = loadPlayersHand()

    again = "y"
    while again == "y":

        print("DEALER'S SHOW CARD: ")


        again = input("Play again? (y/n): ")

    
    print()
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()