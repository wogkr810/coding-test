'''
우선 순위큐 이용
1. input을 받는다.
-> idx,start,end 순 -> [1,3,8] , [8,6,27] .....

2. start시간 기준으로 정렬을 한다.

-> 우선순위큐는 end기준으로 넣을 예정이지만, 시작은 start 시간이 빠른 순이어야함.
-> sort : key = lambda x : x[1] / [1,3,8],[8,6,27] 이면 3,6

3. deque로 선언

-> 시간복잡도 줄이기위해 deque의 popleft 사용

4. heap 선언

-> end 기준으로 우선순위큐 넣을 예정

5. cnt 변수 선언

-> 방의 개수

6. while문 반복 -> class_list 없어질때까지

-> 넣을 class를 class_list에서 뽑음
-> 우선 방의 개수를 늘림 / cnt += 1
-> 우선순위큐에 원소가 존재한다면
   -> 가장 빨리 끝나는 class 하나를 뽑아서 끝나는 시간 체크
   -> 위의 끝나는 시간이 새로 들어온 class보다 빨리 끝나면
   -> 방을 추가할필요가없으니 cnt -= 1
   -> 하지만, 늦게끝난다면, 방도 하나 더 필요하기 cnt 건드리지 않기 + 비교를 위해 뺐던 방 다시 넣기

class는 어차피 방 추가해야하니 넣기


7. 최종 방의 개수 print

-------------예시----------
1
[(14, 2, 3)]
2
[(8, 3, 1), (14, 2, 3)]
3
[(8, 3, 1), (14, 2, 3), (27, 6, 8)]
4
[(8, 3, 1), (20, 6, 5), (14, 2, 3), (27, 6, 8)]
5
[(8, 3, 1), (13, 7, 2), (27, 6, 8), (20, 6, 5), (14, 2, 3)]
5
[(13, 7, 2), (14, 2, 3), (27, 6, 8), (20, 6, 5), (18, 12, 4)]
5
[(14, 2, 3), (18, 12, 4), (27, 6, 8), (20, 6, 5), (21, 15, 6)]
5
[(18, 12, 4), (20, 6, 5), (27, 6, 8), (21, 15, 6), (25, 20, 7)]

'''



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
        in_class = heapq.heappop(heap)
        if in_class[0] <= start:
            cnt -= 1
        else:
            heapq.heappush(heap,(in_class[0],in_class[1],in_class[2]))
            
    heapq.heappush(heap,(end,start,idx))
    

print(cnt)

    