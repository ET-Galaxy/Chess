import chesspieces as ch

#initial positions
WKing=ch.King((5,1), False, 'white', False)
BKing=ch.King((5,8), False, 'black', False)
WQueen=ch.Queen((4,1), 'white')
BQueen=ch.Queen((4,8), 'black')
WRook1=ch.Rook((1,1), 'white')
WRook2=ch.Rook((8,1), 'white')
BRook1=ch.Rook((1,8), 'black')
BRook2=ch.Rook((8,8), 'black')
WBishop1=ch.Bishop((3,1), True, 'white')
WBishop2=ch.Bishop((6,1), True, 'white')
BBishop1=ch.Bishop((3,8), True, 'black')
BBishop2=ch.Bishop((6,8), True, 'black')
#WPawn1=ch.Pawn([1,2], True, 'white')
#WPawn2=ch.Pawn([2,2], True, 'white')
#WPawn3=ch.Pawn([3,2], True, 'white')
#WPawn4=ch.Pawn([4,2], True, 'white')
#WPawn5=ch.Pawn([5,2], True, 'white')
#WPawn6=ch.Pawn([6,2], True, 'white')
#WPawn7=ch.Pawn([7,2], True, 'white')
#WPawn8=ch.Pawn([8,2], True, 'white')
#BPawn1=ch.Pawn([1,7], True, 'black')
#BPawn2=ch.Pawn([2,7], True, 'black')
#BPawn3=ch.Pawn([3,7], True, 'black')
#BPawn4=ch.Pawn([4,7], True, 'black')
#BPawn5=ch.Pawn([5,7], True, 'black')
#BPawn6=ch.Pawn([6,7], True, 'black')
#BPawn7=ch.Pawn([7,7], True, 'black')
#BPawn8=ch.Pawn([8,7], True, 'black')

#Make a move!
n=0
print('White, move 1')
move=input('Input your move in chess notation: ')
name={'K': ch.King, 'Q': ch.Queen, 'B': ch.Bishop, 'R': ch.Rook}
numbers={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
whitepieces={WKing, WQueen, WRook1, WRook2, WBishop1, WBishop2}
blackpieces={BKing, BQueen, BRook1, BRook2, BBishop1, BBishop2}
while move!='STOP':
    n=n+1
    occupied=[]
    #create list of occupied positions
    for i in whitepieces|blackpieces:
        occupied.append(i.position)
    occupied=set(occupied)
    s=0 #this checks if there is any change of position
    if n%2==1:
        for i in whitepieces:
            if type(i)==name.get(move[0]):
                attempt=(numbers[move[-2]],int(move[-1]))
                if i.legal(attempt, occupied):
                    s=1
                    i.position=attempt
                    blackpieces={j for j in blackpieces  if j.position != attempt}
                    break
        if s==0:
            print('Invalid move.')
            raise SystemExit
    else:
        for i in blackpieces:
            if type(i)==name.get(move[0]):
                attempt=(numbers[move[-2]],int(move[-1]))
                if i.legal(attempt, occupied):
                    s=1
                    i.position=attempt
                    whitepieces={j for j in whitepieces  if j.position != attempt}
                    break
        if s==0:
            print('Invalid move.')
            raise SystemExit
    print('Move' +str(n+1))
    move=input('Input your move in chess notation: ')

print(whitepieces, blackpieces)