def solution(skill, skill_trees):
    res = 0
    for skill_tree in skill_trees:
        tmp_stack = ''
        tmp_flag = True
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill:
                tmp_stack += skill_tree[i]

        for j in range(len(tmp_stack)):
            if tmp_stack[j] != skill[j]:
                tmp_flag = False
                break

        if tmp_flag:
            res += 1

    return res