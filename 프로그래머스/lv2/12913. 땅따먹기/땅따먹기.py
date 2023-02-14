def solution(land):
    for i in range(1,len(land)):
        tmp_list = sorted([[j,land[i-1][j]] for j in range(len(land[i-1]))], key = lambda x : x[1])
        tmp_max_idx = tmp_list[-1][0]
        for j in range(4):
            if j == tmp_max_idx:
                land[i][j] += tmp_list[-2][1]
            else:
                land[i][j] += tmp_list[-1][1]

    return max(land[-1])