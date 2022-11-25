from collections import defaultdict
import sys

N = int(sys.stdin.readline())

arr = defaultdict(int)

for _ in range(N):
    int_input = int(sys.stdin.readline())
    if int_input not in arr.keys():
        arr[int_input] = 0
    else:
        arr[int_input] += 1

sort_list = list(arr.items())
sort_list.sort(key=lambda x : (x[1],-x[0]),reverse=True)
print(sort_list[0][0])
