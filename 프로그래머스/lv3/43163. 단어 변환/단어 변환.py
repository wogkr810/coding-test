def solution(begin, target, words):
    if target not in words:
        return 0

    visited_word = {i : False for i in words}
    len_solution = len(target) - 1
    res = []
    
    def dfs(start,cnt):
        if start == target:
            res.append(cnt)
            return
        visited_word[start] = True
        for word in words:
            tmp_cnt = 0
            if not visited_word[word]:
                for i in range(len(word)):
                    if start[i] == word[i]:
                        tmp_cnt += 1
                if tmp_cnt == len_solution:
                    dfs(word,cnt+1)
    dfs(begin,0)
    
    return 0 if not res else min(res)