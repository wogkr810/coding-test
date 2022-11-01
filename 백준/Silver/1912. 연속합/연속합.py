N = int(input())
arr = list(map(int,input().split()))

for i in range(1,N):
    arr[i] = max(arr[i], arr[i]+arr[i-1])

print(max(arr))