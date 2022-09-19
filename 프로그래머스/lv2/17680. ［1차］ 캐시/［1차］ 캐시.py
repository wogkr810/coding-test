def solution(cacheSize, cities):
    cities.reverse()
    cities = list(map(lambda x : x.lower(), cities))
    arr = []
    cnt = 0
    while cities:
        tmp = cities.pop()
        if tmp not in arr:
            arr.append(tmp)
            cnt += 5
            if len(arr) == (cacheSize + 1):
                arr.pop(0)
        else:
            del arr[arr.index(tmp)]
            arr.append(tmp)
            cnt += 1
            
    return cnt