def solution(n, edge):
    # 양방향 그래프화
    graph = [[] for _ in range(n + 1)]
    for left, right in edge:
        graph[left].append(right)
        graph[right].append(left)

    # 간선 이동 거리 표기를 위해 1
    visited = [0] * (n + 1)
    visited[1] = 1
    queue = [1]
    while(queue):
        cur_node = queue.pop(0)
        for target_node in graph[cur_node]:
            if not visited[target_node]:
                # 현재 노드까지 이동 거리 + 1
                visited[target_node] = visited[cur_node] + 1
                queue.append(target_node)
    answer = visited.count(max(visited))
    return answer