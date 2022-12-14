def dfs(pos, tot):
    global answer

    if pos == 11:
        answer = max(answer, tot)
        return
    else:
        for idx in range(11):
            if ability[idx][pos] > 0 and not visited[idx]:
                visited[idx] = True
                dfs(pos + 1, tot + ability[idx][pos])
                visited[idx] = False

C = int(input())

for _ in range(C):
    ability = [list(map(int, input().split())) for _ in range(11)]
    visited = [False for _ in range(11)]

    answer = 0
    dfs(0, 0)

    print(answer)