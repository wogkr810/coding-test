import heapq

def hhmm_to_mm(arr):
    h1, m1 = arr[0].split(":")
    h2, m2 = arr[1].split(":")

    return [int(h1)*60 + int(m1), int(h2)*60 + int(m2)]

def solution(book_time):
    book_time = list(map(hhmm_to_mm, book_time))
    heapq.heapify(book_time)
    cnt = 0

    while book_time:
        end = heapq.heappop(book_time)[1] + 10
        stack = []
        while book_time:
            s, e = heapq.heappop(book_time)
            if s >= end:
                end = e + 10
                continue
            else:
                stack.append([s,e])
        for _ in stack:
            heapq.heappush(book_time,_)
        cnt += 1
    return cnt