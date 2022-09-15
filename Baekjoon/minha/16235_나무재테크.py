from collections import deque

# 봄 : (i, j)에 있는 나무들 탐색
# 나무가 존재하는 경우 순서대로 양분을 먹게함
# 먹을 수 있으면 땅에서 나이만큼 빼고, 나이는 1 증가
# 먹지 못하면 dead에 해당 나무 정보 넣고, tree에서는 빼기
def spring():
    for i in range(N):
        for j in range(N):
            p_tree = sorted(tree[i][j])
            if p_tree:
                for k in range(len(p_tree)):
                    if land[i][j] < p_tree[k]:
                        dead.append([i, j, tree[i][j].pop()])
                    else:
                        land[i][j] -= p_tree[k]
                        tree[i][j][k] += 1

# 여름 : 죽은 나무 리스트 돌면서 죽은 나무 나이 // 2만큼 땅에 더해주기
# 모두 더해준 다음엔 죽은 나무 정보 초기화
def summer():
    for dy, dx, da in dead:
        land[dy][dx] += (da // 2)

    dead.clear()

# 가을 : (i, j)에 있는 나무들 탐색
# 나무가 존재하는 경우 순서대로 나무의 나이가 5의 배수인지 확인
# 5의 배수인 경우 8방향에 대해 범위 내에 있으면 그 위치에 나이가 1인 나무 더해줌
def fall():
    for i in range(N):
        for j in range(N):
            p_tree = tree[i][j]
            if p_tree:
                for k in range(len(p_tree)):
                    if p_tree[k] % 5 == 0:
                        for d in range(8):
                            if 0 <= i + dy[d] < N and 0 <= j + dx[d] < N:
                                tree[i + dy[d]][j + dx[d]].appendleft(1)

# 겨울 : A[i][j]만큼 양분 더해줌
def winter():
    for i in range(N):
        for j in range(N):
            land[i][j] += A[i][j]

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# tree는 입력값인 y, x에 대해 (y-1, x-1)에 나이값을 저장
# 1을 빼는 이유는 문제에서 r과 c가 1부터 시작한다고 했기 때문
tree = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    y, x, z = map(int, input().split())
    tree[y - 1][x - 1].append(z)

land = [[5] * N for _ in range(N)]
dead = []
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

# K년동안 봄, 여름, 가을, 겨울 함수 실행
for i in range(K):
    spring()
    summer()
    fall()
    winter()

# 위의 함수 실행 후 tree의 모든 좌표 돌며 (i, j)의 나무의 갯수를 answer에 저장
answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])

print(answer)