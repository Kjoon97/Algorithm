import sys,re
#sys.stdin = open("input.txt","r")

'''
^ 해당 패턴으로 시작
? 해당 패턴을 0번또는 1번
$ 해당 패턴으로 끝
+ 해당 패턴이 하나 이상
'''

p = re.compile('^[A-F]?A+F+C+[A-F]?$')
T = int(input())
words = []

for _ in range(T):
    s = input()
    if p.match(s)!=None:
        print('Infected!')
    else:
        print('Good')