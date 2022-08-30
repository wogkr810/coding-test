N = int(input())
arr = list(map(int,input().split()))
x= int(input())

arr.sort()

cnt=0
start , end = 0, N-1

while start < end :
    tmp_sum = arr[start] + arr[end]
    if tmp_sum == x:
        cnt += 1
        start += 1
    
    elif tmp_sum > x:
        end -= 1

    elif tmp_sum < x :
        start += 1
        
print(cnt)