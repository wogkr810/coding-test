def solution(food):
    res = ''
    for i in range(1,len(food)):
        for j in range(food[i]//2):
            res += str(i)
    
    res += '0' + res[::-1]
    
    return res
    
    
    