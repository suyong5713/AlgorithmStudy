from collections import deque

def bfs():
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x] - 1
        if x * 2 <= 100000 and not visited[x * 2]:
            queue.appendleft(x * 2)
            visited[x * 2] = visited[x]
        if x + 1 <= 100000 and not visited[x + 1]:
            queue.append(x + 1)
            visited[x + 1] = visited[x] + 1
        if 0 <= x - 1 and not visited[x - 1]:
            queue.append(x - 1)
            visited[x - 1] = visited[x] + 1


n, k = map(int, input().split())
visited = [0] * 100001
queue = deque()
queue.append(n)
visited[n] = 1
print(bfs())