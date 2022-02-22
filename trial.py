import chesspieces as ch
WQueen=ch.Queen((4,8), False, 'white')
occupied={WQueen.position,(4,5)}
attempt=(4,4)

print(WQueen.legal(attempt,occupied))