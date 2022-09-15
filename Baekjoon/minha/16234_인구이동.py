from collections import deque

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


# 인접한 나라 중 인구 이동이 가능한 나라의 group 번호를 업데이트하고 해당 나라의 좌표를 리턴
def find_group(fy, fx, group_idx):
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    q = deque()
    q.append((fy, fx))
    group_changed = [[fy, fx]]

    # bfs로 탐색하며 근처의 점들이 범위 내에 있고 차이가 L~R 안에 들면 반복해서 탐색
    # bfs를 위한 queue 외에 인구이동을 하는 나라를 리턴하기 위한 group_changed에도 좌표 넣음
    while q:
        cy, cx = q.popleft()
        group[fy][fx] = group_idx

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < N and 0 <= nx < N and group[ny][nx] == 0:
                if L <= abs(graph[cy][cx] - graph[ny][nx]) <= R:
                    group[ny][nx] = group_idx
                    q.append((ny, nx))
                    group_changed.append([ny, nx])

    return group_changed


answer = 0

# 인구 이동 발생 일마다 group의 번호를 지정하는 group과 idx를 초기화 시켜준다
while True:
    group = [[0] * N for _ in range(N)]
    is_update = False
    idx = 1

    # 모든 점에 대해 group이 0인 경우 find_group 함수로 인접한 나라 중 인구 이동이 가능한 나라의 group 번호를 업데이트해준다
    for y in range(N):
        for x in range(N):
            if group[y][x] == 0:
                changed = find_group(y, x, idx)
                idx += 1

                # (y, x)에서 인구 이동이 가능한 나라가 2개 이상이 되면 인구 이동을 실행 후 is_update True로 변경
                if len(changed) > 1:
                    tot = 0
                    cnt = len(changed)
                    for chy, chx in changed:
                        tot += graph[chy][chx]

                    population = tot // cnt
                    for chy, chx in changed:
                        graph[chy][chx] = population

                    is_update = True

    # 인구 이동이 실행되지 않았다면 반복문 탈출, 아닌 경우 answer에 1증가
    if not is_update:
        break
    answer += 1

print(answer)