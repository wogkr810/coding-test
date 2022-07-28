N=int(input())
cnt1=0
cnt2=0

def fib_re(n):
    global cnt1
    if n==1 or n==2:
        cnt1+=1
        return 1
    else:
        return fib_re(n-1)+fib_re(n-2)

def fib_dp(n):
    global cnt2
    fib=[0]*(n+1)
    fib[0]=1
    fib[1]=1
    for i in range(2,n):
        cnt2+=1
        fib[i]=fib[i-1]+fib[i-2]
    return fib[n]

def count_re(n):
    fib_re(n)
    return cnt1

def count_dp(n):
    fib_dp(n)
    return cnt2

print(count_re(N))
print(count_dp(N))