from collections import deque

def move(curPos):
    return [curPos - 1, curPos + 1, curPos * 2]

N, K = map(int, input().split())

q = deque()
q.append(N)
visited = [0] * 100001

while q:
    p = q.popleft()
    if p == K:
        print(visited[p])
        exit()
    else:
        for np in move(p):
            if 0 <= np < 100001 and not visited[np]:
                if np == p * 2 and np != 0:
                    visited[np] = visited[p]
                    q.appendleft(np)
                else:
                    visited[np] = visited[p] + 1
                    q.append(np)