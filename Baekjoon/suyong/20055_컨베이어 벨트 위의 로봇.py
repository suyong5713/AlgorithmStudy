N, K = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0] * N
result = 0

while True:
  #벨트 회전
  belt.insert(0, belt.pop())
  robot.insert(0,robot.pop())
  #로봇이 내리는곳은 항상 0
  robot[-1] = 0
  #로봇이 존재하면
  if sum(robot): 
    #내리는곳 N-1의 한칸 전부터 0까지
    for i in range(N-2, -1, -1):
      if robot[i] and not robot[i+1] and belt[i+1] > 0:
        #로봇 전진
        robot[i+1] = 1
        robot[i] = 0
        #벨트 내구도 감소
        belt[i+1] -= 1
    #로봇 전진 후. 내리는곳에 위치한 로봇 내림.
    robot[-1] = 0
  #올리는 곳에 로봇이 없고 벨트 내구도가 남아있다면 로봇 올림
  if not robot[0] and belt[0] >= 1:
    robot[0] = 1
    belt[0] -= 1
  result += 1
  if belt.count(0) >= K:
      break    
print(result)