from math import sqrt


# https://pl.spoj.com/problems/PRIME_T/
def prime_t(m):

    if m == 1:
        print("NIE")
    elif m == 2 or m == 3:
        print("TAK")
    else:
        for i in range(2, int(sqrt(m)) + 1):
            if (m % i) == 0:
                print("NIE")
                return
        print("TAK")

t = int(input())

while t > 0:
    n = int(input())
    prime_t(n)
    t -= 1
