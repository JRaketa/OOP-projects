import random
import time

class Player:
    """Class that represents a player of the game.

    Attributes:
        is_human (bool): the type of player. Player can be either human or
            computer. The True value is associated with human player. The False
            value is associated with computer player. By default it is
            True.
        marker (str): A marker that is associated with the player. The marker
            must a single capital letter. The marker is printed on the game
            board as the player move. By default it is 'X'.

    Methods:
        get_player_move(board): runs get_human_move() function if is_human is
            True. Otherwise, runs get_computer_move() method.
            Args:
                board (Board): an instance of a class Board.
        get_computer_move(board): returns a random move for the computer player.
            Args:
                board (Board): an instance of a class Board.
        get_human_move(): requires to type the move as input.
    """

    def __init__(self, is_human=True, marker='X'):
        """Initialize the values of the instance attributes of an instance of
            Player.

        Args:
            is_human (bool): the type of player. Player can be either human or
                computer. The True value is associated with human player. The
                False value is associated with computer player. By default it is
                True.
            marker (str): A marker that is associated with the player. The marker
                must a single capital letter. The marker is printed on the game
                board as the player move. By default it is 'X'.
        """
        self._is_human = is_human
        self._marker = marker

    @property
    def marker(self):
        """Marker that is associated with the player."""
        return self._marker

    @property
    def is_human(self):
        """Type of the player."""
        return self._is_human

    def get_player_move(self, board):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move(board)

    def get_human_move(self):
        """Requires to type the move as input from human player.

        The input is row and column coordinate of the board. The input structure
        is [number][capital_letter]. [number] is a value from the list of
        [1, 2, 3]. [capital_letter] is a value from the list of ["A", "B", "C"].
        Examples of the input:
            1A, 2B, 3C.
        Correctness of the input value is checked in board.
        """
        move = input("Make move!: ")
        return move

    def get_computer_move(self, board):
        """Generator of the computer move.

        The generator choses randomly one move from the board instance.

        Args:
            board: An instance of a class Board.

        Returns:
            A random value with format: [number][capital_letter]. [number] is from the list [1, 2, 3].
            [capital_letter] is from the list ["A", "B", "C"].
            Example: 1A, 2B, 3C.
        """
        move = random.choice(board.moves)
        print("Computer move:", move, end=" ")
        print("\n")
        return move


