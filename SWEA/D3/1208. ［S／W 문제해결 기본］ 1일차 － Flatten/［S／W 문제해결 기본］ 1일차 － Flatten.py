# import sys
# sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int,input().split()))

    for _ in range(N):
        max_value  = max(arr)
        min_value = min(arr)
        max_idx = arr.index(max_value)
        min_idx = arr.index(min_value)

        arr[max_idx] -= 1
        arr[min_idx] += 1
  
        if arr[max_idx] - arr[min_idx] <= 1:
            break

    print(f'#{tc} {max(arr)-min(arr)}')