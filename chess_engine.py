class ChessGameEngine:
    def __init__(self, player):
        self.player = player
        self.user_input = None
        self.game_over = False
        self.board = [["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p","p","p","p","p","p","p","p"],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ["P","P","P","P","P","P","P","P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]]
        self.game_loop()


    def print_board(self, board):
        k = 8
        for i in range(len(board)):
            row = ""
            num = 0 # number of piece in each row
            for piece in board[i]:
                if num < 8:
                    num +=1
                    row += piece + "|"
                else:
                    num += 1
                    row += piece + "\n"
            print(k, "|"+row)   # prints out the row labels and the board next to it
            k -= 1
        print("""   a b c d e f g h""")  # prints the columns of the board


    def game_loop(self):
        self.print_board(self.board)
        while self.game_over != True:
            print("\n========================================\n")
            self.player_choice()
        print("\n==============Game Aborted==============\n")


    def player_choice(self):
        print("Player " + str(self.player)+"'s turn, what's your move? ")
        self.user_input = input("Enter here: ")
        if (self.user_input.lower() == "quit"):
            self.game_over = True
            self.player_choice()
        elif (self.user_input.lower() == "check"):
            check_piece_pos = str(input("Enter the piece's position on the current board state to check for valid moves: "))
            print(self.valid_moves(check_piece_pos))
        elif len(self.user_input) < 4:
            self.move_piece(self.user_input)
            self.swap_turn()
        else:
            print("\nNot a known command/move, try again\n")


    def swap_turn(self):
        if self.player == 1: self.player += 1
        else: self.player -= 1


    def different_color_check(self, curr_pos, new_pos):
        white_curr = self.board[curr_pos[0]][curr_pos[1]].isupper()
        black_new = self.board[new_pos[0]][new_pos[1]].islower()
        diff_color_pieces = (white_curr and black_new) or (not white_curr and not black_new)
        return diff_color_pieces


    def valid_moves(self, str_current_pos):
        if len(str_current_pos) > 2:
            msg = "\nInvalid position\n"
            return msg
        num_lst = [7,6,5,4,3,2,1,0]
        letter_lst = ["a","b","c","d","e","f","g","h"]
        real_row = num_lst[int(str_current_pos[1]) - 1]
        real_col = int(ord(str_current_pos[0]) - 97)
        piece = self.board[real_row][real_col]
        piece_move = self.piece_dir_moves(piece)
        valid_moves = []
        for move in piece_move:
            if piece.lower() == "k" or piece.lower() == "n":
                new_col = real_col + move[1]
                new_row = real_row + move[0]
                different_color_pieces = self.different_color_check((real_row, real_col), (new_row, new_col))
                if new_col < 0 and new_row < 0:
                    pass
                elif new_col <= 7 and new_row <= 7 :
                    if different_color_pieces or self.board[new_row][new_col] == ".":
                        move_col = letter_lst[(new_col)]
                        move_row = str(num_lst[(new_row)] + 1)
                        valid_moves.append(move_col + move_row)
            elif piece == "p" or piece == "P":
                if piece.islower() and real_row == 1:
                    new_col = real_col + move[1]
                    new_row = real_row + move[0]
                    different_color_pieces = self.different_color_check((real_row, real_col), (new_row, new_col))
                    if new_col < 0 and new_row < 0:
                        pass
                    elif new_col <= 7 and new_row <= 7 :
                        if different_color_pieces or self.board[new_row][new_col] == ".":
                            move_col = letter_lst[(new_col)]
                            move_row = str(num_lst[(new_row)] + 1)
                            valid_moves.append(move_col + move_row)
                elif piece.isupper() and real_row == 6:
                    new_col = real_col + move[1]
                    new_row = real_row + move[0]
                    if new_col < 0 and new_row < 0:
                        pass
                    elif new_col <= 7 and new_row <= 7 :
                        different_color_pieces = self.different_color_check((real_row, real_col), (new_row, new_col))
                        if different_color_pieces or self.board[new_row][new_col] == ".":
                            move_col = letter_lst[(new_col)]
                            move_row = str(num_lst[(new_row)] + 1)
                            valid_moves.append(move_col + move_row)
                    else:
                        pass
            elif piece.lower() == "q" or piece.lower() == "r" or piece.lower() == "b":
                pass
            
        print("\nValid moves for the piece: ")
        return valid_moves

    def piece_dir_moves(self, piece):
        """
        This funciton returns the directions of which the piece can move on the board, mainly applies to all the pieces except for 
        the king piece (k and K), the knight (N and n) and the pawn (P and p) where it shows all the possible positions that it can move
        instead of the general direction like the other pieces
        """
        dir_moves = []
        if piece.lower() == "k" or piece.lower() == "q":
            dir_moves = [(1, 1),(1, 0),(0, 1),(1, -1),(-1, 1),(-1, -1),(0, -1),(-1, 0)] 
        elif piece == "p": # black pawn
            dir_moves = [(1, 0), (1, 1), (1, -1), (2, 0)]
        elif piece == "P": # white pawn
            dir_moves = [(-1, 0), (-1, 1), (-1, -1),(-2, 0)]
        elif piece.lower() == "n":
            dir_moves = [(2, 1),(2, -1),(-1, 2),(1, 2),(-2, 1),(-2, -1),(-1, -2),(1, -2)] 
        elif piece.lower() == "b":
            dir_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        elif piece.lower() == "r":
            dir_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        return dir_moves

    def move_piece(self, move):
        curr_pos = self.board[self.user_input[:2]]
        move_pos = self.board[self.user_input[2:]]
        if self.valid_move(curr_pos, move_pos):
            if len(curr_pos) == 2 and len(move_pos) == 2:
                return

if __name__ == "__main__":
    ChessGameEngine(1)

