from collections import deque
N, M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
degree = [0] * (N+1)
for i in range(M):
    A, B = map(int,input().split())
    graph[A].append(B)
    degree[B] += 1
queue = deque()
for i in range(1, N+1):
    if degree[i] == 0:
        queue.append(i)
answer = []
while queue:
    student = queue.popleft()
    answer.append(student)
    for i in graph[student]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)
print(*answer)

