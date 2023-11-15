from collections import deque

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int,input().split()))

    left = deque([0])
    right = deque(arr[2:])
    ans = 0

    for i in range(2,N-2):
        h = arr[i]
        left.append(arr[i-1])
        right.popleft()
        left_cnt, right_cnt = 256, 256
        left_flag, right_flag = False, False
        for j in range(len(left)-1, len(left)-3, -1):
            if left[j] < h:
                left_cnt = min(left_cnt, h-left[j])
            else:
                left_flag = True
                break
        for k in range(2):
            if right[k] < h:
                right_cnt = min(right_cnt, h-right[k])
            else:
                right_flag = True
                break
        
        if not left_flag and not right_flag:
            ans += min(left_cnt, right_cnt)
    print(f'#{tc} {ans}')