N = int(input())
M = int(input())
arr = list(map(int,input().split()))

arr.sort()
l, r = 0 ,N-1
cnt = 0

while l < r:
    value = arr[l] + arr[r]
    if value == M:
        cnt += 1
        l += 1
    elif value > M:
        r -= 1
    elif value < M:
        l += 1

print(cnt)  