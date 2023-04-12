from collections import deque

def rotate(dir):
    if dir == 0: # 상
        g = list(map(list, zip(*graph)))
        return g
    elif dir == 1: # 하
        t = list(map(list, zip(*graph)))
        g = []
        for i in t:
            g.append(i[::-1])
        return g
    elif dir == 2: # 좌
        g = graph
        return g
    else: # 우
        g = []
        for i in graph:
            g.append(i[::-1])
        return g

def game(dir):
    res = []

    for g in graph:
        while 0 in g:
            g.remove(0)

        idx = 0
        g_res = deque()

        while True:
            if idx == len(g) - 1:
                g_res.append(g[idx])
                break
            elif idx > len(g) - 1:
                break
            else:
                if g[idx] == g[idx + 1]:
                    g_res.append(g[idx] * 2)
                    idx += 2
                elif g[idx] == 0:
                    idx += 1
                else:
                    g_res.append(g[idx])
                    idx += 1

        if dir == 1 or dir == 3:
            g_res.reverse()

        if len(g_res) < N:
            for _ in range(N - len(g_res)):
                if dir == 1 or dir == 3:
                    g_res.appendleft(0)
                elif dir == 0 or dir == 2:
                    g_res.append(0)

        res.append(g_res)
    return res

def re_rotate(dir):
    res = []
    if dir == 2 or dir == 3:
        for i in graph:
            tmp = []
            for j in i:
                tmp.append(j)
            res.append(tmp)
    else:
        for i in range(N):
            tmp = []
            for j in graph:
                tmp.append(j[i])
            res.append(tmp)

    return res


def dfs(cnt):
    global graph, ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, graph[i][j])
        return

    c_graph = [g[:] for g in graph]
    for i in range(4):
        graph = rotate(i)
        graph = game(i)
        graph = re_rotate(i)

        dfs(cnt + 1)
        graph = [g[:] for g in c_graph]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0
dfs(0)
print(ans)