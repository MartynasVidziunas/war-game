import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        """Build a standard 52-card deck."""
        self.cards = [Card(suit, rank) for suit in Card.suits for rank in Card.ranks]

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def deal(self, num_hands, cards_per_hand=None):
        """
        Deal the cards into a specified number of hands.
        
        :param num_hands: Number of hands to deal into.
        :param cards_per_hand: Number of cards per hand, if None deals all cards equally.
        :return: A list of lists, each inner list representing a player's hand.
        """
        if cards_per_hand is None:
            cards_per_hand = len(self.cards) // num_hands
        hands = [[] for _ in range(num_hands)]
        for i in range(cards_per_hand * num_hands):
            hands[i % num_hands].append(self.cards.pop(0))
        return hands

    def draw(self):
        """Draw a single card from the deck."""
        return self.cards.pop(0) if self.cards else None

    def __str__(self):
        return f"Deck of {len(self.cards)} cards"

    def __repr__(self):
        return f"Deck(cards={self.cards})"