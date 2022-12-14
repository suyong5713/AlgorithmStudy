def DFS(res, c, s1, s2, s3, s4):
    global max_num, min_num
    c += 1
    # 전체 연산자 모두를 소모하였을 때
    if sum([s1,s2,s3,s4]) == 0:
        # max, min 최신화 및 종료
        if max_num < res: max_num = res
        if min_num > res: min_num = res
        return
    else:
        # +연산자가 남아있는 경우
        if s1 != 0:
            DFS(res+num[c], c, s1-1, s2, s3, s4)
        # -연산자가 남아있는 경우
        if s2 != 0:
            DFS(res-num[c], c, s1, s2-1, s3, s4)
        # *연산자가 남아있는 경우
        if s3 != 0:
            DFS(res*num[c], c, s1, s2, s3-1, s4)
        # /연산자가 남아있는 경우
        if s4 != 0:
            # 문제 조건에 따른 음수 나누기 방식
            if res < 0:
                res *= (-1)
                DFS(-(res // num[c]), c, s1, s2, s3, s4 - 1)
            else:
                DFS(res // num[c], c, s1, s2, s3, s4 - 1)

# init
n = int(input())
num = list(map(int, input().split()))
state = list(map(int, input().split()))
# 초기 피연산자
res = num[0]
max_num = float("-inf")
min_num = float("inf")
# 결과값, idx, +개수, -개수, *개수, //개수
DFS(res, 0, state[0], state[1], state[2], state[3])
print(max_num)
print(min_num)
