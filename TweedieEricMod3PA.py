# Eric Tweedie mod 3 program assignment
# create a program that computes the "tribonacci" sequence numbers

def tribo(n):
    '''function that computes the "tribonacci" sequence numbers
    from a given input from the user. Program displays the corresponding
    value of the sequence from the user input.
    Input:
        n = integer value from user input
    Output:
        The integer value corresponding to the user input in the tribonacci sequence'''

    # initializing the first three tribonacci numbers
    a, b, c = 1, 1, 1
    if (n < 3):
        return 1
    for i in range(3, n):
        # calculate the next tribonacci number
        a, b, c = b, c, a + b + c
    return c

# call the function with user input
def main():
    while True:
        try:
            n = int(input("Enter a positive number/enter a negative to quit: "))
            if n <= 0:
                break
            elif n > 0:
                print(tribo(n))
            
        except ValueError:
            print("Invalid input, please enter a positive number.")

main()