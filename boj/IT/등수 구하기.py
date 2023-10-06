import sys
sys.stdin = open("input.txt","r")

n , teasoo_score, p = map(int,input().split())
if n==0:
    print(1)
else:
    scores = list(map(int, input().split()))
    cnt =0

    if scores[n-1] >= teasoo_score and n==p: #마지막 값이 내 점수보다 크거나 같으면서 리스트가 꽉찬 경우 -1
        print(-1)
    else:
        for score in scores:
            cnt+=1     #등수 카운팅
            if teasoo_score >= score: #랭킹 리스트가 내 점수보다 더 크거나 동일한 경우 등수 출력.
                print(cnt)
                break
        else:  #랭킹 리스트에 내 점수보다 크거나 같은걸 찾지 못한 경우.
            print(cnt+1)
