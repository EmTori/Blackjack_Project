import csv
def loadCardDeck():
    cardDeck = []
    with open("Card_Deck.csv", "r", newline = "") as file:
        reader = csv.reader(file)
        for row in reader:
            item = [row[0], row[1]]
            cardDeck.append(item)
    return cardDeck

def saveCardDeck(cardDeck):
    with open("Card_Deck.csv", "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerows(cardDeck)

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    cardDeck = loadCardDeck()




if __name__ == "__main__":
    main()