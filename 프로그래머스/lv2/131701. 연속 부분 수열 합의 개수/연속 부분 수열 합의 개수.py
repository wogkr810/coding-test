def solution(elements):
    sum_list = sum(elements)
    len_list = len(elements)
    elements *= 2
    res = set()
    res.add(sum_list)

    for i in range(len_list):
        for j in range(1,len_list):
            res.add(sum(elements[i:i+j]))

    return len(res)