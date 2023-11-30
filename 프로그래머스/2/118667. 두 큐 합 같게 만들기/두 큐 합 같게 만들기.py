from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    one_sum, two_sum = sum(queue1), sum(queue2)
    n, m = len(queue1), len(queue2)
    cnt = 0
    
    if (one_sum + two_sum) % 2 != 0:
        return -1
    
    while True:
        if one_sum == two_sum:
            return cnt
        elif one_sum > two_sum:
            now = queue1.popleft()
            queue2.append(now)
            one_sum -= now
            two_sum += now
            cnt += 1
        elif one_sum < two_sum:
            now = queue2.popleft()
            queue1.append(now)
            one_sum += now
            two_sum -= now
            cnt += 1
        
        if cnt >= (n+m) * 2:
            return -1
        