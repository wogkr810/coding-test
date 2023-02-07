N = int(input())
arr = list(map(int,input().split()))
dp = []

def find_slope(y1,y2,x1,x2):
    return (y2-y1)/(x2-x1)

for i in range(len(arr)):
    left_cnt = 0
    left_slope = 1e10
    for j in range(i-1,-1,-1):
        left_tmp_slope = find_slope(arr[i],arr[j],i,j)
        if left_tmp_slope < left_slope:
            left_slope = left_tmp_slope
            left_cnt += 1

    right_cnt = 0
    right_slope = -1e10
    for k in range(i+1,len(arr)):
        right_tmp_slope = find_slope(arr[k],arr[i],k,i)
        if right_tmp_slope > right_slope:
            right_slope = right_tmp_slope
            right_cnt += 1
    
    dp.append(left_cnt+right_cnt)

print(max(dp))
