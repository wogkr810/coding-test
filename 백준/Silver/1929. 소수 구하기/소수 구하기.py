def prime_sieve(n):
    sieve=[True]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i+i,n+1,i):
                sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]==True]

N, M = map(int,input().split())
sosu_list=list(set(prime_sieve(M))-set(prime_sieve(N-1)))
sosu_list.sort()

for i in range(len(sosu_list)):
    print(sosu_list[i])