import sys

sys.stdin = open("input.txt",'r')
'''
문제: 어떤 퀸도 다른 퀸에 의해서 잡아먹히지 않도록 배치해야함.
     -> 같은 행, 열, 대각선에는 다른 퀸을 놓을 수 없음.
임의의 집합(체스 보드에 있는 n^2개의 가능한 위치)에서 기준(새로 놓을 퀸이 다른 퀸을 위협할 수 없음)에 따라 원소의 순서(퀸을 놓을 수 있는 n개의 위치)를 선택.
참고: https://www.youtube.com/watch?v=z4wKvYdd6wM&list=PLHqxB9kMLLaPOp0jh591QhPvbz4H266SS&index=20
'''
n = int(input())

ans = 0
row = [0] * n

# 같은 열, 같은 대각선에 있는지 체크
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def n_queens(x):
    global ans
    # 마지막 행까지 탐색 끝나면.
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다./ col[행]=열 => (1,1)은 col[1]=1
            row[x] = i
            # 체스를 둘 수 있다면(열, 대각선 검사 통과)
            if is_promising(x):
                n_queens(x + 1)

n_queens(0)
print(ans)