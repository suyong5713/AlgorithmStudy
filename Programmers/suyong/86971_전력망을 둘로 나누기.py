def solution(n, wires):
    min_value = float("inf")
    wires_length = len(wires)
    for i in range(wires_length):
        visited = [False] * (n + 1)
        visited[1] = True
        stack = [1]
        while(stack):
            start_node = stack.pop()
            for idx, wire in enumerate(wires):
                if i == idx:
                    # i번째 간선을 제거. 탐색x
                    continue
                # v1 -> v2 간선 탐색
                if wire[0] == start_node and not visited[wire[1]]:
                    stack.append(wire[1])
                    visited[wire[1]] = True
                # v2 -> v1 간선 탐색
                elif wire[1] == start_node and not visited[wire[0]]:
                    stack.append(wire[0])
                    visited[wire[0]] = True
        group1 = visited.count(True)
        group2 = n - visited.count(True)
        min_value = min(min_value, abs(group1 - group2))
    answer = min_value
    return answer