T = 10
for test_case in range(1, T + 1):
    # 원본 암호문의 길이
    n = int(input())
    # 원본 암호문
    cryptogram = list(map(int, input().split()))
    # 명령어의 개수
    m = int(input())
    # 명령어
    command = list(input().split())
    for i in range(len(command)):
        # 삽입 연산
        if command[i] == "I":
            index = int(command[i + 1])    # 위치
            num = int(command[i + 2])   # 개수
            # 숫자 삽입
            for j in range(num):
                cryptogram.insert(index + j, int(command[i + 3 + j]))
        # 삭제 연산
        elif command[i] == "D":
            index = int(command[i + 1])     # 위치
            num = int(command[i + 2])   # 개수
            # num개의 숫자 삭제
            for j in range(num):
                del cryptogram[index]
        # 추가 연산
        elif command[i] == "A":
            num = int(command[i + 1])   # 개수
            for j in range(1, num + 1):
                cryptogram.append(command[i + j + 1])
    # 10개 항 출력 => int 형식이므로 string으로 매핑해서 출력
    print("#{} {}".format(test_case, " ".join(map(str, cryptogram[:10]))))