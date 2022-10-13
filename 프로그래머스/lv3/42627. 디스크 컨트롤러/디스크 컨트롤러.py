from heapq import heappush, heappop, heapify

def solution(jobs):
    heap = []
    for job in jobs:
        heappush(heap,(job[1],job))

    time = 0
    res = []
    tmp_list = []

    while heap:
        while heap:
            flag = True
            tmp = heappop(heap)
            if tmp[1][0] <= time:
                time += tmp[1][1]
                res.append(time-tmp[1][0])
                flag = False
                break
            else:
                tmp_list.append(tmp)
        if flag:
            tmp_list.sort(key=lambda x : (x[1][0],x[1][1]))
            gt_time = tmp_list.pop(0)
            time = gt_time[1][0]
            time += gt_time[1][1]
            res.append(gt_time[1][1])
        for _ in tmp_list:
            heappush(heap,_)
        tmp_list = []
    
    return int(sum(res)/len(res))