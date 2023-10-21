def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parents(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, costs):
    costs.sort(key = lambda x : x[2])
    parents = [i for i in range(n+1)]
    ans = 0
    
    for cost in costs:
        a, b, c = cost
        if find_parents(parents, a) != find_parents(parents, b):
            union_parents(parents, a, b)
            ans += c
    
    return ans