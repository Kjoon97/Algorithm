import sys
#sys.stdin = open("input.txt","r")
input = sys.stdin.readline
s = input().rstrip()
bomb = list(input().rstrip())

stack =[]

for i in range(len(s)):
    stack.append(s[i])
    if stack[-len(bomb):] ==bomb:
        del stack[-len(bomb):]

if stack: print("".join(stack))
else: print("FRULA")


