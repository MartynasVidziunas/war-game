class Player:
    """ Initializes the Player object with a name and a hand (empty for now) """
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self):
        """ Draw the top card from the player's hand """
        if self.hand:
            return self.hand.pop(0)
        return None

    def add_cards(self, cards):
        """ Add cards to the player's hand """
        if isinstance(cards, list):
            self.hand.extend(cards)
        else:
            self.hand.append(cards)

    def has_cards(self):
        """ Check if the player has any cards left """
        return len(self.hand) > 0

    def __str__(self):
        return f"Player {self.name} with {len(self.hand)} cards"

    def __repr__(self):
        return f"Player(name='{self.name}', hand={self.hand})"

    
