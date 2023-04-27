dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def solution(dirs):
    answer = 0
    visited = set()
    cy, cx = 0, 0

    for dir in dirs:
        if dir == "U":
            i = 0
        elif dir == "D":
            i = 1
        elif dir == "L":
            i = 2
        else:
            i = 3

        ny = cy + dy[i]
        nx = cx + dx[i]

        if -5 <= ny <= 5 and -5 <= nx <= 5:
            if (cy, cx, ny, nx) not in visited :
                visited.add((cy, cx, ny, nx))
                visited.add((ny, nx, cy, cx))
                answer += 1
            cy, cx = ny, nx

    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))