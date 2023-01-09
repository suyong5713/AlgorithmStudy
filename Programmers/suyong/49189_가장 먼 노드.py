def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    # 간선 이동 거리 표기를 위해 1
    visited = [0] * (n + 1)
    visited[1] = 1
    # 양방향 그래프화
    for left, right in edge:
        graph[left].append(right)
        graph[right].append(left)

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

# def solution(n, edge):
#     # 간선 이동 거리 표기를 위해 1
#     visited = [0] * (n + 1)
#     visited[1] = 1
#     queue = [1]
#     while(queue):
#         cur_node = queue.pop(0)
#         for left, right in edge:
#             if left == cur_node:
#                 if not visited[right]:
#                     # 현재 노드까지 이동 거리 + 1
#                     visited[right] = visited[cur_node] + 1
#                     queue.append(right)
#             elif right == cur_node:
#                 if not visited[left]:
#                     visited[left] = visited[cur_node] + 1
#                     queue.append(left)
#     answer = visited.count(max(visited))
#     return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])