T = 10

for test_case in range(1, T + 1):
    N = int(input())
    original = list(map(str, input().split()))

    M = int(input())
    command = list(input().split())

    for i in range(len(command)):
        if command[i] == 'I':
            x = int(command[i + 1])
            y = int(command[i + 2])
            s = command[i+3:i+3+y]
            for j in range(y) :
                original.insert(x+j, s[j])
        elif command[i][0] == 'D':
            x = int(command[i + 1])
            y = int(command[i + 2])
            for j in range(y):
                del(original[x])
        elif command[i][0] == 'A':
            y = int(command[i + 1])
            s = command[i+2:i+2+y]
            for j in range(y):
                original.append(s[j])

    result = ' '.join(original[:10])
    print("#{} {}".format(test_case, result))