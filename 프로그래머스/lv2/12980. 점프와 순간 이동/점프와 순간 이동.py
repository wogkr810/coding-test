def solution(n):
    cnt = 0
    while True:
        if n %2 == 0:
            n = n //2
        else:
            n -= 1
            cnt +=1
            
        if n == 0:
            break
    return cnt