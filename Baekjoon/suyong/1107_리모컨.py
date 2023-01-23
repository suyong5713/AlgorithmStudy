num_split = list(input())
num = int(''.join(num_split))
N = int(input())
if N:
    buttons = input().split()

count = 0
answer = abs(num - 100)
while True:
    if N == 0:
        answer = min(abs(num - 100), len(num_split))
        break
    if count > abs(num - 100):
        answer = abs(num - 100)
        break
    up_side = num + count
    down_side = num - count
    flag = False
    if down_side >= 0:
        for button in buttons:
            if button in list(str(down_side)):
                flag = True
                break
    else:
        flag = True
    if not flag:
        answer = min(answer, len(list(str(down_side))) + count)
        break
    flag = False
    for button in buttons:
        if button in list(str(up_side)):
            flag = True
            break
    if not flag:
        answer = min(answer, len(list(str(up_side))) + count)
        break
    count += 1
print(answer)