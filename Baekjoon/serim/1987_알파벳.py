# def bfs():
#     global result
#     # set의 시간복잡도는 O(1), 큐는 O(N)
#     queue = {(0, 0, alphabets[0][0])}
#     while queue:
#         x, y, visited = queue.pop()
#         for dir in range(4):
#             nx = x + dx[dir]
#             ny = y + dy[dir]
#             if 0 <= nx < r and 0 <= ny < c and alphabets[nx][ny] not in visited:
#                 queue.add((nx, ny, visited + alphabets[nx][ny]))
#                 result = max(result, len(visited) + 1)
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# r, c = map(int, input().split())
# alphabets = [list(input()) for _ in range(r)]
# result = 1
# bfs()
# print(result)

# dfs 풀이 - 시간초과 (어떻게 최적화해야할까..!!)
def dfs(x, y, cnt):
    global result
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < r and 0 <= ny < c and alphabets[nx][ny] not in visited:
            visited.add(alphabets[nx][ny])
            dfs(nx, ny, cnt + 1)
            visited.remove(alphabets[nx][ny])
    else:
        result = max(result, cnt)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
r, c = map(int, input().split())
alphabets = [list(input()) for _ in range(r)]
visited = set()
result = 0
visited.add(alphabets[0][0])
dfs(0, 0, 1)
print(result)