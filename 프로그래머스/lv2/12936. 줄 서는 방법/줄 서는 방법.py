from itertools import permutations
import math

def solution(n, k):
    num_list = [i for i in range(1,n+1)]
    res = []
    while True:
        a, b = divmod(k,math.factorial(n-1))  

        if b ==0:
            res.append(num_list[a-1])
            del num_list[a-1]
        else:
            res.append(num_list[a])
            del num_list[a]

        n -= 1
        k = b

        if n == 2:
            break

    res.extend(list(permutations(num_list))[b-1])
    
    return res