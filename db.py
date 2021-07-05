#!/usr/bin/env python3

import csv
import sys

MONEY_FILE = "money.txt"

#Function will exit the program
def exitProgram():
    print("Exiting program.")
    print()
    print("Bye!")
    sys.exit()

#Load money file
def loadMoney():
    try:
        playersMoney = []
        with open("money.txt", "r", newline = "") as file:
            reader = csv.reader(file)
            for row in reader:
                item = [row[0]]
                playersMoney.append(item)
        return playersMoney
    except FileNotFoundError as e:                            #If the program cant find the card deck file it will end the program
        print("Could not find file: " +MONEY_FILE+ "!")
        exitProgram()
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()

#Save money file
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
        
def main():

    playersMoney = loadMoney()

    again = "y"
    while again == "y":

        print("Money: " + str(playersMoney))

        playersBet = int(input("How much money do you want to bet?: "))

        again = input("Bet again? (y/n): ")

if __name__ == "__main__":
    main()