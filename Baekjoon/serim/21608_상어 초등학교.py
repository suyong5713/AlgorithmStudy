import sys
sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
students = [list(map(int, input().split())) for _ in range(n * n)]
# 자리를 넣을 배열
position = [[0] * n for _ in range(n)]
# 총 만족도
result = 0

# 전체 학생수만큼 반복
for order in range(n ** 2):
    student = students[order]
    # 가능한 모든 자리 배치를 저장할 배열
    temp = []
    for i in range(n):
        for j in range(n):
            # 한 칸에 한 명이므로 비어있어야 가능
            if position[i][j] == 0:
                like = 0    # 인접한 칸의 좋아하는 학생 수
                blank = 0   # 인접한 칸의 비어있는 칸의 수
                # 인접한 네 칸 검사
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 좋아하는 학생
                        if position[nx][ny] in student[1:]:
                            like += 1
                        # 비어있는 칸
                        if position[nx][ny] == 0:
                            blank += 1
                # 가능한 모든 경우의 수 저장
                temp.append([like, blank, i, j])
    # 좋아하는 학생 수, 비어있는 칸은 내림차순. 행, 열은 오름차순.
    temp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    position[temp[0][2]][temp[0][3]] = student[0]

# 인덱스로 좋아하는 학생을 뽑아오기 위해 정렬
students.sort()

# 만족도 총 합 구하기
for i in range(n):
    for j in range(n):
        like = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if position[nx][ny] in students[position[i][j] - 1]:
                    like += 1
        # 좋아하는 학생 수에 따라 거듭제곱
        if like != 0:
            result += 10 ** (like - 1)

print(result)
