import sys
sys.stdin = open("input.txt","r")

s = input()
p = input()

if p in s:
    print(1)
else:
    print(0)