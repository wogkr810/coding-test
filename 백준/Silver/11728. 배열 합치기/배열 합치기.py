N, M = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

print(*sorted((arr1 + arr2)))