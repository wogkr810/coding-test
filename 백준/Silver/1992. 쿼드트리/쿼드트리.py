N=int(input())
arr=[list(input()) for _ in range(N)]

def quad(x,y,N):
    color=arr[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if arr[i][j]!=color:
                print("(",end="")
                quad(x,y,N//2)
                quad(x,y+N//2,N//2)
                quad(x+N//2,y,N//2)
                quad(x+N//2,y+N//2,N//2)  
                print(")",end="") 
                return

    if color=='0':
        print(0,end="")
    else:
        print(1,end="")
    

quad(0,0,N)