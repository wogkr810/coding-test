def solution(N, left, right):
    p, q = divmod(left,N)
    a, b = divmod(right,N)
    arr = []
    for i in range(p+1,a+2):
        arr.extend([i]*i + [j for j in range(i+1,N+1)])

    cnt = N-b-1
    while cnt:
        cnt -= 1
        arr.pop()

    return arr[q:]


    # return arr[left:right+1]