import math

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int,input().split())

cnt = 0

for i in arr:
    cnt += max(math.ceil((i - B) / C), 0) + 1 

print(cnt)