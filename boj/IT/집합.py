import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
n = int(input())
num_set =set()

for _ in range(n):
    s = input().rstrip()
    if s == "all":
        num_set = {x for x in range(1, 21)}
    elif s=="empty":
        num_set =set()
    else:
        cmd, num = s.split()
        num = int(num)
        if cmd == "add":
            num_set.add(num)
        elif cmd == "remove":
            num_set.discard(num)
        elif cmd == "check":
            if num in num_set:
                print(1)
            else:
                print(0)
        elif cmd == "toggle":
            if num in num_set:
                num_set.discard(num)
            else:
                num_set.add(num)