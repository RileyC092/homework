
# ## Rock Paper Scissors vs AI

# __YouTube Link:__ [https://www.youtube.com/watch?v=Us1kfe2zMNA](https://www.youtube.com/watch?v=Us1kfe2zMNA)

# In this lesson, we are learning how to create a Rock Paper Scissors game against an AI.

# Create a program that takes one inputs of Rock, Paper, or Scissors to simulate a 1v1 rock paper scissors game between a human player vs AI.

# ### Problem Overview

# Take a single input of rock, paper, or scissors then compare it to the randomly chosen option for the CPU.

# - How to use membership operators with the ```set``` datatype
# - How to use a while loop to validate user inputs
# - How to use ```choice()``` function from the random module
from random import randrange
from random import choice 

uchoice = input("Enter 'rock' 'paper' or 'scissors': ")
if uchoice == "rock" : 
    (uchoice) = 1
elif uchoice == "paper":
    (uchoice) = 2
elif uchoice == "scissors": 
    (uchoice) = 3 
else: 
    print("???")

ai = int(randrange(1,4))

if ai == 1 : 
    (ai) = "rock"
    print(f"the ai chose {ai}")
elif ai == 2:
    (ai) = "paper"
    print(f"the ai chose {ai}")
elif ai == 3: 
    (ai) = "scissors" 
    print(f"the ai chose {ai}")

if ai == "rock" : 
    (ai) = 1
elif ai == "paper":
    (ai) = 2
elif ai == "scissors": 
    (ai) = 3 

if ai == uchoice:
    print("draw")

elif (uchoice == 1 and ai == 3):  
    print("you won")
elif (uchoice == 2 and ai == 1):  
    print("you won")
elif (uchoice == 3 and ai == 2):  
    print("you won")
else:
    print("You lose")









