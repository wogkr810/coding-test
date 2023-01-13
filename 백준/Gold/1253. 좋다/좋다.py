N = int(input())
arr = list(map(int,input().split()))

arr.sort()

cnt = 0

for i in range(len(arr)):
    tmp_list = arr[:i] + arr[i+1:]
    start = 0
    end = N-2
    while start < end:
        if (tmp_list[start] + tmp_list[end]) == arr[i]:
            cnt += 1
            break
        elif (tmp_list[start] + tmp_list[end]) > arr[i]:
            end -=1
        else:
            start += 1

print(cnt)