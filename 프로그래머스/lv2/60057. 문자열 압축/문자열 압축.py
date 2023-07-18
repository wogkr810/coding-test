def solution(s):
    if len(s) == 1:
        return 1
    
    ans = int(1e9)

    for i in range(1,len(s)//2 +1):
        tmp = s[:i]
        cnt = 1
        res = ''
        for j in range(i,len(s),i):
            if s[j:j+i] == tmp:
                cnt += 1
            else:
                if cnt != 1:
                    res += str(cnt) + tmp
                else:
                    res += tmp            
                cnt = 1
                tmp = s[j:j+i]

        if cnt != 1:
            res += str(cnt) + tmp
        else:
            res += tmp

        ans = min(ans,len(res))

    return ans