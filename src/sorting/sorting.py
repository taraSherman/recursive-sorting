# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    # if arr is less than or equal to 1,
    if len(arr) <= 1:
        # just return arr (cannot sort a single or no element)
        return arr
    # set mid to the middle point of arr (take the length of arr and divide by 2)
    mid = len(arr)//2
    # set the left of mid to arrA
    arrA = arr[:mid]
    # set the right of mid to arrB
    arrB = arr[mid:]
    # sort arrA by running merge_sort on it (recursion)
    newArrA = merge_sort(arrA)
    # sort arrB by running merge_sort on it
    newArrB = merge_sort(arrB)
    # return sorted arr by arr by merging both arrA and arrB
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

