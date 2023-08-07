from itertools import combinations
from collections import Counter, defaultdict

def solution(orders, course):
    hubo = []
    len_max = dict()

    for i in course:
        len_max[i] = 0
        for order in orders:
            for combination in combinations(sorted(order),i):
                hubo.append(''.join(combination))

    counter = Counter(hubo).most_common()
    res = []

    for key, value in counter:
        l_k = len(key)
        len_max[l_k] = max(len_max[l_k], value)
        if value == len_max[l_k] and value >= 2:
            res.append(key)

    return sorted(res)
    