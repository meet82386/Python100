'''
    2 to 10 => Value counted
    J, Q, K => Counted as 10
    A       => 1, or 11.

    try to make maximum number, if it overpass 21 you will immediately loose.
'''
import random

def getCard():
    '''Returns random card from deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0, len(cards)-1)]


def calcScore(cardList):
    """Function to calculate score of player."""

    if sum(cardList) == 21 and len(cardList) == 2:
        return 0

    if 11 in cardList and sum(cardList) > 21:
        cardList.remove(11)
        cardList.append(1)

    return sum(cardList)


consent = input("Do you want to play game blackjack? 'y'or 'n' ")

completed = False

while not completed:
    
    myCards = [getCard(), getCard()]
    computerCards = [getCard(), getCard()]

    userScore = calcScore(myCards)
    computerScore = calcScore(computerCards)

    print(f"Your cards are {myCards} and value: {userScore}") 
    print(f"Computer's first card: {computerCards[0]}")

    if userScore == 0:
        print("You won. BlackJack")
        completed = True
    elif computerScore == 0:
        print("Computer won.")
        completed = True
    elif userScore > 21:
        print(f"Your Score {userScore}. You loose")
        completed = True
    elif computerScore > 21:
        print(f"You won. BlackJack")
        completed = True

    while not completed:
        ip = input("Do you want to draw another card? 'y' or 'n'")
        if ip == 'n':
            completed = True
        else:
            myCards.append(getCard())

            if 

    