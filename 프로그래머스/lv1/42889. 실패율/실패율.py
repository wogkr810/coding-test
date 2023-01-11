from collections import defaultdict

def solution(N, stages):
    fail_dict = defaultdict(int)
    
    for i in range(1,N+1):
        chall = 0
        fail = 0
        for stage in stages:
            if stage >= i:
                chall += 1
            if stage == i:
                fail += 1
        
        if chall == 0:
            fail_dict[i] = 0
        else:
            fail_dict[i] = fail / chall
            
    fail_dict = sorted(fail_dict.items(), key = lambda x : (x[1],-x[0]),reverse = True)
    return [i[0] for i in fail_dict]

    
    return res