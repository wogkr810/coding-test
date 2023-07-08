from collections import defaultdict
import sys

T = int(input())
input = sys.stdin.readline

for cnt in range(T):
    N = int(input())
    rank = list(map(int,input().split()))
    M = int(input())
    swap = [list(map(int,input().split())) for _ in range(M)]


    indegree = defaultdict(int)               
    indegree_del = defaultdict(int)

    for i in range(len(rank)):
        indegree[rank[i]] = N-i        # i번째 원소가 팀 번호니
        indegree_del[rank[i]] = 0      # 원소 입력받을때 마다 하면 순위 겹치니 연산용 사전 만들기
                                  
    for hubo in swap: 
        a, b = hubo
        if indegree[a] > indegree[b]:  # 차이가 날테니 작은거 +1 큰거 -1
            indegree_del[a] -= 1
            indegree_del[b] += 1
        elif indegree[a] < indegree[b]:
            indegree_del[a] += 1
            indegree_del[b] -= 1
        else:
            continue                   # 사실 이부분은 indegree_del 만들고 나서는 필요 없음.

    for key,value in indegree_del.items():
        indegree[key] += value         # indegree_del부분 indegree에 다 하기
    
    # 차수 순서대로 정렬

    res = sorted(indegree.items(), key = lambda x : x[1], reverse = True)
    ans = []        # 답안 받아두기
    rk = 0          # indegree에서 순서 겹치는거 판별 용, 사실 그냥 set으로 한다음 순서 원래 길이랑 달라지면 IMPOSSIBLE해도 됨.
    ans_flag = 0    # "?" 출력했을 때 대비해서, 0,1,2 로 한다음 조건에 따라 값 출력하려고함. 사실 T, F 해도 상관 없음

    for a,b in res:
        if b != rk: # 순서는 다음원소로 계속 갱신 -> 달라야 값 넣기
            ans.append(a)
            rk = b
        else:
            ans_flag = 1 # 순서가 갱신되지않고 전꺼랑 같으면 순위 판별 불가 -> ans_flag 1로 하고 끝
            break

    if ans_flag == 0:
        print(*ans)
    else:
        print('IMPOSSIBLE')