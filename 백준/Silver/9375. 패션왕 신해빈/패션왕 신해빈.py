from collections import defaultdict,Counter
T = int(input())

for _ in range(T):
    N = int(input())
    fashion_dict = defaultdict(int)
    for i in range(N):
        dress, type = input().split()
        fashion_dict[type] += 1
    res = 1
    for i in list(fashion_dict.values()):
        res = res *(i+1)
    print(res-1)
    