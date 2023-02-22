import sys
sys.stdin = open("input.txt", "r")
# x+y+z=k는 x+y=-z+k와 같다는 원리를 이용해서 풀기.
n = int(input())
u = set()
ans =[]
for i in range(n):
    u.add(int(input()))

sums = set()
for x in u:
    for y in u:
        sums.add(x+y)

for k in u:
    for z in u:
        if (k-z) in sums:
            ans.append(k)

#min, max는 O(n)이고 sort는 O(NlogN)으로 sort해서 마지막 값 찾는게 더 빠름
ans.sort()
print(ans[-1])