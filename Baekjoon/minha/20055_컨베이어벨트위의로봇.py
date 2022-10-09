def rotate(l):
    # [1, 2, 3, 4]인 경우 -> [4, 1, 2, 3]이 되도록 리스트 슬라이싱 후 합친 값 리턴
    return l[-1:] + l[:-1]

def move():
    # 끝칸부터 첫칸까지 반복
    for p in range(N - 1, -1, -1):
        # 끝칸인 경우 0으로 바꾸기
        if p == N - 1:
            robot[p] = 0
        # 끝칸이 아닌 경우
        else:
            # 현재 칸에 로봇이 있으며, 다음 칸에는 로봇이 없고, 다음 칸의 내구도가 0보다 크면
            if robot[p] != 0 and robot[p + 1] == 0 and A[p + 1] > 0:
                # 다음 칸에 현재 칸의 로봇 두고, 현재 칸은 비우고, 다음 칸의 내구도 1 감소
                robot[p + 1], robot[p] = robot[p], 0
                A[p + 1] -= 1

def lift():
    # 첫 칸의 내구도가 0보다 크면 로봇을 올리고 내구도 1 감소
    if A[0] > 0:
        robot[0] = 1
        A[0] -= 1

N, K = map(int, input().split())
A = list(map(int, input().split()))
robot = [0 for _ in range(N * 2)]
answer = 1

while True:
    # 컨베이어 벨트 회전
    A = rotate(A)
    # 로봇 회전하기 전 끝칸에 있는거 0으로 값 바꾸고, 로봇 회전
    robot[N - 1] = 0
    robot = rotate(robot)

    # 로봇 한칸씩 움직임
    move()
    # 로봇 올리기
    lift()

    # 내구도가 0인것 K개 이상이면 answer 출력 후 반복문 탈출
    if A.count(0) >= K:
        print(answer)
        break

    # 단계 증가
    answer += 1