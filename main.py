from Game import *
import sys


def startGame():
    game = Game()
    game.display()

    def play():
        move =int(input("What's your move : "))
        game.updateState(move)
        game.display()

    def endGame():
        print("Game Over \n","Winner : ", game.winner)
        restart = input("Would you like to play again? y/n")
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
