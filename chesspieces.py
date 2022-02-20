attempt=[1,2]
class Chess_Pieces:
    def __init__(self, position, alive, colour):
        self.position=position
        self.alive=alive
        self.colour=colour

class Pawn(Chess_Pieces):
    def __init__(self, position, alive, colour):
        self.position=position
        self.alive=alive
        self.colour=colour


class King(Chess_Pieces):
    def __init__(self, position, underattack, colour):
        self.position=position
        self.colour=colour
        self.underattack=underattack
    def check(self, attempt):
        return ((self.position[0]-attempt[0])^2+(self.position[1]-attempt[1])^2<2)

class Queen(Chess_Pieces):
    def __init__(self, position, alive, colour):
        self.position=position
        self.alive=alive
        self.colour=colour
