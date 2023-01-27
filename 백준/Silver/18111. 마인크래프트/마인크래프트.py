N, M , B = map(int,input().split())
arr = []
for _ in range(N):
    arr.extend(list(map(lambda x : int(x),input().split())))

min_arr, max_arr = min(arr), max(arr)
res = []
for target in range(min_arr,max_arr+1):
    remove_block = 0
    get_block = 0
    for i in range(len(arr)):
        if arr[i] == target:
            continue
        elif arr[i] > target:
            remove_block += arr[i] - target
        else:
            get_block += target - arr[i]
    
    if get_block > remove_block + B:
        continue
    
    cnt = remove_block *2 + get_block
    
    res.append([cnt,target])

res.sort(key=lambda x: (x[0],-x[1]))

print(*res[0])