
def num_check(question):
    # get response
    valid = False 
    while not valid:

        error = "please enter a number that is more than zero"

        try:

            #ask user to enter a number
            response = float(input(question))
        
            # checks number is more than zero 
            if response > 0:
                return response
            
            # outputs error if input is valid 
            else:
                print(error)
                print()

        except ValueError:
            print(error)



# calculate
width = num_check("What is the width: ")
height = num_check("What is the height: ")

area = width * height
perimeter = 2 * (width + height)

print("Area: {:.2f} square units".format(area))
print("Perimeter: {} units".format(perimeter))