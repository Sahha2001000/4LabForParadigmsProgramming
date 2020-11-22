import Rational

Rational.Rational().meetUser()

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
userChoose = int(input("Enter 1 if you need decimal fraction\nEnter 2 if you need standart fraction"
                       "\nEnter 3 if you need decimal fraction and standart fraction\nYour number: "))

div = Rational.Rational(num1,num2)

divisor = div.findGCD()
fractionStandart = div.fractionStandart(divisor)
fractionDecimal = div.fractionDecimal(divisor)

Rational.Rational().output(fractionStandart,fractionDecimal,userChoose)



