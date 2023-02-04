def make_k_jinsu(n,k):
    res = ''
    while n>0:
        n, mod = divmod(n,k)
        res += str(mod)
    
    return res[::-1]

def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2,int(n**0.5) +1):
        if n % i == 0:
            return False
    
    return True

def solution(n, k):
    n = make_k_jinsu(n,k)
    res = n.split('0')
    cnt = 0
    for i in res:
        if i:
            if is_prime(int(i)):
                cnt += 1
            
    return cnt
        