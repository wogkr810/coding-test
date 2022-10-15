import heapq

def solution(operations):
    min_heap = []
    max_heap = [] 
    visited = [False] * len(operations)

    for i in range(len(operations)):
        operation, num = operations[i].split()
        num = int(num)
        if operation == "D":
            visited[i] = True

        if operation == "I":
            heapq.heappush(min_heap,(num,i))
            heapq.heappush(max_heap,(-num,i))

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
        return [0,0]
    else:
        return [max(ans),min(ans)]