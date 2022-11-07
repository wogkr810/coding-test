import bisect

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

arr.sort(key=lambda x : x[0])

dp = [arr[0][1]]

for i in range(1,len(arr)):
    if dp[-1] <= arr[i][1]:
        dp.append(arr[i][1])
    else:
        idx = bisect.bisect_left(dp,arr[i][1])
        dp[idx] = arr[i][1]

print(N-len(dp))