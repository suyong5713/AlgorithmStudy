from collections import deque

def find_max(node):
    q = deque()
    visited = [False] * (n + 1)

    q.append((node, 0))
    visited[node] = True
    m_weight = 0
    m_node = -1

    while q:
        node, weight = q.popleft()
        for n_node, n_weight in graph[node]:
            s_weight = weight + n_weight
            if not visited[n_node]:
                q.append((n_node, s_weight))
                visited[n_node] = True
                if m_weight < s_weight:
                    m_weight = s_weight
                    m_node = n_node

    return m_node, m_weight

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))

max_node, _ = find_max(1)
_, answer = find_max(max_node)

print(answer)