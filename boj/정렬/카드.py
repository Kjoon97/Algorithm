import sys

input = sys.stdin.readline  # 입력 줄 수가 많으므로 반드시 필요

d = dict()
for _ in range(int(input())):
    n = int(input())  # 정렬을 위해 정수로 변환
    if d.get(n):
        d[n] += 1
    else:
        d[n] = 1

ans, max_cnt = 0, 0
#딕셔너리 정렬(키와 값 튜플 쌍으로 정렬), 키로 정렬은 d.keys(), 값 정렬은 d.values()
lst = sorted(d.items())

for num, cnt in lst:
    if max_cnt < cnt:
        max_cnt = cnt
        ans = num
print(ans)