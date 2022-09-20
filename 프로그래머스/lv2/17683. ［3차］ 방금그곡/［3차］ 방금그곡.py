from itertools import cycle

def changecode(music_): 
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')    
    return music_

def solution(m, musicinfos):
    music_dict = dict()
    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(',')
        dt = ((int(musicinfos[i][1][:2]) * 60 + int(musicinfos[i][1][3:])) - ((int(musicinfos[i][0][:2]) * 60 + int(musicinfos[i][0][3:]))))

        cycle_list = []
        cnt = 0
        for _ in cycle(list(musicinfos[i][3])):
            cycle_list.append(_)
            cnt +=1
            if cnt == dt:
                break

        cycle_list = changecode(''.join(cycle_list))

        music_dict[musicinfos[i][2]] = cycle_list

    m = changecode(m)

    for key,value in music_dict.items():
        if m in value:
            return key

    else:
        return "(None)"