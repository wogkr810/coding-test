from itertools import combinations

N = int(input())

mp, mf, ms, mv = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

hubo = []

for i in range(1,N+1):
    for comb in combinations([j for j in range(1,N+1)],i):
        tmp_p, tmp_f, tmp_s, tmp_v, tmp_value = 0, 0, 0, 0, 0
        for k in comb:
            tmp_p += arr[k-1][0]
            tmp_f += arr[k-1][1]
            tmp_s += arr[k-1][2]
            tmp_v += arr[k-1][3] 
            tmp_value += arr[k-1][4]

        if tmp_p >= mp and tmp_f >= mf and tmp_s >= ms and tmp_v >= mv:
            hubo.append([tmp_value,list(comb)])

if hubo:
    hubo.sort(key = lambda x : (x[0],x[1]))
    print(hubo[0][0])
    print(*hubo[0][1])
else:
    print(-1)