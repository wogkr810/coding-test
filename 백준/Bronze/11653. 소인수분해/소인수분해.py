def prime_sieve(n):
    sieve=[True]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i+i,n+1,i):
                sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]==True]

N=int(input())
sosu_list=prime_sieve(N)
soinsu_list=[]


while True:
    for i in range(len(sosu_list)):
        if N%sosu_list[i]==0:
            N/=sosu_list[i]
            soinsu_list.append(sosu_list[i])
    if N==1:
        break

soinsu_list.sort()
for i in range(len(soinsu_list)):
    print(soinsu_list[i])