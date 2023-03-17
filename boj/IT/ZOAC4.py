import sys
# sys.stdin = open("input.txt")
import math
h,w,n,m = map(int,input().split())

a = math.ceil(w/(m+1))
b = math.ceil(h/(n+1))

print(a*b)