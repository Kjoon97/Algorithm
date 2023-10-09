import sys
sys.stdin = open("input.txt","r")

s = input()
a_cnt = s.count('a')
s += s[0:a_cnt-1]

min_val = 2147000000

for i in range(len(s)-(a_cnt-1)):
    min_val = min(min_val, s[i:i+a_cnt].count('b'))

print(min_val)

#참고: https://da-y-0522.tistory.com/49