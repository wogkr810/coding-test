N=int(input())
arr=[]
int_list=[]
for i in range(N):
    arr.append(input().split())

for i in range(N):
    if arr[i][0]=='push':
        int_list.append(int(arr[i][1]))
    elif arr[i][0]=='pop':
        if len(int_list)==0:
            print(-1)
        else:
            print(int_list.pop(-1))
    elif arr[i][0]=='size':
        print(len(int_list))
    elif arr[i][0]=='empty':
        if len(int_list)==0:
            print(1)
        else:
            print(0)
    elif arr[i][0]=='top':
        if len(int_list)==0:
            print(-1)
        else:
            print(int_list[-1])