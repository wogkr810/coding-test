from itertools import combinations

N, M = map(int,input().split())
arr = list(map(int,input().split()))

res = []

for combination in list(combinations(arr,3)):
    res.append(sum(combination)-M)

res.sort()
res = [i for i in res if i<=0]

print(max(res)+M)


