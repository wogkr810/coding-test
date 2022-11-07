H, W = map(int,input().split())
arr = list(map(int,input().split()))

result = 0 
for i in range(1,len(arr)-1):
    tmp_min = min(max(arr[:i+1]), max(arr[i:]))
    if arr[i] < tmp_min:
        result += tmp_min-arr[i]

print(result)