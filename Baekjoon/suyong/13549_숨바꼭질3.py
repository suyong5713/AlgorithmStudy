from collections import deque
N, K = map(int,input().split())
max_location = 100_001
visited = [0] * max_location
# 수빈이 1, 동생 2
visited[N] = 1
queue = deque([N])
if N >= K:
    print(N - K)
else:
    while queue:
        current = queue.popleft()
        if K == current:
            print(visited[current] - 1)
            break
        for i in [current, 1, -1]:
            next = current + i
            if 0 <= next < max_location and not visited[next]:
                if i != current:
                    visited[next] = visited[current] + 1
                else:
                    visited[next] = visited[current]
                queue.append(next)