import math

def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True 

N=int(input())
hubo_list=list(map(int,input().split()))
count=0
for i in range(N):
    if is_prime(hubo_list[i]):
        count+=1

print(count)