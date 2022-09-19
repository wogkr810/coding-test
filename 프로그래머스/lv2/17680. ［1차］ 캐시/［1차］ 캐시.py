def solution(cacheSize, cities):
    # deque를 사용하여 popleft 하려했으나, deque는 list처럼 index접근안됨
    cities.reverse()
    # 문제에서 대소문자 구분안한다고함 , TC 5번
    cities = list(map(lambda x : x.lower(), cities))
    # 넣고 더하기
    arr = []
    cnt = 0
    while cities:
        tmp = cities.pop()
        # 없으면 넣고 더하기, 캐시 사이즈 못넘으니 빼기
        if tmp not in arr:
            arr.append(tmp)
            cnt += 5
            if len(arr) == (cacheSize + 1):
                arr.pop(0)
        # 있으면 중간 인덱스 제거해야 하니, 우선 index로 찾고 del로 제거
        # remove도 가능하고, deque를 이용하여 인덱스 찾고 로테이션하고 popleft해도됨
        else:
            del arr[arr.index(tmp)]
            arr.append(tmp)
            cnt += 1
            
    return cnt