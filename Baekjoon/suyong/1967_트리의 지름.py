N = int(input())
graph = [[] for _ in range(N + 1)]
# 무방향 그래프 생성
for i in range(N - 1):
    node1, node2, weight = map(int, input().split())
    graph[node1].append([node2, weight])
    graph[node2].append([node1, weight])

def dfs(start):
    global visited
    for next_node in graph[start]:
        if visited[next_node[0]] == 0:
            visited[next_node[0]] = visited[start] + next_node[1]
            dfs(next_node[0])
    return

visited = [0] * (N + 1)
visited[1] = 1
dfs(1)
node1 = visited.index(max(visited))

visited = [0] * (N + 1)
visited[node1] = 1
dfs(node1)
print(max(visited) - 1)
