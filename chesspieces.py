class Chess_Pieces:
    def __init__(self, position, alive, colour):
        self.position=position
        self.alive=alive
        self.colour=colour

class Pawn(Chess_Pieces):
    def __init__(self, position, alive, colour, history):
        self.position=position
        self.alive=alive
        self.colour=colour
        self.history=history
        
