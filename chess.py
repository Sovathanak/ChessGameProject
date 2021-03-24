import chess_engine
import chess_setup

class Chess:
    def __init__(self):
        self.player_setup = chess_setup.ChessGameSetup()
        self.player = self.player_setup.player
        chess_engine.ChessGameEngine(self.player) 

game = Chess()
