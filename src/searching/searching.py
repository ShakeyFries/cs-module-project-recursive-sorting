# TO-DO: Implement a recursive implementation of binary search
# using code from Geek for geeks: https://www.geeksforgeeks.org/recursive-insertion-sort/
def binary_search(arr, target, start, end):
    # binary search algorithm
    # base case
    # start is >= the end

    if end >= start:
        # establish middle
        middle = (start + end) // 2

        # if target is pointing at the middle then return middle
        if arr[mid] == target:
            return mid

        # if target is < middle then pivot left
        elif arr[mid] > target:
            return binary_search(arr, target, start, middle - 1)

        # if target is >= to middle then pivot right.
        else:
            return binary_search(arr, target, middle +1, end)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here

