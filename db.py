#!/usr/bin/env python3

import sys

#Money file name
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
        money = []
        with open(MONEY_FILE, "r") as file:
            for line in file:
                line = line.replace("\n", "")
                money.append(line)
        return money
    except FileNotFoundError as e:                            #If the program cant find the card deck file it will end the program
        print("Could not find file: " +MONEY_FILE+ "!")
        exitProgram()
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()

#Save money file
def saveMoney(money):
    try:
        with open(MONEY_FILE, "w") as file:
            for line in money:
                file.write(line + "\n") 
    except OSError as e:                                      #OS error will end the program
        print(type(e), e)
        exitProgram()
    except Exception as e:                                    #Exception error will end the program
        print(type(e), e)
        exitProgram()
        
#Main function       
def main():
    money = loadMoney()

if __name__ == "__main__":
    main()
