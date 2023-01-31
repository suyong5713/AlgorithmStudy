n = int(input())
m = int(input())
cost = [[1e9] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a - 1][b - 1] = min(cost[a - 1][b - 1], c)


for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == k:
                cost[j][k] = 0
            else:
                cost[j][k] = min(cost[j][k], cost[j][i] + cost[i][k])

for r in range(n):
    for c in range(n):
        if cost[r][c] == 1e9:
            print(0, end=' ')
        else:
            print(cost[r][c], end=' ')
    print()