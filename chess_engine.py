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



    def game_restart(self):
        print("\n=============Game restarted=============\n")
        self.__init__()

    def print_board(self, board):
        k = 9
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
            k -= 1
            print(k, "|"+row)   # prints out the row labels and the board next to it
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
        elif (self.user_input.lower() == "restart"):
            self.game_restart()
        elif (self.user_input.lower() == "check"):
            check_piece_pos = str(input("Enter the piece's position on the current board state to check for valid moves: "))
            print(self.valid_move(check_piece_pos))
            self.player_choice()
        else:
            curr_pos = (self.board[self.user_input[:2]][0], self.board[self.user_input[:2]][1])
            move_pos = (self.board[self.user_input[2:]][0], self.board[self.user_input[2:]][1])
            if len(curr_pos) == 2 and len(move_pos) == 2:
                return


    def swap_turn(self):
        if self.player == 1: self.player += 1
        else: self.player -= 1


    def valid_move(self, curr_pos):
        if len(curr_pos) > 2:
            msg = "\nInvalid position\n"
            return msg
        valid_moves = []
        num_lst = [7,6,5,4,3,2,1,0]
        letter_lst = ["a","b","c","d","e","f","g","h"]
        p_row = num_lst[int(curr_pos[1]) - 1]
        p_col = int(ord(curr_pos[0]) - 97)
        piece_move = self.piece_dir_moves(self.board[p_row][p_col])
        for i in range(len(piece_move)):
            new_col = p_col + piece_move[i][1]
            new_row = p_row + piece_move[i][0]
            if new_col < 0 and new_row < 0:
                pass
            elif new_col <= 7 and new_row <= 7 :
                # white_new = self.board[new_row][new_col].isupper()
                # white_curr = self.board[p_row][p_col].isupper()
                # black_new = self.board[new_row][new_col].islower()
                # black_curr = self.board[p_row][p_col].islower()
                # if white_curr and black_new or black_curr and white_new:
                if self.board[new_row][new_col] == ".":
                    move_col = letter_lst[(new_col)]
                    move_row = str(num_lst[(new_row)] + 1)
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
            dir_moves = [(1, 0), (2, 0)]
        elif piece == "P": # white pawn
            dir_moves = [(-1, 0), (-2, 0)]
        elif piece.lower() == "n":
            dir_moves = [(2, 1),(2, -1),(-1, 2),(1, 2),(-2, 1),(-2, -1),(-1, -2),(1, -2)] 
        elif piece.lower() == "b":
            dir_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        elif piece.lower() == "r":
            dir_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        return dir_moves
