T=int(input())
for i in range(T):
    H, W, N = map(int,input().split())
    room, floor = divmod(N,H)
    if floor==0:
        if room<10:
            print(str(H)+"0"+str(room))
        else:
            print(str(H)+str(room))
    else:
        if room<9:
            print(str(floor)+"0"+str(room+1))
        elif room==9:
            print(str(floor)+str(room+1))
        else:
            print(str(floor)+str(room+1))