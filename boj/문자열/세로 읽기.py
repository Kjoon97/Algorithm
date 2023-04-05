import sys
sys.stdin = open("input.txt","r")


ch = [list(input()) for _ in range(5)]

max_len = 0
for c in ch:
    lc = len(c)
    if lc>max_len:
        max_len= lc

for j in range(max_len):
    for i in range(5):
        cl = len(ch[i])
        for _ in range(cl,max_len):
            ch[i].append(False)

for j in range(max_len):
    for i in range(5):
        if ch[i][j]==False:
            continue
        print(ch[i][j], end="")