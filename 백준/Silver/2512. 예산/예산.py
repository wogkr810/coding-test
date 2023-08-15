N = int(input())
arr = list(map(int,input().split()))
M = int(input())

start, end = 0,int(1e5)

if sum(arr) <= M:
    print(max(arr))

else:
    res = 0 
    while start <= end:
        tmp_res = 0
        mid = (start+end)//2
        for i in arr:
            tmp_res += min(i, mid)

        if tmp_res > M:
            end = mid - 1
        else:
            start = mid + 1
            res = max(res, tmp_res)
        
    print(end)