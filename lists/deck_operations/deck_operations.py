import random

def create_deck() -> list[str]:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['H', 'D', 'C', 'S']
    deck = []
    for rank in ranks:
        for suit in suits:
            a = rank + suit
            deck.append(a)
    return deck

def shuffle_deck(deck: list[str]) -> list[str]:
    shuffled = deck[:]
    random.shuffle(shuffled)
    return shuffled