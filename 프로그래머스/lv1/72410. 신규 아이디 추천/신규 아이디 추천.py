import re

def solution(new_id):
    # 1단계 : 대문자 -> 소문자
    new_id = new_id.lower()

    # 2단계 : 알파벳 소문자, 숫자 , 뺴기 , 밑줄 ,마침표 제외한거 모두 제거
    new_id = re.sub(r'[^a-z\-\_\.\d]','',new_id)

    # 3단계 : 마침표(.)가 2번 이상 -> 하나의 마침표(.)로
    new_id = re.sub(r'[.]{2,}','.',new_id)

    # 4단계 : 마침표가 처음이나 끝에 위치 -> 제거
    new_id = new_id.strip('.')

    # 5단계 : 빈 문자열이라면 "a" 대입
    if len(new_id) == 0:
        new_id = 'a'

    # 6단계 : 길이가 16자 이상 -> 15개 문자까지만 / 제거 후 '.' 가 끝이라면, '.' 제거
    new_id = new_id[:15].rstrip('.')

    # 7단계: 길이가 2자 이하 -> new_id의 마지막 문자를 길이가 3이 될때까지 반복해서 끝에 붙이기
    while len(new_id)<3:
        new_id += new_id[-1]

    return new_id