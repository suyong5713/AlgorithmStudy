from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def cw(l): # [1, 2, 3, 4]인 경우 -> [4, 1, 2, 3]이 되도록 리스트 슬라이싱 후 합친 값 리턴
    return l[-1:] + l[:-1]

def ccw(l): # [1, 2, 3, 4]인 경우 -> [2, 3, 4, 1]이 되도록 리스트 슬라이싱 후 합친 값 리턴
    return l[1:] + l[:1]

def rotate(x, d, k):
    # 돌려야하는 원판의 리스트를 가지고 와서 횟수만큼 시계방향이나 반시계방향으로 회전
    target = nums[x]
    if d == 0:
        for _ in range(k):
            target = cw(target)
    else:
        for _ in range(k):
            target = ccw(target)

    # 회전을 마쳤다면 해당 원판 바꿔줌
    nums[x] = target

def find_adj(ty, tx, tn):
    # bfs를 돌기 위한 q와 인접한 곳 위치 넣을 target_list
    q = deque()
    target_list = []

    q.append((ty, tx))
    target_list.append((ty, tx))
    visited[ty][tx] = True

    while q:
        py, px = q.popleft()
        for i in range(4):
            ny = py + dy[i]
            nx = px + dx[i]

            # 끝과 끝은 인접 -> 다음 x 좌표가 -1인 경우 이를 M-1로, M인 경우 이를 0으로 바꿔주기
            if nx == -1:
                nx = M - 1
            elif nx == M:
                nx = 0

            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and nums[ny][nx] == tn:
                    q.append((ny, nx))
                    target_list.append((ny, nx))
                    visited[ny][nx] = True

    # 인접한 곳이 1개보다 많으면 인접 리스트 반환, 1개 이하면 빈 리스트 반환
    if len(target_list) > 1:
        return target_list
    else:
        return []

def change():
    cnt = 0
    total = 0
    target_list = []
    # 원판 돌면서 0보다 큰 수가 있다면 카운트 증가, 총합 증가, 해당 좌표 리스트에 추가
    for y in range(N):
        for x in range(M):
            if nums[y][x] > 0:
                cnt += 1
                total += nums[y][x]
                target_list.append((y, x))

    # 카운트가 0보다 크면 평균 구해서 해당 좌표 리스트를 돌며 값 변경
    if cnt > 0:
        avg = total / cnt
        for ty, tx in target_list:
            if 0 < nums[ty][tx] < avg:
                nums[ty][tx] += 1
            elif nums[ty][tx] > avg:
                nums[ty][tx] -= 1

N, M, T = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
orders = [list(map(int, input().split())) for _ in range(T)]

# 순서대로 실행
for ox, od, ok in orders:
    # x의 배수인 원판 구하기
    multiX = []
    for n in range(1, N + 1):
        if n % ox == 0:
            multiX.append(n)

    # x의 배수인 원판 각각에 대해 인덱스 1 감소하고(리스트 인덱스 0부터여서), 회전시키는 함수 실행
    for mx in multiX:
        mx -= 1
        rotate(mx, od, ok)

    # 인접한 숫자 구하기 위한 visited 리스트와 인접한 수가 있을 때와 없을 때를 나눠서 실행시키기 위해 인접한 숫자의 위치를 넣는 zeros
    visited = [[False] * M for _ in range(N)]
    zeros = []
    # 원판의 숫자 하나씩 확인하면서 0이 아니고 확인하지 않은 곳이라면 find_adj 실행 후 인접한 숫자가 있는 위치들 zeros에 넣음
    for y in range(N):
        for x in range(M):
            if nums[y][x] != 0 and not visited[y][x]:
                adj = find_adj(y, x, nums[y][x])
                for a in adj:
                    zeros.append(a)

    # 인접한 숫자가 1개 이상 있다면 0으로 바꿔주고, 아니면 평균 구해서 -1 또는 1하기 위해 change 함수 실행
    if len(zeros) > 0:
        for zy, zx in zeros:
            nums[zy][zx] = 0
    else:
        change()

# 모든 작업이 끝나면 원판 숫자가 저장된 2차원 리스트를 1차원 리스트로 합쳐서 리스트의 합을 출력
print(sum(sum(nums, [])))