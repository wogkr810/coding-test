N = int(input())
crane = sorted(list(map(int,input().split())), reverse= True)
M = int(input())
box = sorted(list(map(int,input().split())), reverse= True)

cnt = 0

if box[0] > crane[0]:
    print(-1)
else:
    while box:
        for i in range(len(crane)):
            for j in range(len(box)):
                if crane[i] >= box[j] :
                    del box[j]
                    break
        cnt += 1
        
    print(cnt)
