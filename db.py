import csv

def loadMoney():
    playersMoney = []
    with open("money.txt", "r", newline = "") as file:
        reader = csv.reader(file)
        for row in reader:
            item = [row[0]]
            playersMoney.append(item)
    return playersMoney

def saveMoney(playersMoney):
    with open("money.txt", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(playersMoney)
        
def main():

    playersMoney = loadMoney()

    again = "y"
    while again == "y":

        print("Money: " + str(playersMoney))

        playersBet = int(input("How much money do you want to bet?: "))

        again = input("Bet again? (y/n): ")

if __name__ == "__main__":
    main()