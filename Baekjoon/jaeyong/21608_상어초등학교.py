# https://www.acmicpc.net/problem/21608
# 상어 초등학교

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n = int(input())
data = [[0] * n for _ in range(n)]

students = [list(map(int, input().split())) for _ in range(n ** 2)]

# 학생 수만큼 반복
# 학생수 : n^2
for o in range(n ** 2):
    student = students[o]

    # tmp 리스트에 가능한 자리를 모두 담은 뒤 정렬 후 자리에 앉힌다
    tmp = []
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                like = 0
                blank = 0

                for d in range(4):
                    y = i + dy[d]
                    x = j + dx[d]

                    if 0 <= y < n and 0 <= x < n:
                        if data[y][x] in student[1:]:
                            like += 1
                        if data[y][x] == 0:
                            blank += 1
                
                tmp.append([like, blank, i, j])

    # like, blank는 크면서 , 행과 열은 작은 순서대로 정렬
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))

    # 정렬 후 제일 앞에 있는 리스트에 있는 행, 열 번호에 학생을 자리에 앉힌다
    data[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
students.sort()

for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            y = i + dy[d]
            x = j + dx[d]
            if 0 <= y < n and 0 <= x < n:
                if data[y][x] in students[data[i][j] - 1]:
                    ans += 1

        if ans != 0:
            result += 10 ** (ans - 1)

print(result)
