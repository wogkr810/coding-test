'''
1 : 1
2 : 2
3 : 3
4 : 5

'''

def solution(n):
    dp = [1,2]
    for i in range(n-2):
        dp.append((dp[-1]+dp[-2])%1000000007)
    return dp[-1] % 1000000007