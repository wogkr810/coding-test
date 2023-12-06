from collections import defaultdict

N = int(input())
stu_dict = defaultdict(list)
arr = []
for _ in range(N**2):
    tmp_input = list(map(int,input().split()))
    stu_dict[tmp_input[0]] = tmp_input[1:]
    arr.append(tmp_input)

dxy = [[-1,0], [0,-1], [0,1], [1,0]]
graph = [[0] * N for _ in range(N)]

for i in range(len(arr)):
    target = arr[i][0]
    hubo = [[0,0,a,0,0] for a in range(N**2)]
    
    
    for j in range(N):
        for k in range(N):
            hubo[j*N+k][3] = j
            hubo[j*N+k][4] = k
            for d in range(4):
                dx = j + dxy[d][0]
                dy = k + dxy[d][1]
                if (0 <= dx < N) and (0 <= dy < N):
                    if graph[dx][dy] in stu_dict[target]:
                        hubo[j*N+k][0] += 1
                    if graph[dx][dy] == 0:
                        hubo[j*N+k][1] += 1
    hubo.sort(key = lambda x : (-x[0], -x[1], x[3], x[4]))


    while hubo:
        now = hubo.pop(0)
        if not graph[now[3]][now[4]]:
            graph[now[3]][now[4]] = target
            break
                
ans = 0
score_dict = {0 : 0, 1 : 1, 2 : 10, 3: 100, 4 : 1000}

for i in range(N):
    for j in range(N):
        cnt = 0
        for d in range(4):
            dx = i + dxy[d][0]
            dy = j + dxy[d][1]
            if (0 <= dx < N) and (0 <= dy < N):
                if graph[dx][dy] in stu_dict[graph[i][j]]:
                    cnt += 1
        ans += score_dict[cnt]

print(ans)
    