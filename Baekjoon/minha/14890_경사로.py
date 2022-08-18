def check(r):
    for i in range(1, N):
        if r[i - 1] == r[i]: # 동일하다면
            if i == N - 1:
                return 1
            else:
                continue

        if abs(r[i - 1] - r[i]) > 1: # 1이상 차이난다면
            return 0

        if r[i - 1] - r[i] == 1: # 이전 길의 수가 큰 경우
            for j in range(L):  # L만큼 길이의 다음 길을 확인
                if i + j >= N or r[i] != r[i + j] or used[i + j]: # 범위를 넘어가거나 / 숫자가 같지 않거나 / 이미 사용한 길이면 0리턴
                    return 0
                if j == L-1 and r[i] == r[i + j]: # 사용 가능한 길일 경우 사용 여부 체크
                    for k in range(L):
                        used[i + k] = True

        if r[i] - r[i-1] == 1: # 이전 길의 수가 작은 경우
            for j in range(L):  # L만큼 길이의 이전전 길을 확인
                if i - j - 1 < 0 or r[i - 1] != r[i - j - 1] or used[i - j - 1]: # 범위를 넘어가거나 / 숫자가 같지 않거나 / 이미 사용한 길이면 0리턴
                    return 0
                if j == L - 1 and r[i - 1] == r[i - j - 1]: # 사용 가능한 길일 경우 사용 여부 체크
                    for k in range(L):
                        used[i - k - 1] = True

        if i == N - 1: # 마지막 길까지 확인했다면
            return 1

N, L = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
res = 0

for i in list(map(list, zip(*road))):
    road.append(i)

for i in road:
    used = [False for _ in range(N)]
    res += check(i)

print(res)