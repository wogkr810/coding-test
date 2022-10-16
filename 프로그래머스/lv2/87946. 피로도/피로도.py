from itertools import permutations

def solution(k, dungeons):
    hubo = []

    for permutes in permutations(dungeons):
        k_copy = k
        cnt = 0
        for permute in permutes:
            min_piro , use_piro = permute
            if min_piro <= k_copy:
                cnt += 1
                k_copy -= use_piro

        hubo.append(cnt)

    return max(hubo)