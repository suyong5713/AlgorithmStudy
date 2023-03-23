def check(x):
    for i in range(x):
        if graph[x] == graph[i] or abs(graph[x] - graph[i]) == x - i:
            return False
    return True


def dfs(row):
    global result
    # 모든 행에 퀸을 놓았으면 결과 +1
    if row == n:
        result += 1
    else:
        for i in range(n):
            graph[row] = i
            # 조건 부합시 다음 퀸을 놓음
            if check(row):
                dfs(row + 1)


n = int(input())
graph = [0] * n
result = 0
dfs(0)
print(result)