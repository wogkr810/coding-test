N=int(input())
arr= [list(map(int,input().split())) for _ in range(N)]

minus=0
zero=0
one=0

def nine(x,y,N):
    global minus, zero, one
    number=arr[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if arr[i][j]!=number:
                nine(x,y,N//3)
                nine(x,y+N//3,N//3)
                nine(x,y+2*N//3,N//3)
                nine(x+N//3,y,N//3)
                nine(x+N//3,y+N//3,N//3)
                nine(x+N//3,y+2*N//3,N//3)
                nine(x+2*N//3,y,N//3)
                nine(x+2*N//3,y+N//3,N//3)
                nine(x+2*N//3,y+2*N//3,N//3)
                return

    if number==-1:
        minus+=1
    elif number==0:
        zero+=1
    elif number==1:
        one+=1

nine(0,0,N)

print(minus)
print(zero)
print(one)