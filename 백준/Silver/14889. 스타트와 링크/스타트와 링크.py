from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

idx_list = [i for i in range(N)]
ans = int(1e10)

for c in combinations(idx_list, int(N/2)):
    first = c
    second = list(set(idx_list) - set(first))
    first_sum, second_sum = 0, 0
    for a,b in combinations(first, 2):
        first_sum += (arr[a][b] + arr[b][a])

    for c,d in combinations(second, 2):
        second_sum += (arr[c][d] + arr[d][c])

    ans = min(ans, abs(first_sum - second_sum))
        
print(ans)
