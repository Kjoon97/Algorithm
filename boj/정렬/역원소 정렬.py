import sys
#sys.stdin = open("input.txt","r")

nums =[]

#입력이 끝날때까지 입력받기.
lines = sys.stdin.readlines()
for line in lines:
    inputs = line.split()
    for num in inputs:
      s = []
      for x in num:
          s.append(x)
      #리스트로 뒤집기.
      s.reverse()
      reversed_num = ''.join(s)
      nums.append(reversed_num)
nums.pop(0)
ans = [int(n) for n in nums]
ans.sort()
# print(ans)
for a in ans:
    print(a)