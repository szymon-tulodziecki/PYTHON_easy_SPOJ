# https://pl.spoj.com/problems/FLAMASTE/

t = int(input())

while t > 0:
    text = input()
    count = 1
    output = ""
    i = 0

    for i in range(1, len(text)):
        if text[i] != text[i-1]:
            if count > 2:
                output += text[i-1] + str(count)
            else:
                output += count * text[i-1]
            count = 1
        else:
            count += 1
    if count > 2:
        output += text[i] + str(count)
    else:
        output += count * text[i]
    print("\n"+ output)

    t -= 1
