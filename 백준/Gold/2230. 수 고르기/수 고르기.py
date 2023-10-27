N, M = map(int,input().split())
arr = [int(input()) for _ in range(N)]

arr.sort()
s, e = 0, 1
ans = int(1e10)
while s < N and e < N:
    value = (arr[e] - arr[s])
    if value >= M:
        ans = min(value,ans)
        s += 1
    else:
        e += 1

if N == 1:
    print(0)
else:
    print(ans)

    
