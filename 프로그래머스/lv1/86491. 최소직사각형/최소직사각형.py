def solution(sizes):
    # sizes_max = max(map(max,sizes))
    # left_sort = sorted(sizes, reverse = True, key = lambda x : x[0])
    # right_sort = sorted(sizes, reverse = True, key = lambda x : x[1])
    
    
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            sizes[i].reverse()
    
    l,r = max(list(map(lambda x : x[0], sizes))), max(list(map(lambda x : x[1], sizes)))
    
    
    return l*r
    
    # 만약 왼쪽 오른쪽 max가 같다면?