# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 전력망을 둘로 나누기 (Level. 2 / 완전탐색)
# 풀이시간 : 30분

def dfs(v, graph, visited, checked):
    # 최초 시작하는 노드에 대해 개수 및 방문지점 초기화
    cnt = 1
    visited[v] = True

    # 최초 시작하는 노드를 기준으로 그래프 탐색
    for i in graph[v]:
        # 방문하지 않았었으면서, 간선을 사용할 수 있는 경우에 탐색
        if visited[i] == False and checked[v][i] == True:
            # 해당 노드를 기준으로 깊이탐색 시작
            cnt += dfs(i, graph, visited, checked)

    # 더 이상 깊이탐색할 노드가 없으면 탐색한 노드 수 반환
    return cnt

def solution(n, wires):
    answer = 1e9

    graph = [[] for _ in range(n + 1)]
    checked = [[True] * (n + 1) for _ in range(n + 1)]

    # 각각의 그래프에 서로의 노드를 추가해 준다
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        # (0을 제외하고) 1부터 9까지에 대한 visited 초기화
        visited = [False for _ in range(n + 1)]

        # a에서 b로 가는 간선은 있지만, b에서 a로 가는 간선은 없음
        checked[a][b] = False # a부터 b로 가는 간선 사용불가 처리
        part_i = dfs(a, graph, visited, checked)
        part_j = dfs(b, graph, visited, checked)
        checked[a][b] = True  # a부터 b로 가는 간선 사용불가 처리

        # 두 파트의 차이가 최소값이라면 answer에 저장
        answer = min(answer, abs(part_i - part_j))

    return answer

# ============================================================= #

def main(t, n, wires, result):
    r = solution(n, wires)
    print('#{}: {}'.format(t + 1, result == r))

if __name__ == '__main__':
    n = [9, 4, 7]
    wires = [
      [[1, 3],[2, 3],[3, 4],[4, 5],[4, 6],[4, 7],[7, 8],[7, 9]], 
      [[1, 2],[2, 3],[3, 4]], 
      [[1, 2],[2, 7],[3, 7],[3, 4],[4, 5],[6, 7]]
    ]
    result = [3, 0, 1]

    for t in range(3):
        main(t, n[t], wires[t], result[t])
