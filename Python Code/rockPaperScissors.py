# this will be the rock paper scissors game!
from random import randint

player = input("rock(r) , paper(p) , scissors(s) ")

# the computer will choose now (create a variable)
choose = randint(1,3)

if choose == 1:
    computer = 'r'
elif choose == 2:
    computer = 'p'
else:
    computer = 's'

# now lets see who won!
if player == computer:
    print("Draw!!!")
elif player == 'r' and computer == 's':
    print("Player Wins!!!")
elif player == 'p' and computer =='r':
    print("Player Wins!!!")
elif player == 's' and computer =='p':
    print("Player Wins!!!")
else:
    print("Computer Wins!!!")