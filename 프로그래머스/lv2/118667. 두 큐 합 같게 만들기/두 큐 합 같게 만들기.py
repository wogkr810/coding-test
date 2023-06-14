from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    one_sum, two_sum = sum(queue1), sum(queue2)
    one_len , two_len = len(queue1) , len(queue2)

    if (one_sum + two_sum) % 2 != 0:      # 모든 수의 합이 홀수면 안됨.
        return -1

    cnt = 0

    while True:
        if one_sum > two_sum:
            tmp_pop = queue1.popleft()
            queue2.append(tmp_pop)
            one_sum -= tmp_pop
            two_sum += tmp_pop 
            cnt += 1       
        elif one_sum < two_sum:
            tmp_pop = queue2.popleft()
            queue1.append(tmp_pop)
            two_sum -= tmp_pop
            one_sum += tmp_pop
            cnt += 1

        if one_sum == two_sum:
            break

        if cnt >= 2 *(one_len + two_len):  # 모두 옮기는과정이 2번 넘으면 그만.
            cnt = -1
            break
    
    return cnt