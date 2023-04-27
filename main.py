import math

# result = 10 * math.cos(math.radians(58)) it must be first converted in radians in order to use the sine and cosine with degrees

def ComponentOperation() :
    # To identify the variable
    vectorvariable = input("What variable are we dealing with? ")
    vectorvariable = vectorvariable.capitalize()

    # To identify the magnitude and direction of that variable
    Magnitude = float(input('Please insert a magnitude value interpreted in units: '))
    Direction = float(input('Please insert a direction value interpreted in degrees: ')) # NOTE: This is only interpreted in degrees. If you want to only input values interpreted in radians, then you should go to lines 19 and 20 and remove the math.radians text from the code
    
    # The operation in which we find the components using the cosine and the sine function.
    # cosine belongs to X and sine belongs to Y

    operationcos = Magnitude * math.cos(math.radians(Direction)) # NOTE: math.radians() converts the value to degrees. If you only want to work with radians, then you should delete it. 
    operationsin = Magnitude * math.sin(math.radians(Direction))

    print(f'The value for the component {vectorvariable}x is: {operationcos} degrees') 
    print(f'The value for the component {vectorvariable}y is: {operationsin} degrees') 

    #A version in which we only left 2 floating digits from the result
    #print(f'The value for the component {vectorvariable}x is: {"%.2f" % operationcos} degrees')
    #print(f'The value for the component {vectorvariable}y is: {"%.2f" % operationsin} degrees')
        
def ComponentDirection() :
    # To identify the variable
    vectorvariable = input("What variable are we dealing with? ")
    vectorvariable = vectorvariable.capitalize()

    # To identify the component of that variable
    ComponentX = input(f'Please insert the component x of {vectorvariable}: ')
    ComponentY = input(f'Please insert the component y of {vectorvariable}: ')

    ArctangOperation = math.degrees(math.atan2(int(ComponentY), int(ComponentX)))
    print(f'The arctang of {ComponentX}/{ComponentY} gave us the direction of {ArctangOperation} degrees')

    #A version in which we only left 2 floating digits from the result
    #print(f'The arctang of {ComponentX}/{ComponentY} gave us the direction of {"%.2f" % ArctangOperation} degrees')

def ComponentMagnitude() :
    # To identify the variable
    vectorvariable = input("What variable are we dealing with? ")
    vectorvariable = vectorvariable.capitalize()

    # To identify the component of that variable
    ComponentX = input(f'Please insert the component x of {vectorvariable}: ')
    ComponentY = input(f'Please insert the component y of {vectorvariable}: ')

    # The operation to find the magnitude
    MagnitudeOperation = math.sqrt(((int(ComponentX) ** 2) + (int(ComponentY) ** 2)))
    print(f'The component of {ComponentX} and {ComponentY} gave us the magnitude of {MagnitudeOperation} units') 

    #A version in which we only left 2 floating digits from the result
    #print(f'The component of {ComponentX} and {ComponentY} gave us the magnitude of {"%.2f" % MagnitudeOperation} units')

def FindComponents():
    # To identify the variable of the points
    vectorpoint1 = input("Which is the first point we are dealing with? ")
    vectorpoint2 = input("Which is the second point we are dealing with? ")

    # Components of each point
    Component1X = int(input("Which is the component X of point1? "))
    Component1Y = int(input("Which is the component Y of point1? "))
    Component2X = int(input("Which is the component X of point2? "))
    Component2Y = int(input("Which is the component Y of point2? "))

    # The operation to find the components on two points
    OperationX = Component1X - Component2X
    OperationY = Component1Y - Component2Y
    print(OperationX, OperationY)

while True :
    option = input('''What do you want to do now?
    1. Find components in a vector which we have a magnitude and a direction.
    2. Find the direction in a vector which we have a component.
    3. Find the magnitude in a vector which we have a component.
    4. Find the magnitude and direction in a vector which we have a component.
    5. Find the component between a point to another point
    q. Exit the program
    ''').lower()
    if option.isdigit() :
        if option == "1" :
            ComponentOperation()
            continue
        elif option == "2" :
            ComponentDirection()
            continue
        elif option == "3" :
            ComponentMagnitude()
            continue
        elif option == "4" :
            ComponentDirection()
            ComponentMagnitude()
            continue
        elif option == '5' :
            FindComponents()
            continue
    else :
        if option == 'q' :
            quit()
        else :
            print("Error, please try again with a value described on the text.")
            quit()
