import random
class Game:
    def __init__(self):
        self.state = ["*"] * 9
        self.counter = 0
        self.winner = "none"
        self.isOver = False
        self.player = "X"
        self.turn = "H"
 
    def display(self):
        matrix = [self.state[i:i+3] for i in range(0,9,3)]
        print("==============================================================")
        for row in matrix:
            print(*row,end="\n\n")
    
    def checkWin(self):
        lib = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for arr in lib:
            similar = all(self.state[index]== self.state[arr[0]] for index in arr)
        
            if similar and self.state[arr[0]] != "*": 
                self.winner = self.state[arr[0]]
                self.isOver = True 
                
        def checkDraw():
            if self.counter >= 8 :
                self.isOver = True

        checkDraw()
    
    def alternate(self):
        if self.turn == "H":
            self.turn = "C"
        elif self.turn == "C" :
            self.turn = "H"

        if self.player == "X":
            self.player = "O"
        elif self.player == "O":
            self.player = "X"

    def updateState(self,index):
        self.checkWin()
        self.state[index]  = self.player
        self.counter  = self.counter + 1
        self.checkWin()

    def cp(self):
        return random.randint(0,8) 
    
    def validate(self, move):
       if move > 8 or self.state[move] != "*" :
            return False
       else : return True

print("")