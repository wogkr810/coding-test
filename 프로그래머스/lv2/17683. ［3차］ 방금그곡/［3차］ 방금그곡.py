def changecode(music): 
    music = music.replace('C#', 'c')
    music = music.replace('D#', 'd')
    music = music.replace('F#', 'f')
    music = music.replace('G#', 'g')
    music = music.replace('A#', 'a')    
    return music

def cal_time(time1, time2):
    start = int(time1.split(":")[0]) * 60 + int(time1.split(":")[1])
    end = int(time2.split(":")[0]) * 60 + int(time2.split(":")[1])
    return (end-start)

def solution(m, musicinfos):
    m = changecode(m)

    music_dict = dict()
    for i in range(len(musicinfos)):
        start , end , title, melody = musicinfos[i].split(',')
        dt = cal_time(start, end)
        melody = changecode(melody)

        iteration, mod = divmod(dt, len(melody))

        melody_cycle = melody * iteration + melody[:mod]

        music_dict[title] = (melody_cycle, dt)
    
    hubo = []
    for key,value in music_dict.items():
        if m in value[0]:
            hubo.append([key,*value])

    hubo.sort(key = lambda x : x[2] ,reverse =True)

    if len(hubo) == 0:
        return "(None)"
    else:
        return hubo[0][0]
 