from collections import deque
import heapq

N = int(input())
class_list = []

for _ in range(N):
    class_list.append(list(map(int,input().split())))

class_list.sort(key=lambda x: x[1])
class_list = deque(class_list)

heap = []

cnt = 0
while class_list:
    idx, start, end = class_list.popleft()
    cnt += 1
    if heap:
        tmp = heapq.heappop(heap)
        if tmp[0] <= start:
            cnt -= 1
        else:
            heapq.heappush(heap,(tmp[0],tmp[1],tmp[2]))
            
    heapq.heappush(heap,(end,start,idx))
    

print(cnt)