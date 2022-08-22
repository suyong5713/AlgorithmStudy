import copy
import sys
sys.stdin = open("input.txt", "r")

def check(graph, dir, x, y):
    for d in dir:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 6:
                break
            elif graph[nx][ny] == 0:
                graph[nx][ny] = 7

def dfs(depth, graph):
    global result
    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += graph[i].count(0)
        result = min(result, cnt)
        return
    graph_copy = copy.deepcopy(graph)
    cctv_num, x, y = cctv[depth]
    for i in direction[cctv_num]:
        check(graph_copy, i, x, y)
        dfs(depth + 1, graph_copy)
        graph_copy = copy.deepcopy(graph)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [0, 3]],
             [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]], [[0, 1, 2, 3]]]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if graph[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([graph[i][j], i, j])
result = 1e9
dfs(0, graph)
print(result)