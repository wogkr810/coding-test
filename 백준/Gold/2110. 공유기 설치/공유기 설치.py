import sys

N, C = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]

arr.sort()
s,e = 1, arr[-1]-arr[0]
result = 0

while s <= e:
    mid = (s+e)//2
    cnt = 1
    tmp_value = arr[0]

    for i in range(1,N):
        if arr[i] >= mid + tmp_value:
            tmp_value = arr[i]
            cnt += 1
    if cnt >= C:
        result = mid
        s = mid + 1
    else:
        e = mid -1
    
print(result)
         