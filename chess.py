class Chess:
    def __init__(self):
        self.game_instructions()
        self.player_choice()

    #def game_engine(self):

    def game_instructions(self):
        with open('GameInstructions.txt', 'r') as f:
            for line in f:
                print(line)


    def main(self):
        player_choice()

    def player_choice(self):
        player_choice = input("What color do you want to be? (w/b) ")
        PLAYER_BLACK_BOARD = [["r", "n", "b", "q", "k", "b", "n", "r"],

        ["p","p","p","p","p","p","p","p"],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ["P","P","P","P","P","P","P","P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]]
        
        PLAYER_WHITE_BOARD = [["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p","p","p","p","p","p","p","p"],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.'],
        ["P","P","P","P","P","P","P","P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]]
        if player_choice.lower() == "w":
            return PLAYER_WHITE_BOARD
        elif player_choice.lower() == "b":
            return PLAYER_BLACK_BOARD
        else:
            print("Invalid choice, try again")
            new_board()

    def print_board(self, board):
        for i in range(len(board)):
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