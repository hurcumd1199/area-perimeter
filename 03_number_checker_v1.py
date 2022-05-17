# get width
valid = False 
while not valid:

    error = "please enter a number that is more than zero"

    try:

        #ask user to enter a number
        width = float(input("enter the width "))
    
        # checks number is more than zero 
        if width > 0:
            valid = True
        
        # outputs error if input is valid 
        else:
            print(error)
            print()

    except ValueError:
        print(error)

# get height
valid = False 
while not valid:

    error = "please enter a number that is more than zero"

    try:

        #ask user to enter a number
        height = float(input("enter the height "))
    
        # checks number is more than zero 
        if height > 0:
            valid = True
        
        # outputs error if input is valid 
        else:
            print(error)
            print()

    except ValueError:
        print(error)

# calculate
area = width * height
print("Area", area)