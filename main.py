print("The tic tac toe program is running")
gameState = ["_"] * 9
gameState[3]="X"

matrix = [gameState[i:i+3] for i in range(0, len(gameState),3)]

for row in matrix:
    print(*row,end="\n\n")
