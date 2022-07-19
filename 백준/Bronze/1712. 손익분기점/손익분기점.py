a, b, c =map(int,input().split())
try:
    res=a/(c-b)
    if res>0:
        print(int(res)+1)
    else:
        print(-1)
except ZeroDivisionError:
    print(-1)
