import Rectangle

engineProgramLoop = True
while engineProgramLoop == True:
    Rectangle.Rectangle().meetUser()

    height = float(input("Enter height your rectangle, please\n--> "))
    width = float(input("Enter width your rectangle, please\n--> "))
    userChooseIO = int(input("Enter 1 if you need square\nEnter 2 if you need perimeter"
                             "\nEnter 3 if you need square and perimeter\n--> "))

    rectangleUser = Rectangle.Rectangle(height, width)

    p = rectangleUser.findPerimeter()
    s = rectangleUser.findSquare()

    rectangleUser.outputRectangle(p, s, userChooseIO)

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
