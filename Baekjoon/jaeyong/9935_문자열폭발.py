string = input()
bomb = input()

stack = []

for s in string:
    stack.append(s)
    if s == stack[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

ans = ''.join(stack)
if ans == '':
    print('FRULA')
else:
    print(ans)
