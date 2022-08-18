def solution(m, n, board):
    ans=board
    def is_four(arr,x,y,char):
        if 0<=x<len(arr)-1 and 0<=y<len(arr[0])-1:
            if char!=0:
                if arr[x+1][y]==char and arr[x][y+1]==char and arr[x+1][y+1]==char:
                    return True
                else:
                    return False

    def make_minus(hubo,arr):
        for i in hubo:
            x,y=i[0],i[1]
            arr[x][y]=-1
            arr[x+1][y]=-1
            arr[x][y+1]=-1
            arr[x+1][y+1]=-1

    def is_minus(arr):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j]==-1:
                    return False
        else:
            return True

    def arr_count(arr):
        zero_count=0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j]==0:
                    zero_count+=1
        return zero_count
    #ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

    for i in range(len(ans)):
        ans[i]=list(ans[i])

    def mat_trans(A):
        row=len(A)
        col=len(A[0])    

        B = [[0 for row in range(row)]for col in range(col)]

        for i in range(row):
            for j in range(col):
                B[j][i]=A[i][j]
        return B

    def rotate_2d(list_2d):
        n = len(list_2d) # 행 길이 계산
        m = len(list_2d[0]) # 열 길이 계산
        new = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new[j][n-i-1] = list_2d[i][j]
        return new

    ans=rotate_2d(ans)

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    n=len(ans)
    m=len(ans[0])

    res=n*m
    while res>0:
        res-=1
        hubo=[]
        for i in range(len(ans)):
            for j in range(len(ans[0])):
                if is_four(ans,i,j,ans[i][j]):
                    hubo.append([i,j])

        make_minus(hubo,ans)

        ttrs=[]
        for i in range(len(ans)):
            que=[]
            cnt=0
            for j in range(len(ans[0])):
                if ans[i][j]!=-1:
                    que.append(ans[i][j])
                else:
                    cnt+=1
            que.extend([0]*cnt)
            ttrs.append(que)

        ans=ttrs.copy()

    return arr_count(ans)

