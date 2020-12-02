import Rational

engineProgramLoop = True
while engineProgramLoop == True:
    Rational.Rational().meetUser()

    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))

    num3 = int(input("Enter number 3: "))
    num4 = int(input("Enter number 4: "))

    operation = input("Operation --> ")

    fraction1 = Rational.Rational(num1, num2)
    fraction2 = Rational.Rational(num3, num4)

    print(f"{fraction1} {operation} {fraction1} ")
    if (num2 == 0) or (num4 == 0):
        print(f"Division by zero denominator:{num2}")
        engineExitLoop = True
        while engineExitLoop == True:
            exitUser = int(input("\nIf you want exit program enter 0\nIf you want retry enter 1\n--> "))
            if (exitUser == 1):
                engineExitLoop = False
            elif (exitUser == 0):
                engineExitLoop = False
                engineProgramLoop = False
            else:
                print("Retry enter, please")
    else:
        fractionDecimal = Rational.Rational.calculate(fraction1, operation, fraction2)
        userChoose = int(input("Enter 1 if you need decimal fraction\nEnter 2 if you need standart fraction"
                               "\nEnter 3 if you need decimal fraction and standart fraction\nYour number: "))

        gcd1 = fraction1.findGCD()
        gcd2 = fraction2.findGCD()

        fractionStandart = Rational.Rational.fractionStandart(num1, num2, num3, num4, gcd1, gcd2)
        if userChoose == 1:
            print(f"Your choose {userChoose}\n")
            print(f"Decimal fraction :{fractionDecimal}")
        elif userChoose == 2:
            print(f"\nYour choose {userChoose}\n")
            print(f"Standart fraction :{fractionStandart}")
        else:
            print(f"Your choose {userChoose}\n")
            print(f"Standart fraction :{fractionStandart}")
            print(f"Decimal fraction :{fractionDecimal}")



        engineExitLoop = True
        while engineExitLoop == True:
            exitUser = int(input("\nIf you want exit program enter 0\nIf you want retry enter 1\n--> "))
            if (exitUser == 1):
                engineExitLoop = False
            elif (exitUser == 0):
                engineExitLoop = False
                engineProgramLoop = False
            else:
                print("Retry enter, please")
