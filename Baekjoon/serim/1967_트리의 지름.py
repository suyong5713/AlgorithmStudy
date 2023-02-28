def dfs(child, weight):
    global result
    left, right = 0, 0
    for c, w in graph[child]:
        temp = dfs(c, w)
        if left <= right:
            left = max(left, temp)
        else:
            right = max(right, temp)
    result = max(result, left + right)
    return max(left + weight, right + weight)


n = int(input())
result = 0
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
dfs(1, 0)
print(result)