import math

def is_prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True    

M=int(input())
N=int(input())

sosu_list=[]
for i in range(M,N+1):
    if is_prime(i):
        sosu_list.append(i)

if len(sosu_list)==0:
    print(-1)
else:
    print(sum(sosu_list))
    print(min(sosu_list))