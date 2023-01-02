def solution(n, words):
    ans = 0
    word_set = set()
    word_set.add(words[0])

    for i in range(1,len(words)):
        if words[i][0] != words[i-1][-1]:
            ans = i
            break

        if words[i] in word_set:
            ans = i
            break

        word_set.add(words[i])

    if ans == 0:
        return [0,0]
    else:
        return [divmod(ans,n)[1]+1,divmod(ans,n)[0]+1]