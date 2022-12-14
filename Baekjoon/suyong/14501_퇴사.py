def DFS(date, earn):
  global max_earn
  if date > N:
    return
  #현재 날짜의 상담 정보
  time, cost = time_cost[date-1]
  #상담 종료일
  end_date = date + time - 1
  if end_date <= N:
    max_earn = max(max_earn, earn+cost)
    DFS(end_date+1, earn+cost)
  DFS(date+1, earn)
max_earn = 0
N = int(input())
time_cost = [list(map(int,input().split())) for _ in range(N)]
DFS(1,0)
print(max_earn)