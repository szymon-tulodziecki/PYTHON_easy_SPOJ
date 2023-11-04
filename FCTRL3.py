t = int(input())

# https://pl.spoj.com/problems/FCTRL3/

while t:
    n = int(input())
    if n > 10:
        print("0 0 \n")
    else:
        outcome = 1
        for i in range(1, n+1):
            outcome *= i
        print((outcome // 10) % 10, outcome % 10)

    t -= 1
