from collections import deque

def topology():
    global ans
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        ans.append(node)

        for con in graph[node]:
            indegree[con] -= 1
            if indegree[con] == 0:
                q.append(con)

N, M = map(int, input().split())

indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

ans = []
topology()

for n in ans:
    print(n, end=' ')