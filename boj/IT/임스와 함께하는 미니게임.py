import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline
n, game = input().split()
n = int(n)
played_people = set()
applyed_people = list()


for _ in range(n):
    people = input().rstrip()
    applyed_people.append(people)

if game == 'Y':
    cnt=0
    play_now = list()
    for ap in applyed_people:
        if ap not in played_people:
            played_people.add(ap)
            play_now.append(ap)

        if len(play_now) ==1:
            cnt+=1
            play_now = list()

elif game == 'F':
    cnt =0
    play_now = list()
    for ap in applyed_people:
        if ap not in played_people:
            played_people.add(ap)
            play_now.append(ap)

        if len(play_now) ==2:
            cnt+=1
            play_now = list()

else:
    cnt =0
    play_now = list()
    for ap in applyed_people:
        if ap not in played_people:
            played_people.add(ap)
            play_now.append(ap)

        if len(play_now) ==3:
            cnt+=1
            play_now = list()
print(cnt)
