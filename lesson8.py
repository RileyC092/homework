
wl = input("Enter 6 game win or loss record (W or L)(E.g. WWWLLW): ")

wins = wl.count("W")
losses = wl.count("L")

if 5<= wins <=6:
    print("You are in group 1")
elif 3<= wins <= 4: 
    print("you are in group 2")  
elif 1<= wins <= 2: 
    print("you are in group 3")
else: 
    print("You are eliminated lol")



