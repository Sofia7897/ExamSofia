"""
PowerOfTen
"""

number = input ("Please enter a max 3 digit number: ")
if int(number) < 0:
    print("Number cannot be negative")
elif int(number) // 1000 != 0:
    print("Number has more than 3 digits")
else:
    if int(number)//100 > 0:
        hunderter = int(number)// 100
        zehner = (int(number) - hunderter*100)//10
        einer = int(number) - hunderter*100 - zehner*10

        print(f"{int(number)} = {hunderter} * 100 + {zehner} * 10 + {einer} * 1")

    elif int(number)//10 > 0:
        zehner = int(number) // 10
        einer = int(number) - zehner * 10

        print(f"{int(number)} = {zehner} * 10 + {einer} * 1")

    else:
        print(f"{int(number)} = {int(number)} * 1")






"""
Cash Box
"""



to_pay = input ("What amount is to be paid?")
if int(to_pay) == 0:
    print("There is nothing to pay! Great!")
elif int(to_pay) < 0:
    print("Negative payment is invalid.")
else:
    received = input ("Please write down how much you are paying:")
    if int(received) < 0:
        print("Negative received amount is invalid.")
    elif int(received) < int(to_pay):
        print("You did not pay enough.")
    else:
        change = int(received) - int(to_pay)
        print("Your change is: " + str(change))


