# x 행에 n이 있는지 확인
def rowCheck(row, n):
    if n in board[row]:
        return False
    return True


# y 열에 n이 있는지 확인
def colCheck(col, n):
    for i in range(9):
        if n == board[i][col]:
            return False
    return True


# x, y 좌표가 포함되어 있는 3x3 크기의 사각형에 n이 있는지 확인
def rectCheck(row, col, n):
    # 5 // 3 = 1, 1 * 3 = 3, [3,4,5]
    row = row // 3 * 3
    col = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == board[row + i][col + j]:
                return False
    return True


def dfs(count):
    global solved
    # 빈칸 개수만큼 채웠으면 stop
    if count == len(blank):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end='')
            print()
            solved = True
        return
    for i in range(1, 10):
        row = blank[count][0]
        col = blank[count][1]
        if rowCheck(row, i) and colCheck(col, i) and rectCheck(row, col, i):
            if solved: break
            board[row][col] = i
            dfs(count + 1)
            board[row][col] = 0


board = [list(map(int, input())) for _ in range(9)]
blank = []
solved = False
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append([i, j])
dfs(0)
