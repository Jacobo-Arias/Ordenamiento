# Counting sort in Python programming


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * size*2

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, size*2):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

data = [97, 139, 195, 85, 105, 79, 162, 129, 25, 148, 63, 118, 35, 0, 16, 77, 174, 42, 110, 51, 72, 141, 108, 182, 54, 140, 24, 92, 119, 27, 165, 185, 5, 37, 19, 196, 107, 14, 153, 144, 187, 17, 149, 50, 64, 179, 104, 13, 62, 115, 159, 143, 32, 70, 93, 132, 109, 29, 106, 96, 122, 20, 94, 36, 114, 145, 111, 1, 180, 88, 7, 126, 74, 39, 53, 147, 116, 173, 30, 46, 183, 191, 4, 198, 134, 193, 18, 59, 76, 164, 136, 33, 199, 160, 48, 178, 154, 103, 158, 138]

# data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)