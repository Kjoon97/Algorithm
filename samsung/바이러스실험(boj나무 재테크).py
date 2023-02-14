# 변수 선언 및 입력
import sys
sys.stdin = open("input.txt","r")
'''
1. 문제:
* 초기: 5개 양분, m개 바이러스
* 실험 한 사이클
    - 1. 각 바이러스는 본인이 속한 칸의 양분을 섭취.(본인의 나이만큼)
    -    같은 칸에 있으면 나이가 어린 바이러스부터 섭취.
    -    양분을 섭취하면 바이러스 나이 +1
    -    양분이 부족하여 본인 나이만큼 섭취 못하면 즉사. 
    - 2. 모든 바이러스 섭취 끝나면 죽은 바이러스 -> 나이//2 = > 양분.
    - 3. 번식 진행 - 5의 배수 나이의 바이러스: 인접한 8개 칸에 나이가 1인 바이러스 생김. 
    - 4. 양분이 추가됨.

2. 입력:
* n: 배지의 크기, m:바이러스 개수, k: 사이클 수 
* 추가되는 양분의 양.
* r,c : 바이러스 위치, age: 바이러스 나이.
'''
n, m, k = tuple(map(int, input().split()))

virus = [[[] for _ in range(n)] for _ in range(n)]
next_virus = [[[] for _ in range(n)] for _ in range(n)]

food = [[5 for _ in range(n)] for _ in range(n)]
next_food = [[0 for _ in range(n)] for _ in range(n)]

add_food = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def simulate():
    # 그 다음 바이러스, 양분 값을 초기화합니다.
    for i in range(n):
        for j in range(n):
            next_virus[i][j] = []
            next_food[i][j] = 0

    # Step1. 바이러스가 양분을 섭취합니다.
    for i in range(n):
        for j in range(n):
            # Step1-1. 바이러스를 나이순으로 정렬합니다.
            virus[i][j].sort()

            # Step1-2. 어린 바이러스부터 순서대로 양분을 섭취합니다.
            for age in virus[i][j]:

                # Case1. 양분이 충분하다면 바이러스는 나이가 1 증가합니다.
                if food[i][j] >= age:
                    food[i][j] -= age
                    next_virus[i][j].append(age + 1)

                # Case2.양분이 불충분하다면 바이러스는 죽고 그 다음 양분으로 쓰입니다.
                else:
                    next_food[i][j] += age // 2

            # Step1-3. 남은 양분 만큼을 그 다음 양분으로 넣어줍니다.
            next_food[i][j] += food[i][j]

    # Step2. 바이러스가 번식을 진행합니다.
    for i in range(n):
        for j in range(n):
            for age in next_virus[i][j]:
                if age % 5 == 0:
                    for d in range(8):
                        nx, ny = i + dx[d], j + dy[d]
                        # 격자 안이라면 나이가 1인 바이러스를 추가합니다.
                        if 0 <= nx < n and 0 <= ny < n:
                            next_virus[nx][ny].append(1)

    # Step3. 각 칸에 입력으로 주어진 만큼 양분이 추가됩니다.
    for i in range(n):
        for j in range(n):
            next_food[i][j] += add_food[i][j]

    # 바이러스, 양분 값을 갱신해줍니다.
    for i in range(n):
        for j in range(n):
            virus[i][j] = next_virus[i][j][:]
            food[i][j] = next_food[i][j]


for _ in range(m):
    r, c, age = tuple(map(int, input().split()))
    virus[r - 1][c - 1].append(age)

# 총 k번 시뮬레이션을 진행합니다.
for _ in range(k):
    simulate()

ans = sum([len(virus[i][j]) for i in range(n) for j in range(n)])
print(ans)