N=int(input())
arr=list(map(int,input().split()))

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

def giyak(a,b):
    a,b=int(a/gcd(a,b)),int(b/gcd(a,b))
    print(str(a)+"/"+str(b))

T=arr.pop(0)
for i in range(len(arr)):
    giyak(T,arr[i])