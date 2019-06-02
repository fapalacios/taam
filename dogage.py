try:
    dogage = float(input("Enter dog age (in years): "))


    while dogage != 0:
        if dogage <= 2:
            humanage = dogage*10.5
        else:
            humanage = 21 + (dogage - 2)*4

        print(str(dogage) + " years for a dog is equivalent to " + 
          str(humanage) + " for humans")
    
        dogage = float(input("Enter dog age (in years):"))
    else:
        print("Bye!")
except ValueError as err:
    print("Invalid age")

