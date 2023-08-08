from collections import deque

def solution(maps):
    dxy = [[1,0],[-1,0],[0,1],[0,-1]]

    maps = [list(mapp) for mapp in maps]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    not_x = []
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X':
                not_x.append([i,j])

    res = []
    for hubo_x, hubo_y in not_x:
        cnt = 0
        if visited[hubo_x][hubo_y]:
            continue
        visited[hubo_x][hubo_y] = True
        q = deque([[hubo_x, hubo_y]])
        cnt += int(maps[hubo_x][hubo_y])
        while q:
            x, y = q.popleft()
            for i in range(4):
                dx = x + dxy[i][0]
                dy = y + dxy[i][1]
                if (0 <= dx < len(maps)) and (0 <= dy < len(maps[0])):
                    if not visited[dx][dy] and maps[dx][dy] != 'X':
                        cnt += int(maps[dx][dy])
                        visited[dx][dy] = True
                        q.append([dx,dy])
        res.append(cnt)

    if res:
        return sorted(res)
    else:
        return [-1]