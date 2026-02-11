

# __YouTube Link:__ [https://www.youtube.com/watch?v=JRy3CWtDFZ8](https://www.youtube.com/watch?v=JRy3CWtDFZ8)


# A telemarketer can be determined if all of the following statements are true:

# - The first digit is 8 or 9.
# - The second and third digits are the same.
# - The last digit is 8 or 9.

# Write a program to determine if the given last four digits would be a telemarketer or not.


# Given 4 inputs to represent the last four digits of a number, determine if the call is from a telemarketer

# - How to index a string to look at individual characters
# - How to use nested if statements

four = (input("Enter last 4 digits of number: "))
#8118
#9119
#8119
#9118
if (four[0]=="9" or four[0]=="8") and (four[3]=="9" or four[3]=="8") and (four[1]==four[2]): 
    print("it is a telemarketer")
else: 
    print("it is not a telemarketer")