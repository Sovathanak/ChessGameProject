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
        print("Player " + str(self.player)+"'s turn, what do you want to do? ")
        self.user_input = input("Enter here: ")
        if (self.user_input.lower() == "quit"):
            self.game_over = True
        elif (self.user_input.lower() == "check"):
            check_piece_pos = str(input("Enter the piece's position on the current board state to check for valid moves: "))
            print(self.valid_move(check_piece_pos))
            self.player_choice()
        else:
            self.move_piece(self.user_input)
            self.swap_turn()


    def swap_turn(self):
        if self.player == 1: self.player += 1
        else: self.player -= 1

    def convert(self, position):
        num_lst = [7,6,5,4,3,2,1,0]
        letter_lst = ["a","b","c","d","e","f","g","h"]
        real_row = num_lst[int(position[1]) - 1]
        real_col = int(ord(position[0]) - 97)
        return real_row, real_col 


    def valid_move(self, str_current_pos):
        if len(str_current_pos) > 2:
            msg = "\nInvalid position\n"
            return msg
        valid_moves = []
        pos = self.convert(str_current_pos)
        piece_move = self.piece_dir_moves(self.board[p_row][p_col])
        for i in range(len(piece_move)):
            if self.board[pos[0]][pos[1]].lower() == "k" or self.board[pos[0]][pos[1]].lower() == "n":
                new_col = pos[1] + piece_move[i][1]
                new_row = pos[0] + piece_move[i][0]
                if new_col < 0 and new_row < 0:
                    pass
                elif new_col <= 7 and new_row <= 7 :
                    white_new = self.board[new_row][new_col].isupper()
                    black_curr = self.board[p_row][p_col].islower()
                    diff_color_pieces = (white_new and black_curr) or (not white_new and not black_curr)
                    if diff_color_pieces or self.board[new_row][new_col] == ".":
                        move_col = letter_lst[(new_col)]
                        move_row = str(num_lst[(new_row)] + 1)
            elif self.board[pos[0]][pos[1]] == "p" or self.board[pos[0]][pos[1]] == "P":
                if self.board[pos[0]][pos[1]].islower():
                    pass
                else:
                    pass
            elif self.board[pos[0]][pos[1]].lower() == "q" or self.board[pos[0]][pos[1]].lower() == "r" or self.board[pos[0]][pos[1]].lower() == "b":
                pass
            valid_moves.append(move_col+move_row)
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
            dir_moves = [(1, 0), (2, 0), (1, 1), (1, -1)]
        elif piece == "P": # white pawn
            dir_moves = [(-1, 0), (-2, 0), (-1, 1), (-1, -1)]
        elif piece.lower() == "n":
            dir_moves = [(2, 1),(2, -1),(-1, 2),(1, 2),(-2, 1),(-2, -1),(-1, -2),(1, -2)] 
        elif piece.lower() == "b":
            dir_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        elif piece.lower() == "r":
            dir_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        return dir_moves


    def move_piece(self, move):
            curr = self.board[self.user_input[:2]]
            move_pos = self.board[self.user_input[2:]]
            if len(curr_pos) == 2 and len(move_pos) == 2:
                return
