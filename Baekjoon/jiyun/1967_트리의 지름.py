# [0. 환경 설정 및 초기 세팅]

import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
MIN = 0  # 주의 : float(-inf)하면 안되더라.. (짬 부족)

class Node:
    def __init__(self, _nodeNum : int , _target : int, _weight: int):
        self.num = _nodeNum
        self.targetNum = _target
        self.weight = _weight

class Tree:
    def __init__(self):
        self.root = 1
        self.tree = defaultdict(list)

    def getTree(self) -> dict:
        return self.tree

    def addNode(self, _nodeInfo : Node):
        nodeNum = _nodeInfo.num
        self.tree[nodeNum].append(_nodeInfo)

# -----------------------------------------------------------------------------------------------------------------------------

def dfs(_nodeNum, _weight):                                         # [2. 솔루션(Solution)]
    global maxDist
    dist1, dist2 = MIN, MIN                                         # [2-1. 현재 노드 기준, 하위 탐색 값 중 가장 큰 합 2개를 저장할 변수 생성]
    childNodes = tree.getTree().get(_nodeNum)
    if childNodes is None : return _weight                          # -> leaf 노드일 경우, 본인의 자식 노드가 없으므로 이동 가중치 바로 리턴.
    for childNodeInfo in childNodes:                                # -> leaf 노드가 아닐 경우, 본인의 자식 노드를 꺼내서 반복해 재귀 탐색.
        returnVal = dfs(childNodeInfo.targetNum, childNodeInfo.weight)
        if returnVal > dist1:
            dist2 = dist1
            dist1 = returnVal
        elif returnVal >= dist2:
            dist2 = returnVal
    maxDist = max(maxDist, dist1 + dist2)                           # [2-2. 현재 노드에서 탐색하여 얻은 최대 2개를 합한 값으로 답 갱신]
    return dist1 + _weight                                          # -> 재귀 종료의 경우, 자신의 부모 노드에게 최대 값 1개만을 리턴.


# -----------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':                                          # [1. 데이터 Input 처리]
    n = int(input())
    tree = Tree()                                                   # [1-1. 빈 트리 생성]
    for _ in range(n - 1):
        parentNum, childNum, weight = map(int, input().split())     # (데이터) 부모 노드, 자식 노드, 가중치
        node = Node(parentNum, childNum, weight)                    # [1-2. 노드 생성]
        tree.addNode(node)                                          # -> 이때 무방향 그래프 아니고, 사실 그냥 방향 그래프

    maxDist = MIN
    dfs(1, 0)
    print(maxDist)