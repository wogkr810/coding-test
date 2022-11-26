import sys

N = int(sys.stdin.readline())
arr1 = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))

arr1.sort()

def binary_search(arr,target):
    start = 0
    end = len(arr) -1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            print(1)
            return
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid -1
    print(0)

for find_value in arr2:
    binary_search(arr1,find_value)
