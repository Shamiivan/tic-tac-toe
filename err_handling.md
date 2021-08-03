#1 Program cannot update state.
    Exp: With a given input as index (ex 1,2,3) the program is suposed to change the index in the gameState to make it X or O depending on who is playing. 
    The program does not do it. 

Hyp: TypeError -> move should be int in updateState(move)
Test : the value of move right before update state is called != int
        TEST positif --> type of move is str




#2 Game does alternate between X and 0
    
Hyp: Implemantation error --> The alternate function is not doing it's job or it is not being called
Test: Value of game.player does not change 
    Positive: value of does not change 

#3 Program allows to change slots that have been player already 
Hyp : Simple mistake -->  Te
SOLVED


#4 Program does not let Human play after the first play.
    After initial play, all the input that goes into the game are genarate by the computer. Does not get another turn 
Hyp: Simple typo --> The alternate function does not what it's supposed to 
Test: Printing the value of game.turn after each input gives "C"
