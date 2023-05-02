# https://school.programmers.co.kr/learn/courses/30/lessons/49994
# 프로그래머스, 방문 길이 (Level. 2)

def solution(dirs):
    visited = set()

    answer = 0
    y = 5
    x = 5

    for d in dirs:
        if d == 'U':
            ny = y - 1
            nx = x
        elif d == 'D':
            ny = y + 1
            nx = x
        elif d == 'R':
            ny = y
            nx = x + 1
        elif d == 'L':
            ny = y
            nx = x - 1

        if 0 <= ny <= 10 and 0 <= nx <= 10:
            if (y, x, ny, nx) not in visited and (ny, nx, y, x) not in visited:
                visited.add((y, x, ny, nx))
                answer += 1

            y = ny
            x = nx
        
    return answer
