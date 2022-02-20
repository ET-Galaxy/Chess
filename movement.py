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

class King(Chess_Pieces):
    def __init__(self, position, underattack, colour):
        self.position=position
        self.colour=colour
        self.underattack=underattack


class Queen(Chess_Pieces):
    def __init__(self, position, alive, colour):
        self.position=position
        self.alive=alive
        self.colour=colour

#initial positions
WKing=King([5,1], False, 'white')
BKing=King([5,8], False, 'black')
WQueen=Queen([4,1], True, 'white')
BQueen=Queen([4,1], True, 'black')

#Make a move!
n=0
move=input('Input your move in chess notation: ')
name={'K': King, 'Q': Queen}
numbers={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
while move!='STOP':
    n=n+1
    if n%2==1:
        for i in {WKing, WQueen}:
            if type(i)==name.get(move[0]):
                i.position=[numbers[move[-2]],int(move[-1])]
    else:
        for i in {BKing, BQueen}:
            if type(i)==name.get(move[0]):
                i.position=[numbers[move[-2]],int(move[-1])]
    move=input('Input your move in chess notation: ')
print(WKing.position)
print(BKing.position)