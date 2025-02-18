# Eric Tweedie Mod 6 Program Assignment
# implement a linear programming solver
# using numpy
import numpy as np
from tabulate import tabulate


#  the number of variables that are equal to the number of constraints
while True:
    x = int(input("Enter the number of variables (ex. 3 or 2): "))
    if x <= 0:
        print("Error: value must be greater than zero.")
    else:
        break

# Asking for the values of the variables for the objective function (aka profit)
variables = []
for i in range(x):
    variable = int(input(f"Enter the coefficient value for variable {i+1} (ex. 3000 or 50): "))
    variables.append(variable)

# Asking for the constraint limit values (aka supply/availability)
limits = []
for i in range(x):
    limit = int(input("Enter the constraint limits (ex. 300 or 750): "))
    limits.append(limit)

b = np.array(limits)

# Asking for the data for the square matrix, which are the constraint values for each variable
arr_values = []
print(f"Enter the data for the square matrix for each spot in the matrix, your matrix is a {x} x {x}")
for i in range(x):
    rows = []
    for j in range(x):
        rows.append(float(input("Enter the value for the matrix (ex. 2): ")))
    arr_values.append(rows)

A = np.array(arr_values)

# inversing the matrix
inv_A = np.linalg.inv(A)

# Getting the dot product of the matrix with the constraint limits for the balanced solution
p = np.linalg.inv(A).dot(b)

# calculating the solo and balanced solutions 
# balanced solution is p but have to multiply with variables values to get overall profit
if x == 2:
    balanced = (p[0] * variables[0]) + (p[1] * variables[1])
    print(f"The balanced solution is {p[0]} units and {p[1]} units for a total profit of ${balanced}.")
if x == 3:
    balanced = (p[0] * variables[0]) + (p[1] * variables[1]) + (p[2] * variables[2])
    print(f"The balanced solution is {p[0]} units, {p[1]} units, and {p[2]} units for a total profit of ${balanced}")

# solo solutions
if x == 2:
    # profit total and unit total for variable 1
    unit1 = (limits[0]/A[0][0])
    unit2 = (limits[1]/A[1][0])
    if unit1 < unit2:
        solo1 = (unit1 * variables[0]) # profit total
        print(f"The solo solution for variable 1 is {unit1} units for a total profit of ${solo1}.")
    elif unit2 < unit1:
        solo2 = (unit2 * variables[1]) # profit total
        print(f"The solo solution for variable 1 is {unit2} units for a total profit of ${solo2}.")

    # profit total and unit total for variable 2
    unit3 = (limits[0]/A[0][1])
    unit4 = (limits[1]/A[1][1])
    if unit3 < unit4:
        solo3 = (unit3 * variables[0]) # profit total
        print(f"The solo solution for variable 2 is {unit3} units for a total profit of ${solo3}.")
    elif unit4 < unit3:
        solo4 = (unit2 * variables[2]) # profit total
        print(f"The solo solution for variable 2 is {unit4} units for a total profit of ${solo4}.")

if x == 3:
    # profit total and unit total for variable 1
    unit1 = (limits[0]/A[0][0])
    unit2 = (limits[1]/A[0][1])
    unit3 = (limits[2]/A[0][2])
    if unit1 < unit2 and unit1 < unit3:
        solo1 = (unit1 * variables[0]) # profit total
        print(f"The solo solution for variable 1 is {unit1} units for a total profit of ${solo1}.")
    elif unit2 < unit1 and unit2 < unit3:
        solo2 = (unit2 * variables[1]) # profit total
        print(f"The solo solution for variable 1 is {unit2} units for a total profit of ${solo2}.")
    elif unit3 < unit1 and unit3 < unit2:
        solo3 = (unit3 * variables[2]) # profit total
        print(f"The solo solution for variable 1 is {unit3} units for a total profit of ${solo3}.")
    
    # profit total and unit total for variable 2
    unit4 = (limits[0]/A[1][0])
    unit5 = (limits[1]/A[1][1])
    unit6 = (limits[2]/A[1][2])
 
    if unit4 < unit5 and unit4 < unit6:
        solo4 = (unit4 * variables[0]) # profit total
        print(f"The solo solution for variable 2 is {unit4} units for a total profit of ${solo4}.")
    elif unit5 < unit4 and unit5 < unit6:
        solo5 = (unit5 * variables[1]) # profit total
        print(f"The solo solution for variable 2 is {unit5} units for a total profit of ${solo5}.")
    elif unit6 < unit4 and unit6 < unit5:
        solo6 = (unit6 * variables[2]) # profit total
        print(f"The solo solution for variable 2 is {unit6} units for a total profit of ${solo6}.")

    # profit total and unit total for variable 3
    unit7 = (limits[0]/A[2][0])
    unit8 = (limits[1]/A[2][1])
    unit9 = (limits[2]/A[2][2])
    if unit7 < unit8 and unit7 < unit9:
        solo7 = (unit7 * variables[0]) # profit total
        print(f"The solo solution for variable 3 is {unit7} units for a total profit of ${solo7}.")
    elif unit8 < unit7 and unit8 < unit9:
        solo8 = (unit8 * variables[1]) # profit total
        print(f"The solo solution for variable 3 is {unit8} units for a total profit of ${solo8}.")
    elif unit9 < unit7 and unit9 < unit8:
        solo9 = (unit9 * variables[2]) # profit total
        print(f"The solo solution for variable 3 is {unit9} units for a total profit of ${solo9}.")

