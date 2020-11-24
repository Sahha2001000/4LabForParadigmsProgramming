import Employee


def inputDate():
    surname = input("\nEnter employee\'s surname\n-->")
    yearBirth = int(input("Enter employee\'s year birth\n-->"))
    monthBirth = int(input("Enter employee\'s month birth\n-->"))
    dayBirth = int(input("Enter employee\'s day birth\n-->"))
    return surname, yearBirth, monthBirth, dayBirth


engineProgramLoop = True
while engineProgramLoop == True:
    Employee.Employee().meetUser()

    size = int(input("Enter how many employees, please.\n--> "))
    employeesAgeList = list()
    employeesAgeTo50List = list()

    userChoose = int(
        input("\nIf you want get age employees enter  1\n"
              "If you find days when their turns 50 years or turned 50 years enter 2\n"
              "If you want get age employees and find days when their turns 50 years or turned 50 years enter 3\n--> "))

    i = 0
    if (userChoose == 1):
        while i < size:
            surname, yearBirth, monthBirth, dayBirth = inputDate()
            employee_n = Employee.Employee(surname, yearBirth, monthBirth, dayBirth)
            print(f"isinstance(employee_n, Employee.Employee -->){isinstance(employee_n, Employee.Employee)}")
            employeesAgeList.append(employee_n.getAgeEmployee())

            i += 1
    elif (userChoose == 2):
        while i < size:
            surname, yearBirth, monthBirth, dayBirth = inputDate()
            employee_n = Employee.Employee(surname, yearBirth, monthBirth, dayBirth)
            print(f"isinstance(employee_n, Employee.Employee -->){isinstance(employee_n, Employee.Employee)}")
            employeesAgeTo50List.append(employee_n.getDayTo50years())
            i += 1
    elif (userChoose == 3):
        while i < size:
            surname, yearBirth, monthBirth, dayBirth = inputDate()
            employee_n = Employee.Employee(surname, yearBirth, monthBirth, dayBirth)
            print(f"isinstance(employee_n, Employee.Employee -->){isinstance(employee_n, Employee.Employee)}")
            employeesAgeList.append(employee_n.getAgeEmployee())
            employeesAgeTo50List.append(employee_n.getDayTo50years())
            i += 1

    i = 0
    if (userChoose == 1):
        while i < size:
            print(f"\nisinstance(employeesAgeList[i], str -->){isinstance(employeesAgeList[i], str)}")
            print(employeesAgeList[i])
            i += 1
    elif (userChoose == 2):
        while i < size:
            print(f"\nisinstance(employeesAgeTo50List[i], str -->){isinstance(employeesAgeList[i], str)}")
            print(employeesAgeTo50List[i])
            i += 1
    else:
        while i < size:
            print(f"\nisinstance(employeesAgeList[i], str -->){isinstance(employeesAgeList[i], str)}")
            print(f"isinstance(employeesAgeTo50List[i], str -->){isinstance(employeesAgeList[i], str)}")
            print(employeesAgeList[i])
            print(employeesAgeTo50List[i])
            i += 1
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
