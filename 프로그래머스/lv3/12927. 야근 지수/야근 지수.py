import heapq

def solution(n, works):
    heap = []
    for work in works:
        heapq.heappush(heap,-work)
    
    while True:
        tmp = -1 * heapq.heappop(heap)
        
        if tmp == 0:
            break
            
        tmp -= 1
        heapq.heappush(heap,-tmp)
            
        n -= 1
        
        if n == 0 :
            break
            
    return sum([i**2 for i in heap])
