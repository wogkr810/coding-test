from collections import deque

def solution(prices):
    prices = deque(prices)
    res = []
    
    while prices:
        cnt = 0
        tmp = prices.popleft()
        for i in prices:
            cnt += 1
            if i < tmp:
                break

        res.append(cnt)

    return res