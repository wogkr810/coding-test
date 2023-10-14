n, l = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

check_arr = []

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(arr[j][i])
    check_arr.append(tmp)
    check_arr.append(arr[i])

ans = 0

def check(array):
    visited = [0] * n
    for i in range(n - 1):
        if array[i] != array[i + 1]:
            if abs(array[i] - array[i+1]) > 1 :
                return False
            else:
                if array[i] - array[i + 1] == 1:
                    if i+1+l > n:
                        return False
                    check = array[i + 1]
                    for j in range(i+1, i+1+l):
                        if visited[j] or array[j] != check:
                            return False
                        visited[j] = 1
                elif array[i] - array[i + 1] == -1:
                    if i - l < - 1:
                        return False
                    check = array[i]
                    for j in range(i, i-l, -1):
                        if visited[j] or array[j] != check:
                            return False
                        visited[j] = 1
    return True

for arrarr in check_arr:
    if check(arrarr):
        ans += 1
                
print(ans)