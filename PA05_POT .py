# https://pl.spoj.com/problems/PA05_POT/

t = int(input())

while t > 0:
    a, b = map(int, input().split())

    if a == 0:
        print("0 \n")
    elif b == 0:
        print("1 \n")
    elif a % 10 == 0:
        print("0 \n")
    elif a % 10 == 1:
        print("1 \n")
    elif a % 10 == 2:
        if b % 4 == 1:
            print("2 \n")
        elif b % 4 == 2:
            print("4 \n")
        elif b % 4 == 3:
            print("8 \n")
        elif b % 4 == 0:
            print("6 \n")
    elif a % 10 == 3:
        if b % 4 == 1:
            print("3 \n")
        elif b % 4 == 2:
            print("9 \n")
        elif b % 4 == 3:
            print("7 \n")
        elif b % 4 == 0:
            print("1 \n")
    elif a % 10 == 4:
        if b % 2 == 1:
            print("4 \n")
        elif b % 2 == 0:
            print("6 \n")
    elif a % 10 == 5:
        print("5 \n")
    elif a % 10 == 6:
        print("6 \n")
    elif a % 10 == 7:
        if b % 4 == 1:
            print("7 \n")
        elif b % 4 == 2:
            print("9 \n")
        elif b % 4 == 3:
            print("3 \n")
        elif b % 4 == 0:
            print("1 \n")
    elif a % 10 == 8:
        if b % 4 == 1:
            print("8 \n")
        elif b % 4 == 2:
            print("4 \n")
        elif b % 4 == 3:
            print("2 \n")
        elif b % 4 == 0:
            print("6 \n")
    elif a % 10 == 9:
        if b % 2 == 1:
            print("9 \n")
        elif b % 2 == 0:
            print("1 \n")

    t -= 1
