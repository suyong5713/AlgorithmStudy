NONE = 'FRULA'

def solution() -> str:
    stack = []
    for i in range(len(string)):
        stack.append(string[i])
        if ''.join(stack[-explode_len:]) == explode_string:
            for _ in range(explode_len):
                stack.pop()
    return ''.join(stack) if stack else NONE


if __name__ == '__main__':
    string, explode_string = input(), input()
    explode_len = len(explode_string)
    print(solution())
