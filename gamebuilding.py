secret =  2
numberofguess = 0
guesslimit = 3
while numberofguess < guesslimit:
    guess = int(input("guess: "))
    numberofguess += 1
    if guess == secret:
        print("you are right")
        break
else:
    print("wrong")

