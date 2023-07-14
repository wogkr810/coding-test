import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
        
    q = []
    length = len(food_times)
    prev_time = 0

    for idx,food_time in enumerate(food_times):
        heapq.heappush(q,(food_time,idx+1))
        
    while True:
        time, idx = heapq.heappop(q)
        heap_time = time
        time -= prev_time
        value = time * length

        length -= 1
        prev_time += time 

        if value > k:
            heapq.heappush(q,(heap_time, idx))
            break
        else:
            k -= value


    q.sort(key = lambda x : x[1])

    return q[k % len(q)][1]
