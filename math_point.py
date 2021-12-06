
x = eval(input("Enter first num"))

y = eval(input("Enter second num"))
status = (x,y)

    match status:
        case(0,0):
            print("origin")

        case(x,0):
            print("x axis")
        
        case(0,y):
            print("y asis")
        
        case _:
            raise ValueError("Not possible")

