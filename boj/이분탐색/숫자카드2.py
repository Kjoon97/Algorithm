import sys
#sys.stdin = open("input.txt","r")
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n = int(input())
sang_card = sorted(list(map(int,input().split())))
m = int(input())
cards = list(map(int,input().split()))

for card in cards:
    r = bisect_right(sang_card,card)
    l = bisect_left(sang_card,card)
    print(r-l, end=" ")