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

def timSort(arr):
    pass

def getSortTimes(N):
    pass
    
def main():
    pass

if __name__ == "__main__":
	main()
