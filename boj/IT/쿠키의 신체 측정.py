import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n = int(input())

board = [list(input().rstrip()) for _ in range(n)]
fwy=0
fwx=0

def find_heart():
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                return i+1,j

#심장 위치
y,x = find_heart()

print(y+1, x+1)

# 왼팔
def find_left_hand(y,x):
    cnt=0
    for i in range(x-1,-1,-1):
        if board[y][i]=='*':
            cnt+=1
        else:
            break
    return cnt

print(find_left_hand(y,x), end=" ")

# 오른팔,
def find_right_hand(y,x,n):
    cnt=0
    for i in range(x+1,n):
        if board[y][i] == '*':
            cnt+=1
        else:
            break
    return cnt

print(find_right_hand(y,x,n), end=" ")

# 허리
def find_waist(y,x,n):
    global fwy,fwx
    cnt=0
    for i in range(y+1,n):
        if board[i][x] == '*':
            cnt+=1
        else:
            fwy= i
            fwx= x
            break
    return cnt

print(find_waist(y,x,n), end=" ")
# 왼발,
start_x = fwx-1
start_y = fwy

def find_left_foot(y,x,n):
    cnt=0
    for i in range(y,n):
        if board[i][x] == '*':
            cnt+=1
        else:
            break
    return cnt

print(find_left_foot(start_y,start_x,n), end=" ")

# 오른발
start_x = fwx+1
start_y = fwy

def find_right_foot(y,x,n):
    cnt=0
    for i in range(y,n):
        if board[i][x] == '*':
            cnt+=1
        else:
            break
    return cnt

print(find_right_foot(start_y, start_x,n))
