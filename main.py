from Game import *
import sys


def startGame():
    game = Game()
    game.display()

    def play():
        while True :
            try : 
                move =int(input("What's your move : "))
                if move > 8:
                    raise
                elif game.state[move] != "*":
                    raise
                else:break
            except: 
                print("Bad input")
        game.updateState(move)
        game.display()

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
