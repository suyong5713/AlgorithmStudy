# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 모음사전 (Level. 2 / 완전탐색)
# 풀이시간 : 1시간

def solution(word):
    w = ['A', 'E', 'I', 'O', 'U']
    dictonary = ['A', 'E', 'I', 'O', 'U']

    before = ['A', 'E', 'I', 'O', 'U']
    temp = []

    for _ in range(2, 6):
        for i in before:
            for j in w:
                temp.append(i + j)

        dictonary.extend(temp)
        before = temp[:]
        temp = []

    dictonary.sort()

    for i, w in enumerate(dictonary):
        if w == word:
            # 사전의 인덱스를 1부터 시작하는 것에 따른 보정
            return i + 1

# ============================================================= #

def main(t, word, result):
    r = solution(word)
    print('#{}: {}, {}, {}, {}'.format(t + 1, result == r, word, result, r))

if __name__ == '__main__':
    word = ['AAAAE', 'AAAE', 'I', 'EIO']
    result = [6, 10, 1563, 1189]

    for t in range(4):
        main(t, word[t], result[t])
