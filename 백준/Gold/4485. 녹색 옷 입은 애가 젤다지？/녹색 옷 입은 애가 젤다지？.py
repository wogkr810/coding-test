import heapq

cnt = 0
while True:
    cnt += 1
    N = int(input())
    if N == 0:
        break
    
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))

    inf_value = 1e9
    distance = [[inf_value] *N for _ in range(N)] 
    dxy = [[1,0],[-1,0],[0,1],[0,-1]]
    q = []
    distance[0][0] = 0
    heapq.heappush(q,(arr[0][0],[0,0]))

    while True:
        cost, [x,y] = heapq.heappop(q)
        if (x,y) == (N-1,N-1):
            break
        for i in range(4):
            dx = x + dxy[i][0]
            dy = y + dxy[i][1]
            if (0<=dx<N) and (0<=dy<N):
                new_cost = cost + arr[dx][dy]
                if distance[dx][dy] > new_cost:
                    distance[dx][dy] = new_cost
                    heapq.heappush(q,(new_cost,[dx,dy]))

    print(f"Problem {cnt}: {distance[N-1][N-1]}")
