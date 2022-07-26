W, H, X, Y ,P = map(int,input().split())
cnt=0
for i in range(P):
    a, b = map(int,input().split())
    d1=((X+W-a)**2+(Y+H/2-b)**2)**0.5
    d2=((X-a)**2+(Y+H/2-b)**2)**0.5
    if (X<=a and a<=X+W) and (Y<=b and b<=Y+H):
        cnt+=1
    elif d1<=H/2:
        cnt+=1
    elif d2<=H/2:
        cnt+=1
print(cnt)