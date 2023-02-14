def solution(dirs):
    visited = set()
    cnt = 0
    x, y = 0, 0

    for dirr in dirs:
        tmp_x, tmp_y = x, y
        if dirr == "U":
            if y < 5:
                y += 1
        elif dirr == "L":
            if -5 < x:
                x -= 1
        elif dirr == "R":
            if x < 5:
                x += 1
        elif dirr == "D":
            if -5 < y:
                y -= 1
        path = (tmp_x,tmp_y,x,y)
        reverse_path = (x,y,tmp_x,tmp_y)
        if path not in visited and (tmp_x,tmp_y) != (x,y):
            cnt += 1
            visited.add(path)
            visited.add(reverse_path)
    return cnt