def solution(n, s):
    hubo =[]
    if n > s :
        return [-1]
    else:
        while s > 0 :
            tmp = round(s/n)
            n = n-1
            if tmp < 2 :
                break
            s = s - tmp
            hubo.append(tmp)
    hubo.sort()
    return hubo