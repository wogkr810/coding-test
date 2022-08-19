arr=[]
for _ in range(3):
    arr.append(list(map(int,input().split())))

#평행이동
x=arr[0][0]
y=arr[0][1]
for i in range(len(arr)):
    arr[i][0]-=x
    arr[i][1]-=y

# 일직선

# A원점 B X축 우측
if arr[1][1]==0 and arr[1][0]>0:
    if arr[2][1]>0:
        print(1)    #반시계
    elif arr[2][1]<0:
        print(-1)   #시계
    elif arr[2][1]==0:
        print(0)    #일직선

# A원점 B X축 좌측
elif arr[1][1]==0 and arr[1][0]<0:
    if arr[2][1]>0:
        print(-1)    #시계
    elif arr[2][1]<0:
        print(1)     #반시계
    elif arr[2][1]==0:
        print(0)     #일직선

# A원점 B y축 위
elif arr[1][0]==0 and arr[1][1]>0:
    if arr[2][0]>0:
        print(-1)    #시계
    elif arr[2][0]<0:
        print(1)     #반시계
    elif arr[2][0]==0:
        print(0)     #일직선

# A원점 B y축 위
elif arr[1][0]==0 and arr[1][1]<0:
    if arr[2][0]>0:
        print(1)    #반시계
    elif arr[2][0]<0:
        print(-1)     #시계
    elif arr[2][0]==0:
        print(0)     #일직선

# A원점 B 1사분면
elif arr[1][0]>0 and arr[1][1]>0:
    if arr[1][0]*arr[2][1]>arr[2][0]*arr[1][1]:  #반시계
        print(1)
    elif arr[1][0]*arr[2][1]<arr[2][0]*(arr[1][1]):
        print(-1)                                  #시계
    elif abs((arr[2][1]-arr[1][1])*(arr[1][0]-arr[0][0]))==abs((arr[1][1]-arr[0][1])*(arr[2][0]-arr[1][0])):
        print(0)                                   #일직선

# A원점 B 2사분면
elif arr[1][0]<0 and arr[1][1]>0:
    if arr[1][0]*arr[2][1]<arr[2][0]*arr[1][1]:  #시계
        print(-1)
    elif arr[1][0]*arr[2][1]>arr[2][0]*arr[1][1]:
        print(1)                                  #반시계
    elif abs((arr[2][1]-arr[1][1])*(arr[1][0]-arr[0][0]))==abs((arr[1][1]-arr[0][1])*(arr[2][0]-arr[1][0])):
        print(0)                                   #일직선

# A원점 B 3사분면
elif arr[1][0]<0 and arr[1][1]<0:
    if arr[1][0]*arr[2][1]<arr[2][0]*arr[1][1]:  #시계
        print(-1)
    elif arr[1][0]*arr[2][1]>arr[2][0]*arr[1][1]:
        print(1)                                  #반시계
    elif abs((arr[2][1]-arr[1][1])*(arr[1][0]-arr[0][0]))==abs((arr[1][1]-arr[0][1])*(arr[2][0]-arr[1][0])):
        print(0)                                   #일직선

# A원점 B 4사분면
elif arr[1][0]>0 and arr[1][1]<0:
    if arr[1][0]*arr[2][1]>arr[2][0]*arr[1][1]:  #반시계
        print(1)
    elif arr[1][0]*arr[2][1]<arr[2][0]*arr[1][1]:
        print(-1)                                  #시계
    elif abs((arr[2][1]-arr[1][1])*(arr[1][0]-arr[0][0]))==abs((arr[1][1]-arr[0][1])*(arr[2][0]-arr[1][0])):
        print(0)                                   #일직선