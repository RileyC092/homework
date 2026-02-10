
#  [https://www.youtube.com/watch?v=Mnb8MY5_pBc](https://www.youtube.com/watch?v=Mnb8MY5_pBc)


# Cost of a single normal Cookie: __$1.25__


# Cost of a single Big cookie: __$2.00__
   
# Cost to make a normal cookie: *$0.50*

# Cost to make a big cookie: *$0.75*

# - How to use ```.count()``` method for Strings in Python

bank = float(input("How much money does vendor have: "))


order = input("Enter cookies customer wants (b or c): ")

small = order.count("c")
big = order.count("b")

sold = int(small) + int(big)
profit = small*0.75 + big*1.5
savings = profit + bank

print(f"the amount of cookies sold is: {sold} the daily profit is {profit} and the cumulative earnings is now {savings} ")



