N, K = map(int,input().split())

pascal = [[1],[1,1]]

for i in range(1,1000):
    tmp_list = []
    tmp_list.append(1)
    for j in range(i):
        tmp_list.append(pascal[i][j] + pascal[i][j+1])
    tmp_list.append(1)
    pascal.append(tmp_list)

print(pascal[N][K] % 10007)
        
