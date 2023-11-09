# https://pl.spoj.com/problems/RNO_DOD/

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    result = sum(a)

    print(str(result) + "\n")
    t -= 1
