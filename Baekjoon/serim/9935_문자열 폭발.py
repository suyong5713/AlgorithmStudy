origin = input()
target = input()
stack = []
for o in origin:
    stack.append(o)
    if o == target[-1] and ''.join(stack[-len(target):]) == target:
        del stack[-len(target):]
result = ''.join(stack)
print("FRULA" if result == "" else result)