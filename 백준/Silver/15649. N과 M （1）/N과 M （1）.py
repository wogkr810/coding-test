from itertools import permutations
N, M = map(int,input().split())

N_list=[i for i in range(1,N+1)]

for i in list(permutations(N_list,M)):
    print(*i)