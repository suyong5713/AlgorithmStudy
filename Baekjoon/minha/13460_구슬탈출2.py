from collections import deque

n, m = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

board = []

def move(i, j, dx, dy):
    c = 0
    while board[i + dx][j + dy] != "#" and board[i][j] != "O":
        i += dx
        j += dy
        c += 1
    return i, j, c

def bfs():
    while q:
        ri, rj, bi, bj, cnt = q.popleft()
        if cnt > 10:
            break
        for i in range(4):
            nri, nrj, rc = move(ri, rj, dx[i], dy[i])
            nbi, nbj, bc = move(bi, bj, dx[i], dy[i])
            if board[nbi][nbj] != "O":
                if board[nri][nrj] == "O":
                    print(cnt)
                    return
                if nri == nbi and nrj == nbj:
                    if rc > bc:
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]
                if ri == nri and rj == nrj and bi == nbi and bj == nbj:
                    continue
                q.append([nri, nrj, nbi, nbj, cnt + 1])
    print(-1)

for i in range(n):
    row = list(input())
    board.append(row)
    for j in range(m):
        if row[j] == "R":
            ri, rj = i, j
        if row[j] == "B":
            bi, bj = i, j
q = deque()
q.append([ri, rj, bi, bj, 1])
bfs()