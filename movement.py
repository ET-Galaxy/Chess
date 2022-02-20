import chesspieces as ch

#initial positions
WKing=ch.King([5,1], False, 'white')
BKing=ch.King([5,8], False, 'black')
WQueen=ch.Queen([4,1], True, 'white')
BQueen=ch.Queen([4,8], True, 'black')
WPawn1=ch.Pawn([1,2], True, 'white')
WPawn2=ch.Pawn([2,2], True, 'white')
WPawn3=ch.Pawn([3,2], True, 'white')
WPawn4=ch.Pawn([4,2], True, 'white')
WPawn5=ch.Pawn([5,2], True, 'white')
WPawn6=ch.Pawn([6,2], True, 'white')
WPawn7=ch.Pawn([7,2], True, 'white')
WPawn8=ch.Pawn([8,2], True, 'white')
BPawn1=ch.Pawn([1,7], True, 'black')
BPawn2=ch.Pawn([2,7], True, 'black')
BPawn3=ch.Pawn([3,7], True, 'black')
BPawn4=ch.Pawn([4,7], True, 'black')
BPawn5=ch.Pawn([5,7], True, 'black')
BPawn6=ch.Pawn([6,7], True, 'black')
BPawn7=ch.Pawn([7,7], True, 'black')
BPawn8=ch.Pawn([8,7], True, 'black')

#Make a move!
n=0
move=input('Input your move in chess notation: ')
name={'K': ch.King, 'Q': ch.Queen, 'P': ch.Pawn}
numbers={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
while move!='STOP':
    n=n+1
    if n%2==1:
        for i in {WKing, WQueen, WPawn1, WPawn2, WPawn3, WPawn4, WPawn5, WPawn6, WPawn7, WPawn8}:
            if type(i)==name.get(move[0]):
                attempt=[numbers[move[-2]],int(move[-1])]
                if i.check(attempt)==True:
                    i.position=attempt
                else:
                    print('Invalid move')
                break
    else:
        for i in {BKing, BQueen, BPawn1, BPawn2, BPawn3, BPawn4, BPawn5, BPawn6, BPawn7, BPawn8}:
            if type(i)==name.get(move[0]):
                i.position=[numbers[move[-2]],int(move[-1])]
    move=input('Input your move in chess notation: ')
print(WKing.position)
print(BKing.position)