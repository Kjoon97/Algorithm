import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

def count_z(str):
    cnt=0
    for c in str:
        if cnt>=3:
            return cnt
        if c not in ['a','e','i','o','u']:
            cnt+=1
        else:
            cnt=0

    return cnt


def count_m(str):
    cnt =0
    for c in str:
        if cnt>=3:
            return cnt
        if c in ['a','e','i','o','u']:
            cnt+=1
        else:
            cnt=0

    return cnt

def cont(str):
    str_list = list(str)
    str_len = len(str_list)
    for i in range(1,str_len):
        if str_list[i-1] == str_list[i]:
            if str_list[i-1] == 'e' or str_list[i-1] == 'o':
                continue
            else:
                return True

    return False


while True:
    password = input().rstrip()
    if password == 'end':
        break

    if any([x in ['a','e','i','o','u'] for x in password]):
        if count_m(password) >= 3 or count_z(password) >= 3:
            print(f"<{password}> is not acceptable.")
        else:
            if cont(password):
                print(f"<{password}> is not acceptable.")
            else:
                print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")