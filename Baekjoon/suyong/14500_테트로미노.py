def dfs(r, c, depth, total):
    global result
    #현재 상태에서 나머지 블럭들이 모두 최대값이라고 가정했을때에도
    #result보다 작다면 return
    if result >= total + max_val * (4 - depth):
        return
    if depth == 4:
        result = max(result, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                #블럭을 두개 골랐을 때
                if depth == 2:
                    #ㅗ 모양을 만들기 위해 nr,nc가 아닌 r,c에서 다시 dfs
                    visited[nr][nc] = True
                    dfs(r, c, depth + 1, total + arr[nr][nc])
                    visited[nr][nc] = False
                visited[nr][nc] = True
                dfs(nr, nc, depth + 1, total + arr[nr][nc])
                visited[nr][nc] = False
#세로 N 가로 M 입력
N, M = map(int, input().split())
#칸에 놓여진 수 입력
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [([False] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
result = 0
#최대 값
max_val = max(map(max, arr))

for row in range(N):
    for col in range(M):
        visited[row][col] = True
        dfs(row, col, 1, arr[row][col])
        visited[row][col] = False

print(result)