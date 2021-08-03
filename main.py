from Game import *
import sys


def startGame():
    while True: 
        try:
            multiplayer = bool(int(input("Multiplayer  mode? 1 for yes, 0 for no  ")))
            break   
        except:
            print("Bad input")


    game = Game()
    
    def getInput():
        if multiplayer == False and game.turn =="C":
            move = game.cp()
        else: 
            move =int(input("What's your move : ")) 
        
        return move


    def play():
        game.display()
        while True:
             move = getInput()
             try : 
                if game.validate(move) == False:
                    print(game.validate(move))
                    raise
                else: break
             except :
                print("Bad input", move, game.state,game.validate(move))

             game.updateState(move)
             game.alternate()
                
    def endGame():
        print("Game Over \n","Winner : ", game.winner)
        restart = input("Would you like to play again? y/n: ")
        if restart == "n":
            print("Twas a good game we should do it again")
            sys.exit()
        elif restart == "y":
            startGame()
         
    while True:         
            if game.isOver == False:
                play()
            elif game.isOver == True:
                endGame()
startGame()
