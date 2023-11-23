N , S = map(int,input().split())
arr = list(map(int,input().split()))

start , end = 0, 0
tmp_sum=arr[start]
min_value=1e10

while start<= end :
    if tmp_sum >= S:
        min_value = min(min_value, end-start+1)
        tmp_sum -= arr[start]
        start+=1
    else:
        end+=1
        if end==N:
            break
        tmp_sum += arr[end]
    
if min_value == 1e10:
    print(0)
else:
    print(min_value)