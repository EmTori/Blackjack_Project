#!/usr/bin/env python3

#Imported modules
import csv
from random import shuffle
import sys
import time
import db

#Card deck and money file name
DECK_FILENAME = "Card_Deck.csv"
MONEY_FILENAME = "money.txt"

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
                card = [row[0], row[1], row[2]]
                cardDeck.append(card)
        return cardDeck
    except FileNotFoundError as e:                                  #If the program cant find the card deck file it will end the program
        print("Could not find file " +DECK_FILENAME+ "!")
        exitProgram()
    except Exception as e:                                          #Exception error will end the program
        print(type(e), e)
        exitProgram()

#Save the card deck file
def saveCardDeck(cardDeck):
    try:
        with open(DECK_FILENAME, "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerows(cardDeck)
    except OSError as e:                                            #OS error will end the program
        print(type(e), e)
        exitProgram()
    except Exception as e:                                          #Exception error will end the program
        print(type(e), e)
        exitProgram()
        
#The player is running out of money/ chips and needs to get more        
def notEnoughMoney(money):
    if float(money[0]) > 5 and float(money[0]) <= 10:               #If the players money is between $5 and $10
        print("You are running low on chips,")                      #Tell the player they are running out of chips
        moreChips = input("Would you like to buy more? (y/n): ")    #Allow player option to get more chips
        if moreChips.lower() == "y":                                #If player chooses to get more chips
            while True:                                             #A while loop that runs until correct data is entered
                try:
                    print()
                    chipAmount = int(input("How many chips do you want? ($5 - $1,000): "))
                except ValueError:                                  #Value error will allow player to input again
                    print("You entered an invalid number. Please try again.")
                    continue
                except Exception as e:                              #Exception error will allow player to input again
                    print("Unexpected exception, plaese try again")
                    print(type(e), e)
                    continue
                if chipAmount < 5 or chipAmount > 1000:             #The player must choose a number between $5 and $1,000
                    print("Please choose an amount between $5 and $1,000.")
                    continue
                else:                                               #If everything is correct
                    print("$" +str(chipAmount)+ " has been added to your funds.")
                    print()
                    totalChips = round(float(money[0]) + chipAmount, 2)
                    money.clear()                                   #Clear money file 
                    money.append(str(totalChips))                   #Add total chips to money file
                    db.saveMoney(money)                             #Save money file
                    break
        elif moreChips.lower() == "n":                              #If player chooses not to get more chips
            print()
            print("Warning! If your funds get much lower you will no longer be able to play.")
            print() 
        else:                                                       #If player something other than 'y' or 'n', their answer defaults to no
            print("'" +str(moreChips)+ "' is an invalid command. We are defaulting your answer to no.")
            print()
            print("Warning! If your funds get much lower you will no longer be able to play.")
            print()
                        
    elif float(money[0]) <= 5:                                      #If the players money is less than $5
        print("You are low on chips, and now need to buy more.")    #They need to get more chips/ money
        print()
        while True:                                                 #A while loop that runs until correct data is entered
            try:
                chipAmount = int(input("How many chips do you want? $5 - $1,000: "))
            except ValueError:                                      #Value error will allow player to input again
                print("You entered an invalid number. Please try again.")
                print()
                continue
            except Exception as e:                                  #Exception error will allow player to input again
                print("Unexpected exception, plaese try again")
                print(type(e), e)
                print()
                continue
            if chipAmount < 5 or chipAmount > 1000:                 #The player must choose a number between $5 and $1,000
                print("Please choose an amount between $5 and $1,000.")
                print()
                continue
            else:                                                   #If everything is correct
                print("$" +str(chipAmount)+ " has been added to your funds.")
                print()
                totalChips = round(float(money[0]) + chipAmount, 2)
                money.clear()                                       #Clear money file 
                money.append(str(totalChips))                       #Add total chips to money file
                db.saveMoney(money)                                 #Save money file
                break

#The player will bet money on their game       
def betMoney(money):
    print("Money: " +str(money[0]))
    while True:                                                     #A while loop that runs until correct data is entered
        try:
            playersBet = float(input("Bet amount: "))               #Player may enter how much they want to bet
        except ValueError:                                          #Value error will allow player to input again
            print("You entered an invalid number. Please try again.")
            print()
            continue
        except Exception as e:                                      #Exception error will allow player to input again
            print("Unexpected exception, try again")
            print(type(e), e)
            print()
            continue
        if playersBet > float(money[0]):                            #Player cannot bet more than the amount of money they have
            print("You cannot bet more money than you have available.")
            print()
            continue
        elif playersBet < 5 or playersBet > 1000:                   #Player cannot bet less than $5 or more than $1000
            print("You may only bet between $5 and $1,000.")
            print()
            continue
        else:                                                       #If everything is correct
            newMoney = round(float(money[0]) - float(playersBet), 2)
            money.clear()                                           #Clear money file 
            money.append(str(newMoney))                             #Add new amount to money file
            db.saveMoney(money)                                     #Save money file
            return playersBet

#If the player is the winner, they win 1.5x their bet
def winningBetCalculation(money, playersBet):
    playersWinnings = round(float(money[0]) + (float(playersBet) * 1.5), 2)
    money.clear()                                                   #Clear money file 
    money.append(str(playersWinnings))                              #Add new amount to money file
    db.saveMoney(money)                                             #Save money file
     
#Assigning values to the cards in the deck
def getScore(hand):
    total = 0                                                       #Total score in hand
    numberOfAces = 0                                                #Number of aces in a hand

    for card in hand:
        score = int(card[2])
        if score == 11:                                             #If the card is an Ace
            numberOfAces += 1                                       #Add 1 to number of aces
        total += score
        if numberOfAces >= 1:                                       #If number of aces is more than 1
            if total > 21:                                          #And total score is more than 21
                total -= 10                                         #Subtract 10 off of score
                numberOfAces -= 1
    return total

#Shuffles and deals the 2 first cards to both the player and dealer
def dealCards(cardDeck, playerHand, dealerHand):
    shuffle(cardDeck)                                               #Shuffles card deck
    
    for i in range(2):                                              #A for loop that adds 2 cards to the players hand
        playerHand.append(cardDeck.pop())
        dealerHand.append(cardDeck.pop())                           #Adds 1 card to the dealers hand

#Player chooses hit or stand   
def hitOrStand(cardDeck, playerHand, dealerHand, hit, stand):
    while True:
        playerChoice = input("Hit or stand? (hit/stand): ")         #Player chooses hit or stand
        if playerChoice.lower() == "hit":                           #Player chooses hit
            hit = True                                              #Hit is set to true
            playerHand.append(cardDeck.pop())                       #Adds card to player hand
            displayCards(playerHand, dealerHand, hit, stand)
            continue
        #If player chooses stand and player score is less than and equal 21 dealer shows cards and draws until dealer score is greater than 17   
        elif playerChoice.lower() == "stand" and getScore(playerHand) <= 21:
            stand = True                                            #Stand is set to true
            hit = False                                             #Hit is set to false
            displayCards(playerHand, dealerHand, hit, stand)        #Dealer shows their cards
            while getScore(dealerHand) <= 16:                       #If dealers score is below 17, they draw another card
                print("The dealer is drawing another card...")
                time.sleep(1)                                       #1 second wait to give the illusion of dealer drawing another card
                dealerHand.append(cardDeck.pop())                   #Adds card to dealer hand
                displayCards(playerHand, dealerHand, hit, stand)    #Dealer shows their cards)
                continue
            break
        #If player chooses stand and player score is greater than 21 dealer only shows cards but dosnt draw anything
        elif playerChoice.lower() == "stand" and getScore(playerHand) > 21:
            stand = True                                            #Stand is set to true
            hit = False                                             #Hit is set to false
            displayCards(playerHand, dealerHand, hit, stand)        #Dealer shows their cards
            break
        else:                                                       #Player enters invalid choice
            print("'" +playerChoice+ "'" +
                  " is not a proprer command." +
                  " Please enter hit or stand.")
            print()
            continue

#Shows the games results depending on what score the player and dealer have       
def gameResults(playerHand, dealerHand, money, playersBet):
    if getScore(playerHand) == 21:                                  #If the player gets 21, they win and get blackjack
        print("Blackjack! You win!")
        print("Congratulations!")
        print()
        winningBetCalculation(money, playersBet)                    #Player wins and gets winnings added to money file
    elif getScore(playerHand) > 21:                                 #If the player gets greater than 21, they bust and lose
        print("You busted and lost.")
        print("Sorry.")
        print()
    elif getScore(dealerHand) > 21:                                 #If the dealer gets greater than 21, they bust and the player wins
        print("Dealer busted, You win!")
        print("Congratulations!")
        print()
        winningBetCalculation(money, playersBet)                    #Player wins and gets winnings added to money file
    elif getScore(playerHand) > getScore(dealerHand):               #If the players score is greater than the dealers, the player wins 
        print("You beat the dealer! Congratulations!")
        print()
        winningBetCalculation(money, playersBet)                    #Player wins and gets winnings added to money file
    elif getScore(playerHand) < getScore(dealerHand):               #If the player score is less than the dealers, the player loses
        print("You lose, Sorry.")
        print()
    else:                                                           #If the dealers score is the same as the players, there is a tie 
        print("There was a tie.")
        print("No one wins.")
        print()
        
#Show the dealers and players hand
def displayCards(playerHand, dealerHand, hit, stand):
    if hit == False and stand == False:                             #If hit and stand is false, print dealers and players hands
        print()
        print("DEALER'S SHOW CARD: ")
        for card in dealerHand[:1]:                                 #A for loop that shows all cards in dealers hand
            print(card[0],card[1])
            print("???")
        print()
        
        print("YOUR CARDS: (" +str(getScore(playerHand))+ " Points)")
        for cards in playerHand:                                    #A for loop that shows all cards in players hand
            print(cards[0], cards[1])
        print()

    elif hit == True:                                               #If hit is true and stand is false, print only players hand
        print()
        print("YOUR CARDS: (" +str(getScore(playerHand))+ " Points)")
        for cards in playerHand:                                    #A for loop that shows all cards in players hand
            print(cards[0], cards[1])
        print()

    elif stand == True:                                             #If hit is true and stand is false, print only players hand
        print()
        print("DEALER'S SHOW CARD: ")
        for cards in dealerHand:                                    #A for loop that shows all cards in dealers hand
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
    again = "y"
    while again.lower() == "y":                                     #While loop for replaying game
        cardDeck = loadCardDeck()                                   #Load card deck
        playerHand = []
        dealerHand = []

        money = db.loadMoney()                                      #Load money file from another python module

        hitting = False
        standing = False

        gameName()
        
        notEnoughMoney(money)
        playersBet = betMoney(money)

        dealCards(cardDeck, playerHand, dealerHand)
        displayCards(playerHand, dealerHand, hitting, standing)
        hitOrStand(cardDeck, playerHand, dealerHand, hitting, standing)

        showScores(playerHand, dealerHand)
        gameResults(playerHand, dealerHand, money, playersBet)
        
        print("Money: " +str(money[0]))
        print()

        again = input("Play again? (y/n): ")
        print()
        
    print("Come back soon!") 
    print("Bye!")

if __name__ == "__main__":
    main()
