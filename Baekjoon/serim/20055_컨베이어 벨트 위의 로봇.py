from collections import deque

n, k = map(int, input().split())
durability = deque(list(map(int, input().split())))
robot = deque([0]*n)
# 단계
result = 0
# 내구도가 0인 칸이 k개 이상이면 break
while durability.count(0) < k:
    # 1
    durability.rotate(1)
    robot.rotate(1)
    # 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    robot[-1] = 0
    # 3
    if sum(robot):
        for i in range(n-2, -1, -1):
            if robot[i] == 1 and robot[i + 1] == 0 and durability[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                durability[i + 1] -= 1
        robot[-1] = 0
    # 4
    if robot[0] == 0 and durability[0] >= 1:
        robot[0] = 1
        durability[0] -= 1
    result += 1

print(result)