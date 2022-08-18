TC = int(input())

for t in range(TC):
    N, M = map(int, input().split())
    target = format(M, 'b')[-N:]

    if len(target) < N:
        print("#{} OFF".format(t + 1))
    else:
        if '0' in target:
            print("#{} OFF".format(t + 1))
        else:
            print("#{} ON".format(t + 1))

# 이진수 구하는 함수
# def getBinaryNum(n, lists):
#     a, b = divmod(n, 2)
#     lists.append(b)
#     if a == 0 :
#         return sorted(lists, reverse=True)
#     else :
#         return getBinaryNum(a, lists)
#
# target = "".join([str(_) for _ in getBinaryNum(M, [])])