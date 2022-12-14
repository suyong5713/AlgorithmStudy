def solution(n, wires):
    answer = 1e9

    for idx in range(len(wires)):
        parent = [i for i in range(n + 1)]

        new_wires = wires[:]
        new_wires.pop(idx)

        for a, b in new_wires:
            if find_parent(a, parent) == find_parent(b, parent):
                continue
            union(a, b, parent)

        parent_res = []
        for i in range(1, n + 1):
            parent_res.append(find_parent(i, parent))

        parent_res = list(set(parent_res))
        diff = abs(parent.count(parent_res[0]) - parent.count(parent_res[1]))
        answer = min(answer, diff)

    return answer

def union(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]