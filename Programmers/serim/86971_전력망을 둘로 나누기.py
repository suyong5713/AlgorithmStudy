from collections import deque, defaultdict

# bfs를 통해 시작 노드와 연결된 노드들의 개수를 파악
def bfs(start, visited, graph):
    queue = deque([start])
    nums = 1
    visited[start] = 1
    while queue:
        now = queue.popleft()
        # 현재 노드와 연결되어 있고
        for i in graph[now]:
            # 방문되지 않았다면
            if not visited[i]:
                nums += 1
                queue.append(i)
                visited[i] = 1
    return nums

def solution(n, wires):
    answer = n
    graph = defaultdict(list)

    # 연결된 전선 등록
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)

    # 연결된 전선을 하나씩 끊으며 양쪽에 속한 송전탑의 개수 차를 파악
    for x, y in wires:
        visited = [0] * (n + 1)
        # 현재 확인할 노드의 한쪽을 방문체크 후
        # 반대편 노드에 대해 방문체크되지 않은 연결된 노드의 개수를 파악
        visited[y] = 1
        nums = bfs(x, visited, graph)
        # 양쪽에 속한 송전탑의 개수가 최소일 때를 찾기
        if abs(nums - (n - nums)) < answer:
            answer = abs(nums - (n - nums))

    return answer