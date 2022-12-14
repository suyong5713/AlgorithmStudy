T = int(input())

for tc in range(T):
    # 0~9까지 코드
    code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    # N개줄에 배열 입력 받으면서 1이 포함되어 있는 배열을 row로 지정
    # 원래 1이 포함된 첫 행만 받고 break를 하려고 했으나, 여러 개 tc에서 입력 받을 때 문제가 되어 끝까지 받음
    N, M = map(int, input().split())
    for i in range(N):
        inp = input()
        if '1' in inp:
            row = inp

    # 한 행에서 뒤에서 처음으로 1이 나오는 곳까지 자름
    row = row[:-row[::-1].find('1')]

    # row를 뒤에서부터 7글자씩 잘라서 nums에 넣음
    # 거꾸로 탐색하기 때문에 마지막에 nums를 reverse
    nums = []
    for i in range(len(row)-1, 0, -7):
        if len(row[i-6:i+1]) == 7:
            nums.append(row[i-6:i+1])
    nums.reverse()

    # code와 매핑
    serialNum = []
    for i in nums:
        for index, num in enumerate(code):
            if i == num:
                serialNum.append(index)

    # 검증 코드 유효성 확인
    verifyNum = 0
    for i in range(len(serialNum)):
        if i % 2 == 0:
            verifyNum += (serialNum[i] * 3)
        else:
            verifyNum += serialNum[i]

    if verifyNum % 10 == 0:
        print("#{} {}".format(tc + 1, sum(serialNum)))
    else:
        print("#{} 0".format(tc + 1))