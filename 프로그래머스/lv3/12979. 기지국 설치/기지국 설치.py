from collections import deque
import math

def solution(n, stations, w):
    stations = deque(stations)
    ans = 0
    s = 1

    while stations:
        tmp_station = stations.popleft()
        ans += max(math.ceil((tmp_station - s - w) / (2*w+1)) , 0)
        s = tmp_station + w + 1

    if n >= s:
        ans += max(math.ceil((n - s + 1) / (2*w+1)) , 0)

    return ans