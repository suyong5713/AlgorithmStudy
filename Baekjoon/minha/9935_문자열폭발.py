my_str = input()
bomb_str = input()

stack = []

for i in range(len(my_str)):
    stack.append(my_str[i])
    if ''.join(stack[-len(bomb_str):]) == bomb_str:
        # stack = stack[:-len(bomb_str)] 시간 초과 남
        for _ in range(len(bomb_str)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')