import sys
from string import ascii_uppercase


def make_table():
    global key, table_linear, table

    for k in key:
        if k not in table_linear:
            table_linear.append(k)

    for alpha in list(ascii_uppercase):
        if alpha == 'J':
            continue
        else:
            if alpha not in table_linear:
                table_linear.append(alpha)

    for i in range(5):
        table.append(table_linear[i * 5:i * 5 + 5])


def make_pair():
    global message, pair
    visited = [False] * len(message)

    for i in range(len(message) - 1):
        if not visited[i]:
            if message[i] == message[i + 1]:
                if message[i] == 'X':
                    pair.append((message[i], 'Q'))
                else:
                    pair.append((message[i], 'X'))
                visited[i] = True
            else:
                pair.append((message[i], message[i + 1]))
                visited[i] = visited[i + 1] = True

    if not visited[-1]:
        pair.append((message[-1], 'X'))


def encoding():
    global table_linear, table, pair, answer
    col_table = list(map(list, zip(*table)))

    for first, second in pair:
        e_first = e_second = ''

        # 두글자가 같은 행에 존재한다면
        for row in table:
            if first in row and second in row:
                for idx, s in enumerate(row):
                    if first == s:
                        e_first = row[(idx + 1) % 5]
                    if second == s:
                        e_second = row[(idx + 1) % 5]

        # 두글자가 같은 열에 존재한다면
        if e_first == '':
            for col in col_table:
                if first in col and second in col:
                    for idx, s in enumerate(col):
                        if first == s:
                            e_first = col[(idx + 1) % 5]
                        if second == s:
                            e_second = col[(idx + 1) % 5]

        if e_first == '':
            fr = fc = sr = sc = -1
            for idx, s in enumerate(table_linear):
                if s == first:
                    fr = idx // 5
                    fc = idx % 5
                if s == second:
                    sr = idx // 5
                    sc = idx % 5

                if idx == len(table_linear) - 1:
                    e_first = table[fr][sc]
                    e_second = table[sr][fc]

        answer.append(e_first)
        answer.append(e_second)


message = sys.stdin.readline().strip()
key = sys.stdin.readline().strip()

table_linear = []
table = []
pair = []
answer = []

make_table()
make_pair()
encoding()

print(''.join(answer))