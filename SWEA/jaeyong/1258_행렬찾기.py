# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18LoAqItcCFAZN
# SWEA1258 행렬찾기

tc = int(input())
n = 0
data = []
visited = []

def get_square(i, j):
    h = i
    w = j

    # 세로 너비 탐색
    while True:
        if h >= n:
            break
        else:
            if data[h][j] == 0:
                break
        h += 1

    # 가로 너비 탐색
    while True:
        if w >= n:
            break
        else:
            if data[i][w] == 0:
                break
        w += 1

    return (h - i, w - j)   # 튜플 형태로 세로 및 가로길이 반환

def set_visited(i, j, size):
    for h in range(i, i + size[0]):
        for w in range(j, j + size[1]):
            visited[h][w] = True

def result_sort(size):
    # 우선순위 : 넓이, 행 길이
    return size[0] * size[1], size[0]

for t in range(tc):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for j in range(n)] for i in range(n)]

    result = []

    for i in range(n):
        for j in range(n):
            if data[i][j] == 0 or visited[i][j] == True:
                continue

            size = get_square(i, j)
            result.append(size)
            set_visited(i, j, size)
    
    # 데이터 정렬
    result.sort(key=result_sort)
    
    # 출력형식 변환
    output = ''
    for r in result:
        output += str(r[0]) + ' '
        output += str(r[1]) + ' '

    print('#{} {} {}'.format(t + 1, len(result), output))
