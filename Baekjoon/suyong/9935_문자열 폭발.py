string = input()
bomb = input()

stack = []
for char in string:
    stack.append(char)
    if len(stack) >= len(bomb) and "".join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]
if stack:
    print("".join(stack))
else:
    print("FRULA")

# mirkovC4nizCC44
# C4