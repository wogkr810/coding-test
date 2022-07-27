import sys

N = int(sys.stdin.readline())
arr=[]
for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

new_arr=[]
for i in range(len(arr)-1):
    new_arr.append(arr[i+1]-arr[i])
    
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

gcd_n=gcd(new_arr[0],new_arr[-1])

for i in range(len(new_arr)):
    gcd_n=gcd(gcd_n,new_arr[i])

def get_yaksu_not1_notn(n):
    yaksu_list=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            yaksu_list.append(i)
            yaksu_list.append(int(n/i))
    
    yaksu_list=list(set(yaksu_list))
    yaksu_list.sort()
    yaksu_list.pop(0)
    
    return yaksu_list

for i in get_yaksu_not1_notn(gcd_n):
    print(i,end=" ")