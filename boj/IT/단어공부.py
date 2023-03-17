import sys
sys.stdin = open("input.txt","r")

s = list(input().upper())
set_s = set(s)
d = {x:0 for x in set_s}
for c in s:
    d[c]+=1
sl = sorted(list(d.items()), key= lambda x: x[1],reverse=True)
if len(sl)==1:
    print(sl[0][0])
elif sl[0][1]==sl[1][1]:
    print("?")
else:
    print(sl[0][0])