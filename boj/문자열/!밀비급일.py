import sys
#sys.stdin = open("input.txt","r")
input = sys.stdin.readline
while True:
    sentence = list(input().rstrip().split())
    if sentence[0] == "END":
        break
    answer = []
    for c in sentence:
        a = list(c)
        a.reverse()
        answer.append(''.join(a))
    answer.reverse()
    print(*answer)