TC = int(input())

for t in range(TC):
    N, M, W = map(int, input().split())

    edges = []

    for _ in range(M):
        s, d, w = map(int, input().split())
        edges.append((s, d, w))
        edges.append((d, s, w))

    for _ in range(W):
        s, d, w = map(int, input().split())
        edges.append((s, d, -w))

    dist = [1e9] * (N + 1)
    dist[1] = 0
    flag = False

    for i in range(N):
        for start, end, weight in edges:
            if dist[end] > dist[start] + weight:
                if i == N - 1:
                    flag = True
                dist[end] = dist[start] + weight

    if flag:
        print("YES")
    else:
        print("NO")