import unittest
import spacegame


class Testspace_game(unittest.TestCase):
    def test___init__(self):
        game = spacegame.space_game()
        self.assertEqual(game.player1_board, spacegame.game_board)
        self.assertEqual(game.player2_board, spacegame.game_board)
        self.assertEqual(game.player1_hand, spacegame.player_hand)
        self.assertEqual(game.player2_hand, spacegame.player_hand)
        self.assertEqual(game.player1_deck, spacegame.player_deck)
        self.assertEqual(game.player2_deck, spacegame.player_deck)

    def test_start_game(self):
        game = spacegame.space_game()
        game.start_game()
        print(game.player1_board)
        self.assertTrue(game.actual_player == 1 or game.actual_player == 2)

if __name__ == '__main__':
    unittest.main()