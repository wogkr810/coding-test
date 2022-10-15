import heapq
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    operations = []
    for i in range(K):
        command, num = sys.stdin.readline().split()
        operations.append([command,int(num)])

    min_heap = []
    max_heap = [] 
    visited = [False] * K

    for j in range(len(operations)):
        operation, num = operations[j]
        if operation == "D":
            visited[j] = True
        num = int(num)
        if operation == "I":
            heapq.heappush(min_heap,(num,j))
            heapq.heappush(max_heap,(-num,j))
        
        elif operation == "D":
            try:
                if num == -1:
                    while True:
                        tmp = heapq.heappop(min_heap)
                        if not visited[tmp[1]]:
                            visited[tmp[1]]=True
                            break
                else:
                    while True:
                        tmp = heapq.heappop(max_heap)
                        if not visited[tmp[1]]:
                            visited[tmp[1]]=True
                            break
            except:
                pass

    ans = []

    while min_heap:
        tmp = min_heap.pop()
        if not visited[tmp[1]]:
            ans.append(tmp[0])

    while max_heap:
        tmp = max_heap.pop()
        if not visited[tmp[1]]:
            ans.append(-tmp[0])
    
    if len(ans) == 0 :
        print("EMPTY")
    else:
        print(max(ans),min(ans))