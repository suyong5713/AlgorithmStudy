# 사전 리스트
dict = []


# dfs로 경우의 수 만들기 (부분집합)
def dfs(wd, c):
    # 길이가 5랑 같아질 시 종료
    if c == 5: return

    # 전체 모음에 대해서
    for s in ['A', 'E', 'I', 'O', 'U']:
        # 기존 받아온 단어에 모음을 하나 새로 추가함
        cwd = wd
        cwd += s
        # 새로운 사전 리스트에 추가
        dict.append(cwd)
        dfs(cwd, c + 1)


def solution(word):
    dfs('', 0)
    # 사전 정렬
    dict.sort()
    # 찾는 값을 인덱스로 탐색
    answer = dict.index(word) + 1
    return answer