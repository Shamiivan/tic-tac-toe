class Game:
    def __init__(self):
        self.state = ["*"] * 9
        self.counter = 0
        self.winner = "none"
        self.isOver = False
        self.player = "X"
 
    def display(self):
        matrix = [self.state[i:i+3] for i in range(0,9,3)]
        print("==============================================================")
        for row in matrix:
            print(*row,end="\n\n")
    
    def checkWin(self):
        lib = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for arr in lib:
            isWin = all(self.state.index == self.state.arr[0] for index in arr)
        
            if isWin: 
                self.winner = self.state.arr[0]
                self.end()
    def checkDraw(self):
        if self.counter == 8 :
            self.end()
    
    def end(self):
        print("game is over")
        self.isOver = False
    def updateState(self,index):
        self.state[index]  = self.player
        if self.player == "X" : 
            self.player ="O"
        else: self.player ="X"

