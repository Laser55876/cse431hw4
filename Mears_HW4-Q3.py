import time
import random

from sortedcontainers import SortedDict
# Sorted Dictionary using a Sorted Array of keys as backend
# https://www.geeksforgeeks.org/python-sorted-containers-an-introduction/

def insertIntoDict(D, arr):
    for v in arr:
        D[v] = v
        
def avgShortRunTimes(arr, unsorted=False, r=10000):
    start = time.time()
    for _ in range(r):
        if (unsorted):
            insertIntoDict(dict(), arr)
        else:
            insertIntoDict(SortedDict(), arr)
    total = time.time() - start
    return total / r

def getInsertionTimes(N):   
    arr = [v for v in range(N)]
    random.shuffle(arr)
    # Unsorted Dictionary (Hash Table)
    start = time.time()
    insertIntoDict(dict(), arr)
    total = time.time() - start
    if (not total):
        total = avgShortRunTimes(arr, True)
    print(f"Total Time for UnsortedDict Insertion of {N} values: {total}")    
    # Sorted Dictionary (Sorted Array)
    start = time.time()
    insertIntoDict(SortedDict(), arr)
    total = time.time() - start
    if (not total):
        total = avgShortRunTimes(arr)
    print(f"Total Time for SortedDict Insertion of {N} values: {total}\n")
    
def main():
    [getInsertionTimes(10 ** N) for N in range(1, 8)]

if __name__ == "__main__":
	main()