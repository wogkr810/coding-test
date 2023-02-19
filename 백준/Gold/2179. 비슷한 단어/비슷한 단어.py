from collections import defaultdict
import sys
input = sys.stdin.readline


N = int(input())
arr = defaultdict(int)
for i in range(N):
    arr[i] = input().strip()

arr_sort = sorted(arr.items(), key = lambda x: (x[1],x[0]))

def find_with(a,b):
    cnt = 0
    len_value = min(len(a),len(b))
    for i in range(len_value):
        if a[i] == b[i]:
            cnt += 1
        else:
            break
    return cnt

length = [0] * N
max_value = 0

for i in range(N-1):
    intersect_value = find_with(arr_sort[i][1],arr_sort[i+1][1]) 
    max_value = max(max_value,intersect_value)
    length[arr_sort[i][0]] = max(length[arr_sort[i][0]], intersect_value)
    length[arr_sort[i+1][0]] = max(length[arr_sort[i+1][0]], intersect_value)


first = 0
for i in range(N):
    if first == 0:
        if length[i] == max(length):
            first = arr[i]
            print(first)
            pre = arr[i][:max_value]
    else:
        if length[i] == max(length) and arr[i][:max_value] == pre:
            print(arr[i])
            break

