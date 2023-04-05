import sys
sys.stdin = open("input.txt","r")

t = int(input())

def check(word, l,r):
    while l<r:
        if word[l]==word[r]:
            l+=1
            r-=1
        else:
            l_remove = check2(word,l+1,r)
            r_remove = check2(word,l,r-1)
            if (l_remove or r_remove):
                return 1
            else:
                return 2
    return 0

def check2(word,l,r):
    while l<r:
        if word[l]==word[r]:
            l+=1
            r-=1
        else:
            return False
    return True

for _ in range(t):
    word = input()
    l=0
    r=len(word)-1

    print(check(word,l,r))