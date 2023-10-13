N = int(input())
arr = list(map(int,input().split()))

ans_flag = -1
ans_set = set()

if N == 1:
    print('A')

elif N == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print('A') 
else:
    for i in range(N-2):
        Q, W, E = arr[i], arr[i+1], arr[i+2]

        if W == Q:
            ans_flag = 0
            idx = i
            break

        if (W-E) % (Q-W) == 0:
            a = int((W-E) / (Q-W))
        else:
            a = (W-E) / (Q-W)

        if (W**2-E*Q)% (W-Q) == 0:
            b = int((W**2-E*Q)/(W-Q))
        else:
            b = (W**2-E*Q)/(W-Q)


        if isinstance(a,int) and isinstance(b,int):
            ans_set.add((a,b))
        else:
            ans_flag = 1
            break

    if ans_flag == 0:
        if set(arr[idx+2:]) == set([arr[idx]]):
            print(arr[idx])
        else:
            print('B')

    elif ans_flag == 1:
        print('B')
        
    else:
        if len(ans_set) == 1:
            a, b = ans_set.pop()
            print(E*a + b)
        else:
            print('B')