from itertools import combinations
from collections import deque


def BFS(s):
    q = deque()
    # 초기값
    start = s[0]
    pp = population[start]
    cc = 1
    q.append(start)
    visited[s[0]] = True
    while q:
        elem = q.popleft()
        # 전체 노드에 대해
        for i in range(n+1):
            # 방문 하지 않고, 현재 꺼내진 노드와 간선이 존재 하며, 해당 팀에 있는 노드일 시
            if not visited[i] and graph[elem][i] and i in s:
                q.append(i)
                visited[i] = True
                pp += population[i]
                cc += 1
    return pp, cc


# init
n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[0]*(n+1) for _ in range(n+1)]
# 행렬 그래프 생성
for i in range(1,n+1):
    graph[i][i] = 1
    line = list(map(int, input().split()))
    for l in line[1:]:
        graph[i][l] = 1
        graph[l][i] = 1
case = []
# 전체 나뉠 수 있는 경우의 수를 생성
# 이 때 생성 되는 경우의 수는 다음과 같음
# (1,), (2,), (3,), ------ ,(1, 2, 4, 5, 6), (1, 3, 4, 5, 6), (2, 3, 4, 5, 6)
# 0번째와 -1번째, 1번째와 -2번째, 2번째와 -3번째 .... n번째와 (n+1)*(-1)번째 <<< 이렇게 매칭됨
for i in range(1,n):
    case += combinations(range(1,n+1),i)
print(case)

# 반만 반복 하도록 함
p = len(case) // 2
res = float('inf')
for i in range(p):
    visited = [False]*(n+1)
    # A팀 BFS 결과
    per1,c1 = BFS(case[i])
    # B팀 BFS 결과
    per2,c2 = BFS(case[(i+1)*(-1)])
    # 두 팀의 개수 결과가 전체 노드 개수와 같을 시
    # 알맞게 분류됨
    if c1+c2 == n:
        per = abs(per1-per2)
        if per < res: res = per
if res == float('inf'): print(-1)
else: print(res)