def check_load(row):
    for i in range(1, N):
        #높이차가 1이상이면 경사로 설치 불가
        if abs(row[i] - row[i - 1]) > 1:
            return False
        #내리막 경사로
        if row[i] < row[i - 1]:
            for j in range(L):
                #인덱스 초과, 경사로 설치공간부족, 이미 경사로 설치된 길
                if i + j >= N or row[i] != row[i + j] or setted[i + j]:
                    return False
                #경사로 설치 공간이 있으면 설치
                if row[i] == row[i + j]:
                    setted[i + j] = True
        #오르막 경사로
        elif row[i] > row[i - 1]:
            for j in range(L):
                if i - j - 1 < 0 or row[i - 1] != row[i - j - 1] or setted[i - j - 1]:
                    return False
                if row[i - 1] == row[i - j - 1]:
                    setted[i - j - 1] = True
    return True

N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
count = 0
for row in matrix:
  setted = [False] * N
  if check_load(row):
    count += 1
#전치 행렬
matrix = list(map(list,zip(*matrix)))
for row in matrix:
  setted = [False] * N
  if check_load(row):
    count += 1
print(count)