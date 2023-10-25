def dfs(air, path, ans, visited, tickets):
    if len(path) == len(tickets)+1:
        ans.append(path)
        return
    
    for idx, ticket in enumerate(tickets):
        if air == ticket[0] and visited[idx] == False:
            visited[idx] = True
            dfs(ticket[1], path+[ticket[1]], ans, visited, tickets)
            visited[idx] = False

def solution(tickets):
    ans = []   
    visited = [False] * len(tickets)


    dfs("ICN", ["ICN"], ans, visited,tickets)

    ans.sort()
    
    return ans[0]