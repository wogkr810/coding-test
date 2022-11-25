import heapq
import sys

N, K = map(int,sys.stdin.readline().split())

jewel = []
for _ in range(N):
    heapq.heappush(jewel,list(map(int,sys.stdin.readline().split())))

bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))

jewel.sort()
bags.sort()

cnt = 0
smaller_than_bag = []

for bag in bags:
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(smaller_than_bag,-jewel[0][1])
        heapq.heappop(jewel)
    if smaller_than_bag:
        cnt -= heapq.heappop(smaller_than_bag)
    elif not jewel:
        break

print(cnt)