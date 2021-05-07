print("helllo")

has_high_income = True
has_good_credit = False
if has_high_income or has_good_credit:
    print("eligible for loan")

#comparison oprtr

temp = 30
if temp > 30:
    print("its a hot day")
else:
    print("its a cold day")

###example
name = input("type name")

if len(name) < 3:
    print("name must be atleast 3 char.")
elif  len(name) > 50:
    print("name must be within 50")
else:
    print("looks good")

#example
weight = int(input("weight ? "))
unit = input("Lbs or Kg ? ")
if unit.upper() == "L":
    print(weight/2.25)
elif unit.upper() == "K":
    print(weight*2.25)
else:
    print("wrong charater")
