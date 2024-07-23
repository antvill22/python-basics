def fuel(frac):
    try:
        x_str, y_str = frac.split('/')
        x = int(x_str)
        y = int(y_str)
        if y == 0 or x > y:
            raise ValueError
        perc=round((x / y) * 100)

        if perc <= 1:
            return 'E'
        elif perc >= 99:
            return 'F'
        else:
            return str(perc) + '%'
    except (ValueError, ZeroDivisionError):
        return None

while True:
    frac = input("Fraction: ").strip()

    r = fuel(frac)

    if r is not None:
        print(r, sep="", end="")
        break
