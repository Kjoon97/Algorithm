import sys

sys.stdin = open("input.txt", "r")
n = int(input())
words = []
for _ in range(n):
    words.append(input())


def sum_num(sentences):
    result = 0
    for c in sentences:
        if c.isdigit():
            result += int(c)
    return result

#짧은 것 먼저, 숫자 합이 작은 것, 사전 순.
words.sort(key=lambda x: (len(x), sum_num(x), x))

for v in words:
    print(v)