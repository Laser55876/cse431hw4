import time
import random

# https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2 # Finding the mid of the array
        L = arr[:mid] # Dividing the array elements
        R = arr[mid:] # into 2 halves
        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half
        i = j = k = 0
        while i < len(L) and j < len(R): # Copy data to temp arrays L[] and R[]
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        while i < len(L): # Checking if any element was left
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
def insertionSort(arr):
    for i in range(1, len(arr)): # Traverse through 1 to len(arr)
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, 
        # to one position ahead of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    
def avgShortRunTimes(arr, merge=False, r=10000):
    start = time.time()
    for _ in range(r):
        if (merge):
            mergeSort(arr[:])
        else:
            insertionSort(arr[:])
    total = time.time() - start
    return total / r

def getSortTimes(N):
    arr = [v for v in range(N)]
    random.shuffle(arr)
    arr1, arr2 = arr[:], arr[:]
    start = time.time()
    mergeSort(arr1)
    total = time.time() - start
    if (not total):
        total = avgShortRunTimes(arr, True)
    print(f"Total Time for Merge Sort of {N} values: {total}")
    start = time.time()
    insertionSort(arr2)
    total = time.time() - start
    if (not total):
        total = avgShortRunTimes(arr)
    print(f"Total Time for Insertion Sort of {N} values: {total}\n")
    
def main():
    [getSortTimes(N) for N in range(10, 201, 10)]
    
if __name__ == "__main__":
	main()