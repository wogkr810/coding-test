from collections import deque

def solution(A, B):
    A.sort()
    B.sort()
    B = deque(B)

    cnt = 0
    for i in range(len(A)):
        while B:
            tmp = B.popleft()
            if tmp > A[i]:
                cnt += 1
                break

    return cnt