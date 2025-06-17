def power(b, e):
    if e == 0:
        return 1
    elif e % 2 == 0:
        half = power(b, e // 2)
        return half * half
    else:
        return b * power(b, e - 1)
