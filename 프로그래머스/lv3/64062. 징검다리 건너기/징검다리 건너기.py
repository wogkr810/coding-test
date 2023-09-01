def solution(stones, k):
    left, right = 1, 2000000000

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            if (stone-mid) <= 0:
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:
                break

        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left