def divide_conquer(x,y,N):
    if N == 1:
        return arr[x][y]
    else:
        divide_conquer_list = [
            divide_conquer(x,y,N//2),
            divide_conquer(x,y+N//2,N//2),
            divide_conquer(x+N//2,y,N//2),
            divide_conquer(x+N//2,y+N//2,N//2)
            ]
        divide_conquer_list.sort()
        return divide_conquer_list[1]

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

print(divide_conquer(0,0,N))