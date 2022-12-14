#문제해결 아이디어
#N극 자성체 블럭은 아래에 S극 자성체 블럭을 만나면 교착상태가 된다.
#S극 자성체 블럭은 아래에 N극 자성체 블럭을 만나면 교착상태가 된다.
#따라서 각 자성체 블럭의 '열'만 체크하면 된다.
#zip(*list)의 기능으로 리스트를 변환.(행렬이 90도 회전.)
#테이블에서 N극[1(N극블럭) 2(S극블럭)]S극 이 연속으로 나타나는 경우를 교착상태로 인정하고 카운트.
#이슈사항: 1212형태로 붙어있는 교착상태를 1개로 인정하는 줄 알고 풀었다가
#문제를 꼼꼼히 읽어보니 1212형태는 2개의 교착상태로 인정한다는 것을 확인함...
for tc in range(10):
    #정사각형 한 변의 길이. 어차피 100고정
    N = int(input())
    result = 0
    square = [[] for _ in range(N)] # 100*0 배열 생성
    for i in range(N):
        square[i] = list(input().split())
    square = list(zip(*square))
    for col in square:
        colString = ''
        for i in col:
            if i == '1' or i == '2':
                colString += i
        result += colString.count('12')
    print("#{} {}".format(tc+1, result))