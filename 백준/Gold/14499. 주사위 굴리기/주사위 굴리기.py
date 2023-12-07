N, M, x, y, K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
com = list(map(int,input().split()))

d = [0] * 6
dxy = [[0,1], [0,-1], [-1,0],[1,0]]

for c in com:
    x += dxy[c-1][0]
    y += dxy[c-1][1]

    if (0 <= x < N) and (0 <= y < M):
        if c == 1:
            d[0], d[1], d[4], d[5] = d[5], d[4], d[0], d[1]
        elif c == 2:
            d[0], d[1], d[4], d[5] = d[4], d[5], d[1], d[0]
        elif c == 3:
            d[2], d[3], d[4], d[5] = d[4], d[5], d[3], d[2]
        elif c == 4:
            d[2], d[3], d[4], d[5] = d[5], d[4], d[2], d[3]

        if arr[x][y] == 0:
            arr[x][y] = d[5]
        else:
            d[5] = arr[x][y]
            arr[x][y] = 0
        print(d[4])
    else:
        x -= dxy[c-1][0]
        y -= dxy[c-1][1]

