from collections import Counter

arr1=[]
arr2=[]
for i in range(3):
    a,b=map(int,input().split())
    arr1.append(a)
    arr2.append(b)

print(Counter(arr1).most_common()[1][0],end=" ")
print(Counter(arr2).most_common()[1][0])