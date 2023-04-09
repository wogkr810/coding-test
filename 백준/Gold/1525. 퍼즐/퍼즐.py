from collections import deque, defaultdict

puzzle = ''
for i in range(3):
    puzzle += ''.join(list(map(str,input().split())))
            
visited_dict = {puzzle : 0}
dxy = [[1,0],[0,1],[-1,0],[0,-1]]
q = deque([puzzle])
ans = -1

while q:
    puzzle = q.popleft()
    cnt = visited_dict[puzzle]
    if puzzle == '123456780':
        ans = cnt
        break
    zero_idx = puzzle.find('0')
    for i in range(4):
        dx = zero_idx //3 + dxy[i][0]
        dy = zero_idx % 3 + dxy[i][1]
        if (0<=dx<3) and (0<=dy<3):
            dz = dy + 3 * dx
            puzzle_list = list(puzzle)
            puzzle_list[dz], puzzle_list[zero_idx] = puzzle_list[zero_idx],puzzle_list[dz]
            puzzle_list = ''.join(puzzle_list)
            if puzzle_list not in visited_dict:
                visited_dict[puzzle_list] = cnt + 1
                q.append(puzzle_list)
            

print(ans)

 
