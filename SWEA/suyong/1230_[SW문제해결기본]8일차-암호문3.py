result =[]
for tc in range(10):
    N = int(input())
    num_list = input().split()
    command_count = int(input())
    command = input().split()
    i = 0
    while i < len(command):
        if command[i] == 'I':
            pos = int(command[i+1])
            count = int(command[i+2])
            for j in range(count):
                num_list.insert(pos+j, command[i+3+j])
            i += count + 3
        elif command[i] == 'D':
            pos = int(command[i+1])
            count = int(command[i+2])
            for j in range(count):
                num_list.pop(pos)
            i += 3
        elif command[i] == 'A':
            count = int(command[i+1])
            for j in range(count):
                num_list.append(command[i+2+j])
            i += 2 + count
    result.append(f'#{tc + 1} {" ".join(num_list[0:10])}')
print('\n'.join(result))