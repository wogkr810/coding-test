def solution(m, n, board):
    # Transpose로도가능하지만, 전치행렬로 할경우 방향이 반대라 아래가 아닌 위로 쌓임 -> 구글링 코드 참고(https://blackon29.tistory.com/63)
    def rotate_2d(list_2d):
        n = len(list_2d) # 행 길이 계산
        m = len(list_2d[0]) # 열 길이 계산
        new = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                new[j][n-i-1] = list_2d[i][j]
        return new

    board=rotate_2d(board)

    # 좌표를 입력 받고, 좌표를 벗어나지않고 위아래대각선이 같으면 Boolean타입
    def is_four(arr,x,y,char):                            
        if 0<=x<len(arr)-1 and 0<=y<len(arr[0])-1:
            if char!=0:                                                                 #밑에서 -1 -> 0으로 치환하기 떄문에 char는 0이 아니어야함
                if arr[x+1][y]==char and arr[x][y+1]==char and arr[x+1][y+1]==char:
                    return True                                                         #여기서 -1로 바꿔버리면 겹치는부분해결 불가능
                else:
                    return False

    # 반복문을 돌며 hubo list와 비교하여, -1로 바꿔줌
    def make_minus(hubo,arr):                             
        for i in hubo:
            x,y=i[0],i[1]
            arr[x][y]=-1
            arr[x+1][y]=-1
            arr[x][y+1]=-1
            arr[x+1][y+1]=-1

    while True:
        hubo=[]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if is_four(board,i,j,board[i][j]):
                    hubo.append([i,j])
        
        
        if len(hubo)==0:                                             #처음에는 무지성 n*m했지만, hubo에 들어가지않으면 그냥 그만하면 됨.
            break

        make_minus(hubo,board)

        ttrs=[]                                                      #블록이 밑으로 내리는게 테트리스같아서..
        for i in range(len(board)):
            que=[]
            cnt=0
            for j in range(len(board[0])):
                if board[i][j]!=-1:                                    # -1이 아니면 리스트에 넣어주고
                    que.append(board[i][j])
                else:
                    cnt+=1
            que.extend([0]*cnt)                                      # count만큼 더해주면서 0*cnt로 extend해주기
            ttrs.append(que)

        board=ttrs.copy()
    
    res=0
    for i in board:
        res+=i.count(0)
    return res