# table showing the data used for the calculations
if x == 2:
    mydata = [
        ["Supply", "item 1", "item 2", "Profit"],
        ["variable 1", A[0][0], A[1][0], variables[0]],
        ["variable 2", A[0][1], A[1][1], variables[1]],
        ["Supply/Availability", b[0], b[1]]
        ]
    # display the table
    print(tabulate(mydata))

if x == 3:
    mydata = [
        ["Supply", "item 1", "item 2", "item 3", "Profit"],
        ["variable 1", A[0][0], A[1][0], A[2][0], variables[0]],
        ["variable 2", A[0][1], A[1][1], A[2][1], variables[1]],
        ["variable 3", A[0][2], A[1][2], A[2][2], variables[2]],
        ["Supply/Availability", b[0], b[1], b[2]]
        ]
    # display the table
    print(tabulate(mydata))
# User guide for input parameters

# Enter the number of variables (ex. 3 or 2): 2
# Enter the coefficient value for variable 1 (ex. 3000 or 50): 50
# Enter the coefficient value for variable 2 (ex. 3000 or 50): 40
# Enter the constraint limits (ex. 300 or 750): 750
# Enter the constraint limits (ex. 300 or 750): 1000
# Enter the data for the square matrix for each spot in the matrix, your matrix is a 2 x 2
# Enter the value for the matrix (ex. 2): 1
# Enter the value for the matrix (ex. 2): 1.5
# Enter the value for the matrix (ex. 2): 2
# Enter the value for the matrix (ex. 2): 1
# The balanced solution is 375.0 units and 250.0 units for a total profit of $28750.0.
# The solo solution for variable 1 is 500.0 units for a total profit of $20000.0.     
# The solo solution for variable 2 is 500.0 units for a total profit of $25000.0.  

# Enter the number of variables (ex. 3 or 2): 3
# Enter the coefficient value for variable 1 (ex. 3000 or 50): 3000
# Enter the coefficient value for variable 2 (ex. 3000 or 50): 2000
# Enter the coefficient value for variable 3 (ex. 3000 or 50): 2000
# Enter the constraint limits (ex. 300 or 750): 300
# Enter the constraint limits (ex. 300 or 750): 200
# Enter the constraint limits (ex. 300 or 750): 300
# Enter the data for the square matrix for each spot in the matrix, your matrix is a 3 x 3
# Enter the value for the matrix (ex. 2): 2
# Enter the value for the matrix (ex. 2): 4
# Enter the value for the matrix (ex. 2): 5
# Enter the value for the matrix (ex. 2): 1 
# Enter the value for the matrix (ex. 2): 2
# Enter the value for the matrix (ex. 2): 4
# Enter the value for the matrix (ex. 2): 8
# Enter the value for the matrix (ex. 2): 0
# Enter the value for the matrix (ex. 2): 3
# The balanced solution is 25.0 units, 20.83333333333333 units, and 33.33333333333332 units for a total profit of $183333.3333333333
# The solo solution for variable 1 is 50.0 units for a total profit of $100000.0.
# The solo solution for variable 2 is 75.0 units for a total profit of $150000.0.
# The solo solution for variable 3 is 37.5 units for a total profit of $112500.0.