from collections import deque
N, K = map(int,input().split())
max_location = 100_001
visited, location = [0] * max_location, [0] * max_location
# 수빈이 1, 동생 2
location[N],location[K] = 1, 2
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
        for i in [1, -1, current]:
            next = current + i
            if 0 <= next < max_location:
                # 방문한적 있는곳이어도 더 빨리 가는 방법이 있음. 최단시간 갱신
                if visited[next]:
                    # i == current -> 수빈이가 순간이동하는 경우. 시간 변화 x
                    if i == current:
                        visited[next] = min(visited[next], visited[current])
                    # 수빈이가 양옆으로 한칸 이동하는 경우. 시간 +1
                    else: visited[next] = min(visited[next], visited[current] + 1)
                # 방문한적 없는 곳
                else:
                    if i != current:
                        visited[next] = visited[current] + 1
                    else:
                        visited[next] = visited[current]
                    queue.append(next)