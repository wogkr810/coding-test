def prime_sieve(n):
    sieve=[True]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            for j in range(i+i,n+1,i):
                sieve[j]=False
    return [i for i in range(2,n+1) if sieve[i]==True]

while True:
    N=int(input())
    if N==0:
        break
    print(len(set(prime_sieve(2*N))-set(prime_sieve(N))))