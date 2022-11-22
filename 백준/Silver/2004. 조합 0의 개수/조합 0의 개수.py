n, m = map(int,input().split())

def two_five_count(n,k):
    cnt = 0
    while n!=0:
        cnt += n//k
        n = n//k
    return cnt

five_count = two_five_count(n,5)-two_five_count(m,5)-two_five_count(n-m,5)
two_count = two_five_count(n,2)-two_five_count(m,2)-two_five_count(n-m,2)
print(min(five_count,two_count))