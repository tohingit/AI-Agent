class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_winner = None

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        row, col = square
        if self.board[row][col] == ' ':
            self.board[row][col] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind, col_ind = square
        row = self.board[row_ind]
        if all([spot == letter for spot in row]):
            return True
        col = [self.board[r][col_ind] for r in range(3)]
        if all([spot == letter for spot in col]):
            return True
        if row_ind == col_ind:
            diagonal1 = [self.board[i][i] for i in range(3)]
            if all([spot == letter for spot in diagonal1]):
                return True
        if row_ind + col_ind == 2:
            diagonal2 = [self.board[i][2 - i] for i in range(3)]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in (spot for row in self.board for spot in row)

    def num_empty_squares(self):
        return sum([row.count(' ') for row in self.board])

    def available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

if __name__ == '__main__':
    game = TicTacToe()
    game.print_board()
