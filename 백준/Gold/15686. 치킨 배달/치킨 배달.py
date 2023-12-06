from itertools import combinations

def distance(a, b, c, d):
    return abs(a-c) + abs(b-d)

N, M = map(int,input().split())
arr = []
ch = []
house = []
for i in range(N):
    tmp_input = list(map(int,input().split()))
    for j in range(N):
        if tmp_input[j] == 2:
            ch.append([i,j])
        if tmp_input[j] == 1:
            house.append([i,j])
    arr.append(tmp_input)

ans = int(1e10)

for combination in combinations(ch,M):
    tmp = 0
    for h in house:
        ch_distance = int(1e10)
        for c in combination:
            tmp_distance = distance(c[0], c[1], h[0], h[1])
            ch_distance = min(ch_distance, tmp_distance)
        tmp += ch_distance
    ans = min(ans, tmp)

print(ans)