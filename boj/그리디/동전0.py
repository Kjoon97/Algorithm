import sys

sys.stdin = open("input.txt","r")

n,k = map(int, input().split())
coins =[]
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
cnt=0
for coin in coins:
    if coin<=k:
        cnt += k//coin
        k= k%coin

print(cnt)

