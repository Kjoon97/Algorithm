import sys
sys.stdin = open("input.txt")
#정렬을 이용해서 양수는 큰 양수끼리, 음수는 작은 음수끼리 곱한다.(1은 더하고, 0은 음수랑 곱하거나 더하기)
n = int(input())
nums = [int(input()) for _ in range(n)]

pos = []
neg = []

for num in nums:
    if num>0:
        pos.append(num)
    else:
        neg.append(num)

pos.sort()
neg.sort(reverse=True)

ans=0
#양수 처리
while len(pos)>=2:
    a = pos.pop()
    b = pos.pop()
    if a==1 or b==1:
        ans+=a+b
    else:
        ans+=a*b
#1개 남을 경우
if pos:
    ans+=pos.pop()

#음수 처리
while len(neg)>=2:
    a=neg.pop()
    b=neg.pop()
    ans+=a*b
#1개 남을 경우
if neg:
    ans+=neg.pop()

print(ans)