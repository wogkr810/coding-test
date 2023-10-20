def solution(storey):
    cnt = 0
    start = 10
    
    if storey <= 9:
        if 0 <= storey <= 5:
            return storey
        else:
            return 11-storey
    
    while True:
        storey, q = divmod(storey,start)    
        if 0 <= q <5:
            cnt += q
        elif q == 5:
            if int(str(storey)[-1]) >= 5:
                storey += 1
            cnt += q
        else:
            cnt += (10-q)
            storey += 1

        if storey == 0:
            break
    return cnt