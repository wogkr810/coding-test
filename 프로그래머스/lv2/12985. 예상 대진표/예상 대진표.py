def solution(n,A,B):
    def roundup(num):
        if (num - int(num)) >= 0.5:
            return int(num) + 1
        else:
            return int(num)

    cnt = 1
    while True:
        A = roundup(A/2)
        B = roundup(B/2)
        if A != B:
            cnt += 1
        else:
            break
    return cnt