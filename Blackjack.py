import csv
def loadCardDeck():
    cardDeck = []
    with open("Card_Deck.csv", "r", newline = "") as file:
        reader = csv.reader(file)
        for row in reader:
            item = [row[0], row[1], row[2]]
            cardDeck.append(item)
    return cardDeck

def saveCardDeck(cardDeck):
    with open("Card_Deck.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(cardDeck)

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    again = "y"
    while again == "y":

        cardDeck = loadCardDeck()

        print(cardDeck)
        print("Money: ", money)

        again = input("Play again? (y/n): ")
    
    print("Come back soon!")
    print("Bye!")

if __name__ == "__main__":
    main()