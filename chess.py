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
        self.clear_screen()
        self.print_board(self.board)
        while self.game_over != True:
            self.player_choice()
        print("Game Finished")


    def player_choice(self):
        print("Player " + str(self.player)+" turn, what do you want to do? ")
        self.playerchoice = input("Enter here: ")
        if len(self.playerchoice) > 4:
            print("Invalid input")
            self.player_choice()
        curr_pos, move_pos = self.playerchoice[:2], self.playerchoice[2:]
        if (self.playerchoice.lower() == "quit"):
            self.game_over = True
        
        

    def clear_screen(self):
        system("cls")


    def swap_turn(self):
        if self.player == 1:
            self.player += 1
        else:
            self.player -= 1

    def player_setup(self):
        player1_choice = input("Player1: What color do you want to be? (w/b) ")
        if player1_choice.lower() == "w":
            self.player = 1
        elif player1_choice.lower() == "b":
            self.player = 2
        else:
            print("Invalid choice, try again")
            self.player_setup()


    def valid_move(self, curr_pos, move_pos):
        return


    def print_board(self, board):
        for i in range(len(board)- 1, -1, -1):
            row = ""
            num = 0
            for piece in board[i]:
                if num < 8:
                    num +=1
                    row += piece + " "
                else:
                    num += 1
                    row += piece + "\n"
            print(i+1, row)   # prints out the row labels and the board next to it
        print("""  a b c d e f g h""")  # prints the columns of the board


game = Chess()