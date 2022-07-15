import unittest
import tictactoe

X = "X"
O = "O"
EMPTY = None


class TicTacToeTest(unittest.TestCase):
    def setUp(self):
        self.empty_board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
        self.o_turn = [[EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
        self.error_board = [[X, X, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
        self.two_possible_actions = [[EMPTY, O, X],
            [O, O, X],
            [O, X, EMPTY]]
        self.draw = [[X, X, O],
            [O, O, X],
            [X, O, X]]
        self.action = (1, 1)
        self.x_wins = [[X, X, X],
            [EMPTY, O, EMPTY],
            [EMPTY, EMPTY, =O]

    def test_player_x(self):
        player = tictactoe.player(self.empty_board)
        self.assertEqual(player, "X")

    def test_player_o(self):
        player = tictactoe.player(self.o_turn)
        self.assertEqual(player, "O")

    def test_player_error(self):
        player = tictactoe.player(self.error_board)
        self.assertEqual(player, "Someone has made 2 moves in a row! ")

    def test_actions(self):
        actions = tictactoe.actions(self.two_possible_actions)
        self.assertIn((2, 2), actions)
        self.assertIn((0, 0), actions)

    def test_no_more_actions(self):
        actions = tictactoe.actions(self.draw)
        self.assertEqual(actions, None)

    def test_action_x(self):
        result = tictactoe.result(self.empty_board, self.action)
        self.assertEqual(result, [[EMPTY, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, EMPTY]])

    def test_action_o(self):
        result = tictactoe.result(self.o_turn, self.action)
        self.assertEqual(result, [[EMPTY, X, EMPTY],
                                  [EMPTY, O, EMPTY],
                                  [EMPTY, EMPTY, EMPTY]])

    def test_winner_x(self):
        winner = tictactoe.winner(self.x_wins)





if __name__ == "__main__":
    unittest.main()
