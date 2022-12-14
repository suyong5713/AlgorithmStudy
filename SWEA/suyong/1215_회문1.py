def palindrome(str):
    count = 0
    for i in range(8-N+1):
            if str[i:i+N] == (str[i:i+N])[::-1]:
                count += 1
    return count

for tc in range(10):
    N = int(input())
    board = [''] * 8
    for i in range(8):
        board[i] = input()
    result = 0
    #가로 회문 탐색
    for string in board:
        result += palindrome(string)
    #보드 90도 회전 후 가로회문 탐색 == 세로회문 탐색
    for string in zip(*board):
        tempString = ''.join(string)
        result += palindrome(tempString)
    print("#{} {}".format(tc+1,result))
