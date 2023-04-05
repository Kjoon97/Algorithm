import sys
sys.stdin = open("input.txt","r")
from collections import defaultdict
T = int(input())


def string_game(string):
    len_string = len(string)
    alpha = defaultdict(list)

    for i in range(len_string):
        if string.count(string[i])>=k:
            alpha[string[i]].append(i)

    if not alpha:
        return (-1,)

    min_str=10000
    max_str=0

    for idx_lst in alpha.values():
        for j in range(len(idx_lst)-k+1):
            temp = idx_lst[j+k-1]-idx_lst[j]+1

            if temp<min_str:
                min_str = temp
            if temp>max_str:
                max_str = temp

    return (min_str, max_str)


for t in range(1,T+1):
    string = input()
    k = int(input())
    print(*string_game(string))