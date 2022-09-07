from collections import defaultdict

def solution(id_list, report, k):
    report = list(set(report))
    reported = defaultdict(int)
    res = [0 for _ in range(len(id_list))]

    for rpt in report:
        reported[rpt.split()[1]] += 1

    for rpt in report:
        if reported[rpt.split()[1]] >= k:
            res[id_list.index(rpt.split()[0])] += 1

    return res