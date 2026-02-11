

# In this lesson, we are learning how to solve the following problem:
    
# Create a program that simulates the ability check from the video game called "Baldur's Gate 3".

# An ability check in Baldur's Gate 3 is determined by first the Difficulty Class (DC). The DC is a number representing how hard a task is. When a player wants to do something uncertain, like jumping a gap or sneaking past guards, the Dungeon Master (DM) sets a DC. The player rolls a 20-sided die (D20) and adds modifiers from their character to the roll. If the total meets or beats the DC, the action succeeds. If not, it fails. The D20 introduces randomness, making even skilled characters sometimes fail in challenging situations, adding excitement to the game.

# The program should take in a single integer value representing the DC then randomly roll a value from 1 to 20 inclusively. Determine if the player was successful at succeeding the ability check.

# ### You will learn:

# - How to use ```randrange()``` function from the random module in Python

from random import randrange

diff = int(input("Enter a difficulty: "))

roll = randrange(1,21)
print(f"the player has rolled a {roll} on their D20")

if roll >= diff: 
    print("You win")
else: 
    print("You lose")