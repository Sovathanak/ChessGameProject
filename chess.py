import chess_engine
import chess_setup

class Chess:
    def __init__(self):
        self.game_setup = chess_setup.ChessGameSetup()
        self.player = self.game_setup.player
    
    def play_game(self):
        chess_engine.ChessGameEngine(self.player)
    
    
if __name__ == "__main__":
    x = Chess()
    x.play_game()

