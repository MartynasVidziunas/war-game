class Card:
    """ A list of valid suits for the cards"""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    
    """ A list of valid ranks for the cards """
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    """ A dictionary mapping each rank to its value, used to compare cards """ 
    values = {rank: value for value, rank in enumerate(ranks, start=2)}

    """ Initilaizes a Card object with suit and rank """ 
    def __init__(self, suit, rank):
        if suit not in Card.suits:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in Card.ranks:
            raise ValueError(f"Invalid rank: {rank}")
        
        self.suit = suit
        self.rank = rank
        self.value = Card.values[rank]
    
    """ Returns a string representation of the card """
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    """  Checks if two cards are equal based on their rank """
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank
        return False

    """ Checks if one card is less than another based on its value """ 
    def __lt__(self, other):
        if isinstance(other, Card):
            return self.value < other.value
        return False

    """ Checks if one card is less than or equal to another based on its value """ 
    def __le__(self, other):
        if isinstance(other, Card):
            return self.value <= other.value
        return False

    """ Checks if one card is greater than another based on its value """ 
    def __gt__(self, other):
        if isinstance(other, Card):
            return self.value > other.value
        return False
    
    """ Checks if one card is greater than or equal to another based on its value """ 
    def __ge__(self, other):
        if isinstance(other, Card):
            return self.value >= other.value
        return False