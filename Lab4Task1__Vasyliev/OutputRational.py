import Rational

engineProgramLoop = True
while engineProgramLoop == True:
    Rational.Rational().meetUser()

    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    if(num2 == 0):
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
        userChoose = int(input("Enter 1 if you need decimal fraction\nEnter 2 if you need standart fraction"
                            "\nEnter 3 if you need decimal fraction and standart fraction\nYour number: "))

        div = Rational.Rational(num1, num2)

        divisor = div.findGCD()
        fractionStandart = div.fractionStandart(divisor)
        fractionDecimal = div.fractionDecimal(divisor)

        div.output(fractionStandart, fractionDecimal, userChoose)

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
