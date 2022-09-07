from collections import defaultdict

def solution(id_list, report, k):
    report = list(set(report))
    reported = defaultdict(int)
    res = [0 for _ in range(len(id_list))]
    k_report = []

    for rpt in report:
        reported[rpt.split()[1]] += 1

    for key, value in reported.items():
        if value >= k:
            k_report.append(key)

    for rpt in report:
        if rpt.split()[1] in k_report:
            res[id_list.index(rpt.split()[0])] += 1

    return res