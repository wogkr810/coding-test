import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    try:
        while scoville:
            tmp = heapq.heappop(scoville)
            if tmp < K:
                next_tmp = heapq.heappop(scoville)
                heapq.heappush(scoville,tmp+2*next_tmp)
                cnt +=1
    except:
        cnt = -1 
    return cnt