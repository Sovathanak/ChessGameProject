from os import system, name

class Chess:
    def __init__(self):
        self.player = None
        self.playerchoice = None
        self.game_over = False
        self.board = [["R", "N", "B", "Q", "K", "B", "N", "R"],
        ["P","P","P","P","P","P","P","P"],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ["p","p","p","p","p","p","p","p"],
        ["r", "n", "b", "q", "k", "b", "n", "r"]]
        self.game_loop()


    def game_loop(self):
        self.player_setup()
        self.print_board(self.board)
        while self.game_over != True:
            print("========================================")
            self.player_choice()
            self.print_board(self.board)
        print("==============Game Aborted==============")


    def game_restart(self):
        print("=============Game restarted=============\n")
        self.__init__()


    def player_choice(self):
        print("Player " + str(self.player)+"'s turn, what do you want to do? ")
        self.playerchoice = input("Enter here: ")
        if (self.playerchoice.lower() == "quit"):
            self.game_over = True
        elif (self.playerchoice.lower() == "restart"):
            self.game_restart()
        elif (self.playerchoice.lower() == "check"):
            check_piece_pos = input("Enter the piece's position on the current board state to check for valid moves: ")
            print(self.valid_move(check_piece_pos))
            self.player_choice()
        else:
            curr_pos, move_pos = (self.board[self.playerchoice[:2]][0], self.board[self.playerchoice[:2]][1]), (self.board[self.playerchoice[2:]][0], self.board[self.playerchoice[2:]][1])
            if len(curr_pos) == 2 and len(move_pos) == 2:
                return


    def swap_turn(self):
        if self.player == 1:
            self.player += 1
        else:
            self.player -= 1


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
        moves = []
        p_row = curr_pos[1]
        p_col = curr_pos[0]
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if 
        return moves


    def print_board(self, board):
        for i in range(len(board)- 1, -1, -1):
            row = ""
            num = 0
            for piece in board[i]:
                if num < 8:
                    num +=1
                    row += piece + "|"
                else:
                    num += 1
                    row += piece + "\n"
            print(i+1, "|"+row)   # prints out the row labels and the board next to it
        print("""   a b c d e f g h""")  # prints the columns of the board



    def piece_dir_moves(self, piece):
        """
        This funciton returns the directions of which the piece can move on the board, mainly applies to all the pieces except for 
        the king piece (k and K), the knight (N and n) and the pawn (P and p)
        """
        dir_moves = []
        if piece.lower() == "k" or piece.lower() == "q":
            moves = [(1, 1),(1, 0),(0, 1),(1, -1),(-1, 1),(-1, -1),(0, -1),(-1, 0)] 
        elif piece == "p": # black pawn
            moves = [(1, 0), (2, 0)]
        elif piece == "P": # white pawn
            moves = [(-1, 0), (-2, 0)]
        elif piece.lower() == "n":
            moves = [(2, 1),(2, -1),(-1, 2),(1, 2),(-2, 1),(-2, -1),(-1, -2),(1, -2)] 
        elif piece.lower() == "b":
            moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        elif piece.lower() == "r":
            moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        return moves


game = Chess()
