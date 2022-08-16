from collections import deque
import sys

N=int(sys.stdin.readline())
arr=[]
hour_list=[]
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

arr.sort(key=lambda x : (x[1],x[0]))
arr=deque(arr)

cnt=0
end_time=0
while arr:
    tmp=arr.popleft()
    if tmp[0]>=end_time:
        cnt+=1
        end_time=tmp[1]

print(cnt)