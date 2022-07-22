import sys

def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

T=int(sys.stdin.readline().rstrip())
for i in range(T):
    N=int(sys.stdin.readline().rstrip())
    a,b=N//2,N//2
    while True:
        if is_prime(a) and is_prime(b):
            print(a,b)
            break
        a-=1
        b+=1