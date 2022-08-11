# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD

# 암호코드를 미리 정의해둔다
# 0과 1로 이루어진 암호코드는 항상 1로 끝난다
code_num = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

def check_data(d):
    s = 0
    arr = [code_num.get(d[(i*7):(i*7) + 7]) for i in range(8)]

    if (((int(arr[0]) + int(arr[2]) + int(arr[4]) + int(arr[6])) * 3) + (int(arr[1]) + int(arr[3]) + int(arr[5])) + int(arr[7])) % 10 == 0:
        s = sum(int(arr[i]) for i in range(len(arr)))

    # 올바른 암호코드인 경우에만 더할 데이터를 반환
    return s

test_case = int(input())
res_print = ''

for tc in range(test_case):
    result = 0
    n, m = map(int, input().split())

    data = [list(input()) for _ in range(n)]

    parent_break = False
    for i in range(n):
        for j in range(m - 1, 0, -1):
            if data[i][j] == '0' and j < 55:    # 해당줄엔 데이터가 없다는 것을 미리 파악
                break
            if data[i][j] == '1':
                d = ''.join(data[i][j + 1 - 56:j + 1])
                s = check_data(d)
                result += s
                parent_break = True
                break
        if parent_break == True:
            break

    res_print += '#{} {}\n'.format(tc + 1, result)

print(res_print)
