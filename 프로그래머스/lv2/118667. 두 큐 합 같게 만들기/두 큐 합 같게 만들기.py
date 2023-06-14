from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    one_sum = sum(queue1)
    two_sum = sum(queue2)
    one_len = len(queue1)
    two_len = len(queue2)
    
    if (one_sum + two_sum) % 2 != 0:
        return -1

    cnt = 0

    if one_sum == two_sum:
        return 0

    while True:
        if one_sum > two_sum:
            tmp_pop = queue1.popleft()
            queue2.append(tmp_pop)
            one_sum -= tmp_pop
            two_sum += tmp_pop        
        elif one_sum < two_sum:
            tmp_pop = queue2.popleft()
            queue1.append(tmp_pop)
            two_sum -= tmp_pop
            one_sum += tmp_pop

        cnt += 1

        if one_sum == two_sum:
            break

        if cnt >= 10 *(one_len + two_len):
            cnt = -1
            break
    
    return cnt