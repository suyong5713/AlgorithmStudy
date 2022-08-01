N = int(input())
original = ''.join(map(str, input().split()))

M = int(input())
command = list(input().split())

def insert(x, s):
    b = original[:x]
    n = ''.join(s)
    a = original[x:]
    return b + n + a

def delete(x, y):
    b = original[:x]
    a = original[x+y:]
    return b + a

def append(s):
    n = ''.join(s)
    return original + n

for i in range(len(command)):
    if command[i] == 'I':
        x = int(command[i + 1])
        y = int(command[i + 2])
        s = command[i + 3:i + 3 + y]
        original = insert(x, s)
        print(original[:61])
    elif command[i] == 'D':
        x = int(command[i + 1])
        y = int(command[i + 2])
        original = delete(x, y)
        print(original[:61])
    elif command[i] == 'A':
        y = int(command[i + 1])
        s = command[i + 2:i + 2 + y]
        original = append(s)
        print(original[:61])
    else:
        continue

result = [original[i:i+6] for i in range(0, len(original), 6)]
changed = " ".join(result[:10])
print(changed)