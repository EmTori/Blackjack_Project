#!/usr/bin/env python3

import csv
import random
import sys

#File names in the current directory
DECK_FILENAME = "Card_Deck.csv"
DEALERS_HAND_FILENAME = "Dealers_Hand.csv"
PLAYERS_HAND_FILENAME = "Players_Hand.csv"

DEALERS_SCORE = 0
PLAYERS_SCORE = 0

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
        print("Starting a new empty file...")
        print()
        return dealersHand
    except Exception as e:
        print(type(e), e)
        exit_program()

#Saves the dealers hand file
def saveDealersHand(dealersHand):
    try:
        with open(DEALERS_HAND_FILENAME, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(dealersHand)
    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

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
        print("Starting a new empty file...")
        print()
        return playersHand
    except Exception as e:
        print(type(e), e)
        exit_program()

#Saves the Player hand file
def savePlayersHand(playersHand):
    try:
        with open(PLAYERS_HAND_FILENAME, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(playersHand)
    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

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
    try:
        with open(DECK_FILENAME, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(cardDeck)
    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def dealersCards(cardDeck, dealersHand):
    randomCard = random.randint(0, len(cardDeck)-1)
    card = cardDeck[randomCard]
    dealersHand.append(card)
    cardDeck.remove(card)
    saveDealersHand(dealersHand)
    saveCardDeck(cardDeck)

def playersCards(cardDeck, playersHand):
    randomCard = random.randint(0, len(cardDeck)-1)
    card = cardDeck[randomCard]
    playersHand.append(card)
    cardDeck.remove(card)
    savePlayersHand(playersHand)
    saveCardDeck(cardDeck)

def showPlayersHand(playersHand):
    print("YOUR CARDS: ")
    for cards in playersHand:
        print(cards[0], cards[1])
    print()

def showDealersHand(dealersHand):
    print("DEALER'S SHOW CARD: ")
    for cards in dealersHand:
        print(cards[0], cards[1])
    print()

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

    cardDeck = loadCardDeck()
    dealersHand = loadDealersHand()
    playersHand = loadPlayersHand()

    again = "y"
    while again == "y":
        dealersCards(cardDeck, dealersHand)
        
        playersCards(cardDeck, playersHand)
        playersCards(cardDeck, playersHand)

        showDealersHand(dealersHand)
        showPlayersHand(playersHand)

        while True:
            playerChoice = input("Hit or stand? (hit/stand): ")
            print()
            if playerChoice == "hit":
                playersCards(cardDeck, playersHand)
                showPlayersHand(playersHand)

            elif playerChoice == "stand":
                dealersCards(cardDeck, dealersHand)
                showDealersHand(dealersHand)
                break

            else:
                print("'" +playerChoice+ "'" + " is not a proprer command." + " Please enter hit or stand.")
                print()
                continue

        again = input("Play again? (y/n): ")

    print()
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()