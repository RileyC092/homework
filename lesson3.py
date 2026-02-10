# Lesson 3

# Given a positive integer input representing the number of equal size tiles, we are to determine the following:
# - Construct the square with the largest area possible
# - Output the side length of the square

#  input 
# int converts the string to an integer now its like a number
tiles = int(input("Enter amount of tiles"))

# proccess
if tiles % 2 == 0: 
    side = (tiles / 2)
    area = side**2

else: 
    tiles = tiles - 1 
    side = tiles / 2 
    area = side**2
# output 
print(f"The largest area possible is {area} and the each side length is {side}")
