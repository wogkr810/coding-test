from collections import defaultdict

def solution(genres, plays):
    total_list = [[idx,(play,genre)] for idx,(play,genre) in enumerate(zip(plays,genres))]
    total_list.sort(reverse=True, key =lambda x : (x[1][0]))
    playlist = defaultdict(list)

    for genre in set(genres):
        playlist[genre] = [0,[]]

    for play in total_list:
        playlist[play[1][1]][0] += play[1][0]
        playlist[play[1][1]][1].append([play[0],play[1][0]])

    playlist = sorted(playlist.items(),key= lambda x : x[1], reverse=True)
    res = []

    for play in playlist:
        cnt = 2
        for _ in play[1][1]:
            res.append(_[0])
            cnt -=1
            if cnt==0:
                break

    return res