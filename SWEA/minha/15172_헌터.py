def permutation(arr):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        global perms
        if len(chosen) == len(arr):
            perms.append(chosen[:])
            return

        for i in range(len(arr)):
            if arr[i] > 0:
                if not used[i]:
                    chosen.append(arr[i])
                    used[i] = 1
                    generate(chosen, used)
                    used[i] = 0
                    chosen.pop()
            elif arr[i] < 0:
                if -arr[i] in chosen:
                    if not used[i]:
                        chosen.append(arr[i])
                        used[i] = 1
                        generate(chosen, used)
                        used[i] = 0
                        chosen.pop()
                else:
                    continue

    generate([], used)

def getTotal(order):
    global res
    d = 0

    d += abs(0 - pos[order[0]][0]) + abs(0 - pos[order[0]][1])
    for s in range(len(order) - 1):
        d += abs(pos[order[s]][0] - pos[order[s + 1]][0]) + abs(pos[order[s]][1] - pos[order[s + 1]][1])

        if s == len(order) - 2:
            res = min(res, d)
        else:
            if res < d:
                break

T = int(input())

for tc in range(T):
    perms = []
    pos = dict()
    res = 1e9

    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 몬스터, 클라이언트의 위치값 딕셔너리로 저장
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                pos[graph[i][j]] = [i, j]

    g = list(set(sum(graph, [])))
    g.remove(0)
    # 이동 가능한 경우(몬스터 n을 잡아야 클라이언트 n 방문 가능) 모두 구함
    permutation(g)

    # 위에서 구한 경우에 대해 이동 거리 구함
    for p in perms:
        getTotal(p)

    print("#{} {}".format(tc + 1, res))
