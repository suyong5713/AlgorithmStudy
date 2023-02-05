INF = int(1e9)

def solution():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        if graph[a][b] > c:
            graph[a][b] = c

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF:  # 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.
                print(0, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수
graph = [[INF] * (n+1) for _ in range(n+1)]
solution()