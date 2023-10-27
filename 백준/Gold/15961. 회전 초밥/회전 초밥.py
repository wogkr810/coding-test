import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.extend(arr)

l, r = 0, 0
counter = defaultdict(int)
ans = 0
counter[c] += 1     

for i in range(k):
    counter[arr[r]] += 1
    r += 1
    
while r < len(arr):
    ans = max(ans,len(counter))
    counter[arr[l]] -= 1
    if counter[arr[l]] == 0:
        del counter[arr[l]]
    
    counter[arr[r]] += 1
    l += 1
    r += 1
    
print(ans)