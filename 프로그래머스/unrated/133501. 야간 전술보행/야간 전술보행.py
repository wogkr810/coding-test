from collections import deque,defaultdict

def solution(distance, scope, times):
    scope = [[idx,i] for idx,i in enumerate(scope)]
    scope.sort(key=lambda x : x[1][0])
    scope = deque(scope)
    time_dict = defaultdict(list)
    for i in range(len(times)):
        time_dict[i] = [0]*times[i][0] + [1]*times[i][1]


    flag = True
    ans = distance
    while scope:
        if not flag:
            break
        idx, [val1,val2] = scope.popleft()
        start = min(val1,val2)
        end = max(val1,val2)
        p,q = divmod(end,len(time_dict[idx]))
        check_schedule = p*time_dict[idx] + time_dict[idx][:q]
        for i in range(start-1,end):
            if check_schedule[i] ==0 :
                ans = i+1
                flag =False
                break

    return ans