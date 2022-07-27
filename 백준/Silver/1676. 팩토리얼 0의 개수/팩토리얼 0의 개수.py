import math

N=int(input())
N=str(math.factorial(N))[::-1]

cnt=0
for i in N:
    if i==str(0):
        cnt+=1
    else:
        break
    
print(cnt)