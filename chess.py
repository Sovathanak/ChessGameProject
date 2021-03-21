from os import system, name

class Chess:
    def __init__(self):
        self.player = None
        self.playerchoice = None
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


    def game_loop(self):
        self.player_setup()
        self.print_board(self.board)
        while self.game_over != True:
            print("\n========================================\n")
            self.player_choice()
            if self.game_over != True:
                self.print_board(self.board)
        print("\n==============Game Aborted==============\n")


    def game_restart(self):
        print("\n=============Game restarted=============\n")
        self.__init__()


    def player_choice(self):
        print("Player " + str(self.player)+"'s turn, what do you want to do? ")
        self.playerchoice = input("Enter here: ")
        if (self.playerchoice.lower() == "quit"):
            self.game_over = True
        elif (self.playerchoice.lower() == "restart"):
            self.game_restart()
        elif (self.playerchoice.lower() == "check"):
            check_piece_pos = str(input("Enter the piece's position on the current board state to check for valid moves: "))
            print(self.valid_move(check_piece_pos))
            self.player_choice()
        else:
            curr_pos, move_pos = (self.board[self.playerchoice[:2]][0], self.board[self.playerchoice[:2]][1]), (self.board[self.playerchoice[2:]][0], self.board[self.playerchoice[2:]][1])
            if len(curr_pos) == 2 and len(move_pos) == 2:
                return


    def swap_turn(self):
        if self.player == 1: self.player += 1
        else: self.player -= 1


    def player_setup(self):
        player1_choice = input("Question for Player 1: What color do you want to be? (w/b) ")
        if player1_choice.lower() == "w":
            self.player = 1
            print("Player " + str(self.player) +" is white")
            print("Player " + str(self.player + 1) +" is black")
            print("========================================")
        elif player1_choice.lower() == "b":
            self.player = 2
            print("Player " + str(self.player - 1) +" is black")
            print("Player " + str(self.player) +" is white")
            print("========================================")
        else: 
            print("Invalid choice, try again")
            self.player_setup()

    def valid_move(self, curr_pos):
        if len(curr_pos) > 2:
            msg = "\nInvalid position\n"
            return msg
        valid_moves = []
        num_lst = [8,7,6,5,4,3,2,1]
        letter_lst = ["h","g","f","e","d","c","b","a"]
        p_row = num_lst[curr_pos[1]]
        p_col = (int(ord(curr_pos[0]) - 97) + 7) % 8
        piece_move = self.piece_dir_moves(self.board[p_row][p_col])
        for i in range(len(piece_move)):
            if p_col + piece_move[i][1] > 7 and p_row + piece_move[i][0] > 7:
                pass
            elif p_col + piece_move[i][1] <= 7 and p_row + piece_move[i][0] <= 7 :
                move_col = letter_lst[(p_col + piece_move[i][1]) % len(num_lst)])
                move_row = str(num_lst[(p_row + piece_move[i][0]) % len(num_lst)])
                valid_moves.append(move_row+move_col)
        print("\nValid moves for the piece: ")
        return valid_moves


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



    def piece_dir_moves(self, piece):
        """
        This funciton returns the directions of which the piece can move on the board, mainly applies to all the pieces except for 
        the king piece (k and K), the knight (N and n) and the pawn (P and p)
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


game = Chess()
