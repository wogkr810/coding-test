T=int(input())
for i in range(T):
    Paren=input()
    ll=len(Paren)
    cnt=0
    while cnt<ll:
        cnt+=1       
        Paren=Paren.replace('()','')

    if len(Paren)==0:
        print('YES')
    else:
        print("NO")
                