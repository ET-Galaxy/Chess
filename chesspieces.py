import numpy as np
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

class Bishop(Chess_Pieces):
    def __init__(self, position, alive, colour):
        self.position=position
        self.alive=alive
        self.colour=colour
    def legal(self, attempt, occupied):
        #diagonal
        if abs(self.position[1]-attempt[1])==abs(self.position[0]-attempt[0]):
            s=int((self.position[1]-attempt[1])/(self.position[0]-attempt[0]))
            passedsquares=[self.position]
            if attempt[0]>self.position[0]:
                while passedsquares[-1]!=attempt:
                    passedsquares.append((passedsquares[-1][0]+1,passedsquares[-1][1]+s))
            else:
                while passedsquares[-1]!=attempt:
                    passedsquares.append((passedsquares[-1][0]-1,passedsquares[-1][1]-s))
            passedsquares.remove(self.position)
            passedsquares.remove(attempt)
            passedsquares=set(passedsquares)
            return(occupied&passedsquares==set())
        else:
            return(False)

class Rook(Chess_Pieces):
    def __init__(self, position, alive, colour):
        self.position=position
        self.alive=alive
        self.colour=colour
    def legal(self, attempt, occupied): 
        if (self.position[1]-attempt[1])*(self.position[0]-attempt[0])==0:
            #horizontal
            passedsquares=[self.position]
            if attempt[0]!=self.position[0]:
                s=np.sign(attempt[0]-self.position[0])
                while passedsquares[-1]!=attempt:
                    passedsquares.append((passedsquares[-1][0]+s,passedsquares[-1][1]))
            #vertical
            else:
                s=np.sign(attempt[1]-self.position[1])
                while passedsquares[-1]!=attempt:
                    passedsquares.append((passedsquares[-1][0],passedsquares[-1][1]+s))
            passedsquares.remove(self.position)
            passedsquares.remove(attempt)
            passedsquares=set(passedsquares)
            return(occupied&passedsquares==set())
        else:
            return(False)

class Queen(Bishop, Rook):
    def __init__(self, position, alive, colour):
        self.position=position
        self.alive=alive
        self.colour=colour
    def legal(self, attempt, occupied):
        return(Bishop.legal(self, attempt, occupied) or Rook.legal(self, attempt, occupied))

class King(Chess_Pieces):
    def __init__(self, position, underattack, colour, moved):
        self.position=position
        self.colour=colour
        self.underattack=underattack
        self.moved=moved
    def safe(self, guarded):
        return(self.position not in guarded)
    def legal(self, attempt, guarded):
        a=(self.position[0]-attempt[0])**2+(self.position[1]-attempt[1])**2
        return (a<=2)
