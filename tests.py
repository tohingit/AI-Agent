import unittest
from tic_tac_toe import TicTacToe
from ai_player import AIPlayer

class TestAIPlayer(unittest.TestCase):

    def test_ai_player_move(self):
        game = TicTacToe()
        ai = AIPlayer('X')
        move = ai.get_move(game)
        self.assertIn(move, game.available_moves())

    def test_ai_player_winning_move(self):
        game = TicTacToe()
        ai = AIPlayer('X')
        game.make_move((0, 0), 'X')
        game.make_move((1, 1), 'X')
        move = ai.get_move(game)
        self.assertEqual(move, (2, 2))

if __name__ == '__main__':
    unittest.main()
