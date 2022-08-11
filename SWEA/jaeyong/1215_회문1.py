MATRIX_SIZE = 8
TEST_CASE = 10


def search_palindrome(arr):
    # 회문탐색
    result = 0

    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE - n + 1):
            if arr[i][j:j + n] == arr[i][j:j + n][::-1]:
                result += 1

    return result


def arr_matrix(arr):
    # 전치행렬 크기
    row = len(arr)
    col = len(arr[0])

    # 전치행렬 초기값 생성
    temp_arr = [[0 for row in range(row)] for col in range(col)]

    # 기존 행렬에 바로 집어넣으면 데이터를 절반까지 못 넣기 때문에
    # 전치행렬에 대한 임시변수를 선언한 다음
    # 기존 행렬을 탐색하며 전치한 좌표에 대해 전치행렬에 값을 삽입한다
    for i in range(row):
        for j in range(col):
            temp_arr[j][i] = arr[i][j]

    return temp_arr


# 테스트케이스 10회
for tc in range(TEST_CASE):
    # 회문 길이가 n개
    n = int(input())

    result = 0
    arr = []

    # 8x8 데이터 입력
    for i in range(MATRIX_SIZE):
        arr.append(list(str(input())))

    # 가로 탐색
    result += search_palindrome(arr)

    # 전치행렬화
    arr = arr_matrix(arr)

    # 세로 탐색
    result += search_palindrome(arr)

    # 데이터 출력
    print('#{} {}'.format(tc + 1, result))
