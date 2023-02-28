import itertools
from collections import deque


def BFS(comb):
    queue = deque()
    queue.extend(comb)
    visited = [[-1] * N for _ in range(N)]
    for target in queue:
        row, col = target
        visited[row][col] = 0
    while queue:
        r, c = queue.popleft()
        for dir in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            n_row, n_col = r + dir[0], c + dir[1]
            if 0 <= n_row < N and 0 <= n_col < N and visited[n_row][n_col] == -1 and lab[n_row][n_col] != 1:
                visited[n_row][n_col] = visited[r][c] + 1
                queue.append([n_row, n_col])
    not_visited_count = 0
    for i, j in virus:
        if [i,j] not in comb:
            visited[i][j] = 0
    for v in visited:
        not_visited_count += v.count(-1)
    if wall_count != not_visited_count:
        return float('inf')
    return max(map(max,visited))


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus = []
wall_count = 0
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append([i, j])
        elif lab[i][j] == 1:
            wall_count += 1
result_list = []
for comb in itertools.combinations(virus, M):
    queue = deque()
    queue.extend(comb)
    result_list.append(BFS(queue))
if min(result_list) == float('inf'):
    print(-1)
else:
    print(min(result_list))
