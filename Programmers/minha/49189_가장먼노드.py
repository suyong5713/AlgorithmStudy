from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    q = deque()
    visited = [0] * (n + 1)

    q.append(1)
    visited[1] = 1

    while q:
        cn = q.popleft()
        cd = visited[cn]
        for nn in graph[cn]:
            if not visited[nn]:
                visited[nn] = cd + 1
                q.append(nn)

    return visited.count(max(visited))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))