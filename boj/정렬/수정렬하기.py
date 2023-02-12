import sys
sys.stdin = open("input.txt","r")
n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

l.sort()

for x in l:
    print(x)