class Board:
    """Class that represents the board of the game.

    Attributes:
        game_board (list):
        moves (list):

    Methods:
        moves_gererate(): generates the list of possible moves.
        print_board(): displays the board.
        submit_move(): inserts input of a player to the board.
        is_move_valid(): checks the input's validity.
        is_winner(): checks if the player is a winner or not. If a row
            or a column or a diagonal or an antidiagonal is filled by markers of
            the player, the player wins.
        check_row(): checks filling of each row by the player's marker.
        check_column(): checks filling of each column by the player's marker.
        check_diagonal(): checks filling of the diagonal by the player's marker.
        check_intidiagonal(): checks filling of the antidiagonal by the player's
            marker.
        check_tie(): checks absense of empty cells in the board.
    """

    EMPTY = 0
    COLUMNS = {"A": 1, "B": 2, "C": 3}
    ROWS = (0, 1, 2)



    def __init__(self, game_board=None):
        """Initialize the instance attributes of the Board's instance.

        Args:
            game_board (bool): the game board that has 3*3 dymention. Resresents
                moves of every player. By default has value None that
                respresents an empty game board.
        """
        if game_board:
            self.game_board = game_board
        else:
            self.game_board = [[0, 0, 0],
                               [0, 0, 0],
                               [0, 0, 0]]
        self.moves = self.moves_gererate()

    def moves_gererate(self):
        """Returns a list of the possible moves.

        Create a list with nine elements. The elements are the board coordinates.
        The elements are strings. The coordinates have format of
        [number][capital_letter]. [number] is a value from the list [1, 2, 3].
        [capital_letter] is a value from the list of ["A", "B", "C"].
        Examples of the coordinates: "1B", "2B", "3C".

        Returns:
            A list of with all coordinates of the board.
        """
        generated_moves = []
        for col in range(len(Board.COLUMNS)):
            col_label = list(Board.COLUMNS.items())[col][0]
            for row in range(len(Board.ROWS)):
                new_move = str(row + 1) + col_label
                generated_moves.append(new_move)
        return generated_moves


    def print_board(self):
        """Displays the board.

        Displays the actual board condition. Columns are labeled by capital
        letters: A, B, C. Rows are labeled by numbers: 1, 2, 3.
        The board has nine cells. Dimention of the board is 3 by 3. The cells
        are separated from each other by vertical bars '|' and dashes '---' as
        vertical and horizontal spliters respectively.
        The cells can be empty or with the player marker.
        Example of the board:
                A   B   C
            1 | X |   |   |
            ---------------
            2 |   | O |   |
            ---------------
            3 |   | X |   |
            ---------------
        """
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
        """Inserts input of a player to the board.

        Converts the player move into the game board coordinates and inserts
        the player's marker into the game board according to this coordinates.

        Args:
            move (str): Coordinate one of the board's cell.
                Example: 1A, 2B, 3C.
            player (Player): an instance of Player. It can be a human player or
                computer player.

        Raises:
            "Enter a valid value": if the input value is invalid.
        """
        if not self.is_move_valid(move):
            print("Enter a valid move (Example: 1B)")
        else:
            column_index = Board.COLUMNS[move[1]] - 1
            row_index = int(move[0]) - 1
            value = self.game_board[row_index][column_index]
            if value == Board.EMPTY:
                self.game_board[row_index][column_index] = player.marker
                self.moves.remove(move)

    def is_move_valid(self, move):
        """Checks the input's validity.

        Checks the input length and input format. Correct input length is 2. The
        first symbol of the input is an integer from the list [1, 2, 3]. The
        second symbol of the input is a capital letter from the list [A, B, C].

        Args:
            move (str): legth of the

        Returns:
            True if the input is valid. False if the input in invalid.
        """
        if len(str(move)) == 2 and int(move[0]) - 1 in Board.ROWS and move[1] in Board.COLUMNS:
            return True



    def is_winner(self, row, column, player):
        """Checks if the player is a winner or not.

        If a row or a column or a diagonal or an antidiagonal is filled with
        markers of the player, the player wins. The winner is checks after every
        move.


        Args:
            row (str): the first symbol of the input. Can be "1" or "2"
            or "3".
            column (str): the second symbol of the input. Can be "A" or "B"
            or "C".
            player (Player): a player that made the move.
        """
        if self.check_row(row, player) == True:
            return True
        elif self.check_column(column, player) == True:
            return True
        elif self.check_diagonal(player) == True:
            return True
        elif self.check_intidiagonal(player) == True:
            return True
        else:
            return False


    def check_row(self, row, player):
        """Checks if a row is filled with the player's marker.

        Converts the row input to integer. The integer is converted to the row's
        index by substructing 1. Counts number of the player's markers in the
        row with this index of the game board.

        Args:
            row (str): the first symbol of the input. Can be "1" or "2"
            or "3".
            column (str): the second symbol of the input. Can be "A" or "B"
            or "C".
            player (Player): a player that made the move.

        Returns:
            True if there are three player's markers in the row. False if there
            are less than three player's marker's in the row.
        """
        row_index = int(row) - 1
        if self.game_board[row_index].count(player.marker) == 3:
            return True

    def check_column(self, column, player):
        """Checks if a column is filled with the player's marker.

        Converts the column to the column's index. Counts number of the player's
        markers in the column of the game board.

        Args:
            column (str): can be "A" or "B" or "C".
            player (Player): a player that made the move.

        Returns:
            True if there are three player's markers in the column. False if there
            are less than three player's marker's in the column.
        """
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
        """Checks if the diagonal is filled with the player's marker.

        Counts number of the player's markers in the diagonal of the game board.

        Returns:
            True if number of the player's markers in the diagonal is three.
            False if number of the player's markers in the diagonal is less than
            three.
        """
        marker_count = 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                marker_count += 1
        if marker_count == 3:
            return True
        else:
            return False


    def check_intidiagonal(self, player):
        """Checks if the antidiagonal is filled with the player's marker.

        Counts number of the player's markers in the antidiagonal of the game
        board.

        Returns:
            True if number of the player's markers in the antidiagonal is three.
            False if number of the player's markers in the antidiagonal is less
            than three.
        """
        marker_count = 0
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                marker_count += 1
        if marker_count == 3:
            return True
        else:
             return False

    def check_tie(self):
        """Checks if it is tie or not.

        Returns:
            True if there are not empty cells in the game board. False if there
            empty cells in the game board.
        """
        empty_counter = 0
        for i in range(3):
            row = self.game_board[i]
            for j in range(3):
                if row[j] == Board.EMPTY:
                    empty_counter += 1
        if empty_counter == 0:
            return True











#print("**************")
#print(" Tic-Tac-Toe!")
#print("**************")

#board = Board()
#human = Player()
#computer = Player(False, 'O')

#board.print_board()



#while True:
#    move = human.get_player_move(board)
#    board.submit_move(move, human)
#    board.print_board()

#    if board.is_winner(move[0], move[1], human) and board.is_move_valid(move):
#        print("You win!")
#        break
#    if board.check_tie():
#        print("It is a tie! Game is over!")
#        break
#    else:
#        time.sleep(1)
#        computer_move = computer.get_computer_move(board)
#        board.submit_move(computer_move, computer)
#        time.sleep(1)
#        board.print_board()
#        if board.is_winner(computer_move[0], computer_move[1], computer) and board.is_move_valid(move):
#            print("Computer won!")
#            break
#        if board.check_tie():
#            print("It is a tie! Game is over!")
#            break
