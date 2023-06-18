from itertools import accumulate

def solution(sequence, k):
    dp = [0] + list(accumulate(sequence))
    n = len(dp)

    res = []
    start = 0
    end = 0

    while end < n:
        tmp_minus = dp[end] - dp[start]
        if tmp_minus == k:
            res.append([start,end-1])
            start +=1
        elif tmp_minus >k:
            start +=1 
        else:
            end += 1


    res.sort(key = lambda x : (x[1]-x[0],x[0]))
    return res[0]