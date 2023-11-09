# https://pl.spoj.com/problems/PRZEDSZK/

t = int(input())

while t > 0:
    a, b = map(int, input().split())

    i = 10
    while True:
        if i % a == 0 and i % b == 0:
            print(i)
            break
        i += 1
    t -= 1
