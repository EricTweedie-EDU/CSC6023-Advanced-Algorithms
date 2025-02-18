# Eric Tweedie
# Program that implements a sorting algorithm and applies it to random vector of 1000 to 10000 elements
# compute the time complexity of your algorithm and verify the time it takes for the 1000 - 10000
# Using the CProfile module record how long the sorting takes for each array
import random
import cProfile
# random vector of elements (range from 1000 - 10000)
vec = []
for i in range(1000):
    vec.append(random.randint(0, 1000))

# sorting algorithm - Bubble Sort
def bubbleSort(arr):
    '''Algorithm that sorts elements by comparing adjacent elements,
    the greater element is swapped with smaller one. The largest element is 
    sorted first to the rightmost side and then the 2nd largest and so on.
    Input: 
        array = unsorted integer values
    Output: 
        array = sorted integer values'''
    n = len(arr)
    
    for i in range(n): # Traverse over all elements in array
        swapped = False
        
        for j in range(0, n-i-1): # swapping elements if element is greater than the next element after it
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if (swapped == False):
            break
    return arr

cProfile.run('bubbleSort(vec)')