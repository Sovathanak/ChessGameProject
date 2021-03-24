class ChessGameSetup:
    def __init__(self):
        self.player_setup()

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
