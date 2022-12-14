# 암호 마지막 자리 인덱스 구하기
def find_index():
    global last_index
    for i in range(len(barcode)):
        if list(reversed(barcode))[i] == 1:
            last_index = i
            break

# 암호 코드 구하기
def find_code():
    global st
    for i in range(len(barcode) - last_index - 56, len(barcode) - last_index):
        code_array.append(str(barcode[i]))
    for i in range(0, len(code_array), 7):
        for j in range(len(rules)):
            if ''.join(code_array[i: i + 7]) == rules[j]:
                st += str(j)

# 정상 코드인지 검사
def find_normal():
    odd = 0
    other = 0
    for i in range(8):
        if i % 2 == 0:
            odd += int(st[i])
        else:
            other += int(st[i])
    return other + odd * 3

tc = int(input())
for test_case in range(1, tc + 1):
    n, m = map(int, input().split())
    last_index = 0
    global barcode
    code_array = []
    rules = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    st = ''
    for _ in range(n):
        input_list = list(map(int, input()))
        if sum(input_list) != 0:
            barcode = input_list

    find_index()
    find_code()
    if (find_normal()) % 10 == 0:
        print("#{} {}".format(test_case, sum(int(i) for i in st)))
    else:
        print("#{} {}".format(test_case, 0))