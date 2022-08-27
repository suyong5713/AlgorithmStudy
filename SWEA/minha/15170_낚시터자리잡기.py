from itertools import permutations

def solve(depth, order, idx, dis, visited):
    global res

    pos = order[idx][0]
    num = order[idx][1]

    if depth == num:
        if idx == 2:
            res = min(res, dis)
            return
        else:
            solve(0, order, idx + 1, dis, visited)
    else:
        for i in range(N):
            if depth == num - 1:
                if pos - i >= 0:
                    if not visited[pos - i]:
                        visited[pos - i] = True
                        dis += (i + 1)
                        if dis < res:
                            solve(depth + 1, order, idx, dis, visited)
                        visited[pos - i] = False
                        dis -= (i + 1)
                if pos + i < N:
                    if not visited[pos + i]:
                        visited[pos + i] = True
                        dis += (i + 1)
                        if dis < res:
                            solve(depth + 1, order, idx, dis, visited)
                        visited[pos + i] = False
                        dis -= (i + 1)
                        break
            else:
                if pos - i >= 0:
                    if not visited[pos - i]:
                        visited[pos - i] = True
                        dis += (i + 1)
                        if dis < res:
                            solve(depth + 1, order, idx, dis, visited)
                        visited[pos - i] = False
                        dis -= (i + 1)
                        break
                if pos + i < N:
                    if not visited[pos + i]:
                        visited[pos + i] = True
                        dis += (i + 1)
                        if dis < res:
                            solve(depth + 1, order, idx, dis, visited)
                        visited[pos + i] = False
                        dis -= (i + 1)
                        break

T = int(input())

for tc in range(T):
    N = int(input())

    fisher = []
    for i in range(3):
        p, n = map(int, input().split())
        fisher.append((p - 1, n))

    order = list(permutations(fisher, 3))

    res = 1e9
    visited = [False] * N
    for o in order:
        solve(0, o, 0, 0, visited)

    print("#{} {}".format(tc + 1, res))