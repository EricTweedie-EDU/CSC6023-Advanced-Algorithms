# CSC6023-Advanced-Algorithms
Repo containing all the course projects 

# Contents

# Module 1
Create a program that implements a sort algorithm of your choice and applies it to a random vector of 1,000 elements
Repeat the process applying it to random vectors of 2,000, 3,000, ... up to 10,000 elements
Compute the time complexity of your algorithm and verify if the time it takes to your 1,000 to 10,000 corresponds to the time complexity prediction. You should use CProfile to record how long the sorting takes for each array

# Module 2
Create a program that asks repeatedly the user positive integer numbers and stores/deletes it in an AVL tree

# Module 3
Create a program that computes the "Tribonacci" sequence numbers, program should asks the user a positive Integer n and the deliver the n-th element of the Tribonacci sequence

# Module 4
Create a program that receives the list of possible named items with the following information: Value ($), Height (in), Width (in), Depth (in)
The limit of the optimal solution is expressed by the volume in cubic inches (in3) and the program has to maximize the value within the cubic limit
Your program should read a textual file with one item type per line with the information separated by comma, for example this fileLinks to an external site. lists four items with values 35, 40, 45, and 58 dollars and increasing dimensions
Your program should capture the overall limit of the package/knapsack from the user.
Your program should read any file with this format (name, value, height, width, depth) per line
Your program must print out the best distribution with a string like: "The suggested items are: 72 Milky Ways and 5 Tootsie Rolls with a total value of $53. There were 4 square inches left unused."
The printed statement must at least include: names of items included; number of items included; total profit; leftover space

# Module 5
Implement a Double Array Queue and test it for a very large case (100,000 randomly decided operations of enqueue or dequeue)
Your program should keep track of the number of costly operations and cheap operations and print them after running.
At the beginning of its run, your program should also ask the user about the ratio between enqueue and dequeue operations:
The probability of enqueues and dequeues should never be of less than half the other (34% enqueues - 66% dequeues or 66% enqueues - 34% dequeues)
Your program should then simulate 100,000 operations according to the probability input by the user. All of the enqueues and all of the dequeues should not happen consecutively but randomly according to the input probability. If your program does all of enqueues and then all of the dequeues, it would not be very interesting to see how many costly and cheap operations there were.

# Module 6
Implement a Linear Programming solver as described in the slides.
Your program will receive the necessary information for an LP problem namely:
○The number of variables (that will be equal to the number of constraint coefficients)
■ x
○The coefficient of each variable for the objective function (the column profit for slide 13 table)
■ f(x)
○The data for the square matrix stating the constraint (the inner elements of slide 13 table)
■ A
○The constraint limits (the last row of slide 13 table)
■ b
Having all input parameters, you will need to compute the possible solution for each variable alone and the solution of the linear equation system Ax = b

# Module 7
Create a program that calls the function myFunction(x) from 0 to 9999 and stores the results in an array. Your program should then apply the Hill Climbing algorithm several times (you can set this up Monte Carlo or Las Vegas style) to find the value of x that delivers the largest value for the function. Each time you call the hill climbing function you will pass in the array and a random starting index, x.
On each attempt at finding the largest value, the initial search value x is chosen randomly between the values 1 to 9998
