def dfs(row, col, color, position, visited):
    global field, broken
    #dfs 4방향 탐색을 1번이라도 수행했는지 판별.
    flag = False
    for d_row, d_col in [[1,0], [0,1], [-1,0], [0,-1]]:
        n_row, n_col = row + d_row, col + d_col
        if 0 <= n_row < 12 and 0 <= n_col < 6:
            # 색이 같고 탐색한적 없으면,
            if field[n_row][n_col] == color and not visited[n_row][n_col]:
                flag = True
                visited[n_row][n_col] = True
                # 삭제될 뿌요 위치 저장
                position.append([n_row,n_col])
                dfs(n_row, n_col, color, position, visited)
    # 연속된 뿌요가 4개 이상이면 제거
    if not flag and len(position) > 3:
        for i, j in position:
            field[i][j] = '.'
            broken = True
    return
def gravity():
    global field
    # 바닥에서 위로 탐색
    for i in range(11, -1, -1):
        for j in range(6):
            # 아래쪽이 빈공간이면
            if field[i][j] == '.':
                row = i - 1
                # 해당 빈공간보다 위쪽 영역에서 뿌요가 있는지 확인. 있으면 swap
                while row >= 0:
                    if field[row][j] != '.':
                        field[row][j], field[i][j] = field[i][j], field[row][j]
                        break
                    else: row -= 1

field = [list(input()) for _ in range(12)]
answer = 0
while True:
    # 연쇄작용이 일어났는지 판별
    broken = False
    visited = [[False] * 6 for _ in range(12)]
    for i in range(11, -1, -1):
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, field[i][j], [[i,j]], visited)
    # 연쇄작용이 한번도 일어나지 않으면 더 이상 필드 변화 없음.
    if not broken:
        break
    # 연쇄작용이 일어남.
    else:
        answer += 1
    # 모든 연쇄작용이 끝난 후 중력 작용
    gravity()
print(answer)