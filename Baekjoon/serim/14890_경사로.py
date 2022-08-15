def check(line):
    runway = [False for _ in range(n)]
    for i in range(n - 1):
        # 높이가 같을 경우 패스
        if line[i] == line[i + 1]:
            continue
        # 높이차가 1보다 클 경우 그 길은 지나갈 수 없음
        if abs(line[i] - line[i + 1]) > 1:
            return False
        # 높 -> 낮
        if line[i] > line[i + 1]:
            temp = line[i + 1]
            for j in range(i + 1, i + 1 + l):
                if 0 <= j < n:
                    if line[j] != temp:
                        return False
                    # 이미 해당 위치에 경사로 존재
                    if runway[j]:
                        return False
                    runway[j] = True
                else:
                    return False
        # 낮 -> 높
        else:
            temp = line[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if line[j] != temp:
                        return False
                    if runway[j]:
                        return False
                    runway[j] = True
                else:
                    return False
    return True


n, l = map(int, input().split())
area = []
for _ in range(n):
    area.append(list(map(int, input().split())))
result = 0

for i in area:
    if check(i):
        result += 1
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(area[j][i])
    if check(temp):
        result += 1

print(result)