N = int(input())
arr = list(map(int,input().split()))
arr.sort()
T = int(input())

cnt = 0
left = 0
right = N-1

while left<right:
    tmp_sum = arr[left] + arr[right]
    if tmp_sum == T:
        cnt +=1
        left += 1
    elif tmp_sum > T:
        right -= 1
    else:
        left += 1

print(cnt)
        
