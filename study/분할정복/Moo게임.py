import sys
#sys.stdin = open("input.txt","r")

'''
(코테 스터디)
문자열을 앞, 중간, 뒤 구간으로 3구간으로 나눠 생각하자.
현재 문자열 길이가 n보다 작을 경우 계속 문자열 길이를 증가시킴으로써 n의 위치는 현재 문자열의 중간 또는 뒷 구간에 위치한다.
중간 구간에 해당할 경우 n-이전 문자열 길이 ==1인 경우 'm' 출력 그렇지 않은 경우 나머지 'o'이므로 'o'출력.
뒷 구간에 해당할 경우 뒷 구간 첫 글자가 앞 구간의 처글자 인 것처럼 가정하고 다시 탐색.
'''

s0 = ["m","o","o"]

def bt(n, depth, b_len):
    #현재 문자열 길이 = (이전 문자열 길이)*2 + (현재 차수)+3
    new_len = 2 * b_len + depth + 3
    if n<=3:
        print(s0[n-1])
        return

    #현재 문자열 길이가 n보다 작을 경우 계속 차수 증가.
    if new_len<n:
        bt(n,depth+1,new_len)
    else:
        #가운데 구간 확인.
        if b_len< n <=b_len+depth+3:
            if n-b_len==1:
                print('m')
            else:
                print('o')
            return
        #뒷구간 확인. 뒷 구간을 앞 구간처럼 탐색하기 위해 빼줌.
        else:
            bt(n-(b_len+depth+3),1,3)

n = int(input())
bt(n,1,3)