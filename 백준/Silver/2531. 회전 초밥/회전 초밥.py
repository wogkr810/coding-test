n, d, k, c = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr += arr

tmp_max = 0
for i in range(0,n+1):
    tmp_set = set(arr[i:i+k])
    tmp_len = len(tmp_set)
    if c not in tmp_set:
        tmp_len += 1

    tmp_max = max(tmp_len,tmp_max)
print(tmp_max)
        
