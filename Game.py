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
            similar = all(self.state[index]== self.state[arr[0]] for index in arr)
        
            if similar and self.state[arr[0]] != "*": 
                self.winner = self.state[arr[0]]
                self.isOver = True 
                
        def checkDraw():
            if self.counter >= 8 :
                self.isOver = True

        checkDraw()
    def updateState(self,index):
        self.checkWin()
        self.state[index]  = self.player
        self.counter  = self.counter + 1
        print(self.counter)

        if self.player == "X" : 
            self.player ="O"
        else: 
            self.player ="X"
            
        self.checkWin()    
