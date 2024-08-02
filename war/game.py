from player import Player
from deck import Deck

# What are some of the best practices when it comes to version control or pair programming?

def set_up_players():
    """ This function sets up and returns players """
    allowed_players = ['2','3','4']
    players_set = False
    player_names = []
    players = []

    while not players_set:
        player_count = input("Amount of players: ") 
        if player_count not in allowed_players:
            print("Invalid player amount. Please pick between 2 to 4 players")
        else:
            players_set = True

    for i in range(int(player_count)):
        name = input(f"Enter the name for player {i + 1}: ").strip()
        if name:
            player_names.append(name)
        else:
            print("Player name cannot be empty. Please enter a valid name.")

    for name in player_names:
        players.append(Player(name))

    return players


def start_round(players):
    """ Draw a card from each players hand and compare """ 
    drawn_cards = []

    # Each player draws a card
    for player in players:
        card = player.draw_card()
        print(f"{player.name} has {len(player.hand)} cards left!")
        if card:
            drawn_cards.append((player, card))
        else:
            print(f"{player.name} has no more cards!")

    # If no players have cards left, the game is over
    if not drawn_cards:
        print("Game over!")
        return False
    
    # Determine the highest card
    highest_card = max(drawn_cards, key=lambda x: x[1])

    # Find all players with the highest card
    winners = [player for player, card in drawn_cards if card == highest_card[1]]

    # Print the result of this round
    for player, card in drawn_cards:
        print(f"{player.name} drew {card}")

    if len(winners) == 1:
        winner = winners[0]
        winner.add_cards([card for _, card in drawn_cards])
        print(f"{winners[0].name} wins this round with {highest_card[1]}!")
    else:
        print(f"It's a tie between {', '.join([player.name for player in winners])} with {highest_card[1]}!")

    return True


def main():
    players = set_up_players()
    deck = Deck()
    deck.shuffle()
    
    hands = deck.deal(len(players))

    for player, hand in zip(players, hands):
        player.add_cards(hand)
    
    # Game loop
    game_continues = True
    while game_continues and all(player.has_cards() for player in players):
        game_continues = start_round(players)
        input("Press Enter to draw the next card...")

    print("The game has ended.")




if __name__ == "__main__":
    main()