import sys
sys.setrecursionlimit(10 ** 9)


def postorder(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if graph[start] < graph[i]:
            mid = i
            break
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(graph[start])


graph = []
while True:
    try:
        graph.append(int(input()))
    except:
        break

postorder(0, len(graph) - 1)
