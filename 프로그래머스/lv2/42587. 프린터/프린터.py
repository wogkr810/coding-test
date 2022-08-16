#예시
'''
#1번 예시
priorities
2 1 3 2 -> 3 2 2 1 -> X 2 2 1 -> X Y 2 1 -> X Y Z 1 -> X Y Z W
location_list 
0 1 2 3 -> 2 3 0 1 -> X 3 0 1 -> X Y 0 1 -> X Y Z 1 -> X Y Z W
(pr , lo) :        (3,2)      (2,3)      (2,0)      (1,1)
cnt=0               1(답)       2          3          4

#2번 예시
priorities
119111->911111->X11111->XY1111->XYZ111->XYZA11->XYZAB1
location_list 
012345->234501->X34501->XY4501->XYZ501->XYZA01->XYZAB1
(pr , lo) :  (9,2)    (1,3)   (1,4)  (1,5)    (1,0)
cnt=0          1        2       3      4        5(답)
'''

from collections import deque

def solution(priorities, location):
    priorities=deque(priorities)
    #location_list -> enumerate로 개선가능할 듯
    location_list=deque([i for i in range(len(priorities))])

    cnt=0

    while priorities:
        cnt+=1
        max_tmp=priorities.index(max(priorities))
        priorities.rotate(-max_tmp)
        location_list.rotate(-max_tmp)
        pr=priorities.popleft()
        lo=location_list.popleft()

        if lo==location:
            return cnt
            break