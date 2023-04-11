import sys
sys.stdin = open("input.txt","r")
'''
문제: 
크기가 3*3인 격자판.
1. 행의 개수 >= 열의 개수 :
모든 행에 대하여 출현 빈도 수가 적은 순으로 정렬.
출현 하는 횟수가 같은 숫자의 경우, 해당 숫자가 작은 순으로 정렬.
정렬할 때, 숫자와 해당하는 숫자의 출현 빈도 출력.
2. 행의 개수<열의 개수:
모든 열
3. 행, 열 길이가 100을 넘기는 경우 처음 100개의 격자를 제외하고 모두 버림. 

입력:
위치r,c, 목표 숫자:k
'''


# 연산함수
# board : NxN 배열, L : 행의 길이 (칼럼 개수)
def operation(board, L):
    for idx, row in enumerate(board):
        temp = []
        for n in set(row):  # 행의 중복을 제거한 후
            if n:  # 0이 아닌 숫자면
                temp.append((n, row.count(n)))  # 해당 숫자에 대한 값을 세어줌
        temp = sorted(temp, key=lambda x: (x[1], x[0]))  # 개수, 숫자 순서로 정렬
        templen = len(temp)
        if templen > 50:
            templen = 50  # 숫자의 개수는 100을 넘어가면 안됨
        L = max(L, templen * 2)  # 행의 길이를 최대로 바꿔줌
        board[idx] = []  # board의 idx행 초기화
        for i in range(templen):  # board의 idx행 재구성
            board[idx].append(temp[i][0])  #숫자
            board[idx].append(temp[i][1])  #개수.

    # 최대 길이만큼 0 채우기
    for idx, row in enumerate(board):
        for _ in range(L - len(row)):
            board[idx].append(0)

    return board, L

if __name__=='__main__' :
    r, c, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(3)]

    rlen, clen = 3, 3
    for time in range(101) :
        if r <= rlen and c <= clen and board[r-1][c-1] == k :
            print(time)
            break
        if rlen >= clen : # R연산
            board, clen = operation(board, clen)
        else : # C연산
            board, rlen = operation(list(map(list,zip(*board))), rlen) # 행과 열을 전치시켜 함수를 실행한다.
            board = list(map(list,zip(*board))) # 행과 열을 원상태로 바꾼다.
    else : # 100초 동안 r행 c열이 k가 아닌 경우
        print(-1)