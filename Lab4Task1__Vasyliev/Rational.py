class Rational(object):
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def meetUser(self):
        print("This program help you create fraction standart and decimal from your 2 numbers\n")
        return 1

    def findGCD(self):
        a = self.numerator
        b = self.denominator
        while (a != 0) and (b != 0):
            if (a > b):
                a = a % b
            else:
                b = b % a
        if a > b:
            gcd = a
            return gcd
        else:
            gcd = b
            return gcd

    def fractionStandart(self, divisor=1):
        a = self.numerator
        b = self.denominator
        a = a / divisor
        b = b / divisor
        fraction = f"{a}/{b}"
        return fraction

    def fractionDecimal(self, divisor=1):
        a = self.numerator
        b = self.denominator
        a = a / divisor
        b = b / divisor
        fraction = a / b
        return fraction

    def output(self, fractionStandart="1/1", fractionDecimal=0.1, userChoose=3):
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
