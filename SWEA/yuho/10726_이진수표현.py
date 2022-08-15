t = int(input())
for test in range(1,t+1):
    n, m = map(int, input().split())
    num = []

    c = 1
    flag = True
    # 마지막 n비트만 파악하면 되기에
    # 10진수를 2진수로 바꿀 때 뒤부터 결과가 나오는 공식을 사용
    while n >= c:
        # 계속 m의 나머지를 구해 1인지 확인
        b = m % 2
        # 0이면 모두 1이 아니므로 실패...
        if b == 0:
            flag = False
            break
        # 탈출하지 않았다면 성공이므로 다음 비트를 구하기 위해 2로 나누어줌
        m //= 2
        c += 1

    if flag: print("#{} ON".format(test))
    else: print("#{} OFF".format(test))