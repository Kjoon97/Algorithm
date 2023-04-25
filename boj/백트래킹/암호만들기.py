import sys
sys.stdin = open("input.txt","r")
n,c = map(int,input().split())
words = list(input().split())
words.sort()
wstack = []
sstack =[]
mo = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
za = {}
def dfs(l):
    if l==n:
        za_cnt=0
        if not any([w in mo for w in wstack]):
            return
        for w in wstack:
            if w not in mo:
                za_cnt+=1
        if za_cnt>=2:
            print(''.join(wstack))
        else:
            return
    else:
        for i in range(c):
            if i not in sstack and all([i > s for s in sstack]):
                wstack.append(words[i])
                sstack.append(i)
                dfs(l+1)
                wstack.pop()
                sstack.pop()

dfs(0)