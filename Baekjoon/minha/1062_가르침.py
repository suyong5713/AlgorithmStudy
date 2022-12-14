def choose_alpha(n, start):
    global result
    if n == 0:
        result = max(result, check())
        return
    for i in range(start, len(alpha_list)):
        alpha.append(alpha_list[i])
        choose_alpha(n - 1, i + 1)
        alpha.pop()


def check():
    res = 0
    for words in arr:
        flag = True
        for i in range(4, len(words)-4):
            if words[i] not in alpha:
                flag = False
                break
        if flag:
            res += 1
    return res


N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input())

alpha = ['a', 'n', 't', 'i', 'c']
alpha_list = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']

result = 0

if K < 5:
    print(result)
else:
    choose_alpha(K - 5, 0)
    print(result)