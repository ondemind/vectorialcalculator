import math

# result = 10 * math.cos(math.radians(58)) it must be first converted in radians in order to use the sine and cosine with degrees

def component_operation() :
    # To identify the variable
    vector_variable = input("What variable are we dealing with? ")
    vector_variable = vector_variable.capitalize()

    # To identify the magnitude and direction of that variable
    magnitude = float(input('Please insert a magnitude value interpreted in units: '))
    direction = float(input('Please insert a direction value interpreted in degrees: ')) # NOTE: This is only interpreted in degrees. If you want to only input values interpreted in radians, then you should go to lines 17 and 18 and remove the math.radians text from the code
    
    # The operation in which we find the components using the cosine and the sine function.
    # cosine belongs to X and sine belongs to Y

    operation_cos = magnitude * math.cos(math.radians(direction)) # NOTE: math.radians() converts the value to degrees. If you only want to work with radians, then you should delete it. 
    operation_sin = magnitude * math.sin(math.radians(direction))

    print(f'The value for the component {vector_variable}x is: {operation_cos} degrees') 
    print(f'The value for the component {vector_variable}y is: {operation_sin} degrees') 

    # A version in which we only left 2 floating digits from the result
    # print(f'The value for the component {vector_variable}x is: {"%.2f" % operation_cos} degrees')
    # print(f'The value for the component {vector_variable}y is: {"%.2f" % operation_sin} degrees')


def component_direction() :
    # To identify the variable
    vector_variable = input("What variable are we dealing with? ")
    vector_variable = vector_variable.capitalize()

    # To identify the component of that variable
    component_x = input(f'Please insert the component x of {vector_variable}: ')
    component_y = input(f'Please insert the component y of {vector_variable}: ')

    # In this case, we use the arctangine to find the direction of the vector
    arctang_operation = math.degrees(math.atan2(int(component_y), int(component_x)))
    print(f'The arctang of {component_x}/{component_y} gave us the direction of {arctang_operation} degrees')

    # A version in which we only left 2 floating digits from the result
    # print(f'The arctang of {component_x}/{component_y} gave us the direction of {"%.2f" % arctang_operation} degrees')


def component_magnitude() :
    # To identify the variable
    vector_variable = input("What variable are we dealing with? ")
    vector_variable = vector_variable.capitalize()

    # To identify the component of that variable
    component_x = input(f'Please insert the component x of {vector_variable}: ')
    component_y = input(f'Please insert the component y of {vector_variable}: ')

    # The operation to find the magnitude
    magnitude_operation = math.sqrt(((int(component_x) ** 2) + (int(component_y) ** 2)))
    print(f'The component of {component_x} and {component_y} gave us the magnitude of {magnitude_operation} units') 

    # A version in which we only left 2 floating digits from the result
    # print(f'The component of {component_x} and {component_y} gave us the magnitude of {"%.2f" % magnitude_operation} units')


def find_components():
    # To identify the variable of the points
    vector_point_1 = input("Which is the first point we are dealing with? ")
    vector_point_2 = input("Which is the second point we are dealing with? ")

    # Components of each point
    component_1x = int(input("Which is the component X of point1? "))
    component_1y = int(input("Which is the component Y of point1? "))
    component_2x = int(input("Which is the component X of point2? "))
    component_2y = int(input("Which is the component Y of point2? "))

    # The operation to find the components on two points
    operation_x = component_1x - component_2x
    operation_y = component_1y - component_2y
    print(operation_x, operation_y)


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
            component_operation()
            continue
        elif option == "2" :
            component_direction()
            continue
        elif option == "3" :
            component_magnitude()
            continue
        elif option == "4" :
            component_direction()
            component_magnitude()
            continue
        elif option == '5' :
            find_components()
            continue
    else :
        if option == 'q' :
            quit()
        else :
            print("Error, please try again with a value described on the text.")
            quit()
