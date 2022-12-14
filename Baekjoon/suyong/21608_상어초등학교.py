d_row = [-1,1,0,0]
d_col = [0,0,-1,1]
satisfaction = [0,1,10,100,1000]
N = int(input())
student_info = [list(map(int,input().split())) for _ in range(N*N)]
layout = [[0] * N for _ in range(N)]
for row in student_info:
    #(행,열,좋아하는애,빈공간)
    score = [(float('inf'), float('inf'), 0, 0) for _ in range(N*N)]
    #빈 자리의 인접한 칸에 좋아하는애가 제일 많은 위치 찾기
    for i in range(N):
        for j in range(N):
            #빈 자리
            if not layout[i][j]:
                #인접 4방 탐색
                prefer = 0
                blank = 0
                #좋아하는 애 몇명? 빈 공간 몇개?
                for k in range(4):
                    n_row = i + d_row[k]
                    n_col = j + d_col[k]
                    if 0 <= n_row < N and 0 <= n_col < N:
                        if layout[n_row][n_col] in row[1:]:
                            prefer += 1
                        #빈 공간
                        if layout[n_row][n_col] == 0:
                            blank += 1
                score[(N * i) + j] = (i,j,prefer,blank)
    #좋아하는애가 많은순 > 빈칸 많은순 > 행이 작은 순 > 열이 작은 순
    score.sort(key = lambda x:(-x[2],-x[3],x[0],x[1]))
    x, y, _, _ = score[0]
    layout[x][y] = row[0]
result = 0
for i in range(N):
    for j in range(N):
        #학생번호로 학생이 좋아하는 애들 찾기
        student = layout[i][j]
        index = 0
        for k in range(N*N):
            if student_info[k][0] == student:
                index = k
                break
        prefer = 0
        for k in range(4):
            n_row = i + d_row[k]
            n_col = j + d_col[k]
            if 0 <= n_row < N and 0 <= n_col < N:
                if layout[n_row][n_col] in student_info[index][1:]:
                    prefer += 1
        result += satisfaction[prefer]
print(result)