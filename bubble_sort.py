# Python program for implementation of Bubble Sort 
from time import time
def bubbleSort(arr): 
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(n): 

        # Last i elements are already in place 
        swap = False
        for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swap = True
        if not swap:
            break


# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90]
# arr = [1,2,3,4,5,6,7,8,9,10,11,13,12]
bubbleSort(arr)
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]), 