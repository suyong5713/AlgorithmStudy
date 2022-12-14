testCase = int(input())
for tc in range(testCase):
    L,U,X = map(int,input().split())
    if L <= X and X <= U:
        print("#{} {}".format(tc+1, 0))
    elif X < L:
        print("#{} {}".format(tc+1, L-X))
    elif U < X:
        print("#{} {}".format(tc+1, -1))