SIZE = 9

def checkRow(_y, _num):
    for x in range(9):
        if arr_sudoku[_y][x] == _num:
            return False
    return True

def checkCol(_x, _num):
    for y in range(9):
        if arr_sudoku[y][_x] == _num:
            return False
    return True

def checkSquare(_y, _x, _num):
    ny, nx = (_y//3)*3, (_x//3)*3
    for y in range(ny, ny+3):
        for x in range(nx, nx+3):
            if arr_sudoku[y][x] == _num:
                return False
    return True

def dfs(depth):
    if depth == len(arr_zero):
        for row in range(SIZE):
            for col in range(SIZE):
                print(arr_sudoku[row][col], end="")
            print()
        exit()
    x, y = arr_zero[depth]
    for num in range(1, 10):
        if checkRow(y, num) and checkCol(x, num) and checkSquare(y, x, num):
            arr_sudoku[y][x] = num
            dfs(depth + 1)
            arr_sudoku[y][x] = 0


arr_sudoku = []
arr_zero = []
for row_i in range(SIZE):
    arr_sudoku.append(list(map(int, input())))
    for col_i in range(SIZE):
        if not arr_sudoku[row_i][col_i]:
            arr_zero.append((col_i, row_i))
dfs(0)