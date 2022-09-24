from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(place, y, x):
    q = deque()
    visited = [[False] * 5 for _ in range(5)]

    # q에 (시작값 y, 시작값 x, 시작값 거리(0)) 넣기
    q.append((y, x, 0))

    while q:
        cy, cx, cd = q.popleft()
        visited[y][x] = True

        for i in range(4):
            # 다음 방향 지정, nd는 현재 거리에서 1 더한 값
            ny = cy + dy[i]
            nx = cx + dx[i]
            nd = cd + 1

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[ny][nx]:
                # 빈자리면 다음 방향 탐색
                if place[ny][nx] == "O":
                    q.append((ny, nx, nd))
                    visited[ny][nx] = True

                # 응시자가 있는 자리인데 거리가 2 이하이면 False 반환
                if place[ny][nx] == "P" and nd <= 2:
                    return False

    return True

def solution(places):
    answer = []

    # 대기실 1개씩 탐색
    for p in places:
        flag = True
        # 대기실의 모든 자리 탐색하며 응시자가 있는 자리면 bfs 수행
        # bfs 결과가 false이면 거리두기 지키지 않음 -> 반복문 탈출
        for y in range(5):
            for x in range(5):
                if p[y][x] == "P":
                    flag = bfs(p, y, x)
                    if not flag:
                        break
            # 이중 반복문 탈출 위해 한번 더 작성
            if not flag:
                break

        # 탐색 결과가 True이면 answer에 1, 아니면 0 담기
        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer

# tc1 -> result = [1, 0, 1, 1, 1]
# places = [
#     ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
#     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
#     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
# print(solution(places))