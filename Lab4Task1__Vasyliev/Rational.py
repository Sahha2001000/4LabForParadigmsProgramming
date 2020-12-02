class Rational(object):
    def __init__(self, numerator=1, denominator=1):
        self.__numerator = numerator
        self.__denominator = denominator

    def meetUser(self):
        print(
            "\nThis program help you calculute (*,/,-,+) and output fraction standart and decimal from your 2 numbers\n")
        return 1

    def numerator(self):
        return self.__numerator

    def denominator(self):
        return self.__denominator

    # numerator.setter
    def numerator(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Error: value is incorrect')
        self.__numerator = value

    # denominator.setter
    def denominator(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Error: value is incorrect')
        self.denominator = value

    def __str__(self):
        return '{}/{}'.format(self.__numerator, self.__denominator)

    #  +
    def __add__(self, other):
        return Rational(self.__numerator + other.__numerator, self.__denominator + other.__denominator)

    # *
    def __mul__(self, other):
        return Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    # -
    def __sub__(self, other):
        return Rational(self.__numerator - other.__numerator, self.__denominator - other.__denominator)

    # /
    def __truediv__(self, other):
        return Rational(self.__numerator / other.__numerator, self.__denominator / other.__denominator)

    def findGCD(self):
        a = self.__numerator
        b = self.__denominator
        if (b == 0):
            return print(f"Division by zero denominator:{b}")
        while (a != 0) and (b != 0):
            if (a > b):
                a = a % b
            else:
                b = b % a
        if a > b:
            gcd = a
        else:
            gcd = b
        return gcd

    def fractionStandart(self, a=1, b=1, c=1, d=1, divisor1=1, divisor2=1):
        a = a / divisor1
        b = b / divisor1
        ab = a / b
        d = d / divisor2
        c = d / divisor2
        dc = d / c
        return f"{ab} / {dc}"

    def calculate(*args):
        try:
            return eval(''.join(map(str, args)))
        except TypeError:
            return None


