def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    def DFS(start):
        if visited[start]:
            return
        visited[start] = True
        for i in range(n):
            if not visited[i] and computers[start][i] ==1:
                DFS(i)
    
    for i in range(n):
        if not visited[i]:
            DFS(i)
            cnt += 1

    return cnt