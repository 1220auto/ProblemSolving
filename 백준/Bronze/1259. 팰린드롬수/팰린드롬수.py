import sys

# n, m = map(int, sys.stdin.readline().split())
# m = int(sys.stdin.readline())
# c, n = map(str, sys.stdin.readline().split())




while True:
    n = input()
    if n == '0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')
