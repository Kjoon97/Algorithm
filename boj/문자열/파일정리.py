import sys
from collections import defaultdict
#sys.stdin = open("input.txt","r")
#input = sys.stdin.readline

n = int(input())
d = defaultdict(int)
for _ in range(n):
    a,b = input().rstrip().split('.')
    d[b]+=1

d = list(d.items())
d.sort()
for x in d:
    print(*x)