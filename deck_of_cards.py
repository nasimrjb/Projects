class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        print(f"{self.value} of {self.suit}")


class Deck:
    remaining = 52

    def __init__(self):
        values = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        self.cards = [Card(suit, value)
                      for s in suits for v in values]
        print(self.cards)

    def count(self):
        return Deck.remaining

    def __repr__(self):
        print(f"Deck of {Deck.remaining} cards")

    def _deal(self, remove_num):
        Deck.remaining = Deck.remaining - remove_num


a = Card("Diamonds", "3")
print(Card.__repr__(a))
Deck()
