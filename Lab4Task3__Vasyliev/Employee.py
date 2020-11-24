import datetime


class Employee(object):
    def __init__(self, surname="Surname", yearBirth=1970, monthBirth=1, dayBirth=1):
        self.surname = surname
        self.yearBirth = yearBirth
        self.monthBirth = monthBirth
        self.dayBirth = dayBirth

    def meetUser(self):
        print("\nThis program help you find age your employees and find days when their turns 50 years")
        return 1

    def getAgeEmployee(self):
        surname = self.surname
        yearBirth = self.yearBirth
        monthBirth = self.monthBirth
        dayBirth = self.dayBirth
        birthDate = datetime.date(yearBirth, monthBirth, dayBirth)
        today = datetime.date.today()
        ageEmployee = (today - birthDate) // datetime.timedelta(days=365.2425)
        return (f"\nEmployee surname: {surname}, he's age: {ageEmployee}")

    def getDayTo50years(self):
        surname = self.surname
        yearBirth = self.yearBirth
        monthBirth = self.monthBirth
        dayBirth = self.dayBirth
        birthDate = datetime.date(yearBirth, monthBirth, dayBirth)
        today = datetime.date.today()
        ageEmployee = (today - birthDate) // datetime.timedelta(days=365.2425)

        remainder = 50 - ageEmployee

        if (remainder < 0):
            # find years 50 birthday date
            yearDate50 = datetime.date(birthDate.year + 50, birthDate.month, birthDate.day)
            return (f"\nThis is employee {surname} over 50 years\nHe is {ageEmployee} years old\n"
                    f"This is date he turned 50: {yearDate50}")
        else:
            # find days to 50 years
            remainder = str(remainder * datetime.timedelta(days=365.2425))[:-10]
            # find years 50 birthday date
            yearDate50 = datetime.date(birthDate.year + 50, birthDate.month, birthDate.day)
            return (f"\nThis is employee \'{surname}\', {remainder} to 50 years.\n"
                    f"This is date he turns 50 years: {yearDate50}")
