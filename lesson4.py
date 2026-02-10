    
from math import ceil

fence1 = input("Enter length of first side of fence: ")
fence1 = len(fence1)

fence2 = input("Enter length of second side of fence: ")
fence2 = len(fence2)

fence3 = input("Enter length of third side of fence: ")
fence3 = len(fence3)

needcan = fence1 + fence2 + fence3

boxes = ceil(needcan/12) 
cost = boxes * 14.95
remainder = (boxes*12) - needcan

print(f"the amount of cans needed is {needcan}, the amount of cans left over is {remainder} and lastly the cost is {cost}")




