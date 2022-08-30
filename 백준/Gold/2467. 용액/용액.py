N = int(input())
arr=list(map(int,input().split()))

left, right = 0 , N-1
min_value = 1e10
hubo=[]

while left < right :
    tmp_sum = arr[left]+arr[right]
    if abs(tmp_sum) < min_value:
        min_value = abs(tmp_sum)
        L = left
        R = right
    
    if tmp_sum > 0 :
        right -=1

    elif tmp_sum < 0 :
        left +=1

    elif tmp_sum == 0 :
        break
    
print(arr[L], arr[R])