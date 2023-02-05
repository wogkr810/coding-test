N, K , P , X = map(int,input().split())

arr = [[0]* 10 for _ in range(10)]
arr[0] = [0,4,3,3,4,3,2,3,1,2]
arr[1] = [4,0,5,3,2,5,6,1,5,4]
arr[2] = [3,5,0,2,5,4,3,4,2,3]
arr[3] = [3,3,2,0,3,2,3,2,2,1]
arr[4] = [4,2,5,3,0,3,4,3,3,2]
arr[5] = [3,5,4,2,3,0,1,4,2,1]
arr[6] = [2,6,3,3,4,1,0,5,1,2]
arr[7] = [3,1,4,2,3,4,5,0,4,3]
arr[8] = [1,5,2,2,3,2,1,4,0,1]
arr[9] = [2,4,3,1,2,1,2,3,1,0]

X = str(X)
X = X.zfill(K) 

cnt = 0
for i in range(1,N+1):
    tmp_cnt = 0
    res = ''

    target = str(i).zfill(K)

    for j in range(len(target)):
        tmp_cnt += arr[int(str(X)[j])][int(target[j])]
        res += target[j]
        if tmp_cnt > P:
            continue

    if 1 <= tmp_cnt <= P:
        cnt += 1
        
print(cnt)
