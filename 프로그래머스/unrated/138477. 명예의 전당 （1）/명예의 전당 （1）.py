import heapq

def solution(k, score):
    heap = []
    res = []
    for sc in score:
        if len(heap) < k:
            heapq.heappush(heap,sc)
        else:
            tmp = heapq.heappop(heap)
            if sc > tmp:
                heapq.heappush(heap,sc)
            else:
                heapq.heappush(heap,tmp)
        res.append(heap[0])
    return res


