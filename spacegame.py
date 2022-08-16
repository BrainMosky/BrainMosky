import random


class space_game:
    '''
    Represent the entire game
    '''
    def  __init__(self) -> None:
        self.player1_board = game_board
        self.player2_board = game_board
        self.player1_hand = player_hand
        self.player2_hand = player_hand
        self.player1_deck = player_deck
        self.player2_deck = player_deck
        self.actual_player = 0

    def start_game(self) -> None:
        self.actual_player = random.randint(1, 2)
        # give both player a deck


class game_board:
    '''
    Represent the board of all played cards
    '''
    def  __init__(self) -> None:
        pass

class player_hand:
    '''
    Represent the player hand
    '''
    def __init__(self) -> None:
        pass

class player_deck:
    '''
    Represent the player hand
    '''
    def __init__(self) -> None:
        pass

class card:
    '''
    Represent the card
    '''
    def __init__(self, card_id) -> None:
        self.card_strengh = 0
        