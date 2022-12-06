N, K = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

left = 1
right = arr[-1]
max_value = 0 

while left <= right:
    mid = (left+right)//2
    cnt = 0
    for wire in arr:
        cnt += wire // mid
    
    if cnt >= K:
        max_value = max(max_value,mid)
        left = mid + 1
    else:
        right = mid - 1

print(max_value)