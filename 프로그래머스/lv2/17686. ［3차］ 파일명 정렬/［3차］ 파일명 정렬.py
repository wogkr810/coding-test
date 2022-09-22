import re
def solution(files):
    pattern = re.compile('\d+')
    for i in range(len(files)):
        int_index = re.search(pattern, files[i])
        files[i] = files[i][:int_index.start()] + "," + files[i][int_index.start() : int_index.end()] + "," + files[i][int_index.end():]
        files[i] = files[i].split(",")

    # HEAD, NUMBER 정렬
    files.sort(key = lambda x : (x[0].lower(),int(x[1])))

    for i in range(len(files)):
        files[i] = ''.join(files[i])
        
    return files