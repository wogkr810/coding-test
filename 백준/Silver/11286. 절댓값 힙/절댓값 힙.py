import heapq
import sys

heap=[]

N=int(sys.stdin.readline())

for i in range(N):
    tmp=int(sys.stdin.readline())
    if tmp==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(tmp),tmp))