import sys

sys.setrecursionlimit(10 ** 6)
node_list = []
while True:
    try:
        node_list.append(int(sys.stdin.readline()))
    except:
        break


def postorder(start_index, end_index):
    if start_index > end_index:
        return

    div = end_index + 1

    for i in range(start_index + 1, end_index + 1):
        if node_list[start_index] < node_list[i]:
            div = i
            break

    postorder(start_index + 1, div - 1)
    postorder(div, end_index)
    print(node_list[start_index])


postorder(0, len(node_list) - 1)
