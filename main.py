class Game:
    def __init__(self):
       self.gameState = ["_"] * 9
    
    def displayGame(self):
        matrix = [self.gameState[i:i+3] for i in range(0, len(self.gameState),3)]
        for row in matrix:
            print(*row,end="\n\n")

g=Game()
g.displayGame()
