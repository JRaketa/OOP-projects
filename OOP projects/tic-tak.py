import random
import time

class Player:


    def __init__(self, is_human=True, marker='X'):
        self._is_human = is_human
        self._marker = marker

    @property
    def marker(self):
        return self._marker

    @property
    def is_human(self):
        return self._is_human

    def get_player_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()

    def get_human_move(self):
        move = input("Make move!: ")
        return move

    def get_computer_move(self):
        row = random.choice([1, 2, 3])
        col = random.choice(["A", "B", "C"])
        move = str(row) + col
        print("Computer move:", move, end=" ")
        print("\n")
        return move


class Board:


    EMPTY = 0
    COLUMNS = {"A": 1, "B": 2, "C": 3}
    ROWS = (0, 1, 2)


    def __init__(self, game_board=None):
        if game_board:
            self.game_board = game_board
        else:
            self.game_board = [[0, 0, 0],
                               [0, 0, 0],
                               [0, 0, 0]]


    def print_board(self):
        print("\n    A   B   C")
        for i, row in enumerate(self.game_board, 1):
            print(i, end=" | ")
            for col in row:
                if col != Board.EMPTY:
                    print(col, end=" | ")
                else:
                    print("  | ", end="")
            print("\n---------------")



    def submit_move(self, move, player):
        if not self.is_move_valid(move):
            print("Enter a valid move (Example: 1B)")
        else:
            column_index = Board.COLUMNS[move[1]] - 1
            row_index = int(move[0]) - 1
            value = self.game_board[row_index][column_index]
            if value == Board.EMPTY:
                self.game_board[row_index][column_index] = player.marker

    def is_move_valid(self, move):
        if len(str(move)) == 2 and int(move[0]) - 1 in Board.ROWS and move[1] in Board.COLUMNS:
            return True



    def is_winner(self, row, column, player):
        if self.check_row(row, player) == True:
            return True
        elif self.check_column(column, player) == True:
            return True
        elif self.check_diagonal(player) == True:
            return True
        elif self.check_intidiagonal == True:
            return True
        else:
            return False


    def check_row(self, row, player):
        row_index = int(row) - 1
        if self.game_board[row_index].count(player.marker) == 3:
            return True

    def check_column(self, column, player):
        column_index = Board.COLUMNS[column] - 1
        marker_count = 0
        for i in range(3):
            if self.game_board[i][column_index] == player.marker:
                marker_count += 1
        if marker_count == 3:
            return True
        else:
            return False

    def check_diagonal(self, player):
        marker_count = 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                marker_count += 1
        if marker_count == 3:
            return True
        else:
            return False


    def check_intidiagonal(self, player):
        marker_count = 0
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                marker_count += 1
        if marker_count == 3:
            return True
        else:
             return False


print("**************")
print(" Tic-Tac-Toe!")
print("**************")

board = Board()
human = Player()
computer = Player(False, 'O')

board.print_board()



while True:
    move = human.get_player_move()
    board.submit_move(move, human)
    board.print_board()

    if board.is_winner(move[0], move[1], human) and board.is_move_valid(move):
        print("You win!")
        break
    else:
        time.sleep(1)
        computer_move = computer.get_computer_move()
        board.submit_move(computer_move, computer)
        time.sleep(1)
        board.print_board()
        if board.is_winner(computer_move[0], computer_move[1], computer) and board.is_move_valid(move):
            print("Computer won!")
            break

