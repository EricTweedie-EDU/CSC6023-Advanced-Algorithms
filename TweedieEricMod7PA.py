# Eric Tweedie Mod 7 Program Assignment 
# create a program that calls the function myFunction(x) from 0 to 9999 and stores the results in an array. Program should then apply the hill climbing algorithm several times
# can set that up using Las Vegas or Monte Carlo style to find the value of x that delivers the largest value for the function.
# Each time you call the function you will pass in the array and a random starting index, x.
# on each attempt at finding the largest value, the initial search value x is chosen randomly between the values 1 to 9998
import random
import math

def myFunction(x):
    if (x == 0):
        return 0
    elif ((math.log2(x) * 7) % 17) < (x % 13):
        return (x + math.log2(x))**3
    elif ((math.log2(x) * 5) % 23) < (x % 19):
        return (math.log2(x)*2)**3
    else:
        return (math.log2(x)**2) - x

# hill climbing algorithm using the Las Vegas style
def hillClimbing(arr, start_index):
    current_index = start_index
    current_value = arr[current_index]
    global_max = max(arr)
    left_value = arr[current_index - 1]
    right_value = arr[current_index + 1]
    right_index = (current_index + 1)
    diffL = left_value - current_value
    diffR = right_value - current_value

    # if the current value is equal to the global max return the value and index
    if current_value == global_max:
        return "Global max is equal to current index/value", current_index, current_value
    while True:
        # if the current value is greater than both left and right, return value and index
        if current_value > left_value and current_value > right_value:
            return current_index, current_value
        # start with looking at the left
        elif left_value > current_value and current_value > right_value:
        # search to the left
            current_index -= 1
            current_value = arr[current_index]
            right_value = arr[current_index + 1]
            if left_value != arr[0]:
                left_value = arr[current_index - 1]
            else:
                return current_index, current_value
            if current_value > (left_value):
                return current_index, current_value   
        # start with looking at the right
        elif right_value > current_value and current_value > left_value:
        # search to the right
            current_index += 1
            current_value = arr[current_index]
            left_value = arr[current_index - 1]
            if right_index < len(arr) - 1:
                right_index += 1
                right_value = arr[right_index]
            else:
                return current_index, current_value
            if current_value > (right_value):
                return current_index, current_value
        # if the starting value is in a pit, so equal increases from the current value to the left and to the right, search to the right
        elif current_value < left_value and current_value < right_value:
            if diffL == diffR:
                current_index += 1
                current_value = arr[current_index]
                right_value = arr[current_index + 1]
                left_value = arr[current_index - 1]
                if current_value > (right_value):
                    return current_index, current_value
            
        # if the current value is in a pit with unequal increases to the left and right, search the greater side
            if diffL > diffR:
                current_index -= 1
                current_value = arr[current_index]
                left_value = arr[current_index - 1]
                right_value = arr[current_index + 1]
                if current_value > (left_value):
                    return current_index, current_value
            elif diffR > diffL:
                current_index += 1
                current_value = arr[current_index]
                right_value = arr[current_index + 1]
                left_value = arr[current_index - 1]
                if current_value > (right_value):
                    return current_index, current_value
            
        # if the values being traversed are the same keep going until the value changes and if the next value is less return the value before the lesser one
        # if the value is greater after the last same value keep going
        # left shoulder traversal
        elif left_value >= current_value:
            current_index -= 1
            current_value = arr[current_index]
            left_value = arr[current_index - 1]
            if current_value > (left_value):
                return current_index, current_value
        # right shoulder traversal
        elif right_value >= current_value:
            while current_index < len(arr) -1:
                current_index += 1
                current_value = arr[current_index]
                if right_index < len(arr) -1:
                    right_index += 1
                    right_value = arr[right_index]
                    if right_index == len(arr) - 1:
                        right_value = arr[right_index]
                        current_value = right_value
                        current_index = right_index
                        return current_index, current_value
                if current_value > (right_value):
                    return current_index, current_value

def main():            
    arr = []
    for i in range(10000):
        arr.append(myFunction(i))

    start_index = random.randint(1, 9998)
    print(hillClimbing(arr, start_index))

main()

# test cases
# arr = [5,6,5,4,4,4,4] 
# si = 3
# arr = [1,2,3,4,5,6,7,8,9,10]
# si = 3
# arr = [3,4,5,2,1,3]
# si = 2
# arr = [1,2,2,2,3,2]
# si = 1