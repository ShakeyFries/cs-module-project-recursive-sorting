# TO-DO: complete the helper function below to merge 2 sorted arrays
# using code from Geek for geeks: https://www.geeksforgeeks.org/recursive-insertion-sort/

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # Your code here
    # find how many elements are in array
    # create array using 0's,
    merged_arr = []

    a = 0
    # pointer for ArrA
    b = 0
    # pointer for ArrB

    # look thru element in merged_arr, compare and point in correct direction.
    while a < len(arrA) and b < len(arrB):
        # compare a & b
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    # recurse and sort
    while a < len(arrA):
        merged_arr.append(arrA[a])
        a += 1
    while b < len(arrB):
        merged_arr.append(arrB[b])
        b += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2 ])
        right = merge_sort(arr[:len(arr) // 2 ])
        arr = merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#     pass

# def merge_sort_in_place(arr, l, r):
#     # Your code here
#     pass

