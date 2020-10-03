# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # set up crawlers
    i = 0
    j = 0
    k = 0
    # so long as the respective indices for arrA and arrB are less than their lengths,
    while i < len(arrA) and j < len(arrB):
        # if arrA's index is less than arrB's index,
        if arrA[i] < arrB[j]:
            # set merged_arr's index to arrA's index
            merged_arr[k] = arrA[i]
            i += 1
        # otherwise,
        else:
            # set merged_arr's index to arrB's index
            merged_arr[k] = arrB[j]
            j += 1
        # arrA's index is no longer less than arrB's index, set merged_arr's index
        k += 1
    # run the same code over each list separately (this is for any remaining items in either list)
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k += 1
        i += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        # set mid to the middle point of arr (take the length of arr and divide by 2)
        mid = (len(arr))//2
        # sort arrA by running merge_sort on it (recursion)
        sorted_left = merge_sort(arr[:mid])
        # sort arrB by running merge_sort on it
        sorted_right = merge_sort(arr[mid:])
        # merge sorted lists and set to sorted_arr
        sorted_arr = (merge(sorted_left, sorted_right))
        # return sorted_arr
        return sorted_arr
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

